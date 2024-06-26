import flet as ft
from stores.counter import state


def main(page: ft.Page):
    return ft.Text(
        "You have been count " + str(state["num"]) + "!",
        text_align=ft.TextAlign.CENTER,
        width=page.width,
        size=30,
    )
