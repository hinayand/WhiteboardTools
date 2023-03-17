import flet as ft
from pages import sys, small_tools_picker, index, dbg
from pages.small_tools import random_school_id
from pages.small_tools import timer
from pages.small_tools import clock


def main(page: ft.Page):
    page.fonts = {
        "Noto Sans": "./NotoSansCJKsc-Regular.ttf"
    }
    page.theme = ft.Theme(use_material3=True, color_scheme_seed="white")

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def route_change(route: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(index.index(page))
        # TODO: Add Route Change Function
        match route.route:
            case "/sys":
                page.views.append(sys.sys(page))
            case "/tools":
                page.views.append(small_tools_picker.small_tools_picker(page))
            case "/tools/random_school_id":
                page.views.append(random_school_id.random_school_id(page))
            case "/tools/timer":
                page.views.append(timer.timer(page))
            case "/tools/clock":
                page.views.append(clock.clock(page))
            case "/dbg":
                page.views.append(dbg.dbg(page))
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="./resource")
