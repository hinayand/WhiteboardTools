import flet as ft
import time
import threading as tr


def height_changer(page: ft.Page, to: int, speed: int):
    for i in range(int(page.window_height), to, speed):
        page.window_height = i
        time.sleep(0.01)
        page.update()


def width_changer(page: ft.Page, to: int, speed: int):
    for i in range(int(page.window_width), to, speed):
        page.window_width = i
        time.sleep(0.01)
        page.update()


def size_changer(page: ft.Page, height: int = 500, width: int = 500, speed: int = 2):
    hc_thread = tr.Thread(target=height_changer, args=(page, height, 0 - speed))
    wc_thread = tr.Thread(target=width_changer, args=(page, width, 0 -speed))
    hc_thread.start()
    wc_thread.start()
    hc_thread.join()
    wc_thread.join()