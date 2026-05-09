import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات (رابطك المباشر)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

# 3. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #f8fafc; }
    
    /* تصميم الكروت */
    .hack-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #1e3a8a;
    }
    
    /* لون النصوص داخل الكرت */
    .info-line { font-size: 16px; margin: 8px 0; color: #1e293b; } /* لون كحلي غامق وواضح */
    .info-label { color: #1e3a8a; font-weight: bold; }
    
    /* صندوق الوصف */
    .description-box {
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #0f172a; /* لون نص أغمق للوصف لسهولة القراءة */
        margin-top: 15px;
        border-right: 4px solid #94a3b8;
    }
    
    /* زر التسجيل */
    .stButton>button {
        border-radius: 10px;
        background-color: #1e3a8a !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(ttl=5)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except:
        return None

df = load_data()

# 4. العنوان الرئيسي
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 5. قسم "قيم فكرتك" (الميزة التفاعلية)
with st.expander("💡 أيقونة: قيم فكرتك للهاكثون"):
    st.markdown("### 📊 محلل الابتكار الشخصي")
    user_idea = st.text_input("ما هي فكرتك الجديدة؟")
    if df is not None:
        target_h = st.selectbox("اختر الهاكثون المستهدف لفكرتك:", df['Name'].unique())
        if st.button("تحليل الفكرة"):
            if user_idea:
                st.balloons()
                st.success(f"فكرة '{user_idea}' رائعة ومناسبة جداً لـ {target_h}! تذكري يا ريماس أن مهاراتك في UI/UX وتطوير AI ستجعل مشروعك يبرز في هذا التحدي.")
            else:
                st.warning("الرجاء كتابة فكرة أولاً.")

# 6. القائمة الجانبية
with st.sidebar:
    st.markdown("<div style='text-align:center;'><b>تطوير المهندسة:</b><br>ريماس الدوسري</div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 ابحث حسب المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 ابحث حسب التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 7. عرض النتائج
if df is not None:
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <h2 style='color: #1e40af; margin-top:0;'>{row.get('Name', 'نشاط تقني')}</h2>
                <div class="info-line"><span class="info-label">📍 المدينة:</span> {row.get('Location', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🎯 التخصص:</span> {row.get('major', 'عام')}</div>
                <div class="info-line"><span class="info-label">📅 التاريخ:</span> {row.get('Data', 'قريباً')}</div>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b><br>{row.get('Description', 'لا يوجد وصف حالياً.')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            link = str(row.get('Link', '')).strip()
            if link and link != 'nan' and len(link) > 5:
                actual_link = link if link.startswith('http') else f"https://{link}"
                st.link_button(f"🔗 سجل الآن في {row.get('Name')}", actual_link)
            st.markdown("<br>", unsafe_allow_html=True)
