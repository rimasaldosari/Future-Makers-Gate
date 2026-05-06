import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. الرابط الخاص بالجدول
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?output=csv"

# 3. تصميم الواجهة (حل مشكلة اختفاء النص)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #ffffff; }
    
    .hack-card {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        border-right: 10px solid #1e3a8a;
    }
    
    /* حل مشكلة اختفاء النص - جعلنا الألوان غامقة جداً */
    .info-line { 
        font-size: 18px; 
        margin: 10px 0; 
        color: #000000 !important; /* أسود صريح */
        font-weight: 500;
    }
    .info-label { 
        color: #1e3a8a !important; 
        font-weight: bold; 
    }
    .description-box {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 8px;
        font-size: 16px;
        color: #1a202c !important; /* أسود صريح للوصف */
        margin-top: 10px;
        border: 1px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(ttl=2)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except: return None

df = load_data()

# 4. العنوان
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 5. القائمة الجانبية
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🔍 البحث</h2>", unsafe_allow_html=True)
    if df is not None:
        # التخصص أولاً ثم المدينة كما طلبتِ
        sel_major = st.selectbox("🎯 التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))
        sel_loc = st.selectbox("📍 المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
    
    st.markdown("---")
    st.markdown("<div style='text-align:center;'><b>تطوير:</b><br>ريماس الدوسري</div>", unsafe_allow_html=True)
    
    # حل مشكلة اللينكد إن: وضعنا الرابط المباشر الرسمي لأنه الأضمن
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")

# 6. عرض البيانات
if df is not None:
    filt_df = df.copy()
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]

    for _, row in filt_df.iterrows():
        if pd.isna(row.get('Name')): continue
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <h2 style='color: #1e3a8a; margin:0;'>{row.get('Name')}</h2>
                <div class="info-line"><span class="info-label">📍 المدينة:</span> {row.get('Location')}</div>
                <div class="info-line"><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion')}</div>
                <div class="info-line"><span class="info-label">🎯 التخصص:</span> {row.get('major')}</div>
                <div class="info-line"><span class="info-label">📅 التاريخ:</span> {row.get('Data')}</div>
                <div class="description-box">
                    <b>📝 التفاصيل:</b><br>{row.get('Description')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            link = str(row.get('Link', '')).strip()
            if link and link != 'nan':
                st.link_button(f"🔗 سجل الآن في {row.get('Name')}", link if link.startswith('http') else f"https://{link}")
            st.markdown("<br>", unsafe_allow_html=True)
