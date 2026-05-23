import streamlit as st
from trend_tracker import show_tracker
from lyrics_engine import show_engine
from audience_manager import show_engagement

st.set_page_config(page_title="Sky Boy Dashboard", layout="wide")
st.title("🚀 Sky Boy Music Dashboard")

# Navigation
menu = ["Dashboard", "Content Engine", "Engagement"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Dashboard":
    show_tracker()
elif choice == "Content Engine":
    show_engine()
elif choice == "Engagement":
    show_engagement()
  
