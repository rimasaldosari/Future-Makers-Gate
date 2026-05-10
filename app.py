import streamlit as st
import pandas as pd
import random

# =========================================
# 1. إعدادات الصفحة
# =========================================
st.set_page_config(
    page_title="بوصلة الفرص التقنية | ريماس الدوسري",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# 2. CSS
# =========================================
st.markdown("""
<style>
#MainMenu, header, footer { visibility: hidden; }
[data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
}

.stApp { background-color: #f8fafc; }

.stats-card {
    background: white; padding: 25px; border-radius: 20px; text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-bottom: 5px solid #1e3a8a;
}
.ai-card {
    background: white; padding: 20px; border-radius: 15px; border-right: 6px solid #2563eb;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 10px;
}
.hack-item {
    background: white; padding: 30px; border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06); margin-bottom: 25px;
    border-right: 10px solid #1e3a8a;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 3. جلب البيانات (الرابط الأساسي)
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def get_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data.fillna("غير محدد")
    except:
        return None

df = get_data()

# =========================================
# العنوان الجديد التسويقي 🔥
# =========================================
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الفرص التقنية للطلاب في السعودية</h1>', unsafe_allow_html=True)

# =========================================
# نظام التوصية الذكي 🤖 (إضافة جديدة)
# =========================================
if df is not None:
    st.markdown("## 🤖 اكتشفي الفرص المناسبة لك")

    col1, col2 = st.columns(2)

    with col1:
        user_major = st.selectbox("🎓 تخصصك", ["اختر"] + sorted(df['major'].unique().tolist()))
        level = st.selectbox("📊 مستواك", ["مبتدئة", "متوسطة", "متقدمة"])

    with col2:
        interest = st.selectbox("💡 اهتمامك", ["ذكاء اصطناعي", "تطبيقات", "أمن سيبراني", "ويب"])
        team = st.radio("👥 هل لديك فريق؟", ["نعم", "لا"])

    if st.button("✨ اقترح لي أفضل الفرص"):
        filtered = df.copy()

        if user_major != "اختر":
            filtered = filtered[filtered['major'] == user_major]

        st.success("هذه أفضل فرص مناسبة لك 👇")
        st.dataframe(filtered.head(5))

    st.divider()

# =========================================
# البحث
# =========================================
search_query = st.text_input("🔍 ابحثي عن هاكثون أو جهة منظمة")

if df is not None:
    # إحصائيات
    s1, s2, s3 = st.columns(3)
    with s1: st.metric("عدد الفرص", len(df))
    with s2: st.metric("عدد المدن", df["Location"].nunique())
    with s3: st.metric("عدد التخصصات", df["major"].nunique())

    # أدوات AI
    c_ai1, c_ai2 = st.columns(2)
    with c_ai1:
        if st.button("✨ ولّد فكرة مشروع"):
            st.success(random.choice(["منصة AI للصحة", "تطبيق تطوع ذكي", "مساعد دراسي بالذكاء الاصطناعي"]))

    with c_ai2:
        if st.button("🎲 اقترح اسم فريق"):
            st.info(random.choice(["Neural Ninjas", "AI Falcons", "Code Masters"]))

    # الفلاتر
    with st.sidebar:
        st.markdown("<h2 style='text-align:center;'>تطوير ريماس الدوسري</h2>", unsafe_allow_html=True)
        st.link_button("💼 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375", use_container_width=True)
        st.markdown("---")
        loc_filter = st.selectbox("📍 المدينة", ["الكل"] + sorted(df['Location'].unique().tolist()))
        major_filter = st.selectbox("🎯 التخصص", ["الكل"] + sorted(df['major'].unique().tolist()))

    # تصفية النتائج
    results = df.copy()

    if search_query:
        results = results[results.astype(str).apply(lambda x: x.str.contains(search_query, case=False).any(), axis=1)]

    if loc_filter != "الكل":
        results = results[results['Location'] == loc_filter]

    if major_filter != "الكل":
        results = results[results['major'] == major_filter]

    # عرض النتائج
    for _, row in results.iterrows():
        st.markdown(f"""
        <div class="hack-item">
            <h2 style="color:#1e40af;">{row['Name']}</h2>
            <p>📍 {row['Location']} | 🏢 {row['Organizaion']} | 🎯 {row['major']}</p>
            <div style="background:#f8fafc; padding:15px; border-radius:10px;">
                <b>عن الفرصة:</b> {row['Description']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        link = str(row['Link']).strip()
        if link != "غير محدد":
            st.link_button(f"🔗 سجل الآن في {row['Name']}", link if link.startswith('http') else f"https://{link}")