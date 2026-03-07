import os
import sqlite3
import datetime
from nonebot import on_message
from nonebot.adapters.onebot.v11 import PrivateMessageEvent
from bronya_bot.services.chat_api import chat_api_session
from bronya_bot.config import LOCALSTORE_DATA_DIR

"""
SQLite 服务
"""

DB_PATH = os.path.join(LOCALSTORE_DATA_DIR, "chat_history.db")

def init_sqlite_db():
    """初始化 SQLite 数据库（创建表）"""
    if not os.path.exists(DB_PATH):
        os.makedirs(LOCALSTORE_DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        create_time TEXT DEFAULT (datetime('now','localtime'))
    )
    ''')
    conn.commit()
    conn.close()

def save_message(user_id, role, content):
    """保存单条消息到 SQLite（通用函数）"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat_history (user_id, role, content) VALUES (?, ?, ?)",
            (str(user_id), role, content)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"保存数据库失败：{e}")

def load_recent_history(user_id, max_turns=10):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT role, content FROM chat_history
            WHERE user_id = ?
            ORDER BY id DESC LIMIT ?
        ''', (str(user_id), 2 * max_turns))
        rows = cursor.fetchall()
        conn.close()

        # 反转顺序 → 正常对话顺序
        history = []
        for role, content in reversed(rows):
            history.append({"role": role, "content": content})
        return history
    except Exception as e:
        print(f"加载历史失败：{e}")
        return []