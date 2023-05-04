from dash import (
    dcc,
    html,
)
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc

from frontendapp import constants as const


def define_layout_for(dash_app):
    dash_app.layout = html.Div([
        _title_layout_for(dash_app),
        _filter_options_layout_for(dash_app),
        _movies_table_layout_for(dash_app),
        _movie_modal_layout_for(dash_app),
    ])

    return dash_app


def _title_layout_for(app):
    return html.Div([
        dbc.Row(dbc.Col(
            html.H1("Movies DB"),
        ),
            style={"text-align": "center"}
        ),
        html.Hr(),
    ])


def _filter_options_layout_for(app):
    return html.Div([
        dbc.Row([
            dbc.Col(html.B("Title:"),
                    width="auto"),
            dbc.Col(dbc.Input(
                id="title-input",
                placeholder="Title...",
                type="text",
                size="small"
            ),
                width=5
            )
        ],
            style={"marginBottom": "15px"}
        ),
        dbc.Row([
            dbc.Col(html.B("Genres:"),
                    width="auto"),
            dbc.Col(dcc.Dropdown(
                [],
                placeholder="Genre...",
                id="genres-dropdown",
                searchable=True,
                multi=True,
            ),
                width=5
            ),
        ],
            style={"marginBottom": "35px"}
        ),
        dbc.Row([
            dbc.Col(html.B("Length (minutes):"),
                    width="auto"),
            dbc.Col(dcc.RangeSlider(
                min=0,
                max=const.MAX_MOVIE_LENGTH_MINS,
                step=1,
                value=[1, 120],
                id="length-slider",
                marks={
                    0: {
                        "label": str(0)
                    },
                    const.MAX_MOVIE_LENGTH_MINS: {
                        "label": str(const.MAX_MOVIE_LENGTH_MINS)
                    }
                },
                tooltip={
                    "placement": "bottom",
                    "always_visible": True
                }
            ),
                width=5
            )
        ],
            style={
                "marginTop": "5px",
                "marginBottom": "5px"
            }
        ),
        dbc.Row([
            dbc.Col(html.B("Year:"),
                    width="auto"),
            dbc.Col(dcc.RangeSlider(
                min=const.MIN_MOVIE_YEAR,
                max=const.MAX_MOVIE_YEAR,
                step=1,
                value=[1970, 2000],
                id="year-slider",
                marks={
                    const.MIN_MOVIE_YEAR: {
                        "label": str(const.MIN_MOVIE_YEAR)
                    },
                    const.MAX_MOVIE_YEAR: {
                        "label": str(const.MAX_MOVIE_YEAR)
                    }
                },
                tooltip={
                    "placement": "bottom",
                    "always_visible": True
                }
            ),
                width=5
            )
        ],
            style={
                "marginTop": "5px",
                "marginBottom": "5px"
            }
        ),
        dbc.Row(dbc.Col(dbc.Button(
            ["Apply filters"],
            id="apply-button",
            color="primary",
        )),
            style={
                "marginTop": "5px",
                "marginBottom": "5px"
            }
        ),
        html.Hr(),
    ])


def _movies_table_layout_for(app):
    return dbc.Row(dbc.Col(
        DataTable(
            [],
            columns=[{"name": c.capitalize(),
                      "id": c}
                     for c in const.MOVIES_TABLE_COLUMNS],
            page_current=0,
            page_size=const.MOVIES_TABLE_PAGE_SIZE,
            id="movies-table",
            editable=False,
            row_selectable="single",
            row_deletable=False,
        ),
        width=10
    ))


def _movie_modal_layout_for(dash_app):
    return html.Div([
        dbc.Row(dbc.Col(dbc.Button(
            ["View Selected Movie"],
            id="view-button",
            color="primary",
            className="d-grid gap-2",
        )),
            style={"marginTop": "15px"}
        ),
        dbc.Row(dbc.Col(dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Selected movie")),
            dbc.ModalBody(
                _modal_body_layout_for(dash_app)
            ),
            dbc.ModalFooter(dbc.Button(
                ["Close"],
                id="close-movie-modal-button",
                color="secondary",
            )),
        ],
            id="movie-modal",
            centered=True,
            scrollable=True,
            size="lg"
        ))),
    ])


def _modal_body_layout_for(dash_app):
    return html.Div([
        dbc.Row(dbc.Col(html.Img(id="movie-poster",
                                 alt="No poster available"))),
        dbc.Row([
            dbc.Col(html.B("Title:"), width="auto"),
            dbc.Col(html.P("", id="movie-title")),
            dbc.Col(html.B("Year:"), width="auto"),
            dbc.Col(html.P("", id="movie-year")),
        ]),
        dbc.Row([
            dbc.Col(html.B("Length:"), width="auto"),
            dbc.Col(html.P("", id="movie-length")),
            dbc.Col(html.B("Rating:"), width="auto"),
            dbc.Col(html.P("", id="movie-rating")),
        ]),
        dbc.Row([
            dbc.Col(html.B("Genre:"), width="auto"),
            dbc.Col(html.P("", id="movie-genre")),
        ]),
        dbc.Row([
            dbc.Col(html.B("Cast:"), width="auto"),
            dbc.Col(html.P("", id="movie-cast")),
        ]),
        dbc.Row([
            dbc.Col(html.B("Plot:"), width="auto"),
            dbc.Col(html.P("", id="movie-plot")),
        ])
    ])
