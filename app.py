import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. تصميم الواجهة (CSS) - نسخة مستقرة جداً
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* تنسيق الخط والاتجاه */
    html, body, [class*="css"] { 
        font-family: 'Cairo', sans-serif; 
        direction: rtl; 
        text-align: right; 
    }

    /* إخفاء شعارات ستريم ليت وأدوات الإدارة نهائياً */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stStatusWidget"] { display: none !important; }
    [data-testid="manage-app-button"] { display: none !important; }
    .viewerBadge_container__1QSob { display: none !important; }

    /* خلفية التطبيق */
    .stApp { background-color: #f8fafc; }

    /* تنسيق القائمة الجانبية لمنع التداخل */
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        min-width: 300px !important;
    }
    
    /* لون النصوص في القائمة الجانبية */
    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h2 {
        color: #FFFFFF !important;
    }

    /* تنسيق بطاقات الهاكثونات (الكروت) */
    .hack-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-right: 5px solid #1e3a8a;
        color: #1e293b;
    }
    
    .status-badge {
        background-color: #dcfce7;
        color: #166534;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 12px;
        float: left;
    }
    
    .info-label { color: #1e3a8a; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. رابط البيانات
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
st.write('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 5. القائمة الجانبية
with st.sidebar:
    st.markdown("<div style='text-align:center;'><h3>تطوير:</h3><h2>ريماس الدوسري</h2></div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    
    st.markdown("### 💡 قيم فكرتك")
    user_idea = st.text_input("ما هي فكرتك؟", placeholder="اكتبي هنا...")
    
    if df is not None:
        target_h = st.selectbox("الهاكثون المستهدف:", df['Name'].unique(), key="sidebar_hack_select")
        if st.button("تحليل الفكرة"):
            if user_idea:
                st.balloons()
                st.success(f"فكرة ممتازة! مهاراتك في UI/UX ستجعلها متصدرة في {target_h}.")

    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 6. عرض النتائج في الصفحة الرئيسية
if df is not None:
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        st.markdown(f"""
        <div class="hack-card">
            <div class="status-badge">✅ متاح</div>
            <h2 style='color: #1e40af; margin:0;'>{row.get('Name')}</h2>
            <div style='margin-top: 10px;'>
                <p><span class="info-label">📍 المدينة:</span> {row.get('Location')}</p>
                <p><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion')}</p>
                <p><span class="info-label">📅 التاريخ:</span> {row.get('Data')}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        link = str(row.get('Link', '')).strip()
        if link and link != 'nan':
            st.link_button(f"🔗 سجل الآن في {row.get('Name')}", link if link.startswith('http') else f"https://{link}")
        st.write("<br>", unsafe_allow_html=True)
