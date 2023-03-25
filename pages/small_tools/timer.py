import flet as ft
from tools import DialogTools
from widgets import NumberPicker
from threading import Timer
import time


def timer(page: ft.Page):
    hour = NumberPicker.NumberPicker(
        page, 23, 0, "小时", page.client_storage.get("hour"))
    minute = NumberPicker.NumberPicker(
        page, 59, 0, "分钟", page.client_storage.get("minute"))
    second = NumberPicker.NumberPicker(
        page, 59, 0, "秒", page.client_storage.get("second"))
    time_end = 0
    total_time = 0
    str_time_control = ft.Text("剩余时间：不可用", style=ft.TextThemeStyle.TITLE_SMALL)
    timer_is_stop = False
    dlg_tools = DialogTools.DialogTools(page)

    view = ft.View("/tools/timer", [
        ft.AppBar(title=ft.Text("计时器")),
        ft.ListView([
            ft.Text("设置", style=ft.TextThemeStyle.TITLE_MEDIUM),
            hour.get_widget(),
            minute.get_widget(),
            second.get_widget(),
            ft.ElevatedButton("开始计时", on_click=lambda _: start_timer()),
            ft.Text("计时", style=ft.TextThemeStyle.TITLE_MEDIUM),
            str_time_control,
            ft.ElevatedButton("停止计时", on_click=lambda _: stop_timer())
        ], expand=True, spacing=5)
    ])

    def start_timer():
        nonlocal time_end, total_time
        time_end = (int(hour.get_value()) * 60 * 60) + \
            (int(minute.get_value()) * 60) + int(second.get_value())
        timer_obj = Timer(1, timer_tick)
        timer_obj.start()
        hour.disable()
        minute.disable()
        second.disable()
        page.client_storage.set("hour", hour.get_value())
        page.client_storage.set("minute", minute.get_value())
        page.client_storage.set("second", second.get_value())
        str_time = f"剩余时间：{(time_end - total_time) // 60 // 60} : {(time_end - total_time) // 60 % 60} : {(time_end - total_time) % 60} "
        str_time_control.value = str_time
        page.update()

    def stop_timer():
        nonlocal timer_is_stop
        timer_is_stop = True
        hour.enable()
        minute.enable()
        second.enable()
        str_time_control.value = "剩余时间：不可用"
        page.update()

    def timer_tick():
        nonlocal total_time, time_end
        total_time += 1
        str_time = f"剩余时间：{(time_end - total_time) // 60 // 60} : {(time_end - total_time) // 60 % 60} : {(time_end - total_time) % 60} "
        str_time_control.value = str_time
        page.update()
        if total_time < time_end and not timer_is_stop:
            timer_obj = Timer(1, timer_tick)
            timer_obj.start()
        elif total_time == time_end or total_time > time_end:
            timer_end()

    def timer_end():
        hour.enable()
        minute.enable()
        second.enable()
        dlg = ft.AlertDialog(title=ft.Text("计时器", style=ft.TextThemeStyle.TITLE_LARGE), content=ft.Text("时间到！"),
                             actions=[ft.TextButton("好的", on_click=lambda _: dlg_tools.close_dlg(dlg))])
        dlg_tools.open_dlg(dlg)
        str_time_control.value = "剩余时间：不可用"
        page.update()

    return view
