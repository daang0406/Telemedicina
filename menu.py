import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# CONFIGURACIÓN INICIAL
st.set_page_config(
    page_title="Plataforma de Trazabilidad",
    page_icon="🏥",
    layout="centered"
)

# LOGIN SIMPLE CON EMAIL RESTRINGIDO
st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")

# Función de autenticación simple
def check_authentication():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        email = st.text_input("Email:")
        
        if st.button("Iniciar Sesión"):
            allowed_email = st.secrets["access"]["allowed_email"]
            if email == allowed_email:
                st.session_state.authenticated = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("🚫 Acceso denegado. Tu cuenta no está autorizada.")
                st.info(f"📧 Cuenta utilizada: {email}")
        return False
    return True

# Verificar autenticación
if not check_authentication():
    st.stop()

# Acceso exitoso
st.title("Plataforma de trazabilidad")

if st.button("Cerrar sesión"):
    st.session_state.authenticated = False
    st.rerun()

# Autenticación con Google Sheets
info = st.secrets["google_service_account"]
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(info, scopes=SCOPES)
client = gspread.authorize(credentials)

st.success(f"Sesión iniciada correctamente como: {st.session_state.user_email}")

# Aquí podrías mostrar más funcionalidades...
# st.write(client.open_by_key("..."))