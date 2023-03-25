import flet as ft
from tools import DialogTools
from widgets import NumberPicker
import random


def random_school_id(page: ft.Page):
    random_id = ft.Text("学号：不可用", style=ft.TextThemeStyle.TITLE_LARGE, text_align=ft.TextAlign.CENTER)
    max_id = NumberPicker.NumberPicker(page, 100, 1, "最大学号", page.client_storage.get("max_id"))

    view = ft.View("/tools/random_school_id", [
        ft.AppBar(title=ft.Text("抽学号")),
        ft.ListView([
            random_id,
            max_id.get_widget(),
            ft.ElevatedButton("开始抽学号", on_click=lambda _: random_choose_id()),
        ], expand=True, spacing=10)
    ])

    def random_choose_id():
        page.client_storage.set("max_id", max_id.get_value())
        random_id.value = "学号：" + str(random.randint(1, max_id.get_value()))
        page.update()

    return view
