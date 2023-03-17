import flet as ft
from threading import Timer


def dbg(page: ft.Page):
    local_view = ft.Markdown(f"{locals()}", selectable=True)
    global_view = ft.Markdown(f"{globals()}", selectable=True)
    
    view = ft.View("/dbg", controls=[
        ft.AppBar(title=ft.Text("Debug Page")),
        ft.ListView([
            local_view,
            global_view
        ], expand=True, spacing=10)
    ])

    def refresh():
        local_view.value = f"{locals()}"
        global_view.value = f"{globals()}"
        page.update()
        Timer(0.1, refresh).start()

    refresh()

    return view
