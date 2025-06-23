import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Configuración de la página
st.set_page_config(page_title="Plataforma de Trazabilidad", page_icon="🏥", layout="centered")

# Recuperar usuario autenticado
user = st.session_state.get("user")
allowed_email = st.secrets["access"]["allowed_email"]

# Si el usuario no está autenticado
if not user:
    st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")
    st.write("Por favor, inicia sesión con tu cuenta autorizada.")
    if st.button("🔐 Iniciar sesión con Google"):
        st.login("google")
    st.stop()

# Verifica el correo autenticado
email = user.get("email")

if email != allowed_email:
    st.error("🚫 Acceso denegado. Este correo no está autorizado.")
    st.info(f"Correo autenticado: {email}")
    if st.button("Cerrar sesión"):
        st.logout()
    st.stop()

# Si todo está correcto
st.success(f"✅ Bienvenido {email}")
st.title("Plataforma de trazabilidad")

# Conexión a Google Sheets
info = st.secrets["google_service_account"]
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
credentials = Credentials.from_service_account_info(info, scopes=scopes)
client = gspread.authorize(credentials)

st.success("Conectado a Google Sheets ✅")
