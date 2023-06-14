
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.deterministic import DeterministicProcess
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

import warnings
warnings.filterwarnings("ignore")

import seaborn as sns
import datetime as dt
from scipy.stats import pearsonr


def modelisation():

   credit_text = "Crédit : [Futura Sciences](https://www.futura-sciences.com/planete/actualites/rechauffement-climatique-simulez-votre-futur-climatique-vous-attend-selon-votre-age-votre-region-105045/)"
   st.image("img/paris_futur.jpg",)
   st.markdown(credit_text)
   st.write(" ")

   df= pd.read_csv('./datasets/datas.csv', sep=',')
   df= df.drop('iso_code', axis = 1)

   feats = df.drop('temp_anomaly', axis = 1)
   target = df['temp_anomaly']


   X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size=0.25, random_state = 42)


   cat_train = pd.get_dummies(X_train['country'], columns = 'country') 
   cat_test = pd.get_dummies(X_test['country'], columns = 'country') 


   X_train2 = pd.concat([X_train,cat_train], axis = 1)
   X_test2 = pd.concat([X_test,cat_test], axis = 1)

   X_train2 = X_train2.drop('country', axis = 1)
   X_test2 = X_test2.drop('country', axis = 1)


   sc = StandardScaler()

   num = ['year', 'population', 'gdp', 'cement_co2', 'co2', 'co2_per_capita', 'coal_co2', 'flaring_co2', 'gas_co2', 'methane', 'nitrous_oxide', 'oil_co2', 'total_ghg']

   X_train2.loc[:,num] = sc.fit_transform(X_train2[num])
   X_test2.loc[:,num] = sc.transform(X_test2[num])


   #if choice == menu_title[4]

   #st.title(choice)




   #Début de la page
   st.write(" ")
   st.markdown('''  
        <div class="box">
            <h3 class="title is-3 has-text-info has-text-centered">Modélisation et Prédictions</h3>
        </div>''', unsafe_allow_html=True)
   st.write(" ")
   st.write(" ")
   st.markdown("""<p style='text-align: justify'>Dans le cadre de notre projet, nous souhaitons prédire les valeurs de notre variable cible soit les anomalies de températures.
               Ainsi, nous avons décidé d'entraîner notre jeu de données sur 1 modèle de régression linaire et 4 modèles de machine learning.
               Pour chaque modèle nous avons utilisé notre jeu de données :  datas.csv.
                   </p>""",  unsafe_allow_html=True)
                   
   

   #Définitions des mesures
   st.markdown("""<p style='text-align: justify'>Nous avons testé la performance de ces modèles à travers différentes métriques :</p>""",  unsafe_allow_html=True)
   st.markdown("- Score : résultat de la précision ('accuracy') du modèle")
   st.markdown("- MAE : Mean Absolute Error ou Erreur Moyenne Absolue")
   st.markdown("- MSE : Mean Squared Error ou Erreur Moyenne au carré")
   st.markdown("- RMSE : Root Mean Squared Error ou Erreur Moyenne de la racine carrée")

   #Présentation des résultats pour chaque modèle
   st.write(" ")
   st.title("**Arbre à décision :**")

   tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Score train", "Score test", "MAE train", "MAE test", "MSE train", "MSE test", "RMSE train", "RMSE test"])

   with tab1:
      st.write("1.0")

   with tab2:
      st.write("0.5715743416280948")

   with tab3:
      st.write("0.000000")
      
   with tab4:
      st.write("0.308000")
      
   with tab5:
      st.write("0.000000")
      
   with tab6:
      st.write("0.147930")
      
   with tab7:
      st.write("0.000000")
      
   with tab8:
      st.write("0.384617")
      

   st.write(" ")
   st.title("**Random Forest :**")

   tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Score train", "Score test", "MAE train", "MAE test", "MSE train", "MSE test", "RMSE train", "RMSE test"])

   with tab1:
      st.write("0.956191893697089")


   with tab2:
      st.write("0.7204673038466303")

   with tab3:
      st.write("0.092556")
      
   with tab4:
      st.write("0.241364")
      
   with tab5:
      st.write("0.014842")
      
   with tab6:
      st.write("0.096519")
      
   with tab7:
      st.write("0.121827")
      
   with tab8:
      st.write("0.310676")
      
   st.write(" ")  
   st.title("**Lasso :**")

   tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Score train", "Score test", "MAE train", "MAE test", "MSE train", "MSE test", "RMSE train", "RMSE test"])

   with tab1:
      st.write("0.6695170836184214")


   with tab2:
      st.write("0.669806081309698")

   with tab3:
      st.write("0.258821")
      
   with tab4:
      st.write("0.260577")
      
   with tab5:
      st.write("0.111965")
      
   with tab6:
      st.write("0.114012")
      
   with tab7:
      st.write("0.334612")
      
   with tab8:
      st.write("0.337657")

   st.write(" ")
   st.title("**Gradient Boosting :**")

   tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Score train", "Score test", "MAE train", "MAE test", "MSE train", "MSE test", "RMSE train", "RMSE test"])

   with tab1:
      st.write("0.8791403341726561")


   with tab2:
      st.write("0.746568463488195")

   with tab3:
      st.write("0.160310")
      
   with tab4:
      st.write("0.227479")
      
   with tab5:
      st.write("0.040946")
      
   with tab6:
      st.write("0.087507")
      
   with tab7:
      st.write("0.202352")
      
   with tab8:
      st.write("0.295816")
      
      
   #Modèle le plus performant 
   st.write(" ")  
   st.markdown("""<p style='text-align: justify'>Nous avons choisi de prendre en considération le résultat de la RMSE dans la comparaison des modèles car cette mesure pénalise également davantage les grands écarts de prédiction.
               De plus, elle a la même unité que la variable cible donc elle sera plus interprétable que la MSE. Le modèle le plus performant pour notre projet est : Gradient Boosting.
                   </p>""",  unsafe_allow_html=True)


   st.write(" ")
   st.title("**Régression linéaire**")
   st.write(" ")
   st.markdown("""<p style='text-align: justify'>Nous avons appliqué la régression linéaire à notre jeu de données afin d'avoir un aperçu de la tendance des prédictions.
               En effet, au vues de nos analyses en amont et des corrélations établies, il semble pertinent d'étudier une potentielle évolution linéaire entre nos valeurs réelles et les valeurs prédites.
               Suite cela, nous avons pu constater qu'une évolution croissante et continue des anomalies de températures apparaissent.
                   </p>""",  unsafe_allow_html=True)


   fig = plt.figure(figsize = (7,7))
   regressor = LinearRegression()
   regressor.fit(X_train2, y_train)

   pred_test = regressor.predict(X_test2)
   plt.scatter(pred_test, y_test, c='green')

   plt.plot((y_test.min(), y_test.max()), (y_test.min(), y_test.max()), color = 'red')
   plt.xlabel("Valeurs prédites")
   plt.ylabel("Valeurs réelles")
   plt.title('Régression Linéaire')
   plt.show()
   st.pyplot(fig)



   #Présentation des features_importances
   st.write(" ")
   st.title("**L'importance des caractéristiques**") 
   st.write(" ")   
   st.markdown("""<p style='text-align: justify'>En fonction des différents modèles nous avons souhaité savoir quels sont les variables ayant le plus d'impact sur les anomalies de températures. Cela varie en fonction du modèle choisi.
                   </p>""",  unsafe_allow_html=True)

   #Arbre de décision
   with st.expander("Feature importances - Arbre de décision"):
       image = Image.open('./img/FI - Arbre decision.png')
       image2 = Image.open('./img/FI2 - Arbre decision.png')
       st.image(image, width=450)
       st.image(image2, width=450)


   #Random Forest
   with st.expander("Feature importances - Random Forest"):
       image3 = Image.open('./img/FI - RandomForest.png')
       image4 = Image.open('./img/FI2 - RandomForest.png')
       st.image(image3, width=450)
       st.image(image4, width=450)
       
       
    #Lasso   
   with st.expander("Feature importances - Lasso"):
       image5 = Image.open('./img/FI - Lasso.png')
       image6 = Image.open('./img/FI2 - Lasso.png')
       st.image(image5, width=450)
       st.image(image6, width=450)  
     
   #Gradient Boosting
   with st.expander("Feature importances - GradientBoosting"):
       image7 = Image.open('./img/FI - GradientBoosting.png')
       image8 = Image.open('./img/FI2 - GradientBoosting.png')
       st.image(image7, width=450)
       st.image(image8, width=450)

       
   st.markdown("""<p style='text-align: justify'>Au vu des résultats obtenues à la suite de cette étape de modélisation :
               </p>""",  unsafe_allow_html=True)
   st.markdown("<ul><li>- Limites des données</ul></li>",  unsafe_allow_html=True)
   st.markdown("<ul><li>- Sujet complexe qui nécessite un grand nombre de caractéristiques</ul></li>",  unsafe_allow_html=True)
   st.markdown("<ul><li>- Modèle de Machine Learning non nécessaire car les données suivent un modèle linéaire temporelle</ul></li>",  unsafe_allow_html=True)
   st.markdown("<ul><li>- Prédictions réalisables avec une régression linéaire</ul></li>",  unsafe_allow_html=True)


   #Prédictions     
   st.write(" ")
   st.write(" ")
   st.markdown('''  
        <div class="box">
            <h3 class="title is-3 has-text-info has-text-centered">Prédictions</h3>
        </div>''', unsafe_allow_html=True)
   st.write(" ")

   st.write(" ")
   st.markdown("""<p style='text-align: justify'>Pour la réalisation des nos prédictions nous avons choisi un modèle de régression linéaire. En effet, il nous semble plus pertinent d'utiliser ce modèle simple au lieu des modèles de Machine Learning entrainés précédemment car nos données suivent une évolution linéaire croissante dans le temps.
                   </p>""",  unsafe_allow_html=True)
   st.write(" ")
   st.markdown(""" 
      <p style='text-align: justify'>En créant une variable contenant les années futures (soit entre 2022 et 2060), on peut appliquer la fonction issue du modèle de régression et l’appliquer à cette fonction. Nous pouvons ainsi extrapoler les anomalies futures.
      </p>""", unsafe_allow_html=True)

  
   st.image("./img/projection_2060.png")


   st.write(" ")
   st.markdown(""" 
      <p style='text-align: justify'>Les prédictions suivent bien la tendance générale à la hausse, avec des anomalies de température dépassant un degré et demi d’ici 2060.
Bien entendu, ce modèle a ses limites ! Avec plus de temps, nous aurions pu étudier des prédictions avec d’autres modèles pour affiner nos observations.
      </p>""", unsafe_allow_html=True)
  
      
   st.write(" ")
   st.write(" ")
   st.markdown('''  
        <div class="box">
            <h3 class="title is-3 has-text-info has-text-centered">Prédire la température de la France</h3>
        </div>''', unsafe_allow_html=True)
   st.write(" ")
   st.markdown('''
              Après avoir essayé toutes les méthodes ci-dessus, nous nous demandés s’il n’existe pas un modèle plus simple pour prédire la hausse des températures ?
    Prédire la température globale nécessite de fournir un jeu de données global de tous les pays au modèle d’analyse. Nous avons dans un premier temps appliqué une régression linéaire sur le jeu de donnée GlobalTemperatures.csv qui reprend les températures globales de la surface terrestre.
    Nous appliquons une technique de diffusion des données (forecasting)
    ''')
 
    #Présentation des prédictions globales et en France
   st.write(" ")
   st.write(" ")
   st.write("**Prédictions des évolutions des températures terrestres moyennes globales 🌍 :**")
   st.write(" ")

   col1, col2, col3, col4 = st.columns(4)

   with col1:
      st.write("Evolution par an")
      st.write("+0,018°C")

   with col2:
      st.write("Evolution par décennie")
      st.write("+0,185°C")

   with col3:
      st.write("Température terrestre en 2030")
      st.write("9,85°C")  
      
   with col4:
      st.write("Température terrestre en 2050")
      st.write("10,22°C")

   st.write(" ")
   st.write(" ")
   st.markdown('''
               <p>Après prédiction sur ce data set, nous faisons l’interprétation suivante :
   Chaque année, la température moyenne des surfaces terrestres augmente en moyenne de 0.018 °C.</p>

    <p>Tous les dix ans, la température moyenne des terres augmente en moyenne de 0,185 °C. La température moyenne des terres en 2030 sera de 9,85 °C et en 2050 de 10,22 °C.
   <p>Le modèle appliqué sur le jeu de donnée isolé de la France permet de faire les prédictions suivantes :</p>
   <br>
   <p>Coefficients: 1.25376118e-05</p>
   <p>Mean squared error: 25.13</p>
   <p>Variance score : -0.01</p>
   <br>
    </p>''', unsafe_allow_html=True)

   st.write(" ")
   st.write("**Prédictions des températures terrestres moyennes en France 🇫🇷 :**")
                   
   col1, col2, col3 = st.columns(3)

   with col1:
      st.write("➢  2030")
      st.write("13,209°C")

   with col2:
      st.write("➢  2050")
      st.write("13,271°C")

   with col3:
      st.write("➢  2100")
      st.write("13,426°C")


