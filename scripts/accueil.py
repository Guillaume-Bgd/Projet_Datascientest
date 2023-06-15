import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def accueil():
    # Ajout du lien vers le fichier CSS de Bulma
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">', unsafe_allow_html=True)

    st.image("img/rechauffement-climatique-petrole-usine.webp")
    credit_text = "Crédit : [Futura Sciences](https://www.futura-sciences.com/planete/actualites/rechauffement-climatique-lobjectif-15-c-rechauffement-climatique-deja-perdu-on-dirige-scenario-moins-3-c-rechauffement-104524/)"
    st.markdown(credit_text)
    st.markdown("<p>Etudes et site réalisés par <code><b>Brunel TCHEKELI</b></code>, <code><b>Guillaume BOGDANOWICZ</b></code> et <code><b>Hélène LEBOURG-KOULIBALY</b></code>", unsafe_allow_html=True)
    st.write("")

    st.markdown('''
    <div class="box">
        <h3 class="title is-3 has-text-info has-text-centered">Introduction</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.divider()
    #if st.button("Afficher l'introduction"):
        # Cacher le bouton après qu'il soit cliqué
       # st.empty()
             
    st.write("""Dans le cadre de notre formation Data Analyst en Bootcamp chez Datascientest, nous avons travaillé sur un projet « fil rouge » nous permettant d’aborder toutes les étapes de développement d’une solution data. 
    Nous avons été sélectionnés pour le projet « Température terrestre » avec comme objectif de constater le réchauffement (et le dérèglement) climatique global à l’échelle de la planète sur les derniers siècles et dernières décennies.   Ce projet nous a permis d’appliquer les compétences apprises au cours de la formation, de pouvoir travailler en équipe et d’avoir la capacité d’apprendre sur des problématiques métier.""")
    
    st.write("")
    content = """
    <p style="text-align: justify;">
    Le rechauffement climatique est un sujet de préoccupation croissante en raison de son impact sur l'environnement, l'économie et la société. Les changements climatiques, en particulier le réchauffement, ont des conséquences néfastes sur la biodiversité, les ressources en eau, l'agriculture, la santé humaine et les infrastructures. Il est donc crucial de surveiller et d'analyser les données de températures mondiales pour mieux comprendre les tendances et les variations, et ainsi anticiper et atténuer les effets du changement climatique.<br><br>
    
    </p>

    <p style="text-align: justify;">
    Dans ce contexte, notre projet de data analyse vise à étudier les données de températures mondiales afin de fournir des informations pertinentes et actualisées sur les tendances, les variations et les anomalies de températures. Nous nous appuierons sur des sources de données fiables et reconnues, telles que les bases de données de la NASA, de Berkeley Earth et de certaines données issues de Kaggle et Github (https://data.giss.nasa.gov/gistemp/ et https://github.com/owid/co2-data). <br><br>
    </p>
    """
    st.write(content, unsafe_allow_html=True)
 
    st.write("")
    content2 ="""
    <p style="text-align: justify;"><b>Méthodologie</b><br><br></p>
 
    <p style="text-align: justify;">Pour mener à bien notre projet de data analyse, nous suivrons une méthodologie rigoureuse et structurée, qui comprendra les étapes suivantes :<br><br>
    <ol>
    <li style="text-align: justify;">Collecte des données : nous collecterons les données de températures mondiales auprès de sources fiables et reconnues, en veillant à couvrir une période suffisamment longue pour permettre l'analyse des tendances et des variations. Nous nous assurerons également que les données soient complètes, cohérentes et de qualité.<br><br></li
 
    <li style="text-align: justify;"> Nettoyage et préparation des données : nous procéderons à un nettoyage et à une préparation minutieuse des données, en éliminant les erreurs, les incohérences et les valeurs manquantes, et en normalisant les données pour faciliter leur analyse et leur comparaison.<br><br></li
 
    <li style="text-align: justify;"> Analyse exploratoire des données : nous réaliserons une analyse exploratoire des données pour identifier les tendances, les variations et les anomalies de température, ainsi que les relations entre les différentes variables. Nous utiliserons des techniques de visualisation des données, telles que les graphiques, les cartes et les tableaux, pour faciliter la compréhension et l'interprétation des résultats.<br><br></li
 
    <li style="text-align: justify;"> Modélisation et prévisions : nous développerons des modèles statistiques et de machine learning pour analyser les relations entre les variables et pour prévoir l'évolution future des températures mondiales. Nous évaluerons la performance de ces modèles en utilisant des indicateurs de qualité, tels que le coefficient de détermination (R²), l'erreur quadratique moyenne (RMSE) et le coefficient de corrélation (r).<br><br></li
 
    <li style="text-align: justify;"> Interprétation et communication des résultats : nous interpréterons les résultats de notre analyse en mettant en évidence les tendances, les variations et les anomalies de températures, ainsi que les implications pour l'environnement, l'économie et la société. Nous communiquerons nos résultats de manière claire et accessible, en utilisant des supports visuels et des explications simples.<br><br></li>
     """
    st.write(content2, unsafe_allow_html=True)
    st.write(" ")
    content3 = """
     <p style="text-align: justify;">
     <b>Résultats attendus<br><br></b>
     </p>
 
     <p style="text-align: justify;">
     Notre projet de data analyse des données de températures mondiales devrait permettre de répondre aux questions suivantes :<br><br>
     </p>
 
     
     <p style="text-align: justify;"><ul><li>Quelles sont les tendances à long terme des températures mondiales ? Y a-t-il une augmentation significative des températures au cours des dernières décennies ?<br><br></li></ul></p>
     <p style="text-align: justify;"><ul><li>Quelles sont les variations saisonnières et géographiques des températures ? Existe-t-il des différences marquées entre les régions et les saisons ?<br><br></li></ul></p>
     <p style="text-align: justify;"><ul><li>Quelles sont les anomalies de température les plus importantes et les plus fréquentes ? Peut-on les attribuer à des événements climatiques spécifiques, tels que les phénomènes El Niño et La Niña ?<br><br></li></ul></p>
     <p style="text-align: justify;"><ul><li>Quels sont les facteurs qui influencent les températures mondiales ? Peut-on établir des relations entre les températures et les émissions de gaz à effet de serre ?<br><br></li></ul></p>
     """
    st.write(content3, unsafe_allow_html=True)


# Afficher le bouton pour montrer/cacher le cadrage
    st.markdown('''
    <div class="box">
        <h3 class="title is-3 has-text-info has-text-centered">Cadrage</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('<hr class="is-divider is-success">', unsafe_allow_html=True)
    if st.button("Afficher le cadrage"):
        # Cacher le bouton après qu'il soit cliqué
        st.empty()

        # Afficher le cadrage
        st.write("""Tout d’abord, nous avons observé les données disponibles sur les sites web mentionnés dans la fiche projet (voir Annexes), respectivement la NASA et Github (https://data.giss.nasa.gov/gistemp/ et https://github.com/owid/co2-data). """)
        st.text("")
        
        st.write("Une première réunion de cadrage nous a permis d’identifier les étapes du projet et de comprendre ce qui était attendu. Nous nous sommes organisés et partagés les tâches à l’aide d’un diagramme de GANTT (voir Annexes) et de réunions régulières afin de suivre nos avancements et répondre à nos problématiques.")

        st.write("A l’aide des datasets et de recherches parallèles sur le sujet, nous avons établi une présentation du projet permettant de délimiter et de comprendre les enjeux de ce dernier.")
        st.text("")
        st.write("L’objectif du projet est de « constater le réchauffement (et le dérèglement) climatique global à l’échelle de la planète sur les derniers siècles et dernières décennies ». Nous avons choisi le cadrage suivant :")
        st.write("1. Découvertes des données et projet")
        st.write("2. Exploration et analyse des données avec Dataviz’")
        st.write("3. Nettoyage et pre-processing")
        st.write("4. Modélisation")

# 

    st.markdown('''
    <div class="box">
        <h3 class="title is-3 has-text-info has-text-centered">Définitions et explications</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('<hr class="is-divider is-success">', unsafe_allow_html=True)
    
    if st.button("Afficher les définitions et explications"):
        # Cacher le bouton après qu'il soit cliqué
        st.empty()

        # Afficher les Définitions et explications
        st.markdown("**Changement climatique** : défini par les Nations Unies comme « […] les variations à long terme de la température et des modèles météorologiques. Il peut s’agir de variations naturelles, dues par exemple à celles du cycle solaire ou à des éruptions volcaniques massives. Cependant, depuis les années 1800, les activités humaines constituent la cause principale des changements climatiques, essentiellement en raison de la combustion de combustibles fossiles comme le charbon, le pétrole et le gaz. La combustion de combustibles fossiles génère des émissions de gaz à effet de serre qui agissent comme une couverture autour de la Terre, emprisonnant la chaleur du soleil et entraînant une hausse des températures.")
        st.text("")

        st.markdown("**Réchauffement climatique** : augmentation générale des températures.")
        st.text("")

        st.markdown("**Les principales causes du changement climatique** : Les émissions de dioxyde de carbone et de méthane, notamment, sont à l’origine des changements climatiques. Elles résultent par exemple de l’utilisation de carburants pour alimenter les véhicules ou du charbon pour chauffer un bâtiment. Le défrichement des terres et des forêts peut également entraîner la libération de dioxyde de carbone. L'agriculture et les moteurs à combustion constituent une source importante d’émissions de méthane. Les secteurs de l’énergie, de l’industrie, des transports et de la construction ainsi que de l’agriculture et d’autres utilisations des terres figurent parmi les principaux émetteurs.")
        st.text("")

        st.markdown("**Les principales conséquences du changement climatique** : sécheresses intenses, pénuries d’eau, graves incendies, élévation du niveau de la mer, inondations, fonte des glaces polaires, tempêtes catastrophiques et déclin de la biodiversité.")
        st.image("img/composantes_climatique.png")
        
#   
    st.markdown('''
    <div class="box">
        <h3 class="title is-3 has-text-info has-text-centered">Gestion du projet</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('<hr class="is-divider is-success">', unsafe_allow_html=True)
    
    if st.button("Afficher les éléments de Gestion du projet"):
        # Cacher le bouton après qu'il soit cliqué
        st.empty()

        st.image("img/Diagramme de Gantt_page_1.jpg", use_column_width=True)
        st.image("img/Diagramme de Gantt_page_2.jpg", use_column_width=True)
        
#

    
    st.markdown('''
    <div class="box">
        <h3 class="title is-3 has-text-info has-text-centered">Glossaire</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('<hr class="is-divider is-success">', unsafe_allow_html=True)
    if st.button("Afficher le Glossaire"):
        # Cacher le bouton après qu'il soit cliqué
        st.empty()

        # Afficher le Glossaire
        st.markdown("**year** – Les années.")
        st.markdown("**population** – La population totale.")
        st.markdown("**gdp** – Produit intérieur brut (PIB).")
        st.markdown("**co2** – Dioxyde de carbone.")
        st.markdown("**cement_co2** – Emission CO₂ du ciment : le ciment est composé de 80 % de calcaire et 20 % d'argile. Les émissions CO₂ du ciment résultent de la décomposition du calcaire par la calcination.")
        st.markdown("**co2_per_capita** – CO₂ par habitant.")
        st.markdown("**coal_co2** – CO₂ produit par le charbon : la combustion du charbon émet des particules volatiles dangereuses : benzène et ses dérivés aromatiques.")
        st.markdown("**flaring_co2** - CO₂ produit par le torchage / brûlage : le torchage est une pratique qui consiste à brûler les rejets de gaz naturels associés à l’extraction de pétrole.")
        st.markdown("**gas_co2** - CO₂ produit par l’essence : combustible liquide qui, mélangé à l'air (carburation), est inflammable et peut être utilisé dans un moteur à explosion (i.e. essence, gazole). La combustion de l’essence produit du CO₂.")
        st.markdown("**methane** – méthane : gaz composé de molécules de quatre atomes d'hydrogène et d'un atome de carbone. Le méthane est le constituant principal du gaz naturel, combustible d'origine fossile. Les sources naturelles incluent les terres marécageuses, les marais, les termites et les océans. Les sources synthétiques incluent l'exploitation et la brûlure des combustibles fossiles, les processus digestifs chez les ruminants tels que le bétail, les paddys de riz et les sites d'enfouissement des déchets.")
        st.markdown("**nitrous_oxide** - Protoxyde d'azote : aussi appelé oxyde nitreux est un composé oxygéné de l’azote.")
        st.markdown("**oil_co2** – CO₂ produit par le pétrole : huile minérale naturelle combustible, hydrocarbure liquide accumulé dans les roches, en gisements. L'exploitation du pétrole est directement liée à la destruction de la forêt et la pollution des nappes phréatiques, mais également par les nombreux déchets d'exploitation ainsi que les produits chimiques libérés pour les différents traitements dans les phases de production de dérivés pétrochimiques.")
        st.markdown("**total_ghg** – Total des émissions à effet de serre.")
        st.markdown("**temp_anomaly** – Les anomalies de températures.")
        st.markdown("**RMSE** – en anglais root mean square error, est la racine carrée de la moyenne des erreurs quadratiques. C’est une mesure utilisée pour évaluer les différences entre les valeurs prédites par un modèle de Machine Learning et les valeurs réelles.")
        st.markdown("**MSE** – en anglais mean squared error, est l’erreur quadratique moyenne qui permet d’évaluer la précision d’une prédiction.")


# Remerciements

    st.markdown('''
    <div class="box">
        <h3 class="title is-3 has-text-info has-text-centered">Remerciements</h3>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('<hr class="is-divider is-success">', unsafe_allow_html=True)
    if st.button("Afficher les remerciements"):
        # Cacher le bouton après qu'il soit cliqué
        st.empty()

        # Afficher le remerciements
        st.markdown('''
            <p>Avant tout, nous souhaitons remercier l’équipe de DataScientest, notre chef de cohorte, <code>Khalil</code>, et plus particulièrement notre tuteur, <code>Tarik ANOUAR</code>, pour son soutien et son suivi pédagogique sans faille, qui nous ont permis de relever les enjeux de cette formation et de mener à bien notre projet.</p>
            ''', unsafe_allow_html=True)
    
    