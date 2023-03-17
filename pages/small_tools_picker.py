import flet as ft
from tools import DialogTools, window_tools


def small_tools_picker(page: ft.Page):
    # window_tools.size_changer(page, 300, 300, 2)
    picker = ft.Dropdown(width=250, options=[
        ft.dropdown.Option("抽学号"),
        ft.dropdown.Option("计时器"),
        ft.dropdown.Option("时钟")
    ], label="小工具选择器", hint_text="选择你要运行的小工具")
    dialog_tools = DialogTools.DialogTools(page)

    view = ft.View("/tools", [
        ft.AppBar(title=ft.Text("白板工具箱-小工具选择")),
        picker,
        ft.ElevatedButton("启动", icon=ft.icons.PLAY_ARROW, on_click=lambda _: launch())
    ])

    def launch():
        match picker.value:
            case "抽学号":
                page.go("/tools/random_school_id")
            case "计时器":
                page.go("/tools/timer")
            case "时钟":
                page.go("/tools/clock")
            case _:
                dlg = ft.AlertDialog(title=ft.Text("白板工具箱", style=ft.TextThemeStyle.TITLE_LARGE),
                                     content=ft.Text("我们遇到了内部错误，请检查你是否选择了还未完成或未发布的小工具！"),
                                     actions=[ft.TextButton("好的", on_click=lambda _: dialog_tools.close_dlg(dlg))])
                dialog_tools.open_dlg(dlg)

    return view
