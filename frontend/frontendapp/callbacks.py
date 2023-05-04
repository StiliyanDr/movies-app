import dash
from dash import ctx
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from frontendapp import database as db


def define_callbacks_for(app):
    @app.callback(
        Output("genres-dropdown", "options"),
        Input("genres-dropdown", "style")
    )
    def update_genre_options(style):
        if (ctx.triggered_id is None):
            return db.list_movie_genres()
        else:
            return dash.no_update

    @app.callback(
        Output("movies-table", "data"),
        Input("apply-button", "n_clicks"),
        State("title-input", "value"),
        State("genres-dropdown", "value"),
        State("length-slider", "value"),
        State("year-slider", "value")

    )
    def update_movies_table(n_clicks, title, genres, length, year):
        if (ctx.triggered_id is not None):
            return db.list_movies(title, genres, length, year)
        else:
            return dash.no_update

    @app.callback(
        Output("movie-poster", "src"),
        Output("movie-title", "children"),
        Output("movie-year", "children"),
        Output("movie-length", "children"),
        Output("movie-rating", "children"),
        Output("movie-genre", "children"),
        Output("movie-cast", "children"),
        Output("movie-plot", "children"),
        Input("view-button", "n_clicks"),
        State("movies-table", "data"),
        State("movies-table", "selected_rows"),
    )
    def update_movie_modal(view_clicks, movies, selected_movies):
        if (ctx.triggered_id is not None and selected_movies):
            m = movies[selected_movies[0]]

            return (
                m["image_url"],
                m["title"],
                str(m["year"]),
                str(m["length"]),
                m["rating"],
                m["genre"],
                m["cast"],
                m["plot"]
            )
        else:
            raise PreventUpdate()

    @app.callback(
        Output("movie-modal", "is_open"),
        Input("movie-title", "children"),
        Input("close-movie-modal-button", "n_clicks")
    )
    def toggle_movie_modal(title, close_clicks):
        return ctx.triggered_id == "movie-title"

    return app
