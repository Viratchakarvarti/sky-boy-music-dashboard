import streamlit as st
import random

def get_trends():
    # Simulation of top 15 trending tags
    tags = ["#LofiMusic", "#Shayari", "#DesiRap", "#NewTrack", "#SkyBoy", "#SadVibes", 
            "#Trending2026", "#MusicProducer", "#ViralReels", "#Heartbreak", 
            "#TrendingAudio", "#EmotionalRap", "#ArtistLife", "#SpotifyIndia", "#Lyrics"]
    return tags

def get_audience_time():
    return "8:30 PM - 10:00 PM"

def show_tracker():
    st.subheader("🔥 Auto-Trend & Audience Alert")
    st.write(f"**Top 15 Tags:** {', '.join(get_trends())}")
    st.info(f"**Best Time to Post:** {get_audience_time()}")
