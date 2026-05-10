import streamlit as st
import pandas as pd
import random

# =========================================
# إعداد الصفحة
# =========================================
st.set_page_config(
    page_title="بوصلة الفرص التقنية",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# CSS نظيف بدون تخريب العناصر
# =========================================
st.markdown("""
<style>

/* اخفاء عناصر Streamlit */
#MainMenu, header, footer {visibility:hidden;}
[data-testid="stToolbar"]{display:none;}
[data-testid="stDecoration"]{display:none;}
[data-testid="stStatusWidget"]{display:none;}
[data-testid="stBottomBlockContainer"]{display:none;}
button[kind="secondary"]{display:none;} /* Manage app */

/* الخط */
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
}

/* الخلفية */
.stApp { background:#f8fafc; }

/* إصلاح النص داخل الحقول */
input, textarea {
    background:white !important;
    color:black !important;
}
div[data-baseweb="select"] * {
    color:black !important;
}
label, .stRadio label {
    color:#1e3a8a !important;
    font-weight:bold;
}

/* إظهار نصوص radio */
.stRadio div {color:black !important;}

/* إظهار الأرقام في metrics */
[data-testid="stMetricValue"] {
    color:#1e3a8a !important;
    font-size:30px !important;
    font-weight:bold;
}
[data-testid="stMetricLabel"] {
    color:#334155 !important;
    font-weight:bold;
}

/* السايدبار */
section[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#0f172a,#1e293b);
}
section[data-testid="stSidebar"] * {color:white !important;}

/* كروت الفرص */
.hack-card {
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
# جلب البيانات
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data
def get_data():
    df = pd.read_csv(SHEET_URL)
    df.columns = df.columns.str.strip()
    return df.fillna("غير محدد")

df = get_data()

# =========================================
# العنوان
# =========================================
st.markdown("<h1 style='text-align:center;color:#1e3a8a;'>🚀 بوصلة الفرص التقنية للطلاب</h1>", unsafe_allow_html=True)

# =========================================
# نظام التوصية 🤖
# =========================================
st.subheader("🤖 اكتشفي الفرص المناسبة لك")

col1,col2 = st.columns(2)

with col1:
    user_major = st.selectbox("🎓 تخصصك", ["اختر"] + sorted(df['major'].unique()))
    level = st.selectbox("📊 مستواك", ["مبتدئة","متوسطة","متقدمة"])

with col2:
    interest = st.selectbox("💡 اهتمامك", ["ذكاء اصطناعي","تطبيقات","أمن سيبراني","ويب"])
    team = st.radio("👥 هل لديك فريق؟", ["نعم","لا"])

if st.button("✨ اقترح لي فرص"):
    filtered = df.copy()
    if user_major != "اختر":
        filtered = filtered[filtered["major"] == user_major]
    st.success("أفضل فرص لك 👇")
    st.dataframe(filtered.head(5))

st.divider()

# =========================================
# البحث
# =========================================
search_query = st.text_input("🔍 ابحثي عن هاكثون أو جهة منظمة")

# =========================================
# الإحصائيات (تم إصلاح الأرقام)
# =========================================
c1,c2,c3 = st.columns(3)
c1.metric("عدد الفرص", len(df))
c2.metric("عدد المدن", df["Location"].nunique())
c3.metric("عدد التخصصات", df["major"].nunique())

# =========================================
# أدوات ممتعة
# =========================================
colA,colB = st.columns(2)

if colA.button("✨ ولّد فكرة مشروع"):
    st.success(random.choice(["منصة AI للصحة","تطبيق تطوع ذكي","مساعد دراسي"]))

if colB.button("🎲 اقترح اسم فريق"):
    st.info(random.choice(["Neural Ninjas","AI Falcons","Code Masters"]))

# =========================================
# Sidebar
# =========================================
with st.sidebar:
    st.markdown("## تطوير ريماس الدوسري")
    st.markdown("""
    <a href="https://www.linkedin.com/in/rimas-aldosari-656a23375" target="_blank">
    <button style="width:100%;padding:12px;border:none;border-radius:10px;background:#2563eb;color:white;font-weight:bold;">
    💼 LinkedIn Profile
    </button></a>
    """, unsafe_allow_html=True)

    st.markdown("---")
    loc_filter = st.selectbox("📍 المدينة", ["الكل"] + sorted(df['Location'].unique()))
    major_filter = st.selectbox("🎯 التخصص", ["الكل"] + sorted(df['major'].unique()))

# =========================================
# فلترة النتائج
# =========================================
results = df.copy()

if search_query:
    results = results[results.astype(str).apply(lambda x: x.str.contains(search_query, case=False).any(), axis=1)]

if loc_filter != "الكل":
    results = results[results["Location"] == loc_filter]

if major_filter != "الكل":
    results = results[results["major"] == major_filter]

# =========================================
# عرض الفرص
# =========================================
for _,row in results.iterrows():
    st.markdown(f"""
    <div class="hack-card">
        <h2 style="color:#1e3a8a;">{row['Name']}</h2>
        <p>📍 {row['Location']} | 🏢 {row['Organizaion']} | 🎯 {row['major']}</p>
        <p><b>عن الفرصة:</b> {row['Description']}</p>
    </div>
    """, unsafe_allow_html=True)

    link = str(row["Link"]).strip()
    if link != "غير محدد":
        st.link_button("🔗 سجل الآن", link if link.startswith("http") else f"https://{link}")