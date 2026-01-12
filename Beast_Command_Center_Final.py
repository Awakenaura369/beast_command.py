import streamlit as st
from groq import Groq
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

# --- الأمان والربط مع الوحش ---
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("⚠️ API Key missing! Check your Streamlit Secrets.")

# --- إعدادات الصفحة ---
st.set_page_config(page_title="BEAST COMMAND CENTER V3", layout="wide")

# --- 🎨 الـ CSS المتقدم (تطوير الواجهة بدمج اللغات) ---
st.markdown("""
    <style>
    .stApp { background: #010409; }
    /* تحسين شكل السايدبار */
    [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    /* أزرار الوحش المتفاعلة */
    div.stButton > button {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff8a8a 100%);
        color: white; border: none; border-radius: 10px;
        padding: 15px 30px; font-weight: bold; width: 100%;
        transition: 0.3s all ease-in-out;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(255, 75, 75, 0.4);
    }
    /* تنسيق النصوص */
    h1, h2, h3 { color: #f0f6fc !important; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 🚀 وظيفة HTML/CSS للبطاقات الاحترافية (Custom Components) ---
def render_beast_card(title, value, subtitle, color="#ff4b4b"):
    card_html = f"""
    <div style="
        background: #161b22; border: 1px solid #30363d; border-top: 4px solid {color};
        padding: 25px; border-radius: 15px; color: white;
        font-family: 'Segoe UI', sans-serif; box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    ">
        <div style="color: #8b949e; font-size: 0.8em; font-weight: bold; letter-spacing: 1px;">{title}</div>
        <div style="font-size: 2.5em; font-weight: 900; margin: 10px 0; color: white;">{value}</div>
        <div style="color: {color}; font-size: 0.9em; font-weight: 500;">{subtitle}</div>
    </div>
    """
    components.html(card_html, height=180)

# --- القائمة الجانبية (The Sidebar) ---
st.sidebar.title("🦁 BEAST V3.0")
menu = st.sidebar.radio("CHOOSE MODULE", [
    "📈 Stats Tracker", 
    "🎨 Portfolio Builder", 
    "🎯 Outreach Hunter", 
    "💰 ROI Predictor",
    "🧠 War Room"
])

# --- 1. Stats Tracker (Visualized) ---
if menu == "📈 Stats Tracker":
    st.header("📈 Business Performance")
    col1, col2, col3 = st.columns(3)
    with col1: render_beast_card("IMPRESSIONS", "1,240", "▲ 15% vs yesterday", "#58a6ff")
    with col2: render_beast_card("CLICKS", "42", "🎯 CTR: 3.38%", "#bc8cff")
    with col3: render_beast_card("REVENUE", "$150", "💰 Beast Mode Active", "#3fb950")
    
    # مبيان Plotly احترافي
    df = pd.DataFrame({'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], 'Clicks': [5, 12, 18, 30, 42]})
    fig = px.area(df, x='Day', y='Clicks', title="Conversion Velocity", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# --- 2. Portfolio Builder ---
elif menu == "🎨 Portfolio Builder":
    st.header("🎨 Portfolio Architect")
    prod = st.text_input("Product Name")
    if st.button("GENERATE PORTFOLIO"):
        res = client.chat.completions.create(
            messages=[{"role": "user", "content": f"Create a full marketing case study for {prod} including ad copy and image prompt."}],
            model="llama-3.3-70b-versatile"
        )
        st.markdown(res.choices[0].message.content)

# --- 3. Outreach Hunter ---
elif menu == "🎯 Outreach Hunter":
    st.header("🎯 Cold Outreach Hunter")
    target = st.text_input("Target Client (e.g. Agency Owner)")
    platform = st.selectbox("Platform", ["LinkedIn", "Instagram", "Email"])
    if st.button("GENERATE SCRIPT"):
        res = client.chat.completions.create(
            messages=[{"role": "user", "content": f"Write a bold {platform} message to {target} selling my AI marketing services."}],
            model="llama-3.3-70b-versatile"
        )
        st.code(res.choices[0].message.content)

# --- 4. ROI Predictor ---
elif menu == "💰 ROI Predictor":
    st.header("💰 ROI Predictor")
    c1, c2 = st.columns(2)
    with c1: budget = st.number_input("Budget ($)", value=1000)
    with c2: price = st.number_input("Product Price ($)", value=50)
    if st.button("Calculate Profits"):
        render_beast_card("Potential Sales", f"{int(budget/25)} Units", "Based on average CPC", "#ffcc00")

# --- 5. War Room ---
elif menu == "🧠 War Room":
    st.header("🧠 Strategy War Room")
    issue = st.text_area("What is your current challenge?")
    if st.button("GET BEAST ADVICE"):
        res = client.chat.completions.create(
            messages=[{"role": "user", "content": f"As a world-class marketing expert, solve: {issue}"}],
            model="llama-3.3-70b-versatile"
        )
        st.info(res.choices[0].message.content)

st.sidebar.markdown("---")
st.sidebar.info("Beast Command Center V3.0 (HTML/CSS/JS Integrated)")
