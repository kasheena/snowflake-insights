import streamlit as st

from utils import gui
# Make sure session state is preserved
for key in st.session_state:
    st.session_state[key] = st.session_state[key]

st.title("Welcome to the Usage Insights app!")
st.sidebar.text(f"Account: {st.secrets.sf_usage_app.account}")
st.sidebar.info("Choose a page!")
st.markdown(
    """
This app provides insights on a demo Snowflake account usage.

### Get started!

👈 Select a page in the sidebar!
    """
)
