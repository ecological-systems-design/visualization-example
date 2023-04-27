from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

# Local files
from layout import create_layout


# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.PULSE]
)

# App layout
app.layout = create_layout(df)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
