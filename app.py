import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط الجدول (تأكدي أنه رابط الـ CSV المنشور)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQG6e9dLydAAngT_ZzYXW2khBDqFVhWEzR_-eufO3jaFB2XYBudVWns9gxYkTmad1pE9-0QVQw8ZCw0/pub?output=csv"

# 3. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #f8fafc; }
    .hack-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 6px solid #1e3a8a;
        color: #1e293b;
    }
    .description-box {
        background-color: #f1f5f9;
        padding: 12px;
        border-radius: 8px;
        font-size: 14px;
        color: #475569;
        margin: 10px 0;
        border-right: 3px solid #64748b;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #1e3a8a;
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
        st.error(f"خطأ في تحميل البيانات: {e}")
        return None

df = load_data()

# 4. القائمة الجانبية
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🔍 التحكم</h2>", unsafe_allow_html=True)
    if df is not None:
        majors = ["الكل"] + sorted(list(df['major'].dropna().unique()))
        sel_major = st.selectbox("اختر التخصص:", majors)
    
    st.markdown("---")
    st.markdown("### 👩‍💻 تطوير وإشراف")
    st.markdown("**ريماس الدوسري**")
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")

# 5. عرض المحتوى الرئيسي
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#64748b;">دليلك الشامل لأحدث الفرص التقنية في المملكة</p>', unsafe_allow_html=True)

if df is not None:
    # الفلترة
    filt_df = df.copy()
    if sel_major != "الكل":
        filt_df = filt_df[filt_df['major'] == sel_major]

    # عرض البطاقات
    for _, row in filt_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <h2 style='color: #1e40af; margin-bottom:10px;'>{row['Name']}</h2>
                <p style='margin:5px 0;'>🏢 <b>الجهة:</b> {row['Organizaion']} | 📍 <b>الموقع:</b> {row['Location']}</p>
                <p style='margin:5px 0;'>🎯 <b>التخصص:</b> {row['major']} | 📅 <b>التاريخ:</b> {row['Data']}</p>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b> {row['Description'] if 'Description' in row and pd.notnull(row['Description']) else 'لا توجد نبذة حالياً.'}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # زر الرابط
            link = str(row['Link']).strip()
            if link.startswith('http'):
                st.link_button(f"🔗 سجل الآن في {row['Name']}", link)
            else:
                st.warning("رابط التسجيل غير متوفر حالياً")
            
            st.markdown("<br>", unsafe_allow_html=True)
else:
    st.info("جاري تحديث البيانات من الجدول... يرجى الانتظار.")
