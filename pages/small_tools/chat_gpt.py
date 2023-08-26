import flet as ft
import openai
import os
import threading
import traceback
from widgets import MessageView

with open("resource/System Prompt.md", encoding="utf-8", mode="r") as f:
    default_sys_prompt = f.read()


def chat_gpt(page: ft.Page):
    def refresh_api_info():
        try:
            openai.api_key = page.client_storage.get("openai_api_key")
            openai.api_base = "https://" + \
                              page.client_storage.get("openai_api_host") + "/v1"
        except Exception:
            if not os.environ.get("OPENAI_API_KEY") is None and not os.environ.get("OPENAI_API_HOST") is None:
                openai.api_key = os.environ.get("OPENAI_API_KEY")
                openai.api_base = "https://" + \
                                  os.environ.get("OPENAI_API_HOST") + "/v1"
            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text("请在环境变量中设置OPENAI_API_KEY和OPENAI_API_HOST，又或者在设置中设置API和API Key"))
                page.snack_bar.open = True
                page.update()

    refresh_api_info()

    if page.client_storage.get("system_prompt") is None or page.client_storage.get("system_prompt") == "":
        messages = [{"role": "system", "content": default_sys_prompt}]
    else:
        messages = [
            {"role": "system", "content": page.client_storage.get("system_prompt")}]
    messages_to_show = ft.ListView(spacing=5, expand=1, auto_scroll=True)
    messages_to_show.controls.append(MessageView.MessageView(
        "S", "SYSTEM", "# 欢迎使用", page).get_widget())

    message_to_send = ft.TextField(
        label="Message", expand=True, multiline=True)

    model_will_use = ft.Dropdown(label="模型选择", options=[
        ft.dropdown.Option("claude-2-100k", "Claude2 100k"),
        ft.dropdown.Option("gpt-3.5-turbo", "GPT-3.5"),
        ft.dropdown.Option("gpt-3.5-turbo-16k", "GPT-3.5 Turbo 16k"),
        ft.dropdown.Option("gpt-4", "GPT-4"),
        ft.dropdown.Option("gpt-4-0613", "GPT-4-0613"),
        ft.dropdown.Option("gpt-4-0314", "GPT-4-0314"),
        ft.dropdown.Option("gpt-4-32k", "GPT-4-32k")
    ])

    def _send_msg():
        refresh_api_info()
        def close_dialog():
            page.dialog.open = False
            page.update()

        reply = ""
        try:
            nonlocal messages_to_show
            messages.append(
                {"role": "user", "content": str(message_to_send.value)})
            response = openai.ChatCompletion.create(
                model=model_will_use.value,
                messages=messages,
                stream=True
            )
            messages_to_show.controls.append(MessageView.MessageView(
                "R", "ROBOT", reply, page).get_widget())
            for chunk in response:
                try:
                    reply += chunk.choices[0].delta.content
                    messages_to_show.controls[-1] = MessageView.MessageView(
                        "R", "ROBOT", reply, page).get_widget()
                    page.update()
                except AttributeError:
                    messages.append(
                        {'role': 'assistant', 'content': str(reply)})
                    print(messages)
        except openai.error.APIError:
            page.dialog = ft.AlertDialog(
                title=ft.Text("错误"),
                content=ft.Text("很抱歉，出错了！\n您的OpenAI API返回了一个错误！\n" + traceback.format_exc(), expand=True),
                actions=[ft.TextButton("我知道了", on_click=lambda _: close_dialog())],
                modal=True
            )
            page.dialog.open = True
            page.update()
        except openai.error.InvalidRequestError:
            page.dialog = ft.AlertDialog(
                title=ft.Text("错误"),
                content=ft.Text(
                    "很抱歉，出错了！\n您可能没有选择模型又或者是你的API不支持你选择的模型！\n" + traceback.format_exc(), expand=True),
                actions=[ft.TextButton("我知道了", on_click=lambda _: close_dialog())],
                modal=True
            )
            page.dialog.open = True
            page.update()
        except openai.error.APIConnectionError:
            page.dialog = ft.AlertDialog(
                title=ft.Text("错误"),
                content=ft.Text(
                    "很抱歉，出错了！\n您的OpenAI API可能格式有误或不存在，请检查您的API地址。\n如果API地址确认无误，但您仍然能看到这个错误窗口，那么请询问API提供者！\n" +
                    traceback.format_exc(), expand=True),
                actions=[ft.TextButton("我知道了", on_click=lambda _: close_dialog())],
                modal=True
            )
            page.dialog.open = True
            page.update()
        except openai.error.AuthenticationError:
            page.dialog = ft.AlertDialog(
                title=ft.Text("错误"),
                content=ft.Text(
                    "很抱歉，出错了！\n您的API Key可能有误、无效、不存在，又可能是API提供者跑路了。\n如果API Key确认无误，但您仍然能看到这个错误窗口，那么请询问API提供者！\n" +
                    traceback.format_exc(), expand=True),
                actions=[ft.TextButton("我知道了", on_click=lambda _: close_dialog())],
                modal=True
            )
            page.dialog.open = True
            page.update()
        except Exception:
            page.dialog = ft.AlertDialog(
                title=ft.Text("错误"),
                content=ft.Text(
                    "很抱歉，出错了！\n这可能是由代码产生的错误，如果您见到了这个弹窗，请截图发给开发者！\n" + str(
                        traceback.format_exc()), expand=True),
                actions=[ft.TextButton("我知道了", on_click=lambda _: close_dialog())],
                modal=True
            )
            page.dialog.open = True
            page.update()

    def send_message():
        if not message_to_send.value == "":
            threading.Thread(target=_send_msg).start()
            messages_to_show.controls.append(MessageView.MessageView(
                "U", "USER", message_to_send.value, page).get_widget())
            message_to_send.value = ""
            page.update()

    def clear_context():
        nonlocal messages, messages_to_show
        if page.client_storage.get("system_prompt") is None or page.client_storage.get("system_prompt") == "":
            messages = [{"role": "system", "content": default_sys_prompt}]
        else:
            messages = [
                {"role": "system", "content": page.client_storage.get("system_prompt")}]
        messages_to_show.controls = []
        messages_to_show.controls.append(MessageView.MessageView(
            "S", "SYSTEM", "# 欢迎使用", page).get_widget())
        page.update()

    def set_system_prompt():
        def on_dialog_ok():
            nonlocal messages
            page.client_storage.set(
                "system_prompt", system_prompt_will_use.value)
            page.dialog.open = False
            if page.client_storage.get("system_prompt") is None or page.client_storage.get("system_prompt") == "":
                messages = [{"role": "system", "content": default_sys_prompt}]
            else:
                messages = [
                    {"role": "system", "content": page.client_storage.get("system_prompt")}]
            messages_to_show.controls = [MessageView.MessageView(
                "S", "SYSTEM", "# 欢迎使用", page).get_widget()]
            page.update()

        def on_dialog_cancel():
            page.dialog.open = False
            page.update()

        system_prompt_will_use = ft.TextField(
            label="提示词", value=page.client_storage.get("system_prompt"), multiline=True)
        page.dialog = ft.AlertDialog(title=ft.Text("设置系统提示词"),
                                     content=system_prompt_will_use,
                                     actions=[
                                         ft.TextButton(
                                             "完成", on_click=lambda _: on_dialog_ok()),
                                         ft.TextButton(
                                             "取消", on_click=lambda _: on_dialog_cancel())
                                     ])
        page.dialog.open = True
        page.update()

    view = ft.View("/chatgpt", controls=[
        ft.AppBar(title=ft.Text(value="ChatGPT")),
        ft.ResponsiveRow([
            ft.Column([
                model_will_use
            ], col={"sm": 6}),
            ft.Column([
                ft.TextButton("设置预设文本", on_click=lambda _: set_system_prompt())
            ], col={"sm": 6})
        ]),
        messages_to_show,
        ft.Row([
            message_to_send,
            ft.IconButton(icon=ft.icons.SEND,
                          on_click=lambda _: send_message()),
            ft.IconButton(icon=ft.icons.CLEAR,
                          on_click=lambda _: clear_context())
        ])
    ])

    return view
