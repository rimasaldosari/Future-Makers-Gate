import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة - يجب أن يكون أول أمر برمجي
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. تحسين التنسيق وإخفاء الأدوات الإضافية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    
    /* إخفاء شريط الإدارة السفلي نهائياً لمنع التداخل */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stStatusWidget"] { display: none !important; }
    [data-testid="manage-app-button"] { display: none !important; }

    /* ضبط عرض القائمة الجانبية لمنع التغطية على الكلام */
    [data-testid="stSidebar"] {
        background-color: #111827;
        min-width: 280px !important;
        max-width: 320px !important;
    }
    
    /* تنسيق كروت الهاكثونات */
    .hack-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-right: 6px solid #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. جلب البيانات
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except: return None

df = load_data()

# 4. واجهة التطبيق
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

with st.sidebar:
    # عرض الاسم بدون لقب كما طلبتِ
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
                st.success(f"فكرة رائعة لـ {target_h}! مهاراتك التصميمية ستجعلها مميزة.")
    
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 5. عرض النتائج النهائية
if df is not None:
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        st.markdown(f"""
        <div class="hack-card">
            <h2 style='color: #1e40af; margin-top:0;'>{row.get('Name')}</h2>
            <p><b>📍 المدينة:</b> {row.get('Location')}</p>
            <p><b>🏢 الجهة:</b> {row.get('Organizaion')}</p>
            <p><b>📅 التاريخ:</b> {row.get('Data')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        link = str(row.get('Link', '')).strip()
        if link and link != 'nan':
            st.link_button(f"🔗 سجل الآن", link if link.startswith('http') else f"https://{link}")
        st.markdown("<br>", unsafe_allow_html=True)
