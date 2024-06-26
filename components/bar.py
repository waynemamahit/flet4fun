import flet as ft

from components.button import IconButton

menu = [
    {
        "name": "Home",
        "url": "/",
        "icon": ft.icons.HOME,
    },
    {
        "name": "About",
        "url": "/about",
        "icon": ft.icons.INFO,
    },
]


class AppBar(ft.AppBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.title = ft.Text("Counter App")
        self.actions = list(
            map(
                lambda el: IconButton(
                    el["icon"],
                    tooltip=el["name"],
                    on_click=lambda e: page.go(el["url"]),
                ),
                menu,
            )
        )
