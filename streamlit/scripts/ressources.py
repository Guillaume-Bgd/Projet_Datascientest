import streamlit as st

def ressources():

	st.image("./img/ressources.jpg")
	credit_text = "Crédit : [Les echos](https://www.lesechos.fr/2015/08/le-stock-mondial-de-ressources-renouvelables-samenuise-269495)"
	st.markdown(credit_text)
	st.write(" ")
	st.markdown('''  
	    <div class="box">
	        <h3 class="title is-3 has-text-info has-text-centered">Ressources</h3>
	    </div><br>''', unsafe_allow_html=True)
	st.write(" ")


	st.write("Ressources pour l'analyse des températures mondiales :")

	st.markdown("● NASA - Global Land-Ocean Temperature Index in 0.01 degrees Celsius")
	st.markdown("[Lien vers les données](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt)")

	st.markdown("● Our World in Data - Data on CO2 and Greenhouse Gas Emissions")
	st.markdown("[Lien vers les données](https://github.com/owid/co2-data)")

	st.markdown("● Our World in Data - Surface temperature anomaly")
	st.markdown("[Lien vers les données](https://ourworldindata.org/grapher/hadcrut-surface-temperature-anomaly)")

	st.markdown("● NOAA Global Temperature Anomalies - Graphing Tool")
	st.markdown("[Lien vers les données](https://www.climate.gov/maps-data/dataset/global-temperature-anomalies-graphing-tool)")

	st.markdown("● GitHub - Global Land and Ocean-and-Land Temperatures")
	st.markdown("[Lien vers les données](https://github.com/gindeleo/climate)")

	st.markdown("● Wikipédia - Anomalies de températures")
	st.markdown("[Lien vers les données](https://en.wikipedia.org/wiki/Temperature_anomaly)")

