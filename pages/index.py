import flet as ft
from tools import DialogTools


def index(page: ft.Page):
    page.window_width = 500
    page.window_height = 500
    page.title = "白板工具箱"
    page.fonts = {
        "Noto Sans": "./resource/NotoSansCJKsc-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Noto Sans")

    def about():
        dlg = ft.AlertDialog(title=ft.Text("关于", style=ft.TextThemeStyle.TITLE_LARGE),
                             content=ft.Text("作者：hinayand\n本程序使用GPL2开源协议开源，违反开源协议者将追究到底！",
                                             style=ft.TextThemeStyle.BODY_LARGE),
                             actions=[
            ft.TextButton("好的", on_click=lambda _:DialogTools.DialogTools(
                page).close_dlg(dlg))
        ])
        DialogTools.DialogTools(page).open_dlg(dlg)
        page.update()

    view = ft.View("/", controls=[
        ft.AppBar(title=ft.Text(value="白板工具箱"),
                  bgcolor=ft.colors.SURFACE_VARIANT),
        ft.Row(
            [
                ft.FilledTonalButton(
                    text="系统相关", icon=ft.icons.SETTINGS, on_click=lambda _: page.go("/sys")),
                ft.FilledTonalButton(
                    text="小工具", icon=ft.icons.EGG, on_click=lambda _: page.go("/tools")),
                ft.FilledTonalButton(
                    text="关于", icon=ft.icons.ACCOUNT_BOX, on_click=lambda _: about()
                )
            ]
        ),
        ft.Column(
            [
                ft.Text("开发者选项", style=ft.TextThemeStyle.BODY_MEDIUM),
                ft.TextButton("调试视图", on_click=lambda _: page.go("/dbg"))
            ]
        )
    ])
    view.vertical_alignment = ft.MainAxisAlignment.CENTER
    return view
