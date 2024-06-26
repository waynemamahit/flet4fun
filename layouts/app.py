import flet as ft

from components.bar import AppBar


def main(page: ft.Page, route: str | None, control: ft.Control):
    return ft.View(
        adaptive=True,
        route=route,
        controls=[
            AppBar(page),
            control,
        ],
    )
