import flet as ft
from tools import DialogTools


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
    return view
