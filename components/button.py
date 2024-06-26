from typing import Any

import flet as ft


class IconButton(ft.IconButton):
    def __init__(self, icon: str, on_click: Any | None, tooltip=""):
        super().__init__()
        self.icon = icon
        self.tooltip = tooltip
        self.on_click = on_click
        self.adaptive = True
