import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات والمعسكرات", layout="wide")

# تصميم CSS ليتناسب مع الصور المرفقة
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .title-text { color: #1e3a8a; font-size: 40px; font-weight: bold; text-align: center; font-family: 'Tajawal', sans-serif; }
    .card {
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        border-left: 8px solid #1e3a8a;
    }
    .card-title { color: #1e3a8a; font-size: 28px; font-weight: bold; margin-bottom: 15px; }
    .info-item { margin-bottom: 10px; font-size: 18px; color: #333; }
    .details-box { background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #edf2f7; margin-top: 15px; }
    .btn-register {
        background-color: #1a202c;
        color: white !important;
        padding: 10px 25px;
        border-radius: 8px;
        text-decoration: none;
        float: right;
        font-weight: bold;
    }
    .sidebar-text { text-align: center; color: #4a5568; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<div class="title-text">🚀 بوصلة الهاكثونات والمعسكرات</div>', unsafe_allow_html=True)

# تقسيم الصفحة إلى أعمدة (المحتوى الرئيسي والقائمة الجانبية)
col_main, col_side = st.columns([3, 1])

with col_main:
    # 1. كرت هاكثون بلاك هات
    st.markdown("""
    <div class="card">
        <div class="card-title">هاكثون بلاك هات</div>
        <div class="info-item">📍 <b>المدينة:</b> الرياض</div>
        <div class="info-item">🏢 <b>الجهة:</b> الاتحاد السعودي</div>
        <div class="info-item">🎯 <b>التخصص:</b> أمن سيبراني</div>
        <div class="info-item">📅 <b>التاريخ:</b> ديسمبر 2026</div>
        <div class="details-box">
            📝 <b>التفاصيل:</b><br>
            أكبر فعالية تقنية في المنطقة لتبادل الخبرات ومواجهة تحديات الأمن السيبراني العالمية.
        </div>
        <br>
        <a href="#" class="btn-register">🔗 سجل الآن</a>
        <div style="clear: both;"></div>
    </div>
    """, unsafe_allow_html=True)

    # 2. كرت معسكرات طويق
    st.markdown("""
    <div class="card">
        <div class="card-title">معسكرات طويق</div>
        <div class="info-item">📍 <b>المدينة:</b> الرياض</div>
        <div class="info-item">🏢 <b>الجهة:</b> أكاديمية طويق</div>
        <div class="info-item">🎯 <b>التخصص:</b> تقنيات متقدمة</div>
        <div class="details-box">
            📝 <b>التفاصيل:</b><br>
            معسكرات احترافية مكثفة لتأهيل الكوادر الوطنية في مجالات البرمجة والذكاء الاصطناعي.
        </div>
        <br>
        <a href="#" class="btn-register">🔗 سجل الآن</a>
        <div style="clear: both;"></div>
    </div>
    """, unsafe_allow_html=True)

    # إضافة قسم "قيم فكرتك" بشكل مبسط بنفس النمط
    with st.expander("🧠 قيم فكرتك (قسم جديد)"):
        user_city = st.text_input("مدينتك:")
        user_major = st.text_input("تخصصك:")
        idea = st.text_area("اشرح فكرتك هنا:")
        if st.button("إرسال للتقييم"):
            st.success("سيتم تقييم فكرتك بناءً على تخصصك وموقعك.")

# القائمة الجانبية (Sidebar)
with col_side:
    st.markdown("<br><br>", unsafe_allow_html=True)
    # إضافة الفلاتر كما ظهرت في صورتك
    st.selectbox("🎯 التخصص:", ["الكل", "أمن سيبراني", "ذكاء اصطناعي", "برمجة"])
    st.selectbox("📍 المدينة:", ["الكل", "الرياض", "جدة", "الخرج"])
    
    st.markdown("---")
    st.markdown("""
    <div class="sidebar-text">
        <b>تطوير:</b><br>
        ريماس الدوسري<br><br>
        <a href='https://www.linkedin.com/in/rimas-aldosari' style='text-decoration:none; color:#1e3a8a;'>LinkedIn Profile 🔗</a>
    </div>
    """, unsafe_allow_html=True)

# ميزة التعديل (Editor) تظهر فقط عند الحاجة
if st.checkbox("🛠️ وضع التعديل (إضافة/تغيير البيانات)"):
    st.info("يمكنك هنا إضافة بيانات جديدة لتظهر في الكروت أعلاه.")
    new_title = st.text_input("اسم الفعالية:")
    # ... يمكن إضافة حقول أخرى هنا لتحديث البيانات ديناميكياً
