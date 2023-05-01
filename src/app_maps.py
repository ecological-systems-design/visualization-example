from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import geopandas as gpd


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.PULSE]
)

app.layout = html.Div([
    html.H4('Examples of urban form metrics by traffic zone (Verkehrszone) in Zurich'),
    html.P("Select a metric to show:"),
    dcc.RadioItems(
        id='column_to_show',
        options=[
            {'label': 'A: Density (residents + jobs) per km²', 'value': 'A'},
            {'label': 'B: Intersection per km²', 'value': 'B'},
            {'label': 'C: Relative road capacity (per residents + jobs)', 'value': 'C'},
        ],
        value="A",
        inline=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("column_to_show", "value"))
def display_choropleth(column_to_show):
    data = gpd.read_file('../data/zones_processed_zurich_epsg4326.gpkg', driver='GPKG')
    fig = px.choropleth_mapbox(
        data,
        geojson=data.geometry,
        color=column_to_show,
        locations=data.index,
        zoom=9,
        center={"lat": 47.363008, "lon": 8.541144})
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_style="carto-darkmatter",
        width=1200,
        height=650
        )
    fig.update_geos(fitbounds="locations")

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
