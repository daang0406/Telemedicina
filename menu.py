import streamlit as st

# Título principal
st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")

# Texto descriptivo (opcional)
st.write("Por favor, autentifíquese para continuar.")

# Botón de autenticación
if st.button("Autenticar con Google"):
    st.login("google")
