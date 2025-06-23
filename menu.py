import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# CONFIGURACIÓN INICIAL
st.set_page_config(
    page_title="Plataforma de Trazabilidad",
    page_icon="🏥",
    layout="centered"
)

# TÍTULO PRINCIPAL
st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")

# VALIDACIÓN MANUAL DE CORREO (ejemplo simple)
email_input = st.text_input("Ingresa tu correo institucional para continuar:")

allowed_email = st.secrets["access"]["allowed_email"]

if email_input:
    if email_input != allowed_email:
        st.error("🚫 Acceso denegado. Tu cuenta no está autorizada.")
        st.info(f"📧 Cuenta utilizada: {email_input}")
        st.stop()
    else:
        st.success(f"✅ Acceso concedido: {email_input}")

        # Conectar a Google Sheets
        info = st.secrets["google_service_account"]
        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        credentials = Credentials.from_service_account_info(info, scopes=SCOPES)
        client = gspread.authorize(credentials)

        st.success("Conexión a Google Sheets exitosa ✅")
        # Aquí puedes abrir un spreadsheet por ID y trabajar con él
        # sheet = client.open_by_key("TU_SPREADSHEET_ID").sheet1
