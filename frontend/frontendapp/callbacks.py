import dash
from dash import ctx
from dash.dependencies import Input, Output

from frontendapp import database as db


def define_callbacks_for(app):
    @app.callback(
        Output("movie-modal", "is_open"),
        Input("view-button", "n_clicks"),
        Input("close-movie-modal-button", "n_clicks")
    )
    def toggle_movie_modal(view_clicks, close_clicks):
        button_clicked = ctx.triggered_id

        return button_clicked == "view-button"

    @app.callback(
        Output("genres-dropdown", "options"),
        Input("genres-dropdown", "style")
    )
    def update_genre_options(style):
        if (ctx.triggered_id is None):
            return db.list_movie_genres()
        else:
            return dash.no_update

    return app
