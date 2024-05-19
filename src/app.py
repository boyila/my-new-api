import streamlit as st
from UIPages.home_page import Conversation


# Function to navigate to different pages
def navigate_to_page(page):
    st.session_state.page = page

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def get_insights():
    with st.sidebar.container():
        st.title("Educational knowledge")
        user_input = st.sidebar.chat_input("type your question here")

def talk_to_robert():
    Conversation().start_conversation()

# Define the content of each page
def home_page():
    st.write("<Financial health dashboard here>")
    talk_to_robert()

def insights_page():
    st.write("<insights and educational recomendations here>")
    get_insights()

def alerts_page():
    st.write("<Alerts list here>")

st.title("FinThrivin")

with st.container():
    st.markdown(
        """
            <style>
            .custom-column {
                padding: 10px 10px; /* Adjust the padding as needed */
            }
            </style>
        """,
        unsafe_allow_html=True
        )
    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        if st.button("🏠 Home", key='home_button'):
            navigate_to_page('Home')
    with col2:
        if st.button("💡 Insights", key='Insights_button'):
            navigate_to_page('Insights')
    with col3:
        if st.button("🔔 Alerts", key='Alerts_button'):
            navigate_to_page('Alerts')

# Render the current page based on the session state
if st.session_state.page == 'Home':
    home_page()
elif st.session_state.page == 'Insights':
    insights_page()
elif st.session_state.page == 'Alerts':
    alerts_page()
