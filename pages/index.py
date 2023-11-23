import flet as ft


def index(page: ft.Page):
    page.window_width = 500
    page.window_height = 500
    page.title = "白板工具箱"

    if not page.client_storage.get("theme_color") is None or not page.client_storage.get("theme_color") == "":
        page.theme.color_scheme_seed = page.client_storage.get("theme_color")

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

    return view
