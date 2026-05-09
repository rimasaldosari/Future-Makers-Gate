import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة (يجب أن يكون أول سطر)
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. تصميم الواجهة (CSS) - النسخة المستقرة والواضحة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    
    /* إخفاء شريط الإدارة السفلي نهائياً */
    #MainMenu, footer, header {visibility: hidden;}
    div[data-testid="stStatusWidget"] { display: none !important; }
    .viewerBadge_container__1QSob { display: none !important; }

    /* تنسيق القائمة الجانبية (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        min-width: 300px !important;
    }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }

    /* تنسيق الكروت (Cards) - حل مشكلة اختفاء النص */
    .hack-card {
        background: white !important;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #1e3a8a;
        color: #1e293b !important; /* لون النص داخل الكرت داكن للوضوح */
    }
    
    .status-available { background-color: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 8px; font-weight: bold; float: left; }
    .info-line { font-size: 16px; margin: 8px 0; color: #1e293b !important; }
    .info-label { color: #1e3a8a !important; font-weight: bold; }
    
    .description-box {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        color: #334155 !important;
        border-right: 4px solid #94a3b8;
    }
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

st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<div style='text-align:center;'><h3>تطوير:</h3><h2>ريماس الدوسري</h2></div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    
    st.markdown("<h3 style='text-align:center; color:#FFD700 !important;'>💡 قيم فكرتك</h3>", unsafe_allow_html=True)
    user_idea = st.text_input("ما هي فكرتك؟", placeholder="اكتبي هنا...")
    
    if df is not None:
        target_h = st.selectbox("الهاكثون المستهدف:", df['Name'].unique())
        if st.button("تحليل الفكرة"):
            if user_idea:
                st.balloons()
                st.success(f"فكرة ممتازة لـ {target_h}! مهاراتك ستميزها.")
    
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 5. عرض النتائج (الكروت المصلحة)
if df is not None:
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <div class="status-available">✅ متاح</div>
                <h2 style='color: #1e40af;'>{row.get('Name')}</h2>
                <div class="info-line"><span class="info-label">📍 المدينة:</span> {row.get('Location')}</div>
                <div class="info-line"><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion')}</div>
                <div class="info-line"><span class="info-label">📅 التاريخ:</span> {row.get('Data')}</div>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b><br>{row.get('Description')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            link = str(row.get('Link', '')).strip()
            if link and link != 'nan':
                st.link_button(f"🔗 سجل الآن", link if link.startswith('http') else f"https://{link}")
            st.markdown("<br>", unsafe_allow_html=True)
