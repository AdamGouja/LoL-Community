from distutils.log import debug
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

dict_LFL =  [
    {'label' : 'GamersOrigin', 'value':'GO'},
    {'label' : 'GameWard', 'value':'GW'},
    {'label' : 'Karmine Corp', 'value':'KC'},
    {'label' : 'LDLC OL', 'value':'LDLC'},
    {'label' : 'Mirage Elyandra', 'value':'ME'},
    {'label' : 'Misfits Premier', 'value':'MSFP'},
    {'label' : 'Solary', 'value':'SLY'},
    {'label' : 'Team BDS Academy', 'value':'BDS'},
    {'label' : 'Team Oplon', 'value':'OPL'},
    {'label' : 'Vitality.Bee', 'value':'VITB'}
]

dict_LEC =  [
    {'label' : 'Astralis', 'value':'AST'},
    {'label' : 'Excel', 'value':'XL'},
    {'label' : 'Fnatic', 'value':'FNC'},
    {'label' : 'G2 Esports', 'value':'G2'},
    {'label' : 'MAD Lions', 'value':'MAD'},
    {'label' : 'Misfits Gaming', 'value':'MSF'},
    {'label' : 'Rogue', 'value':'RGE'},
    {'label' : 'SK Gaming', 'value':'SK'},
    {'label' : 'Team BDS', 'value':'BSD'},
    {'label' : 'Team Vitality', 'value':'VIT'}
]

if __name__ == '__main__':

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
                            {'label': 'Interaction per user', 'value':'interaction'}
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
                                    {'label' : 'Ligue Européenne (LEC)', 'value' : 'LEC'}
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
                            dcc.RangeSlider(
                                id='date_range',
                                marks={-1:'14/11/2021',0:'21/12/2021',1:'12/01/2021',2:'30/01/2021'},
                                min=-1,
                                max=2,
                                value = [-1,2]
                            )
                        ],
                        hidden = False
                    ),

                    html.Div(
                        id='check_team_div',
                        children=[
                            html.H3(
                                children='Team(s) Choice'
                            ),
                            dcc.Checklist(
                                id="check_all",
                                options=[{"label": "Check/Uncheck All", "value": "All"}],
                                value=[],
                                labelStyle={"display": "inline-block"},
                            ),
                            html.H3(),
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
                        children = dcc.Graph(id='graph_figure'),
                        hidden=True
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
                        hidden=False
                    ),
                    
                ],
                style={'border-left':'1px gray solid','flex': 3,'padding': 10}
            )
        ],
        style={'display': 'flex', 'flex-direction': 'row'}
    )

    ###### CALLBACK

    @app.callback(
        Output(component_id="check_team", component_property="value"),
        [Input(component_id="check_all", component_property="value")],
        [State(component_id="check_team", component_property="options")],
    )
    def select_all_none(all_selected, options):
        """
        Select or unselect all the choices in the team choices.
        """
        all_or_none = []
        all_or_none = [option["value"] for option in options if all_selected]
        return all_or_none

    @app.callback(
        Output(component_id="check_team", component_property="options"),
        [Input(component_id="league_choice", component_property="value")]
    )
    def change_team(input_value):
        """
        Select or unselect all the choices in the team choices.
        """
        if input_value == 'LFL':
            return dict_LFL
        else:
            return dict_LEC

    @app.callback(
        [Output(component_id="check_team_div", component_property="hidden"),
        Output(component_id="league_choice_div", component_property="hidden")],
        [Input(component_id="graph_choice", component_property="value")]
    )
    def hide(input_value):
        if input_value == 'interaction':
            return [True, True]
        else :
            return [False, False]

    app.run_server(debug=True)
