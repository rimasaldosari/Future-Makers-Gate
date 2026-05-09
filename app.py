import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات والمعسكرات", layout="wide")

# تخصيص المظهر بـ CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTitle { font-family: 'Tajawal', sans-serif; text-align: center; color: #00d4ff; }
    .footer { text-align: center; padding: 20px; color: #888; font-size: 0.9em; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي (بدون كلمة مهندسة)
st.title("🚀 بوصلة الهاكثونات والمعسكرات")
st.markdown("<h3 style='text-align: center;'>منصة إدارة الابتكار - تطوير ريماس الدوسري</h3>", unsafe_allow_html=True)

# القائمة الجانبية أو التبويبات
tabs = st.tabs(["🔥 الهاكثونات", "🏕️ المعسكرات", "🧠 محلل الأفكار", "📍 مساعدة البوصلة"])

# 1. قسم الهاكثونات
with tabs[0]:
    st.header("🔗 الهاكثونات المتاحة حالياً")
    hackathon_data = pd.DataFrame({
        "الهاكثون": ["هاكثون الطاقة 2026", "هاكثون الذكاء الاصطناعي"],
        "المدينة": ["الرياض", "جدة"],
        "الحالة": ["متاح", "ينتهي قريباً"]
    })
    # خانة قابلة للتعديل
    edited_hacks = st.data_editor(hackathon_data, num_rows="dynamic", key="hacks")

# 2. قسم المعسكرات
with tabs[1]:
    st.header("🏕️ المعسكرات التدريبية")
    bootcamp_data = pd.DataFrame({
        "المعسكر": ["معسكر IBM للوكلاء الذكيين", "معسكر تطوير الويب"],
        "الجهة": ["IBM SkillsBuild", "أكاديمية طويق"],
        "المدة": ["أسبوعين", "شهر"]
    })
    # خانة قابلة للتعديل
    edited_boots = st.data_editor(bootcamp_data, num_rows="dynamic", key="boots")

# 3. قسم محلل الأفكار (إضافة المدينة والتخصص)
with tabs[2]:
    st.header("🧠 قيم فكرتك")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("الاسم", value="ريماس الدوسري")
        major = st.text_input("التخصص", value="هندسة وعلوم الحاسب") # إضافة التخصص
    with col2:
        city = st.text_input("المدينة", value="الخرج") # إضافة المدينة
        idea_title = st.text_input("عنوان الفكرة")
    
    idea_desc = st.text_area("اشرح فكرتك هنا...")
    
    if st.button("تحليل وتقييم الفكرة"):
        st.success(f"تم استلام فكرتك يا {name} في مدينة {city}. سيتم تحليلها بناءً على تخصصك في {major}.")

# 4. مساعدة البوصلة
with tabs[3]:
    st.info("هذا القسم مخصص لمساعدتك في العثور على الفريق المناسب أو توضيح شروط المسابقات.")

# ذيل الصفحة (بدون كلمة مهندسة)
st.markdown("---")
st.markdown(f"""
    <div class='footer'>
        تطوير ريماس الدوسري | جامعة الأمير سطام بن عبدالعزيز
        <br>
        <a href='https://www.linkedin.com/in/rimas-aldosari' target='_blank'>LinkedIn Profile 🔗</a>
    </div>
    """, unsafe_allow_html=True)
