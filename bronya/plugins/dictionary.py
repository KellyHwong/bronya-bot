import random
import os
import nonebot
from nonebot import on_command, CommandSession

from bs4 import BeautifulSoup
from utils.utils import download_page


look_up_prefix = 'https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD/'


@on_command('dictionary', aliases=("dict", "查词", "字典"))
async def dictionary(session: CommandSession):
    bot = session.bot
    bot = nonebot.get_bot()

    word = session.current_arg_text.strip()
    print(word)

    word_url = look_up_prefix + word
    html_doc = download_page(word_url).decode('utf-8')
    with open("test.html", 'w', encoding="utf-8") as f:
        print(html_doc, file=f)
    soup = BeautifulSoup(html_doc, "lxml")
    all_dict_div = soup.find_all("div", {"class": 'cdo-dblclick-area'})
    eng_dict_b = all_dict_div[0].find("b", {"class": 'def'})
    word_def = str(eng_dict_b)
    word_soup = BeautifulSoup(word_def, "lxml")
    word_def_text = word_soup.text
    # for i in word_soup.find_all(attrs={"class": "query"}):
    #     word_def_text += i.text
    #     word_def_text += " "
    await session.send(word_def_text)
