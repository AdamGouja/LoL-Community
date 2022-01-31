from distutils.log import debug
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

import plotly.express as px
import pandas as pd
import pymongo
from pymongo import MongoClient
from datetime import datetime
import sys
sys.path.insert(0, './src')

from main import main_function

dict_LFL =  [
    {'label' : 'GamersOrigin', 'value':'Gamers Origin'},
    {'label' : 'GameWard', 'value':'Gameward'},
    {'label' : 'Karmine Corp', 'value':'KCORP'},
    {'label' : 'LDLC OL', 'value':'LDLC OL'},
    {'label' : 'Mirage Elyandra', 'value':'Mirage Elyandra'},
    {'label' : 'Misfits Premier', 'value':'Misfits Academy'},
    {'label' : 'Solary', 'value':'Solary'},
    {'label' : 'Team BDS Academy', 'value':'BDS Academy'},
    {'label' : 'Team Oplon', 'value':'Team Oplon'},
    {'label' : 'Vitality.Bee', 'value':'Vitality Bee'}
]

dict_LEC =  [
    {'label' : 'Astralis', 'value':'Astralis'},
    {'label' : 'Excel', 'value':'Excel'},
    {'label' : 'Fnatic', 'value':'Fnatic'},
    {'label' : 'G2 Esports', 'value':'G2'},
    {'label' : 'MAD Lions', 'value':'Mad Lions'},
    {'label' : 'Misfits Gaming', 'value':'Misfits'},
    {'label' : 'Rogue', 'value':'Rogue'},
    {'label' : 'SK Gaming', 'value':'SK Gaming'},
    {'label' : 'Team BDS', 'value':'BDS'},
    {'label' : 'Team Vitality', 'value':'Vitality'}
]
list_all_values =  ['Gamers Origin','Gameward','KCORP','LDLC OL','Miage Elyandra','Misfits Academy','Solary','BDS Academy','Team Oplon','Vitality Bee',
'Astralis','Excel','Fnatic','G2','Mad Lions','Misfits','Rogue','SK Gaming','BDS','Vitality']

dict_all = dict_LFL+dict_LEC

main_function()

client = MongoClient('localhost',27017)
db = client.project

all_data = db['all_data']
tag = db['tweets_tag']
users = db['tweets_user']
tweets = db["tweets_day"]
query = {'$or': [{'tag': 'KCORP'}]}

if __name__ == '__main__':
    

    tweets_date = px.line(
        pd.DataFrame(list(tag.find(query))),
        x='date',
        y='count',
        color='tag'
    )
     
    users_pie = px.pie(
        pd.DataFrame(list(users.find())),
        values='interaction', 
        names='username', 
    )

    interaction_per_date = px.line(
        pd.DataFrame(list(tweets.find())),
        x='date',
        y='interaction'
    )


    app = dash.Dash(__name__)



    app.layout = html.Div(
        children=[
            html.Div(
                id='nav_bar',
                children=[
                    html.H2(children='Graph choice'),
                    dcc.Dropdown(
                        id='graph_choice',
                        clearable=False,
                        options=[
                            {'label': 'Tweets per day', 'value':'tweets'},
                            {'label': 'Interaction per user', 'value':'interaction'},
                            {'label': 'Interaction per day', 'value':'interaction_2'}
                        ],
                        value='tweets'
                    ),

                    html.Hr(),


                    html.H2(children='Graph settings'),

                    html.Div(
                        id='league_choice_div',
                        children = [
                            html.H3(children='League Choice'),
                            dcc.Dropdown(
                                id='league_choice',
                                options = [
                                    {'label' : 'Ligue Française (LFL)', 'value' : 'LFL'},
                                    {'label' : 'Ligue Européenne (LEC)', 'value' : 'LEC'},
                                    {'label' : 'LEC & LFL', 'value' : 'all'}
                                ],
                                clearable=False,
                                value = 'LFL'
                            ),
                        ],
                        hidden=False
                    ),                    

                    html.Div(
                        id='date_range_div',
                        children=[
                            html.H3(children='Date range'),
                            dcc.DatePickerRange(
                                id='date_range',
                                min_date_allowed=datetime.strptime('2021-11-14', "%Y-%m-%d").date(),
                                max_date_allowed=datetime.strptime('2022-01-30', "%Y-%m-%d").date(),
                                initial_visible_month=datetime.strptime('2021-11-14', "%Y-%m-%d").date(),
                                end_date=datetime.strptime('2021-01-30', "%Y-%m-%d").date(),
                                start_date=datetime.strptime('2021-11-14', "%Y-%m-%d").date(),
                            ),
                        ],
                        hidden = True
                    ),

                    html.Div(
                        id='check_team_div',
                        children=[
                            html.H3(
                                children='Team(s) Choice'
                            ),
                            dcc.Checklist(
                                id='check_team',
                                options = dict_LFL,

                                labelStyle={'display': 'block'}
                            ) 
                        ],
                        hidden = False
                    ),

                    html.Hr(),

                    html.Div(children='Clément MAURER & Adam GOUJA -- ESIEE PARIS')                    
                ],
                style={'flex': 1,'padding': 10}
            ),
            html.Div(
                id='fig',
                children=[
                    html.H1(id='graph_title'),

                    html.Div(
                        id='figure_display',
                        children = dcc.Graph(id='graph_figure',figure=tweets_date),
                        hidden=False
                    ),

                    html.Div(
                        id='map_display',
                        children = html.Iframe
                        (
                            id='map', 
                            style={'display': 'block'},
                            height='400px',
                            width='100%'
                        ),
                        hidden=True
                    ),
                    
                ],
                style={'border-left':'1px gray solid','flex': 3,'padding': 10}
            )
        ],
        style={'display': 'flex', 'flex-direction': 'row'}
    )

    ###### CALLBACK

    @app.callback(
        Output(component_id="check_team", component_property="options"),
        [Input(component_id="league_choice", component_property="value")]
    )
    def change_teams(input_value):
        """
        Select or unselect all the choices in the team choices.
        """
        if input_value == 'LFL':
            return dict_LFL
        elif input_value == 'LEC':
            return dict_LEC
        else :
            return dict_all

    @app.callback(
        [Output(component_id="check_team_div", component_property="hidden"),
        Output(component_id="league_choice_div", component_property="hidden"),
        Output(component_id="graph_title",component_property="children"),
        Output(component_id="graph_figure",component_property="figure")],
        [Input(component_id="graph_choice", component_property="value"),
        Input(component_id="check_team", component_property="value")]
    )
    def hide_and_title(input_value,team):
        
        if not team:
            team = list_all_values

        tags = team
        liste = []
        dic = {}
        for i in tags:
            dic['tag'] = i
            liste.append(dic.copy())
        Query = {"$or" : liste}

        if input_value == 'interaction':
            return [True, True, "Most interacted users since the beginning of the Season", users_pie]
        elif input_value == 'tweets' :
            return [False, False, "Number of tweets per day per Topic since the beginning of the Season",px.line(
            pd.DataFrame(list(tag.find(Query))),
            x='date',
            y='count',
            color='tag'
        )]
        else :
            return [True, True, "Number of interactions per day since the beginning if the Season", interaction_per_date]


    app.run_server(debug=False)
