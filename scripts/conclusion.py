
import streamlit as st


def conclusion():
    st.image("./img/terre.png")
    credit_text = "Crédit : [Wikipedia](https://fr.m.wikipedia.org/wiki/Fichier:The_Earth_seen_from_Apollo_17_with_white_background.jpg)"
    st.markdown(credit_text)
    st.write(" ")
    st.markdown('''  
        <div class="box">
            <h3 class="title is-3 has-text-info has-text-centered">Conclusion</h3>
        </div>''', unsafe_allow_html=True)
    st.write(" ")

    st.markdown("""
<br>
    <p style='text-align: justify'>L'élaboration de notre projet nous permet d’avancer l’hypothèse que les anomalies des températures terrestres sont, sans équivoque, 
    liées aux activités humaines et notamment aux émissions de CO2 résultant des différentes industries et de l’exploitation des ressources pétrolières.
    Il est donc très probable que, tant que ces facteurs continueront d’augmenter, nous assisterons à une augmentation des anomalies de la température à la hausse<p>
<br>
    <p style='text-align: justify'>Afin d’étudier davantage le phénomène du réchauffement climatique il serait intéressant d’avoir d’autres variables explicatives spécifiques. 
    En effet, l’étude approfondie de nos données a relevé certaines limites et, si le temps nous le permettait, il serait très intéressant de connaître 
    les subtilités du fonctionnement du dérèglement climatique terrestre grâce à d’autres données, notamment les températures océaniques ou d’autres données climatiques.
    Des données issues des moyens de transports utilisés par les hommes (navires, avions, voitures) seraient également utiles. 
    Les activités humaines sont-elles bien les seules responsables du dérèglement que nous constatons ?</p>
<br>
    <p style='text-align: justify'>Ce projet nous a permis d’étudier une thématique que nous ne connaissions que de manière 
    superficielle (de part sa couverture médiatique notamment) et également à apprendre, grâce à l’analyse des données, à observer visuellement l’évolution du 
    phénomène observé, de poser des hypothèses et, pourquoi pas, d’établir une conclusion. D’autre part, nous avons su identifier les limites de nos ressources 
    et dresser une liste de nos besoins pour une éventuelle analyse plus poussée.</p>
<br>
    <p style='text-align: justify'>Enfin, ce projet nous a permis de mettre en pratique les connaissances que nous avons acquises au cours de notre formation
    et d’apprendre concrètement ce qui est attendu d’un Data Analyst. Toutes les techniques que nous avons découvertes, comme la collecte et le nettoyage
     des données, le processing puis la data visualisation et la modélisation nous ont été indispensables pour mener notre projet à bien 
     et conclure à des observations factuelles vérifiées.</p>
""", unsafe_allow_html=True)