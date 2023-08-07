import flet as ft
import openai
import threading
from widgets import MessageView


# while True:
#     reply: str = ""

def chat_gpt(page: ft.Page):
    openai.api_key = page.client_storage.get("openai_api_key")
    openai.api_base = "https://" + page.client_storage.get("openai_api_host") + "/v1"
    print(openai.api_key)
    print(openai.api_base)

    messages = [{"role": "system", "content": "你是一个AI大语言模型"}]
    messages_to_show = ft.ListView(spacing=5, expand=True, auto_scroll=True)
    messages_to_show.controls.append(MessageView.MessageView("S", "SYSTEM", "# 欢迎使用").get_widget())

    message_to_send = ft.TextField(label="Message", expand=True)

    model_will_use = ft.Dropdown(label="模型选择", options=[
        ft.dropdown.Option("claude-2-100k", "Claude2 100k"),
        ft.dropdown.Option("gpt-3.5-turbo-16k", "GPT-3.5 Turbo 16k"),
        ft.dropdown.Option("gpt-4", "GPT-4")
    ])

    def _send_msg():
        nonlocal messages_to_show
        messages.append({"role": "user", "content": str(message_to_send.value)})
        response = openai.ChatCompletion.create(
            model=model_will_use.value,
            messages=messages,
            stream=True
        )
        reply = ""
        messages_to_show.controls.append(MessageView.MessageView("R", "ROBOT", reply).get_widget())
        for chunk in response:
            try:
                reply += chunk.choices[0].delta.content
                messages_to_show.controls[-1] = MessageView.MessageView("R", "ROBOT", reply).get_widget()
                page.update()
            except Exception as e:
                messages.append({'role': 'assistant', 'content': str(reply)})
                print(e.args)

    def send_message():
        if not message_to_send.value == "":
            threading.Thread(target=_send_msg).start()
            messages_to_show.controls.append(MessageView.MessageView("U", "USER", message_to_send.value).get_widget())
            message_to_send.value = ""
            page.update()

    def clear_context():
        nonlocal messages, messages_to_show
        messages = [{"role": "system", "content": "你是一个AI大语言模型"}]
        messages_to_show.controls = []
        messages_to_show.controls.append(MessageView.MessageView("S", "SYSTEM", "# 欢迎使用").get_widget())
        page.update()


    view = ft.View("/tools/chat-gpt", controls=[
        ft.AppBar(title=ft.Text(value="ChatGPT")),
        ft.ListView([
            ft.Row([
                model_will_use
            ]),
            ft.Row([
                messages_to_show
            ]),
            ft.Row([
                message_to_send,
                ft.IconButton(icon=ft.icons.SEND, on_click=lambda _: send_message()),
                ft.IconButton(icon=ft.icons.CLEAR, on_click=lambda _: clear_context())
            ])
        ], expand=True, spacing=10, padding=10, auto_scroll=True)
    ])

    return view
