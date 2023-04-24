import random

import flet as ft
from tools import DialogTools

op_code = random.randint(100000, 999999)


def index(page: ft.Page):
    page.window_width = 500
    page.window_height = 500
    page.title = "白板工具箱"

    view = ft.View("/", controls=[
        ft.AppBar(title=ft.Text(value="白板工具箱")),
        ft.ListView([
            ft.ElevatedButton(
                text="系统相关", icon=ft.icons.SETTINGS, on_click=lambda _: page.go("/sys")),
            ft.ElevatedButton(
                text="小工具", icon=ft.icons.EGG, on_click=lambda _: page.go("/tools")),
            ft.ElevatedButton("设置", on_click=lambda _: page.go("/setting"), icon=ft.icons.SETTINGS)
        ], expand=True, spacing=10)
    ])
    view.vertical_alignment = ft.MainAxisAlignment.CENTER

    if page.platform == ft.WEB_BROWSER and page.client_storage.get("web-mode-verify") is False:
        user_input_op_code = ft.TextField(label="访问码")
        view = ft.View("", controls=[
            ft.AppBar(title=ft.Text(value="白板工具箱——Web模式")),
            ft.ListView([
                user_input_op_code,
                ft.ElevatedButton("验证")
            ])
        ])

        def on_verify():
            if int(user_input_op_code.value) == op_code:
                page.client_storage.set("web-mode-verify", True)
            else:
                dlg = ft.AlertDialog(modal=True, title=ft.Text("验证失败", style=ft.TextThemeStyle.TITLE_LARGE),
                                     content=ft.Text("访问码错误！", style=ft.TextThemeStyle.BODY_LARGE))
                dlg.actions = [ft.TextButton("好的", on_click=DialogTools.DialogTools(page).close_dlg(dlg))]

    return view


def web_desktop_index(page: ft.page):
    page.window_width = 500
    page.window_height = 500
    page.title = "白板工具箱"

    view = ft.View("/", controls=[
        ft.AppBar(title=ft.Text(value="白板工具箱——Web模式")),
        ft.ListView([
            ft.ElevatedButton(
                text="系统相关", icon=ft.icons.SETTINGS, on_click=lambda _: page.go("/sys")),
            ft.ElevatedButton(
                text="小工具", icon=ft.icons.EGG, on_click=lambda _: page.go("/tools")),
            ft.ElevatedButton("设置", on_click=lambda _: page.go("/setting"), icon=ft.icons.SETTINGS)
        ], expand=True, spacing=10),
        ft.Text(f"访问码：{op_code}")
    ])
