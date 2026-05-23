import streamlit as st
import time
from trend_tracker import show_tracker
from lyrics_engine import show_engine
from audience_manager import show_engagement

st.set_page_config(page_title="Sky Boy Dashboard", layout="wide")
st.title("🚀 Sky Boy Music Dashboard")

# Navigation Sidebar
menu = ["Trend Tracker", "Content Engine", "Engagement"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Trend Tracker":
    show_tracker()
    # Auto-refresh loop
    if st.button("Refresh Trends"):
        st.rerun()
elif choice == "Content Engine":
    show_engine()
elif choice == "Engagement":
    show_engagement()

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by Sky Boy")
