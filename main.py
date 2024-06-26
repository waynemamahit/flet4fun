import flet as ft

import routes


def main(page: ft.Page):
    page.adaptive = True
    page.title = "My Counter App"

    routes.main(page)


ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=80)
