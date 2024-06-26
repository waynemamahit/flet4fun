import flet as ft

from components.button import IconButton
from components.text import Text
from stores.counter import state


def main(page: ft.Page) -> ft.Row:

    def minus_click(e):
        global state
        state["num"] = state["num"] - 1
        render()

    def plus_click(e):
        global state
        state["num"] = state["num"] + 1
        render()

    # Reactive Element
    def render():
        txt_label.value = str(state["num"])
        txt_label.update()
    
    txt_label = ft.Text(
        value=str(state['num']),
        text_align=ft.TextAlign.CENTER,
        size=25,
        weight=ft.FontWeight.BOLD
    )

    return ft.Row(
        wrap=True,
        width=page.width,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            IconButton(ft.icons.REMOVE, on_click=minus_click),
            txt_label,
            IconButton(ft.icons.ADD, on_click=plus_click),
        ],
    )
