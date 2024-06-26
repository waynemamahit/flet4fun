import flet as ft

from layouts import app
from pages import about, index


def main(page: ft.Page):

    def route_change(e):
        page.views.clear()

        troute = ft.TemplateRoute(page.route)
        if troute.match("/about"):
            page.views.append(
                app.main(
                    page,
                    "/about",
                    about.main(page),
                )
            )
        else:
            page.views.append(app.main(page, "/", index.main(page)))

        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)
