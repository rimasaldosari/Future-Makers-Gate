import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات", layout="wide")

# رابط الجدول الخاص بك (الذي نشرته بصيغة CSV)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQG6e9dLydAAngT_ZzYXW2khBDqFVhWEzR_-eufO3jaFB2XYBudVWns9gxYkTmad1pE9-0QVQw8ZCw0/pub?output=csv"

# تحسين التصميم (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #f4f7f9; }
    .hack-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 5px solid #007bff;
    }
    .main-title { color: #1e3a8a; font-size: 35px; font-weight: bold; text-align: center; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(ttl=60)
def load_data():
    return pd.read_csv(SHEET_URL)

df = load_data()

st.markdown('<p class="main-title">🚀 بوصلة الهاكثونات والمعسكرات التقنية</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>دليلك الشامل لأحدث الفرص في المملكة وجامعة سطام</p>", unsafe_allow_html=True)

# الفلاتر في القائمة الجانبية
with st.sidebar:
    st.header("🔍 فلاتر البحث")
    major_list = ["الكل"] + list(df['major'].unique())
    selected_major = st.selectbox("اختر التخصص:", major_list)
    
    loc_list = ["الكل"] + list(df['Location'].unique())
    selected_loc = st.selectbox("المنطقة أو الجامعة:", loc_list)

# تصفية البيانات
filt_df = df.copy()
if selected_major != "الكل": filt_df = filt_df[filt_df['major'] == selected_major]
if selected_loc != "الكل": filt_df = filt_df[filt_df['Location'] == selected_loc]

# عرض النتائج بشكل أجمل
st.subheader(f"✨ الفرص المتاحة ({len(filt_df)})")

for _, row in filt_df.iterrows():
    with st.container():
        st.markdown(f"""
        <div class="hack-card">
            <h2 style='color: #0056b3; margin-top:0;'>{row['Name']}</h2>
            <p>🏢 <b>الجهة:</b> {row['Organizaion']}</p>
            <p>🎯 <b>التخصص:</b> {row['major']}</p>
            <p>📅 <b>التاريخ:</b> {row['Data']}</p>
            <p>📍 <b>الموقع:</b> {row['Location']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر التسجيل برابط خارجي
        link = str(row['Link']).strip()
        if link.startswith('http'):
            st.link_button(f"🔗 سجل الآن في {row['Name']}", link)
        else:
            st.warning("⚠️ الرابط في الجدول غير صحيح، تأكد أنه يبدأ بـ http")
        st.write("")

