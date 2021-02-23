# Copyright (c) ProgrammerX 2015 - 2020*, Vladimir, Russia. This project created by ProgrammerX Company. It's owner
# MrOlegTitov has full right to control this project.

from pypresence import Presence
from time import time

RPC = Presence("813849996943556651")
btns = [
    {
        "label": "YouTube",
        "url": "https://www.youtube.com/channel/UC5ccP3-TIDFWgzPbgyQXJGg"
    },
    {
        "label": "Github",
        "url": "https://github.com/MrOlegTitov"
    }
]

RPC.connect()
RPC.update(
    state="Работаю в Programmer X!",
    details="Мяу!",
    start=time(),
    buttons=btns,
    large_image="programmer_x_logo",
    small_image="kuzya",
    large_text="А что вы хотели здесь увидеть?",
    small_text="Это моя кошка :)"
)

input()
