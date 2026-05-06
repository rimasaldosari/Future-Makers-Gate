import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات (الرابط المباشر الصحيح)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?output=csv"

# 3. الرابط الذكي للينكد إن
LINKEDIN_SMART_URL = "https://appurl.io/X_yrk-MQaa"

# 4. التصميم (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #f8fafc; }
    .hack-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #1e3a8a;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #1e3a8a !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# دالة تحميل البيانات مع معالجة الأخطاء
@st.cache_data(ttl=5)
def load_data():
    try:
        # قراءة البيانات مع التأكد من الترميز
        data = pd.read_csv(SHEET_URL, on_bad_lines='skip')
        data.columns = data.columns.str.strip() # إزالة المسافات من أسماء الأعمدة
        return data
    except Exception as e:
        st.error(f"حدث خطأ في تحميل البيانات: {e}")
        return None

df = load_data()

# 5. الواجهة
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🔍 خيارات البحث</h2>", unsafe_allow_html=True)
    
    sel_major = "الكل"
    sel_loc = "الكل"
    
    if df is not None:
        # التخصص أولاً
        if 'major' in df.columns:
            all_majors = ["الكل"] + sorted(df['major'].dropna().unique().tolist())
            sel_major = st.selectbox("🎯 ابحث حسب التخصص:", all_majors)
        
        # المدينة ثانياً (تحت التخصص)
        if 'Location' in df.columns:
            all_locations = ["الكل"] + sorted(df['Location'].dropna().unique().tolist())
            sel_loc = st.selectbox("📍 ابحث حسب المدينة:", all_locations)
    
    st.markdown("---")
    st.markdown("<div style='text-align:center;'><b>تطوير:</b><br>ريماس الدوسري</div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", LINKEDIN_SMART_URL)

# 6. عرض النتائج
if df is not None:
    filt_df = df.copy()
    if sel_major != "الكل":
        filt_df = filt_df[filt_df['major'] == sel_major]
    if sel_loc != "الكل":
        filt_df = filt_df[filt_df['Location'] == sel_loc]

    if filt_df.empty:
        st.warning("لا توجد نتائج حالياً.")
    else:
        for _, row in filt_df.iterrows():
            with st.container():
                st.markdown(f"""
                <div class="hack-card">
                    <h2 style='color: #1e40af;'>{row.get('Name', 'نشاط تقني')}</h2>
                    <p><b>📍 المدينة:</b> {row.get('Location', 'غير محدد')}</p>
                    <p><b>🏢 الجهة:</b> {row.get('Organizaion', 'غير محدد')}</p>
                    <p><b>🎯 التخصص:</b> {row.get('major', 'عام')}</p>
                    <p><b>📅 التاريخ:</b> {row.get('Data', 'قريباً')}</p>
                    <div style="background:#f1f5f9; padding:10px; border-radius:5px;">
                        {row.get('Description', 'لا يوجد وصف.')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                link = str(row.get('Link', '')).strip()
                if link and link != 'nan':
                    st.link_button(f"🔗 سجل الآن", link if link.startswith('http') else f"https://{link}")
                st.markdown("<br>", unsafe_allow_html=True)
