import streamlit as st
from groq import Groq
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

# --- الربط مع المحرك النووي (Groq) ---
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("⚠️ API Key missing! Add 'GROQ_API_KEY' to your Streamlit Secrets.")

# --- إعدادات الصفحة الفخمة ---
st.set_page_config(page_title="BEAST COMMAND V4.0", layout="wide")

# --- 🎨 الـ CSS المتطور (دمج لغات البرمجة) ---
st.markdown("""
    <style>
    .stApp { background: #010409; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    div.stButton > button {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff8a8a 100%);
        color: white; border: none; border-radius: 12px;
        padding: 12px 24px; font-weight: bold; width: 100%;
        transition: 0.3s all ease-in-out;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 75, 75, 0.4);
    }
    .stNumberInput, .stTextInput, .stTextArea, .stSelectbox {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 10px !important;
        color: white !important;
    }
    h1, h2, h3 { color: #f0f6fc !important; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 🚀 وظيفة HTML/CSS للبطاقات (The Visual Engine) ---
def render_beast_card(title, value, subtitle, color="#ff4b4b"):
    card_html = f"""
    <div style="
        background: #161b22; border: 1px solid #30363d; border-top: 5px solid {color};
        padding: 20px; border-radius: 15px; color: white;
        font-family: 'Segoe UI', sans-serif; box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    ">
        <div style="color: #8b949e; font-size: 0.8em; font-weight: bold; text-transform: uppercase;">{title}</div>
        <div style="font-size: 2.5em; font-weight: 900; margin: 5px 0; color: white;">{value}</div>
        <div style="color: {color}; font-size: 0.9em; font-weight: 500;">{subtitle}</div>
    </div>
    """
    components.html(card_html, height=170)

# --- Sidebar Navigation (ترسانة الأسلحة) ---
st.sidebar.title("🦁 BEAST ARSENAL")
menu = st.sidebar.selectbox("SELECT WEAPON", [
    "📈 Performance Tracker", 
    "🚀 Gig Booster (Link)",
    "🎨 Portfolio Architect", 
    "🎯 Outreach Hunter", 
    "💰 ROI Predictor",
    "☢️ Trigger Map",
    "⚡ Viral Hooks",
    "🧠 Strategy War Room"
])

# --- 1. MODULE: Performance Tracker ---
if menu == "📈 Performance Tracker":
    st.header("📈 Business Analytics")
    c1, c2, c3 = st.columns(3)
    with c1: imp = st.number_input("Impressions", min_value=1, value=1500)
    with c2: clicks = st.number_input("Clicks", min_value=0, value=50)
    with c3: orders = st.number_input("Orders", min_value=0, value=3)
    
    ctr = (clicks/imp*100) if imp > 0 else 0
    st.markdown("---")
    m1, m2, m3 = st.columns(3)
    with m1: render_beast_card("REACH", f"{imp:,}", "Total Visibility", "#58a6ff")
    with m2: render_beast_card("CTR", f"{ctr:.2f}%", f"{clicks} clicks", "#bc8cff")
    with m3: render_beast_card("REVENUE", f"${orders*30}", "Beast Profit", "#3fb950")

# --- 2. MODULE: Gig Booster (NEW) ---
elif menu == "🚀 Gig Booster (Link)":
    st.header("🚀 Gig URL Intelligence")
    gig_url = st.text_input("Paste your Fiverr Gig URL:")
    if gig_url:
        st.success("Link Armed! 🎯")
        action = st.radio("Action:", ["SEO Analysis", "Social Media Promo"])
        if st.button("Launch Action"):
            prompt = f"Analyze/Promote this Gig URL: {gig_url}. Platform/Action: {action}. Be aggressive and high-converting."
            res = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
            st.info("The Result:")
            st.write(res.choices[0].message.content)

# --- 3. MODULE: Portfolio Architect ---
elif menu == "🎨 Portfolio Architect":
    st.header("🎨 Portfolio Architect")
    niche = st.text_input("Niche/Product Name")
    if st.button("Build Masterpiece"):
        res = client.chat.completions.create(messages=[{"role": "user", "content": f"Create a viral portfolio case study for {niche}."}], model="llama-3.3-70b-versatile")
        st.markdown(res.choices[0].message.content)

# --- 4. MODULE: Outreach Hunter ---
elif menu == "🎯 Outreach Hunter":
    st.header("🎯 Cold Outreach Hunter")
    target = st.text_input("Target (e.g., E-com CEO)")
    plat = st.selectbox("Platform", ["LinkedIn", "Instagram", "Email"])
    if st.button("Generate Poison Script"):
        res = client.chat.completions.create(messages=[{"role": "user", "content": f"Write a killer {plat} script to {target}."}], model="llama-3.3-70b-versatile")
        st.code(res.choices[0].message.content)

# --- 5. MODULE: ROI Predictor ---
elif menu == "💰 ROI Predictor":
    st.header("💰 ROI Predictor")
    rc1, rc2 = st.columns(2)
    with rc1: bud = st.number_input("Budget ($)", value=1000)
    with rc2: p_price = st.number_input("Product Price ($)", value=50)
    if st.button("Predict Wealth"):
        render_beast_card("Potential ROI", f"{((bud*2)/bud)*100}%", "Estimated Growth", "#ffcc00")

# --- 6. MODULE: Trigger Map ---
elif menu == "☢️ Trigger Map":
    st.header("☢️ Psychological Trigger Map")
    audience = st.text_input("Target Audience (e.g., Small Biz Owners)")
    if st.button("Decode Psychology"):
        res = client.chat.completions.create(messages=[{"role": "user", "content": f"Give me the deepest fears and desires of {audience}."}], model="llama-3.3-70b-versatile")
        st.write(res.choices[0].message.content)

# --- 7. MODULE: Viral Hooks ---
elif menu == "⚡ Viral Hooks":
    st.header("⚡ Viral Hook Generator")
    topic = st.text_input("Content Topic")
    if st.button("Generate Hooks"):
        res = client.chat.completions.create(messages=[{"role": "user", "content": f"Give me 5 scroll-stopping hooks for {topic}."}], model="llama-3.3-70b-versatile")
        st.success(res.choices[0].message.content)

# --- 8. MODULE: Strategy War Room ---
elif menu == "🧠 Strategy War Room":
    st.header("🧠 Beast War Room")
    prob = st.text_area("Describe the market war...")
    if st.button("Consult the Beast"):
        res = client.chat.completions.create(messages=[{"role": "user", "content": f"Solve this marketing problem like a billionaire: {prob}"}], model="llama-3.3-70b-versatile")
        st.write(res.choices[0].message.content)

st.sidebar.markdown("---")
st.sidebar.write("🦁 **Beast Command V4.0**")
st.sidebar.write("Status: **Nuclear Ready** ☢️")
