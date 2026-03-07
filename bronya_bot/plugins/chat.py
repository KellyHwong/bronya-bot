from nonebot import on_message
from nonebot.adapters.onebot.v11 import PrivateMessageEvent

import bronya_bot.services.sqlite.sqlite_service as sqlite_service
from bronya_bot.services.chat_api import chat_api_session

history_sessions = {}  # 会话全局内存缓存
MAX_TURNS = 20  # 保留20轮对话
MODEL_NAME = "llama3.2:latest"

# 创建消息处理器，监听所有消息
private_chat = on_message(priority=1)


@private_chat.handle()
async def handle_private_chat(event: PrivateMessageEvent):
    if not isinstance(event, PrivateMessageEvent):
        return

    user_id = event.user_id
    message_text = event.get_message().extract_plain_text().strip()
    if not message_text:
        return

    # 从数据库初始化历史
    if user_id not in history_sessions:
        history_sessions[user_id] = sqlite_service.load_recent_history(
            user_id, MAX_TURNS
        )

    # 获取当前内存中的历史
    history = history_sessions[user_id]

    # 构造用户消息
    user_msg = {"role": "user", "content": message_text}

    # 传给 AI：历史 + 当前消息
    messages = history + [user_msg]

    # 调用 AI API
    response = await chat_api_session(MODEL_NAME, messages)

    # 处理响应
    if response and isinstance(response, dict):
        content = response.get("content", "")

        # 保存本轮对话到数据库
        ai_content = response.get("content", "")
        sqlite_service.save_message(user_id, "user", message_text)
        sqlite_service.save_message(user_id, "assistant", ai_content)

        # 更新内存历史
        history.append(user_msg)
        history.append(response)
        history_sessions[user_id] = history[-2 * MAX_TURNS :]  # 限制最大轮数

        await private_chat.finish(content)
    else:
        await private_chat.finish("抱歉，我暂时无法回答你的问题。")
