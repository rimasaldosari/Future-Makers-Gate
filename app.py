import streamlit as st
import pandas as pd
import random

# =========================================
# إعدادات الصفحة
# =========================================

st.set_page_config(
    page_title="بوصلة الهاكثونات | ريماس الدوسري",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# CSS
# =========================================

st.markdown("""
<style>

#MainMenu { visibility: hidden; }
header { visibility: hidden; }
footer { visibility: hidden; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
button[kind="header"] { display: none !important; }

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
}

.stApp {
    background-color: #f8fafc;
}

[data-testid="stSidebar"] {
    background-color: #1e3a8a !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.hack-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    border-right: 8px solid #1e3a8a;
    transition: 0.3s ease;
    direction: rtl;
    text-align: right;
}

.hack-card:hover {
    transform: translateY(-5px);
}

.status-badge {
    background-color: #dcfce7;
    color: #166534;
    padding: 5px 12px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 14px;
    display: inline-block;
    margin-bottom: 10px;
}

.info-line {
    font-size: 16px;
    margin: 8px 0;
    color: #1e293b;
}

.info-label {
    color: #1e3a8a;
    font-weight: bold;
}

.description-box {
    background-color: #f1f5f9;
    padding: 15px;
    border-radius: 10px;
    font-size: 15px;
    color: #0f172a;
    margin-top: 15px;
    border-right: 4px solid #94a3b8;
}

.stats-box {
    background: white;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.07);
    margin-bottom: 15px;
}

.ai-box {
    background: linear-gradient(135deg,#eff6ff,#ffffff);
    padding: 20px;
    border-radius: 15px;
    border-right: 6px solid #2563eb;
    margin-top: 15px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# رابط البيانات
# =========================================

SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except Exception as e:
        st.error(f"خطأ في تحميل البيانات: {e}")
        return None

df = load_data()

# تشخيص مؤقت
if df is not None:
    st.write(df.head())
else:
    st.error("❌ ما قدر يحمل البيانات من الشيت")

# =========================================
# الواجهة الرئيسية
# =========================================

st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

search_term = st.text_input("🔍 ابحثي عن هاكثون أو جهة منظمة", placeholder="مثال: سدايا - الرياض")

if df is not None:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="stats-box"><h2>🚀 {len(df)}</h2><p>عدد الفرص</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stats-box"><h2>📍 {df["Location"].nunique()}</h2><p>عدد المدن</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="stats-box"><h2>🎯 {df["major"].nunique()}</h2><p>عدد التخصصات</p></div>', unsafe_allow_html=True)

# مولد الأفكار
st.markdown('<div class="ai-box"><h3>💡 مولد أفكار هاكثونية</h3></div>', unsafe_allow_html=True)
if st.button("💡 ولّد فكرة جديدة"):
    ideas = ["تطبيق ذكي للمكفوفين", "منصة AI للصحة النفسية", "مساعد ذكي للفرص التدريبية"]
    st.success(random.choice(ideas))

# =========================================
# القائمة الجانبية
# =========================================

with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding-bottom: 10px;'>
    <b style='font-size: 1.1em;'>تطوير:</b><br>
    <span style='font-size: 1.3em; font-weight: bold;'>ريماس الدوسري</span>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("🔗 حسابي على LinkedIn", "https://www.linkedin.com/in/rimas-aldosari-656a23375")

    st.markdown("---")

    if df is not None:
        sel_loc = st.selectbox("📍 حسب المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 حسب التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# =========================================
# عرض النتائج
# =========================================

if df is not None:
    filt_df = df.copy()

    if search_term:
        filt_df = filt_df[filt_df.astype(str).apply(lambda row: row.str.contains(search_term, case=False).any(), axis=1)]
    if sel_loc != "الكل":
        filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل":
        filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <span class="status-badge">✅ نشط</span>
                <h2 style='color:#1e40af; margin-top:8px;'>{row.get('Name', 'نشاط تقني')}</h2>
                <p class="info-line"><span class="info-label">📍 المدينة:</span> {row.get('Location', 'غير محدد')}</p>
                <p class="info-line"><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion', 'غير محدد')}</p>
                <p class="info-line"><span class="info-label">🎯 التخصص:</span> {row.get('major', 'عام')}</p>
                <p class="info-line"><span class="info-label">📅 التاريخ:</span> {row.get('Data', 'قريباً')}</p>
                <div class="description-box">
                    <b>📝 عن الفرصة:</b><br>
                    {row.get('Description', 'لا يوجد وصف.')}
                </div>
            </div>
            """, unsafe_allow_html=True)

            link = str(row.get('Link', '')).strip()
            if link and link != 'nan' and len(link) > 5:
                actual_link = link if link.startswith('http') else f"https://{link}"
                st.link_button("🔗 اضغط هنا للتسجيل", actual_link)
            else:
                st.info("رابط التسجيل سيتم تحديثه قريباً")

            st.markdown("<br>", unsafe_allow_html=True)