import streamlit as st
import pandas as pd
import random

# =========================================
# إعداد الصفحة
# =========================================
st.set_page_config(
    page_title="بوصلة الفرص التقنية | ريماس الدوسري",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# CSS النهائي (إخفاء كل عناصر Streamlit + إصلاح الألوان)
# =========================================
st.markdown("""
<style>

/* اخفاء كل أدوات Streamlit */
#MainMenu, header, footer {visibility:hidden;}
[data-testid="stToolbar"]{display:none;}
[data-testid="stDecoration"]{display:none;}
[data-testid="stStatusWidget"]{display:none;}
[data-testid="stBottomBlockContainer"]{display:none;}
[data-testid="stAppViewContainer"] > .main > div:last-child {display:none;}
button[kind="secondary"]{display:none;} /* زر Manage app */

/* الخط */
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
}

/* خلفية */
.stApp { background-color:#f8fafc; }

/* إصلاح النص داخل الحقول */
div[data-baseweb="select"] > div {
    background-color:white !important;
    color:black !important;
}
input, textarea {
    background-color:white !important;
    color:black !important;
}
label {color:#1e3a8a !important; font-weight:bold;}

/* السايدبار */
section[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#0f172a,#1e293b);
}
section[data-testid="stSidebar"] * {color:white !important;}

/* كرت الفرص */
.hack-item {
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0 4px 20px rgba(0,0,0,0.06);
    margin-bottom:25px;
    border-right:10px solid #1e3a8a;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# قاعدة البيانات (Google Sheet)
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def get_data():
    try:
        df = pd.read_csv(SHEET_URL)
        df.columns = df.columns.str.strip()
        return df.fillna("غير محدد")
    except:
        return None

df = get_data()

# =========================================
# العنوان
# =========================================
st.markdown("<h1 style='text-align:center;color:#1e3a8a;'>🚀 بوصلة الفرص التقنية للطلاب في السعودية</h1>", unsafe_allow_html=True)

# =========================================
# نظام التوصية الذكي 🤖
# =========================================
if df is not None:
    st.markdown("## 🤖 اكتشفي الفرص المناسبة لك")

    col1, col2 = st.columns(2)
    with col1:
        user_major = st.selectbox("🎓 تخصصك", ["اختر"] + sorted(df['major'].unique().tolist()))
        level = st.selectbox("📊 مستواك", ["مبتدئة","متوسطة","متقدمة"])
    with col2:
        interest = st.selectbox("💡 اهتمامك", ["ذكاء اصطناعي","تطبيقات","أمن سيبراني","ويب"])
        team = st.radio("👥 هل لديك فريق؟", ["نعم","لا"])

    if st.button("✨ اقترح لي أفضل الفرص"):
        filtered = df.copy()
        if user_major != "اختر":
            filtered = filtered[filtered['major']==user_major]
        st.success("هذه أفضل فرص مناسبة لك 👇")
        st.dataframe(filtered.head(5))

    st.divider()

# =========================================
# البحث
# =========================================
search_query = st.text_input("🔍 ابحثي عن هاكثون أو جهة منظمة")

if df is not None:
    s1,s2,s3 = st.columns(3)
    s1.metric("عدد الفرص", len(df))
    s2.metric("عدد المدن", df["Location"].nunique())
    s3.metric("عدد التخصصات", df["major"].nunique())

    # أدوات AI
    c1,c2 = st.columns(2)
    if c1.button("✨ ولّد فكرة مشروع"):
        st.success(random.choice(["منصة AI للصحة","تطبيق تطوع ذكي","مساعد دراسي بالذكاء الاصطناعي"]))
    if c2.button("🎲 اقترح اسم فريق"):
        st.info(random.choice(["Neural Ninjas","AI Falcons","Code Masters"]))

    # Sidebar
    with st.sidebar:
        st.markdown("<h2 style='text-align:center;'>تطوير ريماس الدوسري</h2>", unsafe_allow_html=True)
        st.markdown("""
        <a href="https://www.linkedin.com/in/rimas-aldosari-656a23375" target="_blank">
        <button style="width:100%;padding:12px;border-radius:10px;border:none;background:#2563eb;color:white;font-weight:bold;">
        💼 LinkedIn Profile
        </button></a>
        """, unsafe_allow_html=True)

        st.markdown("---")
        loc_filter = st.selectbox("📍 المدينة", ["الكل"] + sorted(df['Location'].unique().tolist()))
        major_filter = st.selectbox("🎯 التخصص", ["الكل"] + sorted(df['major'].unique().tolist()))

    # الفلترة
    results = df.copy()
    if search_query:
        results = results[results.astype(str).apply(lambda x: x.str.contains(search_query, case=False).any(), axis=1)]
    if loc_filter != "الكل":
        results = results[results['Location']==loc_filter]
    if major_filter != "الكل":
        results = results[results['major']==major_filter]

    # عرض الفرص
    for _, row in results.iterrows():
        st.markdown(f"""
        <div class="hack-item">
            <h2 style="color:#1e40af;">{row['Name']}</h2>
            <p>📍 {row['Location']} | 🏢 {row['Organizaion']} | 🎯 {row['major']}</p>
            <p><b>عن الفرصة:</b> {row['Description']}</p>
        </div>
        """, unsafe_allow_html=True)

        link = str(row['Link']).strip()
        if link != "غير محدد":
            st.link_button(f"🔗 سجل الآن في {row['Name']}", link if link.startswith("http") else f"https://{link}")