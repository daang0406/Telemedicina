import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Configuración de la página
st.set_page_config(page_title="Plataforma de Trazabilidad", layout="centered")

# Email permitido desde secrets
allowed_email = st.secrets["access"]["allowed_email"]

def login_screen():
    st.header("🔐 Acceso restringido")
    st.subheader("Esta app es privada. Inicia sesión para continuar.")
    if st.button("Iniciar sesión con Google"):
        st.login("google")

def main_app(email):
    st.title("🏥 Plataforma de Trazabilidad de Insumos Médicos")
    st.success(f"Bienvenido: {email}")

    # Conexión a Google Sheets
    info = st.secrets["google_service_account"]
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    credentials = Credentials.from_service_account_info(info, scopes=scopes)
    client = gspread.authorize(credentials)
    st.success("Conexión con Google Sheets exitosa ✅")

# Flujo principal
user = st.session_state.get("user")

if not user:
    login_screen()
    st.stop()

email = user.get("email")

if email != allowed_email:
    st.error("🚫 Acceso denegado. Tu cuenta no está autorizada.")
    st.info(f"Correo autenticado: {email}")
    if st.button("Cerrar sesión"):
        st.logout()
    st.stop()

# Si todo está bien
main_app(email)