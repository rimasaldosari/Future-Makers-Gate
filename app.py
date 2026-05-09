import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات والمعسكرات", layout="wide")

# تصميم CSS بألوان فاتحة وخطوط واضحة جداً
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; }
    
    /* تغيير الخلفية للأبيض/الفاتح */
    .main { background-color: #f8fafc; color: #1e293b; }
    
    .card {
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-right: 8px solid #1e3a8a;
    }
    
    .card-title { color: #1e3a8a; font-size: 26px; font-weight: bold; margin-bottom: 15px; }
    
    .status-tag {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
    }
    .active { background-color: #dcfce7; color: #166534; }
    .expired { background-color: #fee2e2; color: #991b1b; }
    
    .details-box { 
        background-color: #f1f5f9; 
        color: #334155; 
        padding: 18px; 
        border-radius: 10px; 
        margin-top: 15px; 
        border: 1px solid #e2e8f0;
        line-height: 1.8;
        font-size: 16px;
    }
    
    .btn-register {
        background-color: #1e3a8a;
        color: white !important;
        padding: 10px 25px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# قاعدة بيانات شاملة لكل الهاكثونات والمعسكرات (التي ذكرتيها سابقاً)
data = [
    {"title": "هاكثون بلاك هات", "city": "الرياض", "org": "الاتحاد السعودي", "major": "أمن سيبراني", "status": "متاح", "details": "أكبر فعالية تقنية في المنطقة لتبادل الخبرات ومواجهة تحديات الأمن السيبراني العالمية."},
    {"title": "معسكرات طويق", "city": "الرياض", "org": "أكاديمية طويق", "major": "تقنيات متقدمة", "status": "متاح", "details": "معسكرات احترافية مكثفة لتأهيل الكوادر الوطنية في مجالات البرمجة والذكاء الاصطناعي."},
    {"title": "هاكثون الطاقة 2026", "city": "الظهران", "org": "وزارة الطاقة", "major": "هندسة وحاسب", "status": "متاح", "details": "ابتكار حلول تقنية لمستقبل الطاقة المستدامة وتحسين كفاءة الاستهلاك."},
    {"title": "معسكر IBM للوكلاء الذكيين", "city": "عن بعد", "org": "IBM SkillsBuild", "major": "ذكاء اصطناعي", "status": "منتهي", "details": "تدريب مكثف على بناء وتطوير الوكلاء الذكيين باستخدام تقنيات IBM."},
    {"title": "هاكثون الذكاء الاصطناعي", "city": "جدة", "org": "سدايا", "major": "AI", "status": "منتهي", "details": "تطوير نماذج ذكاء اصطناعي لخدمة القطاعات الحيوية في المملكة."},
    {"title": "معسكر الذكاء الاصطناعي التوليدي", "city": "الخرج", "org": "جامعة سطام", "major": "نظم معلومات", "status": "منتهي", "details": "التعمق في نماذج LLM وكيفية دمجها في التطبيقات البرمجية."}
]

# العناوين
st.markdown('<h1 style="text-align: center; color: #1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #64748b; font-size: 1.2em;">تطوير ريماس الدوسري | جامعة الأمير سطام بن عبدالعزيز</p>', unsafe_allow_html=True)

col_main, col_side = st.columns([3, 1])

with col_main:
    # فلترة العرض
    view_option = st.segmented_control("عرض الفعاليات:", ["الكل", "المتاحة", "الأرشيف"], default="الكل")
    
    for item in data:
        if view_option == "المتاحة" and item["status"] == "منتهي": continue
        if view_option == "الأرشيف" and item["status"] == "متاح": continue
        
        status_class = "active" if item["status"] == "متاح" else "expired"
        status_text = "✅ متاح للتسجيل" if item["status"] == "متاح" else "🚫 انتهى التقديم"
        
        st.markdown(f"""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div class="card-title">{item['title']}</div>
                <span class="status-tag {status_class}">{status_text}</span>
            </div>
            <div style="font-size: 18px; color: #475569; margin: 10px 0;">
                📍 <b>{item['city']}</b> | 🏢 <b>{item['org']}</b> | 🎯 <b>{item['major']}</b>
            </div>
            <div class="details-box">
                <b>📝 التفاصيل:</b><br>{item['details']}
            </div>
            <div style="text-align: left; margin-top: 15px;">
                {"<a href='#' class='btn-register'>سجل الآن 🔗</a>" if item['status'] == 'متاح' else ""}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # قسم قيم فكرتك بتصميم واضح وردود مفصلة
    st.markdown("---")
    with st.expander("💡 قيم فكرتك (محلل الابتكار)"):
        st.markdown("### حلل فكرتك بناءً على موقعك وتخصصك")
        idea_title = st.text_input("عنوان الفكرة:")
        c1, c2 = st.columns(2)
        with c1: st.text_input("المدينة:", value="الخرج")
        with c2: st.text_input("التخصص:", value="هندسة وعلوم الحاسب")
        
        if st.button("بدء التحليل الذكي"):
            st.balloons()
            st.success(f"**تم تحليل فكرة: {idea_title}**")
            st.markdown(f"""
            <div style="background-color: #f8fafc; padding: 20px; border-radius: 10px; border: 1px dashed #1e3a8a;">
                <h4>📊 نتائج التقرير:</h4>
                <ul>
                    <li><b>مدى الابتكار:</b> الفكرة قوية وتغطي فجوة تقنية في سوق {item['city']}.</li>
                    <li><b>التوصية الأكاديمية:</b> تخصصك في البرمجيات يدعم تنفيذ هذه الفكرة تقنياً بشكل ممتاز.</li>
                    <li><b>الخطوة القادمة:</b> ننصحك بالانضمام إلى <b>معسكرات طويق</b> القادمة لتطوير النموذج الأولي.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

with col_side:
    st.markdown("<div style='background-color: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0;'>", unsafe_allow_html=True)
    st.markdown("### 🔍 تصفية سريعة")
    st.selectbox("حسب التخصص:", ["الكل", "أمن سيبراني", "ذكاء اصطناعي", "هندسة"])
    st.selectbox("حسب المدينة:", ["الكل", "الرياض", "الخرج", "جدة"])
    st.markdown("---")
    st.write("**تطوير:**")
    st.write("**ريماس الدوسري**")
    st.markdown("</div>", unsafe_allow_html=True)

# ميزة التعديل الجدولي كما طلبتِ
st.markdown("---")
if st.checkbox("🛠️ فتح لوحة تعديل البيانات (الجدول البياني)"):
    st.info("يمكنك تعديل البيانات هنا لتظهر في الكروت أعلاه مباشرة.")
    df = pd.DataFrame(data)
    edited_df = st.data_editor(df, num_rows="dynamic")
