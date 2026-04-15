import streamlit as st
from recupererData import RecupererData
from isoFormat import formater_temps

st.set_page_config(page_title="IDF-TRANSPORT", layout="centered")

st.title("🚇 IDF-TRANSPORT")
st.markdown("### Récupérez le délai de transport pour une ligne et un arrêt donnés.")

with st.form("search_form"):
    ville = st.text_input("Choisissez votre ville")
    arret = st.text_input("Choisissez votre arrêt")
    bus = st.text_input("Choisissez votre bus")
    
    submit = st.form_submit_button("Lancer la recherche", use_container_width=True)

if submit:
    if not ville or not arret or not bus:
        st.warning("Veuillez remplir tous les champs.")
    else:
        with st.spinner('Recherche en cours...'):
            resultat = RecupererData(bus=bus, ville=ville, arret=arret)

        if isinstance(resultat, dict):
            st.divider()
            t_initial = formater_temps(resultat.get("temps_initial"))
            t_reel = formater_temps(resultat.get("temps_reel"))
            
            res_col1, res_col2 = st.columns(2)
            
            with res_col1:
                
                st.metric(label="Temps Initial", value=t_initial)
            
            with res_col2:
                st.metric(label="Temps Réel", value=t_reel)
        else:
            st.error(resultat)