########################################################################################
   st.divider()
   from sklearn.utils import shuffle
   from sklearn import linear_model

   # Chargement des données
   df = pd.read_csv("./datasets/GlobalLandTemperaturesByCountry.csv", index_col=0, parse_dates=True)

   # Fonction pour la prédiction de température
   def predict_temperature(date):
       # Filtrage des données pour la France
       df_france = df.loc[df["Country"]=="France"].copy()
       df_france = df_france.dropna(subset=["AverageTemperature"])
       
       # Mélange des données et calcul du nombre de jours depuis le jour 1 dans l'ensemble de données
       temp = shuffle(df_france["AverageTemperature"])
       days_since = pd.Series((temp.keys().year * 365 + temp.keys().month * 30 + temp.keys().day) - (1796*365 + 1*30 + 1), index=temp.keys(), name="DaysSince")
       data = pd.concat([temp, days_since], axis=1)
       
       # Division des données en ensembles d'apprentissage et de test
       train = data.iloc[:-int(len(data)*.2)]
       test = data.iloc[-int(len(data)*.2):]
       
       # Entraînement du modèle de régression linéaire
       regr = linear_model.LinearRegression()
       regr.fit(train["DaysSince"].to_frame(), train["AverageTemperature"].to_frame())
       
       # Prédiction de la température pour la date donnée
       days_since_date = (pd.to_datetime(date).year * 365 + pd.to_datetime(date).month * 30 + pd.to_datetime(date).day) - (1796*365 + 1*30 + 1)
       temperature_pred = regr.predict(pd.DataFrame([days_since_date], columns=["DaysSince"]))
       
       return temperature_pred[0][0]

   # Chargement des données
   df = pd.read_csv("./datasets/GlobalLandTemperaturesByCountry.csv", index_col=0, parse_dates=True)

   st.write(" ")
   st.write(" ")
   st.markdown('''  
        <div class="box">
            <h3 class="title is-3 has-text-info has-text-centered">Testez la prédiction en choisissant une date !</h3>
        </div>''', unsafe_allow_html=True)
   st.write(" ")

   # Interface utilisateur Streamlit
   st.title("Prédiction de la température")

   # Sélection de la date
   date = st.date_input("Sélectionnez une date")

   if date:
       # Prédiction de la température pour la date sélectionnée
       temperature_pred = predict_temperature(date)
       st.write("Température prédite pour la France le", date, ":", round(temperature_pred, 3))