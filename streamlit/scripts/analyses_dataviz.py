# Import des packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import pandas as pd
import plotly_express as px
import plotly.offline as pyo
from plotly.subplots import make_subplots
import plotly.graph_objs as go

import warnings
warnings.filterwarnings('ignore')

###############################

def analyses_dataviz():
    #st.image("img/paris_futur.jpg",)
    credit_text = "Crédit : [Futura Sciences](https://www.futura-sciences.com/planete/actualites/rechauffement-climatique-brutalite-rechauffement-climatique-actuel-nous-precipite-t-elle-vers-transition-phase-98756/)"
    st.image("img/climat-terre-chaos.png",)
    st.markdown(credit_text)
    
    st.write(" ")
    st.markdown('''
    <div class="box">
       <h3 class="title is-3 has-text-info has-text-centered">Berkeley earth</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.write(" ")
    st.markdown('''
    Les données sources traitées dans cette partie proviennent des Data sets disponibles sur le site de Berkeley Earth. Cette organisation indépendante américaine se consacre à la science des données environnementales et agrège différentes sources, notamment l'analyse GISTEMP réalisée sous l'égide de la NASA.

    Pour nos analyses, nous utilisons les ensembles de données suivants :

    Températures globales :

        Complete_TAVG_complete.txt : il s'agit de la liste des températures globales moyennes sur les terres.

    Températures par hémisphère :

        northern-hemisphere-TAVG-Trend.txt : cette liste contient les températures moyennes de l'hémisphère nord.
        southern-hemisphere-TAVG-Trend.txt : il s'agit de la liste des températures moyennes de l'hémisphère sud.

    Ces fichiers contienent un résumé détaillé des résultats moyens de la surface terrestre obtenus par la méthode de calcul de Berkeley. Les températures sont en degrés Celsius et sont rapportées en tant qu'anomalies par rapport à la moyenne de janvier 1951 à décembre 1980. Les incertitudes représentent l'intervalle de confiance à 95% pour les effets de sous-échantillonnage statistique et spatial. Cette période a été sélectonnée en raison de sa fiabilité et de son exhaustivité en termes d'observations, mais surtout parce qu'elle représente une médiane pour l'ensemble des données du jeu de données. En règle générale, la moitié des données se situent en dessous de ces valeurs de référence, tandis que l'autre moitié se trouve au-dessus. 
    ''', unsafe_allow_html=True)
    st.write(" ")
    st.markdown('''
                <h3 class="title is-3  has-text-centered">Température moyenne globale</h3>
    ''', unsafe_allow_html=True)
    
    st.write(" ")
    st.markdown('''Nous commençons par traiter les données de température moyenne (temperature average).''', unsafe_allow_html=True)
    st.markdown('''Pour déterminer la température absolue d'un mois spécifique, il est nécessaire d'ajouter la valeur d'anomalie correspondante du même mois dans la liste de référence des températures (période 1951-1980).
    Les références nous permettent de calculer les températures en termes de valeurs absolues. 
    Ces références sont stockées dans l'entête du fichier de donnée téléchargé et sont à retrouver dans le fichier d'origine txt à partir de la ligne 54 et 55 du jeu de données ''', unsafe_allow_html=True)
    
    st.markdown(''' voici le tableau de référence pour les temperatures moyennes globales :  
                
        mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ref = [2.60, 3.20, 5.29, 8.28, 11.27, 13.42, 14.30, 13.84, 12.05, 9.21, 6.08, 3.63]
        month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        ''', unsafe_allow_html=True)
        
    st.write(" ")
    st.markdown(" A partir de ce tableau de référence, nous calculons la temperature moyenne absolue sans incertitude.")
    
    headers = ['Year', 'Month', 'Anomaly-Gl', 'Uncertainty-Gl']
    
    df = pd.read_csv('./datasets/Complete_TAVG_complete.txt', header = 33, sep='\s+', names = headers, index_col=False)
    df = df.rename({'Year':'year' ,'Month':'month', 'Anomaly-Gl':'anomaly', 'Uncertainty-Gl':'uncert'}, axis=1)
    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ref = [2.60, 3.20, 5.29, 8.28, 11.27, 13.42, 14.30, 13.84, 12.05, 9.21, 6.08, 3.63]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    df_ref = pd.DataFrame({'mois': mois, 'ref': ref, 'month': month})
    for index, row in df.iterrows():
        month = row['month']
        valeur = df_ref.loc[df_ref['month'] == month]['ref'].values[0]
        df.loc[index, 'ref'] = valeur
    df["temp_abs"] = df["anomaly"] + df["ref"]
    df = df.drop("ref", axis = 1)
    df.insert(0, 'date', pd.to_datetime(df['year'].map(str) + '-' + df['month'].map(str) + '-15'))
    st.write(" ")
    st.write("Nous choisissons de remplir les colonnes manquantes par la moyenne. En raison du faible nombre de données manquantes, ce choix n'aura pas d'effet négatif sur les calculs.")
    df = df.fillna(df.mean())
    df['moy_mobile']=df['temp_abs'].rolling(12).mean()
    st.write(" ")
    st.markdown('''Les colonnes que nous n'avons pas retenues lors du chargement des données rapportent les anomalies et incertitudes sous la forme de moyennes glissantes annuelles, quinquennales, décennales et vicennales, centrées sur le mois considéré.
    Par exemple, la moyenne annuelle de janvier à décembre 1950 est rapportée à juin 1950, ce qui explique la présence de « NaNs » en début et fin de ces colonnes dans les Data Sets.
    ''', unsafe_allow_html=True)
    st.write(" ")
    st.write("Nous avons fait le choix de calculer notre moyenne glissante par an (soit pour 12 mois glissants) avec la méthode rolling() de Pandas")
    
    st.write(" ")
    if st.button("Afficher l'entête du dataframe"):
        st.write(df.head(15))
    
    sns.set_theme()
    fig = plt.figure(figsize=(20,7))
    sns.lineplot(x='date', y='moy_mobile', data =df ,color='red', ci= None, label='Moyenne glissante sur 12 mois')
    st.pyplot(fig);
      
    st.write(" ")
    st.write("Par la suite nous affichons le même graphique que le précédent mais cette fois-ci en ajoutant les températures moyennes mensuelles")
    
    # Set the figure size and grid.
    fig1= plt.figure(figsize=(24,10))
    plt.grid(color='grey', alpha=0.2)
    
    # Display line for monthly measures
    plt.plot(df['date'], df['temp_abs'], c='lightgrey', zorder=1)
    # Display points (circles) for monthly measures
    plt.scatter(df['date'], df['temp_abs'], c=df['temp_abs'], cmap='jet', s=15, zorder=2,
              label='Moyennes mensuelles')
    # Display 12-months moving average as a straight, larger line.
    plt.plot(df['date'], df['moy_mobile'], color='k', linewidth=2, label='Moyenne glissante sur 12 mois')
    
    # Add the cmap.
    plt.colorbar()
    plt.clim(df['temp_abs'].min(), df['temp_abs'].max())
    
    # Labels, legend, title.
    plt.xlabel('Date (par mois)')
    plt.ylabel('Température absolue en °C')
    plt.legend()
    plt.title('Evolution des températures globales par mois');
    st.pyplot(fig1)   
    
    st.info("On observe sur le graphique ci-dessus des variations saisonières correspondant à chaque année, matérialisées par les bandes de couleurs. La moyenne glissante semble confirmer une hausse relativement constante des températures.")
    
    if st.button("Afficher l'incertitude"):
        temp_year = df[:-1][['year', 'temp_abs', 'uncert']].groupby('year').mean().reset_index()
        # Set the figure size and grid.
        fig2 = plt.figure(figsize=(24,10))
        plt.grid(color='grey', alpha=0.2)
        
        # Display absolute temperatures.
        plt.plot(temp_year['year'], temp_year['temp_abs'], c='grey', zorder=1)
        
        plt.scatter(temp_year['year'], temp_year['temp_abs'],
              edgecolor='none', zorder=2, label='Moyennes annuelles')
        plt.fill_between(temp_year['year'], 
                 temp_year['temp_abs'] - temp_year['uncert'], 
                 temp_year['temp_abs'] + temp_year['uncert'],
                     color='#D3D3D3', zorder=0, label='Incertitude')
        plt.colorbar()
        plt.clim(temp_year['temp_abs'].min(), temp_year['temp_abs'].max())
        
        # Labels, legend, title.
        plt.xlabel('Date (par annnée)')
        plt.ylabel('Température absolue en °C')
        plt.title('Evolution des températures globales (surface terres uniquement) par an, avec incertitude')
        plt.legend();
        st.pyplot(fig2) 
    
#######################################
    st.write(" ")
    st.markdown('''
                <h3 class="title is-3  has-text-centered">Analyse des données par hémishères Nord et Sud</h3>
    ''', unsafe_allow_html=True)
    
    headers = ['Year', 'Month', 'Anomaly-NH', 'Uncertainty-NH']

    df_North = pd.read_csv('./datasets/northern-hemisphere-TAVG-Trend.txt', header = 69, sep='\s+', names = headers, index_col=False)
    df_North = df_North.rename({'Year':'year' ,'Month':'month', 'Anomaly-NH':'north_anomaly', 'Uncertainty-NH':'north_uncert'}, axis=1)
    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ref = [-2.06, -0.04,  4.57, 10.35, 15.74, 19.67, 21.32, 20.21, 16.63, 10.99, 4.52, -0.38]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    df_ref_North = pd.DataFrame({'mois': mois, 'ref': ref, 'month': month})
    
    for index, row in df_North.iterrows():
        month = row['month']
        valeur = df_ref_North.loc[df_ref_North['month'] == month]['ref'].values[0]
        df_North.loc[index, 'ref'] = valeur
    
    df_North["north_temp_abs"] = df_North["north_anomaly"] + df_North["ref"]
    
    df_North['north_moy_mobile']=df_North['north_temp_abs'].rolling(12).mean()
    df_North = df_North.drop("ref", axis = 1)
    
    # importation du jeu de données des températures de l'hémisphère Sund: southern-hemisphere-TAVG-Trend.txt
    headers_2 = ['Year', 'Month', 'Anomaly-SH', 'Uncertainty-SH']
    
    df_South = pd.read_csv('./datasets/southern-hemisphere-TAVG-Trend.txt', header = 69, sep='\s+', names = headers_2, index_col=False)
    df_South["Year"] = df_South["Year"].astype("int")
    df_South = df_South.rename({'Year':'year', 'Month':'month', 'Anomaly-SH':'south_anomaly', 'Uncertainty-SH':'south_uncert'}, axis=1)

    # les références sont à retrouver dans le fichier d'origine txt à partir de la ligne 54 et 55 du jeux de données
    
    mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ref = [ 20.81, 20.10, 18.76, 16.60, 14.57, 12.81, 12.34, 13.50, 15.48, 17.41, 19.30, 20.44]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    df_ref_South = pd.DataFrame({'mois': mois, 'ref': ref, 'month': month})
    
    df_South["year"] = df_South["year"].astype(int)
    
    for index, row in df_North.iterrows():
        month = row['month']
        valeur = df_ref_South.loc[df_ref_South['month'] == month]['ref'].values[0]
        df_South.loc[index, 'ref'] = valeur
    
    # Supprimer les lignes contenant des valeurs non valides dans la colonne "year"
    df_South = df_South.dropna(subset=["year"]).copy()
    
    # Convertir la colonne "year" en entier
    df_South["year"] = df_South["year"].astype(int)
    
    # Effectuer les autres opérations
    df_South["south_temp_abs"] = df_South["south_anomaly"] + df_South["ref"].astype(float)
    df_South['south_moy_mobile'] = df_South['south_temp_abs'].rolling(12).mean()
    df_South = df_South.drop("ref", axis=1)

    # fusion des deux datasets
    
    df_hemisphere = df_North.merge(right = df_South, on = ['year', 'month'], how = 'outer')     
    # Exportation Dataframe de températures_hémisphériques
    df_hemisphere.to_csv("temp_hemispheres.csv")
    
    fig3 = plt.figure(figsize=(24,10))
    plt.grid(color='grey', alpha=0.2)# Compute average absolute temperatures by year
    temp_year = df_hemisphere.groupby('year').mean().reset_index()
    
    # 
    plt.plot(temp_year['year'], temp_year['north_temp_abs'], c= "b", label = 'Hémisphère N')
    plt.fill_between(temp_year['year'], 
               temp_year['north_temp_abs'] - temp_year['north_uncert'], 
               temp_year['north_temp_abs'] + temp_year['north_uncert'],
               color="blue", alpha = 0.2, label=('Incertitude '+ 'Hémisphère N'))
    
    plt.plot(temp_year['year'], temp_year['south_temp_abs'], c= "r", label = 'Hémisphère S')
    plt.fill_between(temp_year['year'], 
               temp_year['south_temp_abs'] - temp_year['south_uncert'], 
               temp_year['south_temp_abs'] + temp_year['south_uncert'],
               color="red", alpha = 0.2, label=('Incertitude '+ 'Hémisphère S'))
 
    plt.xlabel('Date (par année)')
    plt.ylabel('Température absolue en °C')
    plt.title('Evolution comparée des températures dans les 2 hémisphères')
    plt.legend();
    st.write(" ")
    st.write("Nous chargeons par la suite les données relatives aux hémisphères nord et sud. L'objectif est de comparer la hausse des températures selon les hémisphères")
    st.write(" ")
    st.pyplot(fig3) 
    st.write(" ")
    st.info("On remarque sur le graphique ci-dessus une tendance nette à la hausse dans les 2 hémisphères. Les températures mesurées dans l'hémisphère sud maintiennent un écart positif de 6°C env. par rapport à l'hémisphère nord.")
    st.divider()
    st.write("Après avoir fait notre comparaison, nous avons fusionné les trois datasets afin d'avoir un seul dataset. Nous utilisons par la suite ce dataset pour afficher un diagrame polaire")
    st.write(" ")
    st.info("Le diagramme polaire permet d'avoir une vue globale de l'évolution des températures sur une période donnée. Les données sont représentées sous forme de courbes circulaires, ce qui facilite la comparaison des valeurs à différents moments ou emplacements.")
    st.info("Un diagramme polaire permet d'avoir une visualisation des changements dans le temps : En utilisant un diagramme polaire interactif, nous pouvons représenter les données de températures sur différentes périodes de temps (par exemple, année par année) et observer les changements au fil du temps. Cela permet d'identifier les tendances à long terme et les variations interannuelles")
    global_and_hem = df.merge(right = df_hemisphere, on = ['year', 'month'], how = 'outer')
    global_and_hem[1500:2500]
    # create a dictionary to map numeric values to month names
    month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                   7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    
    # replace numeric values in Month column with month names
    global_and_hem['month_str'] = global_and_hem['month'].replace(month_names)

    # Diagramme polaire des Anomalies de température par mois
    
    # create subplots with polar charts
    fig4 = make_subplots(rows=1, cols=1, subplot_titles=('',),
                        specs=[[{'type': 'polar'}]])
    
    # create traces for each year, with a slider to select the year
    for year in global_and_hem['year'].unique():
        trace = go.Scatterpolar(r=global_and_hem[global_and_hem['year']==year]['anomaly'],
                                theta=global_and_hem[global_and_hem['year']==year]['month_str'],
                                name=str(year), # convert Year in string
                                showlegend=False)
        fig4.add_trace(trace)
    
    # adjust polar plot layout
    fig4.update_layout(polar=dict(radialaxis=dict(range=[-3, 3])),
    updatemenus=[dict(type='buttons',
          showactive=False,
          buttons=[dict(label='Play',
                        method='animate',
                        args=[None, {'frame': {'duration': 100, 'redraw': True},
                                     'fromcurrent': True,
                                     'transition': {'duration': 0}}]),
                   dict(label='Pause',
                        method='animate',
                        args=[[None], {'frame': {'duration': 0, 'redraw': False},
                                       'mode': 'immediate',
                                       'transition': {'duration': 0}}])])],
    sliders=[dict(active=0,
       yanchor='top',
       xanchor='left',
       currentvalue=dict(font=dict(size=16), prefix='Year: ', visible=True, xanchor='right'),
       pad=dict(t=35, r=20),
       len=0.9,
       steps=[dict(label=str(year),
                   method='update',
                   args=[{'visible': [(i == j) for j in range(len(global_and_hem['year'].unique()))]},
                         {'title': "Anomalies de température globales pour l'année {}".format(year)}])
          for i, year in enumerate(global_and_hem['year'].unique())])])
    
    fig4.update_layout(width=1000, height=600)
    st.write(fig4)
    st.info("Le diagramme polaire ci-dessus montre l'évolution des températures au fil des années. Vers les années 1750 les anomalies de températures se rapprochent plus du centre, ce qui indique une température basse. En faisant défiler les années, on remarque que les courbes s'éloignent du centre et montrent nettement un tendance à la hausse des anomalies de températures. Le phénomène de réchauffement climatique semble être réel.")
    
    
   
 # #####################################################
    st.divider() 
    st.write(" ")
    st.markdown('''
    <div class="box">
       <h3 class="title is-3 has-text-info has-text-centered">Nasa GISS Temperature analysis</h3>
    </div>
   ''', unsafe_allow_html=True)
    st.write(" ")
    st.warning(" Dans cette partie de notre analyse, nous chargeons les données issues du site de la NASA. Nous commenceons le dataset 'global_temperature.csv'. ")
    df_nasa = pd.read_csv('./datasets/global_temperature.csv', sep=",", skiprows=1)
    df_nasa = df_nasa.replace(['***'], np.nan)
    df_nasa.fillna(method='bfill', inplace=True)
   # Nettoyage des données
    df_nasa = df_nasa.drop(df_nasa.columns[[ 14,15,16,17,18]], axis=1) # Supprimer la première colonne et la colonne inutile
    df_nasa = df_nasa.dropna() # Supprimer les lignes avec des valeurs manquantes
    
    # Ajouter une colonne pour la température moyenne annuelle
    df_nasa['annual_mean'] = df_nasa.iloc[:, 1:13].mean(axis=1)
    
    # Afficher les 5 premières lignes du jeu de données
    
    # Modification des type de valeurs

    dictionnaire = {'Jan': 'float', 'Feb':'float', 'Mar':'float',
                    'Apr':'float', 'May':'float','Jun':'float',
                    'Jul':'float', 'Aug':'float', 'Sep':'float',
                    'Oct': 'float','Nov': 'float', 'Dec': 'float',
                    'J-D': 'float', 'annual_mean': 'float'}
    
    df_nasa = df_nasa.astype(dictionnaire)
    df_nasa_trans = df_nasa.set_index("Year").T
    if st.button("Afficher l'entête du dataframe transformé "):
        st.write(df_nasa_trans.head())
   # Selection des années à garder
    
    decennie = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140]
    
    nasa_decade = df_nasa_trans.iloc[:, decennie]
    if st.button("Afficher l'entête des décennies retenues "):
        st.write(nasa_decade.head())
    
    p = sns.relplot(kind='line', data=nasa_decade, marker = 'o', palette="viridis", height=5, aspect=11.7/8.27)
                
    plt.xlabel("Mois de l'année");
    plt.ylabel('Anomalie');
    plt.title("Cycle saisonnier des températures par décénnie");
    st.warning("L'objectif de cette visualisation est de comparer l'évolution des températures par mois et par décénie")
    st.pyplot(p)
    st.info("On peut remarquer que ce graphique vient confirmer l'observation selon laquelle les températures ont augmentées sur tous les mois de l’année depuis 1880 et que cette tendance s’est renforcée ces 20 dernières années.")
    
    st.markdown('''
                <h5 class="title is-5 has-text-centered">Analyse des données de 'hadcrut-surface-temperature-anomaly.csv</h5>
    ''', unsafe_allow_html=True)
    hadcrut_temp = pd.read_csv('./datasets/hadcrut-surface-temperature-anomaly.csv', sep=",")
    hadcrut_temp = hadcrut_temp.rename({"Entity": "country",
                          "Code" : "iso_code" ,
                          "Year": "year",
                          "Surface temperature anomaly" : "temp_anomaly"}, axis = 1)
        # Data - we need iso alpha-3 codes
    map_countries = hadcrut_temp.dropna(axis = 0).groupby(by = [ 'country', 'year','iso_code']).mean().reset_index()
    
    # Min temperature is -5.453083, and because the size in a map cannot be negative, we will add 6 to all temperatures
    # to "standardize the data"
    map_countries['temp_anomaly'] = map_countries['temp_anomaly'] + 7
    
    fig5 = px.scatter_geo(map_countries, locations='iso_code', color='temp_anomaly',
                         color_discrete_sequence = ('#283747', '#2874A6', '#3498DB', '#F5B041', '#E67E22', '#A93226'),
                         hover_name="country", size="temp_anomaly", size_max=15, opacity = 0.8,
                         animation_frame="year",
                         projection="natural earth", title='Carte interactive - Augmentation des temperatures')
    fig.show()
    st.warning("Attention ! Par soucis de normalisation et parce que la carte ne peut accepter de valeur négative, nous avons ajouté (+) 7 à toutes les valeurs")
    st.warning("Pour avoir la valeur réelle, merci de soustraire 7 dans la valeur de temp_anomaly")
    st.write(fig5)
   
    country_temp = hadcrut_temp.groupby(by = [ 'country', 'year','iso_code']).mean().reset_index()
    fig6 = px.choropleth(country_temp, locations="country", locationmode = "country names", color="temp_anomaly",
                         animation_frame="year",
                        color_continuous_scale="viridis",
                        title="Anomaly des temperature moyenne par pays")
    st.write(fig6)
    st.write(" ")
    st.markdown('''
    <div class="box">
       <h3 class="title is-3 has-text-info has-text-centered">Exploration des dataframe issue de Kaggle</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    
    land_temp = pd.read_csv('./datasets/GlobalLandTemperaturesByCountry.csv', sep=",", parse_dates= ['dt'])
    land_temp.rename(columns = {'dt':'Date'}, inplace = True)
    parse_dates= ['dt']
#  ###

    land_temp_clear = land_temp[~land_temp['Country'].isin(
        ['Denmark', 'Antarctica', 'France', 'Europe', 'Netherlands',
         'United Kingdom', 'Africa', 'South America'])]
    
    land_temp_clear = land_temp_clear.replace(
       ['Denmark (Europe)', 'France (Europe)', 'Netherlands (Europe)', 'United Kingdom (Europe)'],
       ['Denmark', 'France', 'Netherlands', 'United Kingdom'])
    
    # Let's average temperature for each country
    
    countries = np.unique(land_temp_clear['Country'])
    mean_temp = []
    for country in countries:
        mean_temp.append(land_temp_clear[land_temp_clear['Country'] == country]['AverageTemperature'].mean())      
    data = [dict(
            type='choropleth',
            locations=countries,
            z=mean_temp,
            locationmode='country names',
            text=countries,
            marker=dict(
                line=dict(color='rgb(0,0,0)', width=1)),
            colorbar=dict(
                tickprefix='',
                title='# Average\nTemperature,\n°C')
        )
    ]

    layout = dict(
        title='Average land temperature in countries',
        geo=dict(
            showframe=False,
            showocean=True,
            oceancolor='rgb(0,255,255)',
            projection=dict(
                type='orthographic',
                rotation=dict(
                    lon=60,
                    lat=10),
            ),
            lonaxis=dict(
                showgrid=True,
                gridcolor='rgb(102, 102, 102)'
            ),
            lataxis=dict(
                showgrid=True,
                gridcolor='rgb(102, 102, 102)'
            )
        ),
    )

    fig7 = go.Figure(data=data, layout=layout)

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig7)
    
    # Sort the countries by the average temperature and plot Horizontal Bar
    
    mean_temp_bar, countries_bar = (list(x) for x in zip(*sorted(zip(mean_temp, countries), 
                                                                 reverse = True)))
    sns.set(font_scale=0.9) 
    f, ax = plt.subplots(figsize=(4.5, 50))
    colors_cw = sns.color_palette('coolwarm', len(countries))
    sns.barplot(x=mean_temp_bar, y=countries_bar, palette = colors_cw[::-1])
    Text = ax.set(xlabel='Average temperature', title='Average land temperature in countries')
    st.write(f)
    st.info("ce graphique montre la moyenne des températures par pays (des pays les plus chauds aux pays les plus froids.)")

    land_temp["Year"] = pd.DatetimeIndex(land_temp['Date']).year
    land_temp["Month"] = pd.DatetimeIndex(land_temp['Date']).month
    land_temp['Month'] = land_temp['Month'].astype(str) 
    land_temp.loc[land_temp['Month']=='1','Month'] = 'January'
    land_temp.loc[land_temp['Month']=='2','Month'] = 'February'
    land_temp.loc[land_temp['Month']=='3','Month'] = 'March'
    land_temp.loc[land_temp['Month']=='4','Month'] = 'April'
    land_temp.loc[land_temp['Month']=='5','Month'] = 'May'
    land_temp.loc[land_temp['Month']=='6','Month'] = 'June'
    land_temp.loc[land_temp['Month']=='7','Month'] = 'July'
    land_temp.loc[land_temp['Month']=='8','Month'] = 'August'
    land_temp.loc[land_temp['Month']=='9','Month'] = 'September'
    land_temp.loc[land_temp['Month']=='10','Month'] = 'October'
    land_temp.loc[land_temp['Month']=='11','Month'] = 'November'
    land_temp.loc[land_temp['Month']=='12','Month'] = 'December'
    
    st.write(" ")
    st.markdown('''
                <h6 class="title is-6 has-text-centered">Comparaison des températures par saison</h6>
    ''', unsafe_allow_html=True)
    st.write(" ")
    st.markdown('''
    <ul>
       <li> Eté = Summer</li>
       <li> Hiver = Winter</li>
       <li> Printemp = Spring</li>
       <li> Automne = Autumn</li>
    </ul>
    ''', unsafe_allow_html=True)
    
    month_season = {
    "January": "Winter",
    "February": "Winter",
    "March": "Spring",
    "April": "Spring",
    "May": "Spring",
    "June": "Summer",
    "July": "Summer",
    "August": "Summer",
    "September": "Autumn",
    "October": "Autumn",
    "November": "Autumn",
    "December": "Winter"
    }

    land_temp['Season'] = ''
    
    for month, season in month_season.items():
        land_temp.loc[land_temp['Month'] == month, 'Season'] = season
    
    year_season = land_temp.groupby(by = ['Year','Season']).mean().reset_index()
    
    Winter = year_season.loc[year_season['Season'] == 'Winter',:]
    Spring = year_season.loc[year_season['Season'] == 'Spring',:]
    Summer = year_season.loc[year_season['Season'] == 'Summer',:]
    Autumn = year_season.loc[year_season['Season'] == 'Autumn',:]
    
    fig8 = go.Figure()
    for template in ["plotly_white"]:
        fig8.add_trace(go.Scatter(x=Winter['Year'], y=Winter['AverageTemperature'],
                        mode='lines',
                        name='Winter',
                        marker_color='#838B8B'))
        fig8.add_trace(go.Scatter(x=Spring['Year'], y=Spring['AverageTemperature'],
                        mode='lines',
                        name='Spring',
                        marker_color='#FFB5C5'))
        fig8.add_trace(go.Scatter(x=Summer['Year'], y=Summer['AverageTemperature'],
                        mode='lines',
                        name='Summer',
                        marker_color='#87CEFF'))
        fig8.add_trace(go.Scatter(x=Autumn['Year'], y=Autumn['AverageTemperature'],
                        mode='lines',
                        name='Autumn',
                        marker_color='#FF8000'))
        fig8.update_layout(
        height=800,
        xaxis_title="Years",
        yaxis_title='Temperature in degree',
        title_text='Average Temperature seasonwise over the years',
        template=template)
    st.write(fig8)
    st.markdown('''Sur ce graphique on remarque également :
                
    - une hausse des températures dès les années 1850.
    - Les températures de l'automne et celles du printemp sont similaires
    ''', unsafe_allow_html=True)
    st.write(" ")
   
    
 # #####################################################
  