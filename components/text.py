import flet as ft


class Text(ft.Text):
    def __init__(self, value):
        super().__init__()
        self.value = str(value)
        self.text_align = ft.TextAlign.CENTER
        self.width = 100
