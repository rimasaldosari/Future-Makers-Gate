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
# 2. CSS - إخفاء الأدوات وتنسيق الألوان
# =========================================
st.markdown("""
<style>
/* إخفاء شريط Streamlit العلوي والسفلي */
#MainMenu, header, footer { visibility: hidden; }
[data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
div[data-testid="stStatusWidget"] { display: none !important; }
.stDeployButton { display:none !important; }

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
}

.stApp { background-color: #f8fafc; }

/* تنسيق النصوص في الإحصائيات والأدوات لضمان الوضوح */
.stats-card {
    background: white; padding: 25px; border-radius: 20px; text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-bottom: 5px solid #1e3a8a;
}
.stats-card h2 { color: #1e3a8a !important; margin: 0; }
.stats-card p { color: #475569 !important; font-weight: bold; }

.ai-card {
    background: white; padding: 20px; border-radius: 15px; border-right: 6px solid #2563eb;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 10px;
}
.ai-card h3 { color: #1e3a8a !important; }
.ai-card p { color: #334155 !important; }

.hack-item {
    background: white; padding: 30px; border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06); margin-bottom: 25px;
    border-right: 10px solid #1e3a8a;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 3. جلب البيانات
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=5)
def get_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data.fillna("غير محدد")
    except: return None

df = get_data()

# =========================================
# 4. واجهة التطبيق
# =========================================
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

search_query = st.text_input("🔍 ابحثي عن هاكثون أو جهة منظمة", placeholder="مثال: سدايا - الرياض")

if df is not None:
    # الإحصائيات
    s1, s2, s3 = st.columns(3)
    with s1: st.markdown(f'<div class="stats-card"><h2>{len(df)}</h2><p>فرصة تقنية</p></div>', unsafe_allow_html=True)
    with s2: st.markdown(f'<div class="stats-card"><h2>{df["Location"].nunique()}</h2><p>مدينة</p></div>', unsafe_allow_html=True)
    with s3: st.markdown(f'<div class="stats-card"><h2>{df["major"].nunique()}</h2><p>تخصص</p></div>', unsafe_allow_html=True)

    # أدوات AI
    c_ai1, c_ai2 = st.columns(2)
    with c_ai1:
        st.markdown('<div class="ai-card"><h3>💡 مولد الأفكار الذكي</h3><p>دعي الذكاء الاصطناعي يقترح عليكِ فكرة مشروع</p></div>', unsafe_allow_html=True)
        if st.button("✨ ولّد فكرة مشروع"):
            st.success(random.choice(["منصة AI للصحة", "تطبيق تطوع ذكي", "مساعد دراسي بالذكاء الاصطناعي"]))
    with c_ai2:
        st.markdown('<div class="ai-card"><h3>👥 مقترح أسماء الفرق</h3><p>اختاري اسماً مميزاً لفريقك في المنافسة</p></div>', unsafe_allow_html=True)
        if st.button("🎲 اقترح اسم فريق"):
            st.info(random.choice(["Neural Ninjas", "AI Falcons", "Code Masters"]))

    # القائمة الجانبية (هنا التعديلات المطلوبة)
    with st.sidebar:
        # 1. تغيير العبارة الترحيبية
        st.markdown("<h2 style='text-align:center; color:white;'>تطوير ريماس الدوسري</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        # 2. إصلاح رابط لينكدإن ليفتح مباشرة
        st.link_button("💼 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        loc_filter = st.selectbox("📍 المدينة", ["الكل"] + sorted(df['Location'].unique().tolist()))
        major_filter = st.selectbox("🎯 التخصص", ["الكل"] + sorted(df['major'].unique().tolist()))

    # تصفية وعرض النتائج
    results = df.copy()
    if search_query:
        results = results[results.astype(str).apply(lambda x: x.str.contains(search_query, case=False).any(), axis=1)]
    if loc_filter != "الكل": results = results[results['Location'] == loc_filter]
    if major_filter != "الكل": results = results[results['major'] == major_filter]

    for _, row in results.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="hack-item">
                <h2 style="color:#1e40af;">{row['Name']}</h2>
                <p>📍 {row['Location']} | 🏢 {row['Organizaion']} | 🎯 {row['major']}</p>
                <div style="background:#f8fafc; padding:15px; border-radius:10px; border:1px solid #e2e8f0;">
                    <b>عن الفرصة:</b> {row['Description']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            link = str(row['Link']).strip()
            if link != "غير محدد":
                st.link_button(f"🔗 سجل الآن في {row['Name']}", link if link.startswith('http') else f"https://{link}")
