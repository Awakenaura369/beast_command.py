import streamlit as st
from groq import Groq
import pandas as pd
import plotly.express as px

# --- إعداد الأمان والوحش (Groq) ---
# تأكد من وضع GROQ_API_KEY في Streamlit Secrets
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("⚠️ API Key missing! Add 'GROQ_API_KEY' to your Streamlit Secrets.")

# --- إعدادات الصفحة الفخمة ---
st.set_page_config(page_title="BEAST COMMAND CENTER", layout="wide", initial_sidebar_state="expanded")

# --- CSS مخصص لإضفاء طاقة الثراء ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🦁 BEAST COMMAND")
st.sidebar.subheader("Strategic Arsenal")
menu = st.sidebar.radio("CHOOSE YOUR WEAPON:", [
    "📈 Performance Tracker", 
    "🎨 Portfolio Architect", 
    "🎯 Cold Outreach Hunter",
    "💰 ROI Predictor",
    "🧠 Beast Strategy Room"
])

# --- 1. MODULE: Performance Tracker ---
if menu == "📈 Performance Tracker":
    st.header("📈 Fiverr Performance Analytics")
    col1, col2, col3 = st.columns(3)
    with col1: imp = st.number_input("Impressions", value=1000)
    with col2: clicks = st.number_input("Clicks", value=30)
    with col3: orders = st.number_input("Orders", value=2)
    
    ctr = (clicks / imp * 100) if imp > 0 else 0
    st.markdown("---")
    m1, m2, m3 = st.columns(3)
    m1.metric("Click-Through Rate (CTR)", f"{ctr:.2f}%", delta="Beast Mode" if ctr > 2 else "Improve It")
    m2.metric("Conversion Rate", f"{(orders/clicks*100 if clicks > 0 else 0):.2f}%")
    m3.metric("Total Revenue", f"${orders * 30}")
    
    df = pd.DataFrame({"Metric": ["Impressions", "Clicks*10", "Orders*100"], "Value": [imp, clicks*10, orders*100]})
    fig = px.bar(df, x="Metric", y="Value", color="Metric", template="plotly_dark", title="Growth Velocity Chart")
    st.plotly_chart(fig, use_container_width=True)

# --- 2. MODULE: Portfolio Architect ---
elif menu == "🎨 Portfolio Architect":
    st.header("🎨 Portfolio Masterpiece Creator")
    product = st.text_input("Product Name (e.g., Eco-Friendly Bottle)")
    tone = st.selectbox("Tone", ["Luxury", "Aggressive", "Scientific", "Minimalist"])
    
    if st.button("🚀 Craft Portfolio Case Study"):
        with st.spinner("The Beast is building your portfolio..."):
            prompt = f"Create a full marketing case study for {product} in a {tone} tone. Include: Project Title, The Hook, Ad Copy, Laser-Targeting (Interests/Behaviors), and an AI Image Prompt."
            res = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
            st.success("Masterpiece Ready!")
            st.markdown(res.choices[0].message.content)

# --- 3. MODULE: Cold Outreach Hunter ---
elif menu == "🎯 Cold Outreach Hunter":
    st.header("🎯 Cold Outreach Hunter")
    target = st.text_input("Target Client (e.g., Real Estate Agent in Dubai)")
    platform = st.selectbox("Platform", ["LinkedIn", "Instagram DM", "Email"])
    
    if st.button("Generate Poisonous Script"):
        prompt = f"Write a killer {platform} outreach message to {target}. Use a bold, expert tone. Focus on how my AI-powered marketing (Groq) beats the competition. Make it short and impossible to ignore."
        res = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
        st.code(res.choices[0].message.content, language='text')

# --- 4. MODULE: ROI Predictor ---
elif menu == "💰 ROI Predictor":
    st.header("💰 The Beast ROI Predictor")
    c1, c2 = st.columns(2)
    with c1:
        budget = st.number_input("Ad Spend ($)", value=1000)
        cpc = st.number_input("CPC ($)", value=0.5)
    with c2:
        conv = st.slider("Conversion Rate (%)", 0.5, 10.0, 2.5)
        price = st.number_input("Product Price ($)", value=50)
    
    sales = (budget / cpc) * (conv / 100)
    rev = sales * price
    roas = rev / budget if budget > 0 else 0
    
    st.markdown("---")
    r1, r2, r3 = st.columns(3)
    r1.metric("Est. Sales", f"{int(sales)} Units")
    r2.metric("Total Revenue", f"${rev:,.2f}")
    r3.metric("Expected ROAS", f"{roas:.2f}x")

# --- 5. MODULE: Beast Strategy Room ---
elif menu == "🧠 Beast Strategy Room":
    st.header("🧠 The War Room")
    problem = st.text_area("What is your biggest business challenge right now?")
    if st.button("Consult the AI Oracle"):
        res = client.chat.completions.create(messages=[{"role": "user", "content": f"You are a world-class marketing billionaire. Solve this: {problem}"}], model="llama-3.3-70b-versatile")
        st.info("The Beast's Verdict:")
        st.write(res.choices[0].message.content)

st.sidebar.markdown("---")
st.sidebar.write("🦁 **Marketing Beast v2.0**")
st.sidebar.write("Status: **Dominating the Market**")
