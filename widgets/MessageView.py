import flet as ft


class MessageView(object):
    def __init__(self, avatar_content: str, avatar_tooltip: str, message_content: str):
        self.avatar_content = avatar_content
        self.avatar_tooltip = avatar_tooltip
        self.message_content = message_content
        self.widget = ft.Card(
            ft.Container(
                ft.Row([
                    ft.CircleAvatar(content=ft.Text(self.avatar_content), tooltip=self.avatar_tooltip,
                                    bgcolor=ft.colors.BLUE_GREY_50),
                    ft.Markdown(self.message_content, selectable=True, extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                                code_theme="atom-one-dark", code_style=ft.TextStyle(font_family="Monospace"), expand=1)
                ])
                , padding=10)
        )

    def get_widget(self):
        return self.widget
