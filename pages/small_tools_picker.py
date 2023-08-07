import flet as ft
from flet import TapEvent
from tools import DialogTools, window_tools


def small_tools_picker(page: ft.Page):
    # window_tools.size_changer(page, 300, 300, 2)
    picker = ft.ListView([
        ft.ElevatedButton("抽学号", on_click=lambda _: launch("抽学号")),
        ft.ElevatedButton("计时器", on_click=lambda _: launch("计时器")),
        ft.ElevatedButton("时钟", on_click=lambda _: launch("时钟")),
        ft.ElevatedButton("ChatGPT", on_click=lambda _: launch("ChatGPT"))
    ], expand=True, spacing=5)
    dialog_tools = DialogTools.DialogTools(page)

    view = ft.View("/tools", [
        ft.AppBar(title=ft.Text("白板工具箱-小工具选择")),
        picker
    ]) 

    def launch(tool_name: str):
        match tool_name:
            case "抽学号":
                page.go("/tools/random_school_id")
            case "计时器":
                page.go("/tools/timer")
            case "时钟":
                page.go("/tools/clock")
            case "ChatGPT":
                page.go("/tools/chat-gpt")
            case _:
                dlg = ft.AlertDialog(title=ft.Text("白板工具箱", style=ft.TextThemeStyle.TITLE_LARGE),
                                     content=ft.Text("我们遇到了内部错误，请检查你是否选择了还未完成或未发布的小工具！"),
                                     actions=[ft.TextButton("好的", on_click=lambda _: dialog_tools.close_dlg(dlg))])
                dialog_tools.open_dlg(dlg)

    return view
