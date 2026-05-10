import streamlit as st
import pandas as pd
import random

# =========================================
# 1. إعدادات الصفحة
# =========================================
st.set_page_config(
    page_title="بوصلة الهاكثونات | ريماس الدوسري",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# 2. CSS - تعديل الألوان لضمان الوضوح التام
# =========================================
st.markdown("""
<style>
/* إخفاء عناصر Streamlit */
#MainMenu, header, footer { visibility: hidden; }
[data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
}

.stApp {
    background-color: #f0f2f6; /* خلفية الصفحة رمادي فاتح جداً لبروز الكروت */
}

/* كروت الهاكثونات */
.hack-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    border-right: 8px solid #1e3a8a;
    color: #1e293b !important; /* لون النص الأساسي داكن */
}

/* العناوين داخل الكرت */
.hack-card h2 {
    color: #1e40af !important;
    margin-top: 0;
    font-weight: 700;
}

/* الحالة */
.status-badge {
    background-color: #dcfce7;
    color: #166534;
    padding: 5px 12px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 14px;
    float: left;
}

/* المعلومات */
.info-line {
    font-size: 16px;
    margin: 8px 0;
    color: #334155 !important; /* لون كحلي داكن وواضح */
}

.info-label {
    color: #1e3a8a !important;
    font-weight: bold;
}

/* صندوق الوصف */
.description-box {
    background-color: #f8fafc;
    padding: 15px;
    border-radius: 10px;
    font-size: 15px;
    color: #0f172a !important; /* لون النص في الوصف أغمق */
    margin-top: 15px;
    border: 1px solid #e2e8f0;
}

/* صناديق الإحصائيات والأدوات */
.stats-box, .ai-box {
    background: white;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.07);
    margin-bottom: 15px;
    color: #1e293b !important;
}

.ai-box {
    text-align: right;
    border-right: 6px solid #2563eb;
    background: linear-gradient(135deg, #f0f7ff, #ffffff);
}

/* زر لينكدإن */
.linkedin-btn {
    background-color: #0A66C2;
    color: white !important;
    padding: 12px 16px;
    border-radius: 12px;
    text-align: center;
    display: block;
    text-decoration: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 3. رابط Google Sheet (الخاص بك)
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except:
        return None

df = load_data()

# =========================================
# 4. محتوى التطبيق
# =========================================
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# البحث والإحصائيات
search_term = st.text_input("🔍 ابحثي عن هاكثون أو جهة منظمة", placeholder="مثال: سدايا - الأمن السيبراني")

if df is not None:
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown(f'<div class="stats-box"><h2>🚀 {len(df)}</h2><p>عدد الفرص</p></div>', unsafe_allow_html=True)
    with col2: st.markdown(f'<div class="stats-box"><h2>📍 {df["Location"].nunique()}</h2><p>عدد المدن</p></div>', unsafe_allow_html=True)
    with col3: st.markdown(f'<div class="stats-box"><h2>🎯 {df["major"].nunique()}</h2><p>التخصصات</p></div>', unsafe_allow_html=True)

# أدوات AI (مولد أفكار وأسماء فرق)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="ai-box"><h3>💡 مولد أفكار</h3></div>', unsafe_allow_html=True)
    if st.button("ولّد فكرة جديدة"):
        st.success(random.choice(["تطبيق AI للصحة", "منصة تطوع ذكية", "مساعد دراسي ذكي"]))
with c2:
    st.markdown('<div class="ai-box"><h3>👥 أسماء فرق</h3></div>', unsafe_allow_html=True)
    if st.button("اقترح اسم فريق"):
        st.info(random.choice(["Neural Ninjas", "AI Falcons", "Code Masters"]))

# القائمة الجانبية
with st.sidebar:
    st.markdown("<div style='text-align:center;'><b>ريماس الدوسري</b></div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# عرض كروت الهاكثونات من الجدول
if df is not None:
    filt_df = df.copy()
    if search_term:
        filt_df = filt_df[filt_df.astype(str).apply(lambda row: row.str.contains(search_term, case=False).any(), axis=1)]
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <div class="status-badge">✅ نشط</div>
                <h2>{row.get('Name', 'نشاط تقني')}</h2>
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
            if link and link != 'nan':
                st.link_button(f"🔗 سجل الآن في {row.get('Name')}", link if link.startswith('http') else f"https://{link}")
