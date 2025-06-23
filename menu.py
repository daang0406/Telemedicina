import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Título antes del login
st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")

# Obtener usuario autenticado (si existe)
user = st.session_state.get("user")
allowed_email = st.secrets["access"]["allowed_email"]

# Si el usuario no está autenticado
if not user:
    st.write("Por favor, autentifíquese para continuar.")
    if st.button("Autenticar con Google"):
        st.login("google")

# Si el usuario está autenticado
else:
    email = user.get("email")

    # Validar si es el correo permitido
    if email == allowed_email:
        st.title("Plataforma de trazabilidad")

        # Conexión con Google Sheets
        info = st.secrets["google_service_account"]
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        credenciales = ServiceAccountCredentials.from_json_keyfile_dict(info, scope)
        cliente = gspread.authorize(credenciales)

        st.success(f"Sesión iniciada como: {email}")

    else:
        st.error("Acceso denegado. Este correo no está autorizado.")
        if st.button("Cerrar sesión"):
            st.logout()
