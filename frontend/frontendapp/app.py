from dash import Dash
import dash_bootstrap_components as dbc

from frontendapp.callbacks import define_callbacks_for
from frontendapp.layout import define_layout_for


app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP])
app = define_layout_for(app)
app = define_callbacks_for(app)
