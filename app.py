from flask import Flask, jsonify, request
import dash
from dash import html
from dash import dcc
from dash import Input, Output, State

app = Flask(__name__)

steel_news = [{
    "Title": "Steel Industry Shows Resilience Amid Global Challenges",
    "Source": "Industry Insider",
    "Date": "2023-11-10",
    "Reliability Score": 5
    },
{
    "Title": "Innovations in Stainless Steel Production Lead to Cost Reductions",
    "Source": "MetalTech Weekly",
    "Date": "2023-11-11",
    "Reliability Score": 7
}]

GPTs_list = [{"GPT name":["GPT A","GPT B", "GPT C", "GPT D"]}]

# Endpoint to get price information
@app.route('/news', methods=['GET'])
def get_price():
    return jsonify(steel_news)

# Endpoint to update price information
@app.route('/news', methods=['POST'])
def update_price():
    data = request.get_json()
    steel_news["news"] = data["news"]
    return jsonify(steel_news)

# Endpoint for home page that returns steel_news
@app.route('/home', methods=['GET'])
def get_home_data():
    return jsonify({"news": steel_news})

# Initialize Dash app
dash_app = dash.Dash(__name__, server=app)

# Define layout using Dash components
dash_app.layout = html.Div(children=[
                                    html.Div([
                                        html.H1("Reliability Scoring",style={'textAlign': 'left', 'font-size': 24, 'color': '#503D36'}),

                                        dcc.Tabs(id='tabs-example-1', value='tab-1', children=[
                                            dcc.Tab(label='Tab one', value='tab-1'),
                                            dcc.Tab(label='Tab two', value='tab-2'),
                                        ]),
                                        html.Div(id='tabs-example-content1'),
                                    ])

])


@dash_app.callback(Output('tabs-example-content1', 'children'),
              [Input('tabs-example-1', 'value')])

#render price content in tab1
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([    
                html.H3('Steel news'),
                
                dcc.Checklist(['step 1'],
                                inline=True
                            ),

                html.Table([
                    html.Tr([
                        html.Th("Title", style={'text-align': 'left', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Th("Source", style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Th("Date", style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'})
                    ])

                ] + [
                    html.Tr([
                        html.Td(news["Title"], style={'text-align': 'left', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Td(news["Source"], style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Td(news["Date"], style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'})    
                    ])
                    for news in steel_news
                ])
            ]),

            html.Div([   
                dcc.Checklist(['step 2'],
                                inline=True
                            ),

                html.Table([
                    html.Tr([
                        html.Th("GPT name", style={'text-align': 'left', 'border': 'solid 1px black', 'padding': '1rem'})
                    ])

                ] + [

                    html.Tr([
                        html.Td(name["GPT name"], style={'text-align': 'left', 'border': 'solid 1px black', 'padding': '1rem'})  
                    ])
                    for name in GPTs_list
                ])
            ]),

            html.Div([   
                dcc.Checklist(['step 3'],
                                inline=True
                            ),

                html.Table([
                    html.Tr([
                        html.Th("Title", style={'text-align': 'left', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Th("Source", style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Th("Date", style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Th("Reliability Score", style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'})
                    ])
                ] + [
                    html.Tr([
                        html.Td(news["Title"], style={'text-align': 'left', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Td(news["Source"], style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Td(news["Date"], style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem'}),
                        html.Th(news["Reliability Score"], style={'text-align': 'center', 'border': 'solid 1px black', 'padding': '1rem',}) 
                    ])
                    for news in steel_news
                ])
            ])

        ])
    else:
        return '404 - Page not found'

# Run app
if __name__ == '__main__':
    app.run(debug=True)


