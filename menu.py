import streamlit as st

st.set_page_config(page_title="Test Auth")

st.title("🔐 Prueba de Login con Google")

user = st.session_state.get("user")

if not user:
    st.write("Haz clic para iniciar sesión.")
    if st.button("Login con Google"):
        st.login("google")
    st.stop()

st.success(f"¡Autenticado como {user['email']}!")
if st.button("Cerrar sesión"):
    st.logout()
