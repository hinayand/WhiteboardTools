import flet as ft
from threading import Timer


def dbg(page: ft.Page):
    local_view = ft.Markdown(f"{locals()}", selectable=True)
    global_view = ft.Markdown(f"{globals()}", selectable=True)
    timer = None
    refresh_switch = ft.Switch(label="继续刷新", on_change=lambda _: refresh_stat_change())
    
    view = ft.View("/dbg", controls=[
        ft.AppBar(title=ft.Text("Debug Page")),
        ft.ListView([
            local_view,
            global_view
        ], expand=True, spacing=10),
        refresh_switch
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
            timer.cancel()
            refresh_switch.label = "停止刷新"
            page.update()

    return view
