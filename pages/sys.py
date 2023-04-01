import flet as ft
import os
import time
import asyncio
import threading as tr
from tools import DialogTools, window_tools


def sys(page: ft.Page) -> ft.View:
    dialog_tools = DialogTools.DialogTools(page)
    # page.window_height = 420
    # page.window_width = 355
    # window_tools.size_changer(page, 420, 355, 2)
    view = ft.View("/sys", [
        ft.AppBar(title=ft.Text("白板工具箱-系统相关")),
        ft.ListView([
            ft.ElevatedButton(text="关闭白板", icon=ft.icons.POWER_OFF, on_click=lambda _: shutdown()),
            ft.ElevatedButton(text="重启白板", icon=ft.icons.REFRESH, on_click=lambda _: restart()),
            ft.ElevatedButton(text="注销", icon=ft.icons.LOGOUT, on_click=lambda _: logoff()),
            ft.ElevatedButton(text="取消关机", icon=ft.icons.CANCEL, on_click=lambda _: cancel_shutdown())
        ], expand=True, spacing=5),
    ])

    def shutdown():
        dlg = ft.AlertDialog(title=ft.Text("你的白板将在30秒后关机！"),
                             actions=[ft.TextButton("好的", on_click=lambda _: dialog_tools.close_dlg(dlg))])
        os.system("shutdown -s -t 30")
        dialog_tools.open_dlg(dlg)

    def restart():
        dlg = ft.AlertDialog(title=ft.Text("你的白板将在30秒后重启！"),
                             actions=[ft.TextButton("好的", on_click=lambda _: dialog_tools.close_dlg(dlg))])
        os.system("shutdown -r -t 30")
        dialog_tools.open_dlg(dlg)

    def logoff():
        os.system("logoff")

    def cancel_shutdown():
        dlg = ft.AlertDialog(title=ft.Text("你的白板已经取消关机！"),
                             actions=[ft.TextButton("好的", on_click=lambda _: dialog_tools.close_dlg(dlg))])
        os.system("shutdown -a")
        dialog_tools.open_dlg(dlg)

    return view
