import flet as ft
from flet import ThemeMode

def setting(page: ft.Page) -> ft.View:
    material3_switch = ft.Switch(label="使用新版本的Material Design（默认启用，仅在本次会话中保留）", on_change=lambda _: theme_change())
    dark_mode_switch = ft.Switch(label="暗色模式（不支持旧版本Material Design）", on_change=lambda _: theme_change())

    material3_switch.value = True
    dark_mode_switch.value = page.client_storage.get("dark_mode")

    view = ft.View("/setting", [
        ft.AppBar(title=ft.Text("设置")),
        ft.ListView([
            ft.Text("界面设置", style=ft.TextThemeStyle.BODY_LARGE),
            material3_switch,
            dark_mode_switch
        ], expand=True, spacing=5)
    ])

    def theme_change():
        page.theme.use_material3 = material3_switch.value
        if dark_mode_switch.value:
            page.theme_mode = ThemeMode.DARK
        else:
            page.theme_mode = ThemeMode.LIGHT
        page.client_storage.set("dark_mode", dark_mode_switch.value)
        page.update()
    
    theme_change()

    return view
