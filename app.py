import streamlit as st
import pandas as pd
import random

# =========================================
# 1. إعدادات الصفحة
# =========================================
st.set_page_config(
    page_title="بوصلة الهاكثونات | ريماس الدوسري",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# 2. CSS - إخفاء كل أدوات الحساب وتعديل الألوان
# =========================================
st.markdown("""
<style>
/* إخفاء شريط الأدوات العلوي، القائمة، والمشاركة (إخفاء تام) */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}
[data-testid="stStatusWidget"] {display: none !important;}
button[kind="header"] {display: none !important;}

/* تنسيق الخط والاتجاه */
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
}

/* لون الخلفية الأساسي */
.stApp { background-color: #f8fafc; }

/* إصلاح نصوص الإحصائيات (حل مشكلة الأبيض في أبيض) */
.stats-box {
    background: white;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.07);
    margin-bottom: 15px;
    border: 1px solid #e2e8f0;
}
.stats-box h2 { color: #1e3a8a !important; margin: 0; font-weight: bold; }
.stats-box p { color: #475569 !important; margin: 0; font-weight: bold; }

/* إصلاح نصوص الأدوات الذكية */
.ai-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border-right: 6px solid #2563eb;
    margin: 15px 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.ai-box h3 { color: #1e3a8a !important; font-weight: bold; margin-bottom: 10px; }
.ai-box p { color: #334155 !important; font-size: 15px; }

/* كروت الهاكثونات */
.hack-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    border-right: 8px solid #1e3a8a;
    color: #1e293b !important;
}
.hack-card h2 { color: #1e40af !important; margin-top: 0; }
.info-label { color: #1e3a8a !important; font-weight: bold; }
.description-box {
    background-color: #f1f5f9;
    padding: 15px;
    border-radius: 10px;
    color: #0f172a !important;
    border-right: 4px solid #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 3. رابط البيانات وتحميلها
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except:
        return None

df = load_data()

# =========================================
# 4. محتوى التطبيق
# =========================================
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

search_term = st.text_input("🔍 ابحثي عن هاكثون أو جهة منظمة", placeholder="مثال: سدايا - الرياض")

if df is not None:
    # عرض الإحصائيات
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown(f'<div class="stats-box"><h2>🚀 {len(df)}</h2><p>عدد الفرص</p></div>', unsafe_allow_html=True)
    with col2: st.markdown(f'<div class="stats-box"><h2>📍 {df["Location"].nunique()}</h2><p>عدد المدن</p></div>', unsafe_allow_html=True)
    with col3: st.markdown(f'<div class="stats-box"><h2>🎯 {df["major"].nunique()}</h2><p>التخصصات</p></div>', unsafe_allow_html=True)

# الأدوات الجانبية
with st.sidebar:
    st.markdown("<div style='text-align:center;'><b>ريماس الدوسري</b></div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 حسب المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 حسب التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# عرض كروت الهاكثونات
if df is not None:
    filt_df = df.copy()
    if search_term:
        filt_df = filt_df[filt_df.astype(str).apply(lambda row: row.str.contains(search_term, case=False).any(), axis=1)]
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <h2 style="color:#1e40af;">{row.get('Name', 'نشاط تقني')}</h2>
                <div class="info-line"><span class="info-label">📍 المدينة:</span> {row.get('Location', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🎯 التخصص:</span> {row.get('major', 'عام')}</div>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b><br>{row.get('Description', 'لا يوجد وصف حالياً.')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            link = str(row.get('Link', '')).strip()
            if link and link != 'nan':
                st.link_button(f"🔗 سجل الآن", link if link.startswith('http') else f"https://{link}")
