import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# CONFIGURACIÓN INICIAL
st.set_page_config(
    page_title="Plataforma de Trazabilidad",
    page_icon="🏥",
    layout="centered"
)

# LOGIN CON GOOGLE OAUTH
st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")

# Recuperar usuario autenticado y correo permitido desde secrets
user = st.session_state.get("user")
allowed_email = st.secrets["access"]["allowed_email"]

if not user:
    st.write("Por favor, autentifíquese para continuar.")
    if st.button("Iniciar Sesión con Google"):
        st.login("google")
    st.stop()

email = user.get("email")
if email != allowed_email:
    st.error("🚫 Acceso denegado. Tu cuenta no está autorizada.")
    st.info(f"📧 Cuenta utilizada: {email}")
    if st.button("Cerrar sesión"):
        st.logout()
    st.stop()

# Acceso exitoso
st.title("Plataforma de trazabilidad")

# Autenticación con Google Sheets
info = st.secrets["google_service_account"]
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(info, scopes=SCOPES)
client = gspread.authorize(credentials)

st.success(f"Sesión iniciada correctamente como: {email}")

if st.button("Cerrar sesión"):
    st.logout()

# Aquí podrías mostrar más funcionalidades...
# st.write(client.open_by_key("..."))