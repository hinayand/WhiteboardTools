import flet as ft
from pages import sys_setting, small_tools_picker, index, dbg, setting
from pages.small_tools import random_school_id
from pages.small_tools import timer
from pages.small_tools import clock
from pages.small_tools import chatgpt


def router_func(route_str: str, page: ft.Page):
    page.views.append(index.index(page))
    if route_str.split("/")[1] == "":
        pass
    elif route_str.split("/")[1] == "dbg":
        page.views.append(dbg.dbg(page))
    elif route_str.split("/")[1] == "setting":
        page.views.append(setting.setting(page))
    elif route_str.split("/")[1] == "sys":
        page.views.append(sys_setting.sys(page))
    elif route_str.split("/")[1] == "tools":
        page.views.append(small_tools_picker.small_tools_picker(page))
        try:
            if route_str.split("/")[2] == "random_school_id":
                page.views.append(random_school_id.random_school_id(page))
            elif route_str.split("/")[2] == "timer":
                page.views.append(timer.timer(page))
            elif route_str.split("/")[2] == "clock":
                page.views.append(clock.clock(page))
            elif route_str.split("/")[2] == "chatgpt":
                page.views.append(chatgpt.chatgpt(page))
        except IndexError:
            pass
