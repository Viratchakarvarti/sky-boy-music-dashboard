import streamlit as st

def generate_viral_package(title, theme, lyrics):
    desc = f"""🎵 Title: {title}
✨ Theme: {theme}

{lyrics}

--------------------------------------------------
Subscribe for more Lofi & Desi Rap!
#SkyBoy #Music #NewSong2026 #Trending #ViralMusic

Follow on: @nmxmusicyt | @feelthelinesyt
"""
    keywords = "Sky Boy music, viral song, lofi ghazal, desi rap, emotional shayari, trending 2026, music producer"
    return desc, keywords

def show_engine():
    st.subheader("✍️ Viral Content Engine")
    title = st.text_input("Song Title:")
    theme = st.text_input("Song Theme:")
    snippet = st.text_area("Snippet:")
    
    if st.button("Generate Package"):
        d, k = generate_viral_package(title, theme, snippet)
        st.subheader("📝 Description:")
        st.text_area("Copy this:", value=d, height=200)
        st.subheader("🔑 SEO Tags:")
        st.text_area("Copy this:", value=k)
