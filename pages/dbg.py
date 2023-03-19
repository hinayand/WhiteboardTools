import flet as ft
from threading import Timer


def dbg(page: ft.Page):
    local_view = ft.Markdown(f"{locals()}", selectable=True)
    global_view = ft.Markdown(f"{globals()}", selectable=True)
    timer = None
    
    view = ft.View("/dbg", controls=[
        ft.AppBar(title=ft.Text("Debug Page")),
        ft.ListView([
            local_view,
            global_view
        ], expand=True, spacing=10),
        ft.ElevatedButton("停止刷新", on_click=lambda _: stop())
    ])

    def refresh():
        local_view.value = f"{locals()}"
        global_view.value = f"{globals()}"
        nonlocal timer
        page.update()
        timer = Timer(0.1, refresh)
        timer.start()

    def stop():
        timer.cancel()

    refresh()

    return view
