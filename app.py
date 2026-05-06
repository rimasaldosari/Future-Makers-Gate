import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات الخاص بك (تم تحديثه برابطك الجديد)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?output=csv"

# 3. تصميم الواجهة المطور (CSS)
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
        margin-bottom: 25px;
        border-right: 8px solid #1e3a8a;
        color: #1e293b;
    }
    .description-box {
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #334155;
        margin: 15px 0;
        border-right: 4px solid #94a3b8;
        line-height: 1.6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #1e3a8a;
        color: white;
        font-weight: bold;
        height: 50px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(ttl=60)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        return data
    except Exception as e:
        st.error(f"خطأ في تحميل البيانات من الجدول: {e}")
        return None

df = load_data()

# 4. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🔍 خيارات التصفية</h2>", unsafe_allow_html=True)
    if df is not None:
        majors = ["الكل"] + sorted(list(df['major'].dropna().unique()))
        sel_major = st.selectbox("اختر التخصص:", majors)
    
    st.markdown("---")
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("### 👩‍💻 تطوير وإشراف")
    st.markdown("**ريماس الدوسري**")
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. عرض المحتوى الرئيسي
st.markdown('<h1 style="text-align:center; color:#1e3a8a; font-size: 45px;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#64748b; font-size: 20px;">دليلك التقني الموثوق لاقتناص الفرص في المملكة</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if df is not None:
    # تطبيق الفلترة
    filt_df = df.copy()
    if sel_major != "الكل":
        filt_df = filt_df[filt_df['major'] == sel_major]

    # عرض البطاقات البرمجية
    for _, row in filt_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <h2 style='color: #1e40af; margin-top:0;'>{row['Name']}</h2>
                <p style='font-size: 17px; margin:8px 0;'>🏢 <b>الجهة:</b> {row['Organizaion']} | 📍 <b>الموقع:</b> {row['Location']}</p>
                <p style='font-size: 17px; margin:8px 0;'>🎯 <b>التخصص:</b> {row['major']} | 📅 <b>التاريخ:</b> {row['Data']}</p>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b><br>{row['Description'] if 'Description' in row and pd.notnull(row['Description']) else 'لا توجد نبذة متوفرة حالياً لهذا النشاط.'}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # زر الرابط الذكي
            link = str(row['Link']).strip()
            if link.startswith('http'):
                st.link_button(f"🔗 سجل الآن في {row['Name']}", link)
            else:
                st.warning("⚠️ رابط التسجيل غير متوفر حالياً أو يحتاج لتحديث")
            
            st.markdown("<br>", unsafe_allow_html=True)
else:
    st.info("جاري سحب البيانات المحدثة من الجدول... تأكدي من نشر الجدول على الويب بصيغة CSV.")


