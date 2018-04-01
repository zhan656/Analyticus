import pandas as pd
from states_trans import states
from config import api_key
import plotly
import plotly.plotly as py
class main():
    
    def per_year(data_all_years,state_pop, year):
        # Sum up all flu cases and flu percent in each state in given year
        df_state1 = data_all_years.loc[data_all_years['year']==year,:]
        df_grouped_flu = df_state1.groupby(['state']).sum()
        df_grouped_flu = pd.DataFrame(df_grouped_flu[['flu_cases','flu_percent']])
        # sum_cases = df_grouped_flu['flu_cases'].sum()
        # percent_flu = [(i/sum_cases)*100 for i in df_grouped_flu['flu_cases']]
        # df_grouped_flu['flu_percent'] = percent_flu
       
       # Accumulated Vaccination Rate and Cases in each state
        df_grouped_vac = df_state1.loc[df_state1['week']==52,['state','vac_percent','vaccinations']]
        df_grouped_vac.head()
        
        # Create a State Abbreviation table
        state_name_df = pd.DataFrame({"state":df_state1['state'].unique()})
        state_name_df['code'] = [states[i] for i in state_name_df['state']]
        state_name_df.head()
        
        # Add corresponding State code to grouped flu table
        df_grouped_flu['code'] = list(state_name_df['code'])
        df_grouped_flu['code'] =df_grouped_flu['code'].astype(str)
        df_grouped_flu.tail(10)
        
        # Add corresponding State code to grouped flu table
        df_grouped_vac['code'] = list(state_name_df['code'])
        df_grouped_vac['code'] = df_grouped_vac['code'].astype(str)
        df_grouped_vac.head(10)
        
        # df with both flu and vaccinations
        df_flu_vac = pd.merge(df_grouped_vac, df_grouped_flu, on="code")
        df_flu_vac['population'] = [float(state_pop.loc[st,str(year)]) for st in df_flu_vac['state']]
        df_flu_vac['flu_percent'] = df_flu_vac['flu_cases']/df_flu_vac['population']/10   
        return (df_flu_vac)
    
    
    def plot_heatmaps(df_flu_vac,year):
        
        # API key to 'Plotly'
        plotly.tools.set_credentials_file(username='zhan656', api_key=api_key)
        
        # Converting each Column name in 'df_flu_vac' to tring type
        for col in df_flu_vac.columns:
            df_flu_vac[col] = df_flu_vac[col].astype(str)
        
        # Color scale for flu map
        scl_flu = [[0.0, 'rgb(255, 230, 230)'],[0.1, 'rgb(255, 179, 179)'],[0.2, 'rgb(255, 128, 128)'],\
           [0.3, 'rgb(255, 77, 77)'],[0.4, 'rgb(255, 26, 26)'],[0.5, 'rgb(230, 0, 0)'],\
            [0.6, 'rgb(179, 0, 0)'],[0.7, 'rgb(153, 0, 0)'],[0.8, 'rgb(128, 0, 0)'],[0.9, 'rgb(102, 0, 0)'],\
           [1.0, 'rgb(51, 0, 0)']]
        
        # color scale in vaccinations map
        scl_vac = [[0.0, 'rgb(230, 247, 255)'],[0.1, 'rgb(179, 231, 255)'],[0.2, 'rgb(128, 215, 255)'],\
           [0.3, 'rgb(77, 198, 255)'],[0.4, 'rgb(26, 182, 255)'],[0.5, 'rgb(0, 157, 230)'],\
            [0.6, 'rgb(0, 139, 204)'],[0.7, 'rgb(0, 122, 179)'], [0.8, 'rgb(0, 105, 153)'],[0.9, 'rgb(0, 87, 128)'],\
           [1.0, 'rgb(0, 70, 102)']]
        
        # text in flu heatmap
        df_flu_vac['flu_text'] = df_flu_vac['code'] + '<br>' +\
                    "Flu Percentage: " + df_flu_vac['flu_percent'] + '<br>' +\
                    "Flu Cases: " + df_flu_vac['flu_cases']
        # text in vac heatmap
        df_flu_vac['vac_text'] = df_flu_vac['code'] + '<br>' +\
                    "Vaccination Percentage: " + df_flu_vac['vac_percent'] + '<br>' +\
                    "Vaccination Cases: " + df_flu_vac['vaccinations']
        
        # Data in flu heatmaps
        data_flu = [ dict(
                    type='choropleth',
                    colorscale = scl_flu,
                    autocolorscale = False,
                    locations = df_flu_vac['code'],
                    z = df_flu_vac['flu_percent'].astype(float),
                    locationmode = 'USA-states',
                    text = df_flu_vac['flu_text'],
                    marker = dict(
                        line = dict (
                            color = 'rgb(255,255,255)',
                            width = 2
                        ) ),
                    colorbar = dict(
                        title = "Flu Percentage")
                    ) ]
        
        # Data in vac heatmaps
        data_vac = [ dict(
                    type='choropleth',
                    colorscale = scl_vac,
                    autocolorscale = False,
                    locations = df_flu_vac['code'],
                    z = df_flu_vac['vac_percent'].astype(float),
                    locationmode = 'USA-states',
                    text = df_flu_vac['vac_text'],
                    marker = dict(
                        line = dict (
                            color = 'rgb(255,255,255)',
                            width = 1
                        ) ),
                    colorbar = dict(
                        title = "Vaccination Percentage")
                    ) ]
         
        # layout in flu heatmaps
        layout_flu = dict(
                title = '<b>Flu Percentage by State Heatmap {} - {}<b>'.format(str(year),str(year+1)),
                font = dict(size=18, color='rgb(0,0,0)'),
                geo = dict(
                    scope='usa',
                    projection=dict( type='albers usa' ),
                    showlakes = True,
                    lakecolor = 'rgb(255, 255, 255)'),
               
                     )
        
        # layout in vac heatmaps
        layout_vac = dict(
                title = '<b>Vaccination Percentage by State Heatmap {} - {}<b>'.format(str(year),str(year+1)),
                font = dict(size=18, color='rgb(0,0,0)'),
                geo = dict(
                    scope='usa',
                    projection=dict( type='albers usa' ),
                    showlakes = True,
                    lakecolor = 'rgb(255, 255, 255)'),
            
)
        # plotting 'flu' and 'vac'
        fig_flu = dict( data=data_flu, layout=layout_flu )
        url = py.plot( fig_flu, filename='flu_map'+str(year))
        fig_vac = dict( data=data_vac, layout=layout_vac)
        url = py.plot( fig_vac, filename='vac_map'+str(year))        

        