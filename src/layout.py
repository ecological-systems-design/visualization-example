# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px


def create_layout(df):
    accordion = create_some_element()
    rows = create_rows()
    layout = html.Div([
        html.Div(children='My First App with Data and a Graph'),
        dash_table.DataTable(data=df.to_dict('records'), page_size=10),
        dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
        rows,
        accordion,
    ])
    return layout


def create_rows():
    rows = html.Div([
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row([
            dbc.Col(html.Div("One of three columns"), width=1, style={"backgroundColor": "pink"}),
            dbc.Col(html.Div("One of three columns"), width=2, style={"backgroundColor": "yellow"}),
            dbc.Col(html.Div("One of three columns"), width=3, style={"backgroundColor": "red"}),
        ])
    ], style={"margin": "50px"})
    return rows


def create_some_element():
    accordion = html.Div(
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        html.P("This is the content of the first section"),
                        dbc.Button("Click here"),
                    ],
                    title="Item 1",
                ),
                dbc.AccordionItem(
                    [
                        html.P("This is the content of the second section"),
                        dbc.Button("Don't click me!", color="danger"),
                    ],
                    title="Item 2",
                ),
                dbc.AccordionItem(
                    "This is the content of the third section",
                    title="Item 3",
                ),
            ],
        )
    )
    return accordion
