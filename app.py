import streamlit as st
import pandas as pd
import random

# =========================================
# إعدادات الصفحة
# =========================================

st.set_page_config(
    page_title="بوصلة الهاكثونات | ريماس الدوسري",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# CSS + إخفاء أدوات Streamlit
# =========================================

st.markdown("""
<style>

/* إخفاء عناصر Streamlit */
#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

button[kind="header"] {
    display: none !important;
}

/* الخط */
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
}

.stApp {
    background-color: #f8fafc;
}

/* كروت الهاكثونات */
.hack-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    border-right: 8px solid #1e3a8a;
    transition: 0.3s ease;
}

.hack-card:hover {
    transform: translateY(-5px);
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
    color: #1e293b;
}

.info-label {
    color: #1e3a8a;
    font-weight: bold;
}

/* الوصف */
.description-box {
    background-color: #f1f5f9;
    padding: 15px;
    border-radius: 10px;
    font-size: 15px;
    color: #0f172a;
    margin-top: 15px;
    border-right: 4px solid #94a3b8;
}

/* الإحصائيات */
.stats-box {
    background: white;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.07);
    margin-bottom: 15px;
}

/* أدوات AI */
.ai-box {
    background: linear-gradient(135deg,#eff6ff,#ffffff);
    padding: 20px;
    border-radius: 15px;
    border-right: 6px solid #2563eb;
    margin-top: 15px;
    margin-bottom: 15px;
}

/* زر لينكدإن */
.linkedin-btn {
    background-color:#0A66C2;
    color:white !important;
    padding:12px 16px;
    border-radius:12px;
    text-align:center;
    display:block;
    text-decoration:none;
    font-weight:bold;
    transition:0.3s;
}

.linkedin-btn:hover {
    transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# رابط Google Sheet
# =========================================

SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

# =========================================
# تحميل البيانات
# =========================================

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
# العنوان الرئيسي
# =========================================

st.markdown(
    """
    <h1 style="text-align:center; color:#1e3a8a;">
    🚀 بوصلة الهاكثونات والمعسكرات
    </h1>
    """,
    unsafe_allow_html=True
)

# =========================================
# البحث
# =========================================

search_term = st.text_input(
    "🔍 ابحثي عن هاكثون أو جهة منظمة",
    placeholder="مثال: سدايا - الأمن السيبراني - الرياض"
)

# =========================================
# الإحصائيات
# =========================================

if df is not None:

    total_hackathons = len(df)
    total_locations = df['Location'].nunique()
    total_majors = df['major'].nunique()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="stats-box">
        <h2>🚀 {total_hackathons}</h2>
        <p>عدد الفرص</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stats-box">
        <h2>📍 {total_locations}</h2>
        <p>عدد المدن</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stats-box">
        <h2>🎯 {total_majors}</h2>
        <p>عدد التخصصات</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================
# مولد أفكار
# =========================================

st.markdown("""
<div class="ai-box">
<h3>💡 مولد أفكار هاكثونية</h3>
<p>اضغطي الزر لتحصلي على فكرة مشروع تقنية جاهزة ✨</p>
</div>
""", unsafe_allow_html=True)

ideas = [
    "تطبيق ذكي يساعد المكفوفين بالتنقل داخل الجامعات",
    "منصة AI لتحليل الإرهاق النفسي للطلاب",
    "تطبيق لتنظيم استهلاك المياه بالمنازل",
    "مساعد ذكي للبحث عن الفرص التدريبية",
    "منصة توصل المتطوعين بالفعاليات المناسبة لهم",
    "تطبيق يكتشف الأخبار المزيفة باستخدام الذكاء الاصطناعي",
    "منصة لإدارة فرق الهاكثونات بسهولة"
]

if st.button("💡 ولّد فكرة جديدة"):
    st.success(random.choice(ideas))

# =========================================
# اقتراح أسماء فرق
# =========================================

st.markdown("""
<div class="ai-box">
<h3>👥 اقتراح أسماء فرق</h3>
<p>احصلي على اسم احترافي لفريقك 🚀</p>
</div>
""", unsafe_allow_html=True)

team_names = [
    "Vision Coders",
    "AI Falcons",
    "Future Minds",
    "Code Storm",
    "Quantum Team",
    "Byte Builders",
    "Neural Ninjas"
]

if st.button("🎲 اقترح اسم فريق"):
    st.info(random.choice(team_names))

# =========================================
# تقييم الفكرة
# =========================================

with st.expander("📊 قيم فكرتك للهاكثون"):

    idea_input = st.text_area(
        "اكتبي فكرتك:",
        placeholder="مثال: تطبيق يساعد الطلاب على إدارة الوقت..."
    )

    if st.button("🚀 تحليل الفكرة"):

        if idea_input:

            innovation = random.randint(70, 98)
            execution = random.randint(60, 95)
            impact = random.randint(75, 99)

            st.success("✅ تم تحليل الفكرة")

            st.write("💡 الابتكار")
            st.progress(innovation)

            st.write("⚙️ قابلية التنفيذ")
            st.progress(execution)

            st.write("🌍 التأثير المجتمعي")
            st.progress(impact)

            suggestions = [
                "إضافة ذكاء اصطناعي قد يرفع تميز المشروع.",
                "يفضل تحسين تجربة المستخدم.",
                "الفكرة مناسبة جدًا للهاكثونات الصحية.",
                "يمكن تحويل المشروع إلى منتج حقيقي.",
                "إضافة تطبيق جوال سيزيد قوة المشروع."
            ]

            st.info(random.choice(suggestions))

# =========================================
# القائمة الجانبية
# =========================================

with st.sidebar:

    st.markdown("""
    <div style='text-align:center;'>
    <b>تطوير المهندسة:</b><br>
    ريماس الدوسري
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <a class="linkedin-btn"
    href="linkedin://in/rimas-aldosari-656a23375">

    🔗 حسابي على LinkedIn

    </a>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if df is not None:

        sel_loc = st.selectbox(
            "📍 حسب المدينة:",
            ["الكل"] + sorted(df['Location'].dropna().unique().tolist())
        )

        sel_major = st.selectbox(
            "🎯 حسب التخصص:",
            ["الكل"] + sorted(df['major'].dropna().unique().tolist())
        )

# =========================================
# عرض النتائج
# =========================================

if df is not None:

    filt_df = df.copy()

    # فلترة البحث
    if search_term:

        filt_df = filt_df[
            filt_df.astype(str)
            .apply(
                lambda row:
                row.str.contains(search_term, case=False).any(),
                axis=1
            )
        ]

    # فلترة المدينة
    if sel_loc != "الكل":
        filt_df = filt_df[filt_df['Location'] == sel_loc]

    # فلترة التخصص
    if sel_major != "الكل":
        filt_df = filt_df[filt_df['major'] == sel_major]

    # عرض البيانات
    for _, row in filt_df.iterrows():

        with st.container():

            st.markdown(f"""
            <div class="hack-card">

                <div class="status-badge">
                ✅ نشط
                </div>

                <h2 style='color:#1e40af; margin-top:0;'>
                {row.get('Name', 'نشاط تقني')}
                </h2>

                <div class="info-line">
                <span class="info-label">📍 المدينة:</span>
                {row.get('Location', 'غير محدد')}
                </div>

                <div class="info-line">
                <span class="info-label">🏢 الجهة:</span>
                {row.get('Organizaion', 'غير محدد')}
                </div>

                <div class="info-line">
                <span class="info-label">🎯 التخصص:</span>
                {row.get('major', 'عام')}
                </div>

                <div class="info-line">
                <span class="info-label">📅 التاريخ:</span>
                {row.get('Data', 'قريباً')}
                </div>

                <div class="description-box">
                📝 <b>عن الفرصة:</b><br>
                {row.get('Description', 'لا يوجد وصف حالياً.')}
                </div>

            </div>
            """, unsafe_allow_html=True)

            # رابط التسجيل
            link = str(row.get('Link', '')).strip()

            if link and link != 'nan' and len(link) > 5:

                actual_link = (
                    link if link.startswith('http')
                    else f"https://{link}"
                )

                st.link_button(
                    "🔗 اضغط هنا للتسجيل",
                    actual_link
                )

            else:
                st.info("رابط التسجيل سيتم تحديثه قريباً")

            st.markdown("<br>", unsafe_allow_html=True)