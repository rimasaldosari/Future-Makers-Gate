import streamlit as st
import pandas as pd

st.set_page_config(page_title="Future Makers Gate", layout="wide")

# =========================================
# CSS تنظيف الواجهة + اخفاء Manage App
# =========================================
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
button[title="Manage app"]{display:none !important;}
div[style*="position: fixed"]{display:none !important;}
</style>
""", unsafe_allow_html=True)

# =========================================
# رابط الشيت
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

# =========================================
# قراءة البيانات بذكاء (يدعم عربي وانجليزي)
# =========================================
@st.cache_data
def load_data():
    df = pd.read_csv(SHEET_URL)
    df.columns = df.columns.str.strip().str.lower()

    # توحيد اسماء الأعمدة مهما كانت مكتوبة
    rename_map = {
        "name":"title","اسم الفرصة":"title",
        "location":"city","city":"city","المدينة":"city",
        "organizer":"org","organization":"org","الجهة":"org",
        "major":"major","track":"major","التخصص":"major",
        "description":"desc","details":"desc","الوصف":"desc",
        "link":"link","url":"link","الرابط":"link"
    }

    df = df.rename(columns=rename_map)

    # لو عمود ناقص ينشئه تلقائياً
    for col in ["title","city","org","major","desc","link"]:
        if col not in df.columns:
            df[col] = "غير متوفر"

    return df

df = load_data()

# =========================================
# SIDEBAR
# =========================================
st.sidebar.title("تطوير ريماس الدوسري")
st.sidebar.link_button("LinkedIn Profile", "https://linkedin.com")

cities = ["الكل"] + sorted(df["city"].dropna().unique())
majors = ["الكل"] + sorted(df["major"].dropna().unique())

city_filter = st.sidebar.selectbox("📍 المدينة", cities)
major_filter = st.sidebar.selectbox("🎯 التخصص", majors)
team = st.sidebar.radio("👥 هل لديك فريق؟", ["نعم", "لا"])

# =========================================
# فلترة البيانات
# =========================================
filtered = df.copy()
if city_filter != "الكل":
    filtered = filtered[filtered["city"] == city_filter]
if major_filter != "الكل":
    filtered = filtered[filtered["major"] == major_filter]

# =========================================
# الاحصائيات (الارقام اللي كانت مختفية)
# =========================================
c1,c2,c3 = st.columns(3)
c1.metric("عدد الفرص", len(df))
c2.metric("عدد التخصصات", df["major"].nunique())
c3.metric("عدد المدن", df["city"].nunique())

st.divider()

# =========================================
# عرض الكروت (المشكلة كانت هنا)
# =========================================
for i,row in filtered.iterrows():
    st.markdown(f"""
    ### {row['title']}
    🎯 {row['major']} | 🏢 {row['org']} | 📍 {row['city']}

    {row['desc']}
    """)
    
    st.link_button("سجل الآن 🔗", row["link"])
    st.divider()