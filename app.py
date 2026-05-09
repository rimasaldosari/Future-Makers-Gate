import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

# 3. تصميم الواجهة (CSS) - النسخة الاحترافية لإخفاء كل أدوات ستريم ليت
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    
    /* إخفاء شريط القائمة العلوي والسفلي وشعار ستريم ليت والتاج الأحمر */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stStatusWidget"] { display: none !important; }
    .viewerBadge_container__1QSob { display: none !important; }
    .stDeployButton { display: none !important; }
    
    .stApp { background-color: #f8fafc; }
    
    /* تنسيق القائمة الجانبية (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #111827; 
    }
    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        font-size: 16px;
    }
    [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
        margin-top: 0;
    }
    [data-testid="stSidebar"] h2 {
        color: #FFFFFF !important;
        margin-top: 5px;
        font-weight: bold;
    }

    /* تنسيق كروت الهاكثونات والمعسكرات */
    .hack-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #1e3a8a;
    }
    
    .status-available { background-color: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 8px; font-weight: bold; font-size: 14px; float: left; }
    .status-expired { background-color: #fee2e2; color: #991b1b; padding: 5px 12px; border-radius: 8px; font-weight: bold; font-size: 14px; float: left; }
    
    .info-line { font-size: 16px; margin: 8px 0; color: #1e293b; }
    .info-label { color: #1e3a8a; font-weight: bold; }
    
    .description-box {
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #0f172a;
        margin-top: 15px;
        border-right: 4px solid #94a3b8;
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

st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar)
with st.sidebar:
    # تم ضبط الاسم بدون كلمة المهندسة وبشكل مرتب
    st.markdown("<div style='text-align:center;'><h3>تطوير:</h3><h2>ريماس الدوسري</h2></div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    
    # قسم "قيم فكرتك" - محسن
    st.markdown("<h3 style='text-align:center; color:#FFD700 !important;'>💡 قيم فكرتك للهاكثون</h3>", unsafe_allow_html=True)
    user_idea = st.text_input("ما هي فكرتك الجديدة؟", placeholder="اكتبي فكرتك هنا...", key="idea_input")
    
    if df is not None:
        hack_names = df['Name'].unique().tolist()
        target_h = st.selectbox("اختر الهاكثون المستهدف لفكرتك:", hack_names, key="hack_select")
        
        if st.button("تحليل الفكرة"):
            if user_idea:
                st.balloons()
                st.success(f"فكرة '{user_idea}' ممتازة ومناسبة لـ {target_h}! مهاراتك الإبداعية يا ريماس ستجعلها تنافسية.")

    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 ابحث حسب المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 ابحث حسب التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 5. عرض النتائج (Cards)
if df is not None:
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        status = str(row.get('Data', '')).strip()
        status_class = "status-expired" if "منتهي" in status else "status-available"
        status_text = "🚫 انتهى" if "منتهي" in status else "✅ متاح"

        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <div class="{status_class}">{status_text}</div>
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
            if link and link != 'nan' and "منتهي" not in status:
                actual_link = link if link.startswith('http') else f"https://{link}"
                st.link_button(f"🔗 سجل الآن في {row.get('Name')}", actual_link)
            st.markdown("<br>", unsafe_allow_html=True)
