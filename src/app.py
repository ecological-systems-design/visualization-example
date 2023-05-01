from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px


# Read data
dataframe = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.PULSE]
)

# App layout
app.layout = html.Div([
    html.H1("Visualization example"),
    html.H2("My First App with Data and a Graph"),
    dash_table.DataTable(data=dataframe.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(dataframe, x='continent', y='lifeExp', histfunc='avg')),
])


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
