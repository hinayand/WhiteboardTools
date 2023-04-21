import flet as ft
from threading import Timer


def dbg(page: ft.Page):
    local_view = ft.Markdown(f"{locals()}", selectable=True)
    global_view = ft.Markdown(f"{globals()}", selectable=True)
    timer = None
    refresh_switch = ft.Switch(label="继续刷新", on_change=lambda _: refresh_stat_change())
    code_inject_input = ft.TextField(label="临时插入代码执行", multiline=True, max_lines=100)
    
    view = ft.View("/dbg", controls=[
        ft.AppBar(title=ft.Text("Debug Page")),
        ft.ListView([
            local_view,
            global_view
        ], expand=True, spacing=10),
        ft.ListView([
            refresh_switch,
            code_inject_input,
            ft.ElevatedButton("临时注入代码执行", on_click=lambda _: code_inject_runner())
        ], expand=True, spacing=5)
    ])

    def refresh():
        local_view.value = f"{locals()}"
        global_view.value = f"{globals()}"
        nonlocal timer
        page.update()
        timer = Timer(0.1, refresh)
        timer.start()

    refresh()

    def refresh_stat_change():
        if refresh_switch.value == False:
            refresh()
            refresh_switch.label = "继续刷新"
            page.update()
        else:
            # timer.cancel()
            refresh_switch.label = "停止刷新"
            page.update()

    def code_inject_runner():
        exec(code_inject_input.value)
        code_inject_input.value = ""
        page.update()

    return view
