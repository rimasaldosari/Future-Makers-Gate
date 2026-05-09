import streamlit as st

# إعدادات الصفحة والخطوط
st.set_page_config(page_title="بوصلة الهاكثونات والمعسكرات", layout="wide")

# تصميم CSS لتحسين الوضوح وتطابق الألوان
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; }
    
    .main { background-color: #0e1117; }
    .card {
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #161b22;
        border-right: 6px solid #1e3a8a; /* تمييز الجهة اليمنى للغة العربية */
    }
    .status-expired { color: #ff7b72; font-weight: bold; border: 1px solid #ff7b72; padding: 2px 8px; border-radius: 5px; font-size: 0.8em; }
    .status-active { color: #3fb950; font-weight: bold; border: 1px solid #3fb950; padding: 2px 8px; border-radius: 5px; font-size: 0.8em; }
    .card-title { color: #58a6ff; font-size: 22px; font-weight: bold; margin-bottom: 10px; }
    .details-box { background-color: #f0f6fc; color: #1f2328; padding: 15px; border-radius: 8px; margin-top: 10px; line-height: 1.6; }
    .sidebar-content { text-align: center; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# بيانات شاملة (تتضمن المنتهي والمتاح)
all_events = [
    {"title": "هاكثون بلاك هات", "city": "الرياض", "org": "الاتحاد السعودي", "major": "أمن سيبراني", "status": "متاح", "details": "أكبر فعالية تقنية في المنطقة لتبادل الخبرات ومواجهة تحديات الأمن السيبراني العالمية."},
    {"title": "معسكرات طويق", "city": "الرياض", "org": "أكاديمية طويق", "major": "تقنيات متقدمة", "status": "متاح", "details": "معسكرات احترافية مكثفة لتأهيل الكوادر الوطنية في مجالات البرمجة والذكاء الاصطناعي."},
    {"title": "هاكثون الحج", "city": "جدة", "org": "SAFCSP", "major": "تقنيات الحج", "status": "منتهي", "details": "تجربة ابتكارية لخدمة ضيوف الرحمن عبر حلول تقنية ذكية."},
    {"title": "معسكر الذكاء الاصطناعي التوليدي", "city": "الخرج", "org": "جامعة سطام", "major": "AI", "status": "منتهي", "details": "تدريب مكثف على نماذج اللغة الكبيرة وتطبيقاتها العملية."}
]

# العنوان الرئيسي
st.markdown('<h1 style="text-align: center; color: white;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #8b949e;">منصة إدارة الابتكار المتكاملة - ريماس الدوسري</p>', unsafe_allow_html=True)

col_main, col_side = st.columns([3, 1])

with col_main:
    # تقسيم العرض حسب الحالة
    display_type = st.radio("عرض الفعاليات:", ["الكل", "المتاحة حالياً", "الأرشيف (المنتهية)"], horizontal=True)
    
    for ev in all_events:
        if display_type == "المتاحة حالياً" and ev["status"] == "منتهي": continue
        if display_type == "الأرشيف (المنتهية)" and ev["status"] == "متاح": continue
        
        status_class = "status-active" if ev["status"] == "متاح" else "status-expired"
        status_label = "✅ متاح للتسجيل" if ev["status"] == "متاح" else "🚫 انتهى التسجيل"
        
        st.markdown(f"""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div class="card-title">{ev['title']}</div>
                <span class="{status_class}">{status_label}</span>
            </div>
            <div style="margin-top: 10px;">
                <span>📍 {ev['city']}</span> | <span>🏢 {ev['org']}</span> | <span>🎯 {ev['major']}</span>
            </div>
            <div class="details-box">
                <b>📝 التفاصيل:</b><br>{ev['details']}
            </div>
            <div style="text-align: left; margin-top: 15px;">
                {"<a href='#' style='color:#58a6ff; text-decoration:none; font-weight:bold;'>🔗 رابط التقديم</a>" if ev['status'] == 'متاح' else ""}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # قسم قيم فكرتك مع ردود واضحة
    st.markdown("---")
    with st.expander("🧠 قيم فكرتك (محلل الابتكار)"):
        st.subheader("تحليل الجدوى والابتكار")
        idea_name = st.text_input("عنوان الفكرة:")
        c1, c2 = st.columns(2)
        with c1: st.text_input("المدينة:", value="الخرج")
        with c2: st.text_input("التخصص:", value="هندسة وحاسب")
        
        if st.button("تحليل الفكرة"):
            st.info("**جاري التحليل...**")
            # نموذج لردود واضحة ومفصلة
            st.markdown(f"""
            ### 📊 نتيجة تقييم فكرة: {idea_name}
            *   **القيمة الابتكارية:** فكرة واعدة تتناسب مع سوق العمل في المملكة.
            *   **الملاءمة للتخصص:** متوافقة جداً مع مسارك الأكاديمي.
            *   **توصية البوصلة:** ننصحك بالتقديم بها في **هاكثون بلاك هات** القادم.
            """)

with col_side:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/96/compass.png") # أيقونة تعبيرية
    st.markdown("### الفلاتر")
    st.selectbox("التخصص:", ["الكل", "أمن سيبراني", "برمجة", "ذكاء اصطناعي"])
    st.selectbox("المدينة:", ["الكل", "الرياض", "الخرج", "جدة"])
    st.markdown("---")
    st.write("**تطوير:**")
    st.write("ريماس الدوسري")
    st.markdown("</div>", unsafe_allow_html=True)

# وضع التعديل لإضافة هاكثونات جديدة
if st.checkbox("🛠️ فتح لوحة التحكم (إضافة معسكرات/هاكثونات)"):
    with st.form("add_event"):
        st.write("إضافة فعالية جديدة للمنصة")
        new_t = st.text_input("الاسم:")
        new_s = st.selectbox("الحالة:", ["متاح", "منتهي"])
        new_d = st.text_area("وصف دقيق:")
        if st.form_submit_button("حفظ التغييرات"):
            st.success("تم تحديث قاعدة البيانات بنجاح!")
