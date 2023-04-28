import random

import flet as ft
from tools import DialogTools

op_code = random.randint(100000, 999999)


def index(page: ft.Page, **kargs):
    page.window_width = 500
    page.window_height = 500
    page.title = "白板工具箱"

    actions_list = ft.ListView([
        ft.ElevatedButton(text="系统相关", icon=ft.icons.SETTINGS, on_click=lambda _: page.go("/sys")),
        ft.ElevatedButton(text="小工具", icon=ft.icons.EGG, on_click=lambda _: page.go("/tools")),
        ft.ElevatedButton("设置", on_click=lambda _: page.go("/setting"), icon=ft.icons.SETTINGS)
    ], expand=True, spacing=10)

    # Basic View
    view = ft.View("/", controls=[
        ft.AppBar(title=ft.Text(value="白板工具箱")),
        actions_list
    ])
    view.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Webview - need verify
    if kargs.get("web_mode") and not page.client_storage.get("web_mode_verify"):
        user_input_op_code = ft.TextField(label="访问码")
        view = ft.View("/", controls=[
            ft.AppBar(title=ft.Text(value="白板工具箱——Web模式")),
            ft.ListView([
                user_input_op_code,
                ft.ElevatedButton("验证", on_click=lambda _: on_verify())
            ])
        ])

        def on_verify():
            if int(user_input_op_code.value) == op_code:
                page.client_storage.set("web_mode_verify", True)
                page.views.clear()
                page.views.append(index(page))
                page.update()
            else:
                dlg = ft.AlertDialog(modal=True, title=ft.Text("验证失败", style=ft.TextThemeStyle.TITLE_LARGE),
                                     content=ft.Text("访问码错误！", style=ft.TextThemeStyle.BODY_LARGE))
                dlg.actions = [ft.TextButton("好的", on_click=DialogTools.DialogTools(page).close_dlg(dlg))]

    if kargs.get("web_mode") and not page.client_storage.get("web_mode_verify"):
        print(op_code)

    return view
