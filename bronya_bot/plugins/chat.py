from nonebot import on_message
from nonebot.adapters.onebot.v11 import PrivateMessageEvent
from bronya_bot.services.chat_api import chat_api_session

# 创建消息处理器，监听所有消息
private_chat = on_message(priority=1)

@private_chat.handle()
async def handle_private_chat(event: PrivateMessageEvent):
    # 只处理私聊消息
    if not isinstance(event, PrivateMessageEvent):
        return
    
    # 获取消息内容
    event_msg = event.get_message()
    message_text = event_msg.extract_plain_text()
    
    if message_text:
        print(f"Private message: {message_text}")
    
    # 构建消息列表
    messages = [
        {
            "role": "user",
            "content": message_text
        }
    ]
    
    # 调用 chat_api_session 获取回复
    model_name = "qwen2.5:7b"
    response = await chat_api_session(model_name, messages)
    
    # 处理响应
    if response and isinstance(response, dict):
        content = response.get("content", "")
        await private_chat.finish(content)
    else:
        await private_chat.finish("抱歉，我暂时无法回答你的问题。")