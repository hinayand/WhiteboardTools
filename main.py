import flet as ft
import sys
from flet import ThemeMode
from pages import sys_setting, small_tools_picker, index, dbg, setting
from pages.small_tools import random_school_id
from pages.small_tools import timer
from pages.small_tools import clock

web_mode = False

for i in range(0, len(sys.argv)):
    if sys.argv[i] == "remote":
        web_mode = True
        break

def main(page: ft.Page):
    page.fonts = {
        "Harmony Sans": "./resource/HarmonyOS_Sans_SC_Regular.ttf"
    }
    page.theme = ft.Theme(use_material3=True, color_scheme_seed="white", font_family="Harmony Sans")
    if page.client_storage.get("dark_mode") == True:
        page.theme_mode = ThemeMode.DARK
    else:
        page.theme_mode = ThemeMode.LIGHT

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def route_change(route: ft.RouteChangeEvent):
        # TODO: Add Route Change Function
        page.views.clear()
        if web_mode:
            page.views.append(index.index(page, web_mode=True))
        else:
            page.views.append(index.index(page))
        # This is old page route codes.
        # match route.route:
        #     case "/sys":
        #         page.views.append(sys.sys(page))
        #     case "/tools":
        #         page.views.append(small_tools_picker.small_tools_picker(page))
        #     case "/tools/random_school_id":
        #         page.views.append(random_school_id.random_school_id(page))
        #     case "/tools/timer":
        #         page.views.append(timer.timer(page))
        #     case "/tools/clock":
        #         page.views.append(clock.clock(page))
        #     case "/dbg":
        #         page.views.append(dbg.dbg(page))
        #     case "/setting":
        #         page.views.append(setting.setting(page))

        if route.route.split("/")[1] == "":
            pass
        elif route.route.split("/")[1] == "dbg":
            page.views.append(dbg.dbg(page))
        elif route.route.split("/")[1] == "setting":
            page.views.append(setting.setting(page))
        elif route.route.split("/")[1] == "sys":
            page.views.append(sys_setting.sys(page))
        elif route.route.split("/")[1] == "tools":
            page.views.append(small_tools_picker.small_tools_picker(page))
            try:
                if route.route.split("/")[2] == "random_school_id":
                    page.views.append(random_school_id.random_school_id(page))
                elif route.route.split("/")[2] == "timer":
                    page.views.append(timer.timer(page))
                elif route.route.split("/")[2] == "clock":
                    page.views.append(clock.clock(page))
            except IndexError:
                pass

        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.client_storage.set("web_mode_verify", False)

if not web_mode:
    ft.app(target=main)
else:
    ft.app(target=main, view=ft.WEB_BROWSER)
