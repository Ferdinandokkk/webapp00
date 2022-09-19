# myFirstStreamlitApp.py
  
#import the library
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Palmeiras o maior do mundo")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Rony")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Rústico")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("VAMO PRA CIMA PORCOOOOO")

col1, col2, col3 = st.columns(4)
col1.metric("Temperatura", "19 °C", "-15 °C")
col2.metric("Sensação Térmica", "20°C", "-2 °C")
col3.metric("Vento", "30 kmh", "-8%")
col4.metric("Humidade", "86%", "4%")

