import flet as ft
from tools import DialogTools
from widgets import NumberPicker
from threading import Timer
import time


def clock(page :ft.Page):
    clock = ft.Text("", style=ft.TextThemeStyle.TITLE_MEDIUM)

    view = ft.View("/tools/clock", [
        ft.AppBar(title=ft.Text("时钟"), bgcolor=ft.colors.SURFACE_VARIANT),
        clock,
        ft.FloatingActionButton("退出", icon=ft.icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
    ])

    def refresh_clock():
        clock.value = time.strftime("当前日期：%Y-%m-%d 当前时间：%X")
        page.update()
        timer_obj = Timer(0.01, refresh_clock)
        timer_obj.start()
    
    timer_obj = Timer(0.01, refresh_clock)
    timer_obj.start()

    return view
