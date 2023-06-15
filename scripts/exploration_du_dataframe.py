# -*- coding: utf-8 -*-
"""

"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import statsmodels.api as sm
import io
from PIL import Image
    
def exploration_du_dataframe():
    
    credit_text = "Crédit : [Futura Sciences](https://www.futura-sciences.com/planete/actualites/rechauffement-climatique-simulez-votre-futur-climatique-vous-attend-selon-votre-age-votre-region-105045/)"
    st.image("img/climat_futur.webp",)
    st.markdown(credit_text)
    st.write(" ")
    st.markdown('''
    <div class="box">
        <h3 class="title is-3 has-text-info has-text-centered">Exploration du dataframe</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.write(" ")
    st.markdown("""Pour mener ce projet, nous nous sommes basés sur l'étude des données sur les émissions de CO2 dans le monde et les anomalies annuelles de températures.""")
    
    st.divider()
    st.markdown('''
                <h3 class="title is-3  has-text-centered">Présentation des différentes sources de données utilisées.</h3>
    ''', unsafe_allow_html=True)
    st.write(" ")
    
    st.markdown("""
    
    Le dataset 'datas.csv' a été créé à partir de deux sources de données : 
    
    - **Data on CO2 and Greenhouse Gas Emissions** by Our World in Data (https://github.com/owid/co2-data)
    
    Cet ensemble de données extrêmement riche sur les émissions de CO2 et de gaz à effet de serre est un ensemble de mesures clés gérées par Our World in Data. Il est mis à jour régulièrement et comprend des données sur les émissions de CO2 (annuelles, par habitant, cumulatives et basées sur la consommation), d’autres gaz à effet de serre, le bouquet énergétique et d’autres paramètres pertinents. 
    
    Les informations pour les années les plus anciennes (la plus ancienne date est 1750) ne sont pas toujours renseignées. Cela s’explique par l’absence de stockage de données et des technologies correspondantes. C’est pourquoi nous avons décidé de commencer l’analyse à partir de 1910 afin d’avoir toutes les données nécessaires pour notre analyse.
    D'autre part, la multitude de variables disponibles (plus de 70) a nécéssité une sélection afin de nous concentrer sur les éléments les plus utiles et les plus représentatifs.
    
    Il est necessaire de procéder à un nettoyage du jeu de données et sélectionner uniquement les colonnes qui seraient pertinentes pour notre étude.
    
    Nous faisons notre sélection de colonnes en optant pour les émissions annuelles de CO2, les émissions de CO2 lors de la production de gaz, de pétrole et de charbon ainsi que les émissions de méthane, d'oxyde nitrique et de gaz à effet de serre.
    
    - country : continent géographique.
    - iso_code : au départ conservé dans l'idée de produire des cartes, mais inutile au final
    - year : année d'observation.
    - gdp : Produit intérieur brut (PIB).
    - population : population humaine.
    - co2 : Émissions annuelles de dioxyde de carbone, mesurées en millions de tonnes.
    - coal_co2 : Émissions annuelles de dioxyde de carbone (CO₂) issues du charbon, basées sur la production, mesurées en millions de tonnes. La combustion du charbon émet des particules volatiles dangereuses : benzène et ses dérivés aromatiques.
    - gas_co2 : Émissions annuelles de dioxyde de carbone (CO₂) issues du gaz, basées sur la production, mesurées en millions de tonnes.
    - oil-co2 : Émissions annuelles de dioxyde de carbone (CO₂) issues du pétrole, basées sur la production, mesurées en millions de tonnes. CO₂ produit par le pétrole : huile minérale naturelle combustible, hydrocarbure liquide accumulé dans les roches, en gisements. L'exploitation du pétrole est directement liée à la destruction de la forêt et la pollution des nappes phréatiques, mais également par les nombreux déchets d'exploitation ainsi que les produits chimiques libérés pour les différents traitements dans les phases de production de dérivés pétrochimiques.
    - flaring_co2 - CO₂ produit par le torchage / brûlage : le torchage est une pratique qui consiste à brûler les rejets de gaz naturels associés à l’extraction de pétrole.
    - methane : Émissions totales, y compris le changement d'affectation des terres et la foresterie, mesurées en millions de tonnes d'équivalents en dioxyde de carbone. Les sources naturelles incluent les terres marécageuses, les marais, les termites et les océans. Les sources synthétiques incluent l'exploitation et la brûlure des combustibles fossiles, les processus digestifs chez les ruminants tels que le bétail, les paddys de riz et les sites d'enfouissement des déchets.
    - nitrous_oxide : Émissions totales d'oxyde nitreux, y compris le changement d'affectation des terres et la foresterie, mesurées en millions de tonnes d'équivalents en dioxyde de carbone.
    - total_ghg : Émissions totales de gaz à effet de serre, y compris le changement d'affectation des terres et la foresterie, mesurées en millions de tonnes d'équivalents dioxyde de carbone.
    
    Lors du nettoyage de ce jeu de données, nous avons décidé de remplacer les nan par la première valeur rencontrée selon la méthode (method = 'ffill'), qui remplace la valeur manquante d'une variable par la première valeur rencontrée dans la colonne.
    
    """)
    
    st.write("")
    
    code = '''df = df[["country", "iso_code" ,"year", "gdp","population", "co2", "coal_co2", "gas_co2", "methane", "nitrous_oxide", "total_ghg", "oil_co2" ]]'''
    st.code(code)
    
    st.markdown("""
    
    - **Climate at a Glance Global Time Series** (https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series)
    
    La composante mondiale de Climate at a Glance (GCAG) fournit des informations sur la température à l’échelle mondiale à l’aide de données de l’analyse de la température de surface globale de la NOAA (National Oceanic and Atmospheric Administration), qui utilise des collectes de données complètes sur une couverture mondiale accrue sur les terres (Historique mondial Réseau de climatologie - mensuel) et océans (Température de surface de la mer reconstruite étendue). Les données sont fournies à l’échelle mondiale, par hémisphère et par les composantes de surface des terres et des océans. 
    
    Étant donné que ces données sont principalement destinées à l’étude de la variabilité du climat, les observations ont été ajustées pour tenir compte des effets artificiels introduits dans les données climatiques par des facteurs tels que : changements d’instruments, déplacement de stations, changements de pratiques d’observateurs et urbanisation. Certaines des données fournies les plus récentes sont préliminaires et peuvent être modifiées après un contrôle de qualité approprié. Par conséquent, certaines valeurs peuvent différer des observations officielles.
    
    Nous avons donc compilé les données par années et pour chacun des continents (Europe, Asie, Amérique du Nord, Amérique du Sud et Océanie) afin de pouvoir fusionner ces données avec celles relatives aux émissions de CO2 dont le dataset est établi sur la même architecture : les colonnes 'country' et 'year' sont communes aux deux dataframes.
    
    """)
    
    
    st.divider()
    
    st.subheader("Le dataset 'datas'.")
    
    df = pd.read_csv('./datasets/datas.csv', sep = ',', header = 0)
    
    st.markdown("""
    Le dataframe 'datas' est issu de la fusion des deux jeux de données (émissions de CO2 et anomalies annuelles de températures mondiales).""")
    
    code = '''datas = df.merge(right = tempcont, how = 'inner', on = ['year', 'country'])'''
    st.code(code)
    
    st.markdown("""
    
    A l'exception de la colonne 'iso_code', il ne contient aucune valeur manquante. Dans le processus de nettoyage, cette colonne a été supprimée. Le tableau statistique généré par la fonction ‘describe’ nous a permis d’inspecter globalement nos données. Nous pouvons noter un écart important entre les troisièmes quartiles et les valeurs maximales, notamment pour la colonne ' CO₂' ou 'methane'. Nous pouvons constater de grands écarts entre les valeurs minimales et maximales, ce qui coïncide par exemple avec les importantes disparités entre l’Asie et l’Océanie. Il est intéressant de noter, qu’il y a une différence importante entre la valeur minimum (0.109) et la valeur maximale (16.295) concernant le CO₂ par habitant. Ce tableau permet de constater de fortes disparités dans nos données que nous avons également pu voir lors de mise en forme des données, notamment entre les continents.
    """)
    
    st.write("")
    
    st.subheader("**Aperçu du dataframe.**")
    
    st.write("")
    
    st.markdown("Premier aperçu du dataframe en affichant les dix premières lignes. On constate que la colonne 'iso_code' est vide. On la supprimera un peu plus tard.")
    
    st.write("")
    
    st.dataframe(df.head(10))
    
    st.markdown("Le dataframe, excepté la colonne 'iso_code', ne contient aucune valeur manquante. L'ensemble des données sont du type float, donc explicatives numériques. Seule la colonne 'country' est de type catégoriel.")
    
    st.write("")
    
    st.markdown("Affichage des informations principales du dataframe nous permet de vérifier la nature des différentes variables et la présence éventuelle de nan.")
    
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    
    st.markdown("La fonction describe permet d'inspecter les données numériques. On remarque rapidement un écart important entre les troisièmes quartiles et les valeurs maximales, notamment pour la colonne 'co2' ou 'methane'. De plus, les moyennes des valeurs de ces colonnes sont relativement faibles et se rapprochent de la médiane, ce qui sous-entend que certaines valeurs, peu nombreuses, sont très fortes.")
    
    st.write("")
    
    st.markdown("Nous pouvons constater de grands écarts entre les valeurs minimales et maximales, ce qui coïncide par exemple avec les importantes disparités entre l'Asie et l’Océanie.")
    
    st.write("")
    
    st.markdown("Il est intéressant de noter, qu’il y a une différence importante entre la valeur minimum (0.109) et la valeur maximale (16.295) concernant le CO₂ par habitant. Ce tableau permet de constater de fortes disparités dans nos données que nous avons également pu voir lors de mise en forme des données, notamment entre les continents.")
    
    st.write("")
    
    describe = df.describe(include='all')
    st.write(describe)
    
    st.markdown("La colonne 'iso_code' est inutile, on la supprime du dataframe :")
    
    code = '''df = df.drop('iso_code', axis = 1)'''
    st.code(code)
        
    df = df.drop('iso_code', axis = 1)
    
    
    
                
    st.title('**Corrélations et tests statistiques**')
    
    st.write("")
    
    st.markdown("Le but de cette section est d'établir les liens possibles de corrélation entre les différentes variables du dataframe. Certaines variables sont peut-être plus liées à la variable cible et l'évolution de leurs valeurs à probablement un impact sur l'évolution des valeurs de la variable cible.") 
    
    st.write("Nous allons afficher la table des corrélations entre les différentes valeurs numériques.")
    
    st.write("La heatmap issue de cette table nous permets d'identifier les corrélations les plus fortes en relation avec notre valeur cible (à savoir la colonne 'temp_anomaly'). Il semble que les variables 'year', 'gas_co2' et 'total_ghg' soient parmi les plus corrélées avec la cible.")
    
    fig = cor = df.corr()
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(cor, annot=True, ax=ax, cmap='inferno');
    st.pyplot(fig)
    
    st.markdown("En nous focalisant sur la ligne concernant la variable cible 'temp_anomaly', nous constatons les plus fortes corrélations avec les variables suivantes : 'year', 'gas_co2', 'methane', 'nitrous_oxide' et 'total_ghg'.")
    
    st.write("Nous pouvons aussi constater des corrélations notamment entre :")
    
    st.write("- le méthane et le total des émission de gaz à effet de serre (0.97)")
    st.write("- le protoxyde d'azote et le total des émission de gaz à effet de serre (0.96)")
    st.write("- le CO₂ et le CO₂ produit par charbon (0.95)")
    st.write("- le CO₂ et le CO₂ produit par pétrole (0.94)")
    st.write("- le CO₂ produit par ciment et le CO₂ produit par charbon (0.93)")
    st.write("- le CO₂ produit par ciment et le total des émission de gaz à effet de serre (0.89)")
    st.write("- le CO₂ et CO₂ produit par l’essence (0.89)")
    st.write("- le CO₂ produit par ciment et le méthane (0.85)")
    st.write("- la population et le CO₂ produit par le ciment (0.82)")
    
    st.write("")
    
    st.subheader('**Tests de Pearson sur les principales variables**')
    
    st.write("")
    
    st.markdown("Nous allons appliquer le test de Pearson afin de comparer la corrélation entre la valeur cible 'temp_anomaly' et les principales variables explicatives. Ce test permet d'étudier une relation linéaire entre deux variables quantitatives.")
    
    st.write("Voici les résultats des différents tests, comparant la variable 'temp_anomaly' aux autres variables ci-dessous :")
    
    st.write("")
    
    d = {'variable':['total_ghg','co2','year','gas_co2'],'p-value':['1.4115724450324765e-73','4.829346051341192e-41','4.707702307798167e-134','5.795158957191762e-59'],'coefficient':[pearsonr(x = df["total_ghg"], y = df["temp_anomaly"])[0],pearsonr(x = df["co2"], y = df["temp_anomaly"])[0],pearsonr(x = df["year"], y = df["temp_anomaly"])[0],pearsonr(x = df["gas_co2"], y = df["temp_anomaly"])[0]]}
    
    pearson = pd.DataFrame(d)
                        
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.table(pearson)
    
    st.markdown("On remarquera que toutes les p-value sont extrèmement petites, témoignant d'une forte corrélation entre les variables.")
    
    st.write("")
    
    st.subheader('**Affichage des courbes de répartition.**')
    
    st.write("")
    
    st.markdown("Nous allons afficher la courbe de répartition de chacune des variables du dataset, par continent :")
     
    st.write("")
    
    import scipy.stats as stats
    
    # Catégories uniques de la colonne "country"
    categories = df['country'].unique()
    
    # Itérer sur les colonnes
    for col in df.columns[1:]:
        # Créer la figure et les sous-graphiques
        fig, axs = plt.subplots(1, len(categories), figsize=(18, 5))
    
        # Itérer sur les catégories et afficher les graphiques
        for i, cat in enumerate(categories):
            ax = axs[i]
            subset_data = df[df['country'] == cat]
            stats.probplot(subset_data[col], dist="norm", plot=ax)
            ax.set_xlabel('Quantiles théoriques')
            ax.set_ylabel('Quantiles observés')
            ax.set_title('qq-plot - ' + col + ' (' + cat + ')')
            ax.grid(True, linestyle='--')
    
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)
        
    st.markdown("Il semble que l'ensemble des variables ne sont pas réparties selon la loi normale. Ce qui laisse à penser qu'un facteur artificiel a une influence sur leurs répartitions.")
    
    st.write("Il est également intéressant de noter que, pour la variable des anomalies de températures, la distribution est différente selon les pays, ce qui sous-entend que les anomalies de températures ne sont pas homogènes sur le globe même si une linéarité demeure.")
    
    st.write("")
    
    st.write("Une étude plus poussée à l'aide de visualisations graphiques nous permettra d'affiner notre analyse.")