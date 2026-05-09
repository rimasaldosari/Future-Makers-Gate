import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة - ضروري تكون أول سطر
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. تصميم الواجهة (CSS) - تم حل مشكلة التداخل وإخفاء الأشرطة نهائياً
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    
    /* إخفاء شريط الإدارة السفلي نهائياً */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stStatusWidget"] { display: none !important; }
    [data-testid="manage-app-button"] { display: none !important; }
    .viewerBadge_container__1QSob { display: none !important; }

    /* تحسين شكل القائمة الجانبية عشان ما تغطي على المحتوى */
    [data-testid="stSidebar"] {
        background-color: #111827;
        min-width: 250px !important;
        max-width: 350px !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        font-size: 16px;
    }

    /* تنسيق الكروت */
    .hack-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-right: 6px solid #1e3a8a;
    }
    
    .status-available { background-color: #dcfce7; color: #166534; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 13px; float: left; }
    .info-label { color: #1e3a8a; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. تحميل البيانات
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except: return None

df = load_data()

# 4. العنوان الرئيسي
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 5. القائمة الجانبية المحدثة (بدون لقب المهندسة وبدون تداخل)
with st.sidebar:
    st.markdown("<div style='text-align:center; color:white;'><h3>تطوير:</h3><h2>ريماس الدوسري</h2></div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    
    st.markdown("<h3 style='text-align:center; color:#FFD700 !important;'>💡 قيم فكرتك</h3>", unsafe_allow_html=True)
    user_idea = st.text_input("ما هي فكرتك؟", placeholder="اكتبي هنا...")
    
    if df is not None:
        target_h = st.selectbox("الهاكثون المستهدف:", df['Name'].unique())
        if st.button("تحليل الفكرة"):
            if user_idea:
                st.balloons()
                st.success(f"فكرة رائعة لـ {target_h}! مهاراتك في UI/UX بتميزها.")
    
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 6. عرض النتائج
if df is not None:
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        status = str(row.get('Data', '')).strip()
        st.markdown(f"""
        <div class="hack-card">
            <div class="status-available">✅ متاح</div>
            <h2 style='color: #1e40af; margin-top:0;'>{row.get('Name')}</h2>
            <div style='margin: 10px 0;'>
                <p><span class="info-label">📍 المدينة:</span> {row.get('Location')}</p>
                <p><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion')}</p>
                <p><span class="info-label">📅 التاريخ:</span> {row.get('Data')}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        link = str(row.get('Link', '')).strip()
        if link and link != 'nan':
            st.link_button(f"🔗 سجل الآن", link if link.startswith('http') else f"https://{link}")
        st.markdown("<br>", unsafe_allow_html=True)
