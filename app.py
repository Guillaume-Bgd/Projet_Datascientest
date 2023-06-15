import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu

icon = "img/temperature_icon.png"
st.set_page_config(
    page_title="Global warming",
    page_icon = icon,
    # page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
    )

    
# Ajout du lien vers le fichier CSS de Bulma
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">', unsafe_allow_html=True)

# Create a sidebar menu 
with st.sidebar:
    credit_text = "Crédit : [Almanach.com](https://www.almanac.com/content/earth-day-date-activities-history)"
    st.markdown(credit_text)
    #st.image("/img/earth-tree.jpg")
    
    
    choice = option_menu(
        menu_title = "Menu",
        options=["Accueil", "Exploration des données", "Analyses et dataviz", "Modélisation et Prédictions", "Conclusion", "Ressources"],
        icons=['house', "database-fill-gear",'bar-chart-line-fill', 'gear', "list-task", "book"], # bootstrap icons
        menu_icon="list", default_index=0 ) #, orientation="horizontal")

    st.sidebar.markdown('''
    <div class="box">
        <h6 class="title is-6 has-text-info">Membres du projet  :</h6>
    </div>
     ''', unsafe_allow_html=True)
    
    st.write(" ")
    st.write(" ")
    
    
    # Noms des membres
    # 1
    st.markdown('<h6 class="title is-6 has-text-primary">Brunel TCHEKELI</h6>', unsafe_allow_html=True)
    st.write(" ")
    col1, col2 = st.columns(2)

    # Première colonne
    with col1:
        #st.image("img/linkedin_icon.png", width=30)
        st.write("[LinkedIn](https://www.linkedin.com/in/brunel-tchekeli/)")

    # Deuxième colonne
    with col2:
        #st.image("img/github_logo.png", width=30)
        st.write("[GitHub](https://github.com/btchekeli)")

    # 2.
    st.write(" ")
    st.markdown('<h6 class="title is-6 has-text-primary">Guillaume BOGDANOWICZ</h6>', 
            unsafe_allow_html=True)
    st.write(" ")
    col1, col2 = st.columns(2)

    # Première colonne
    with col1:
        #st.image("img/linkedin_icon.png", width=30)
        st.write("[LinkedIn](https://www.linkedin.com/in/guillaumebogdanowicz/)")

    # Deuxième colonne
    with col2:
        #st.image("img/github_logo.png", width=30)
        st.write("[GitHub]( )")
        
    # 3.  
    st.write(" ")
    st.markdown('<h6 class="title is-6 has-text-primary">Hélène LEBOURG-KOULIBALY</h6>', 
            unsafe_allow_html=True)
    st.write(" ")
    col1, col2 = st.columns(2)

    # Première colonne
    with col1:
        #st.image("img/linkedin_icon.png", width=30)
        st.write("[LinkedIn](https://www.linkedin.com/in/h%C3%A9l%C3%A8ne-lebourg-koulibaly/)")

    # Deuxième colonne
    with col2:
        #st.image("img/github_logo.png", width=30)
        st.write("[GitHub]( )")
        
# Import Pages
from scripts.accueil import accueil
from scripts.exploration_du_dataframe import exploration_du_dataframe
from scripts.analyses_dataviz import analyses_dataviz
from scripts.modelisation import modelisation
from scripts.conclusion import conclusion
from scripts.ressources import ressources


# MENU
# Introduction
if choice == "Accueil":
    accueil()

# Exploration des données
elif choice == "Exploration des données":
    exploration_du_dataframe()

# Analyse et Visualisations   
elif choice == "Analyses et dataviz":
    analyses_dataviz()

# Modélisation ML   
elif choice == "Modélisation et Prédictions":
    modelisation()    

# Conclusion    
elif choice == "Conclusion":
    conclusion()    

# Ressources 

elif choice == "Ressources":
    ressources() 


else:
    accueil()
    
