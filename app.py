import streamlit as st
import google.generativeai as genai
from datetime import datetime

# 1. إعدادات الصفحة والهوية الاحترافية (ريماس الدوسري)
st.set_page_config(
    page_title="بوصلة الابتكار | ريماس الدوسري",
    page_icon="🎯",
    layout="wide"
)

# 2. كود CSS لتنظيف الواجهة وإخفاء بصمة المنصة
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none;}
    
    .hack-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        border-right: 10px solid #1e3a8a;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .camp-card {
        background-color: #f8fafc;
        border-radius: 15px;
        padding: 20px;
        border-right: 10px solid #059669;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .badge-timer {
        background-color: #fff7ed;
        color: #9a3412;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- العنوان الرئيسي ---
st.title("🚀 بوصلة الهاكثونات والمعسكرات")
st.markdown("#### منصة إدارة الابتكار - تطوير المهندسة ريماس الدوسري")

# 3. نظام التبويبات المطور
tab_hacks, tab_camps, tab_ai_chat, tab_ai_critic, tab_success, tab_admin = st.tabs([
    "🔥 الهاكثونات", "🏕️ المعسكرات", "💬 مساعد البوصلة", "🧠 محلل الأفكار", "🏆 النجاحات", "🔐 لوحة الإدارة"
])

# محاكاة لقاعدة بيانات (سيتم استبدالها بـ Session State للتعديل المباشر)
if 'data_list' not in st.session_state:
    st.session_state.data_list = [
        {"type": "هاكثون", "name": "هاكثون الطاقة 2026", "date": "2026-06-10", "loc": "الرياض"},
        {"type": "معسكر", "name": "معسكر IBM للذكاء الاصطناعي", "date": "2026-07-01", "loc": "عن بعد"}
    ]

# --- 1. تبويب الهاكثونات ---
with tab_hacks:
    st.subheader("الهاكثونات المتاحة")
    for item in st.session_state.data_list:
        if item['type'] == "هاكثون":
            st.markdown(f"""<div class="hack-card"><h3>{item['name']}</h3><p>📍 {item['loc']} | 📅 {item['date']}</p></div>""", unsafe_allow_html=True)

# --- 2. تبويب المعسكرات (الجديد) ---
with tab_camps:
    st.subheader("المعسكرات التقنية القادمة")
    for item in st.session_state.data_list:
        if item['type'] == "معسكر":
            st.markdown(f"""<div class="camp-card"><h3>{item['name']}</h3><p>📍 {item['loc']} | 📅 {item['date']}</p></div>""", unsafe_allow_html=True)

# --- 3. مساعد البوصلة و 4. محلل الأفكار و 5. النجاحات (نفس الكود السابق مع الاحتفاظ بالخصوصية) ---
with tab_success:
    st.subheader("🏆 إنجازات المهندسة ريماس")
    st.info("إتمام معسكر IBM للذكاء الاصطناعي بنجاح.")
    st.markdown(f'<a href="linkedin://in/rimas-aldosari" style="color:#0077b5; font-weight:bold;">LinkedIn Profile 🔗</a>', unsafe_allow_html=True)

# --- 6. لوحة الإدارة (التعديل المباشر من الموقع) ---
with tab_admin:
    st.subheader("🔐 إدارة المحتوى (بدون جداول خارجية)")
    pwd = st.text_input("كلمة مرور الإدارة:", type="password")
    
    if pwd == "Remas2026":
        st.success("مرحباً ريماس! يمكنك الآن الإضافة أو الحذف مباشرة.")
        
        # نموذج الإضافة
        with st.form("add_new"):
            st.write("### إضافة فرصة جديدة")
            category = st.selectbox("النوع:", ["هاكثون", "معسكر"])
            name = st.text_input("الاسم:")
            loc = st.text_input("الموقع:")
            date = st.date_input("التاريخ:")
            if st.form_submit_button("إضافة الآن 🚀"):
                st.session_state.data_list.append({"type": category, "name": name, "date": str(date), "loc": loc})
                st.rerun()

        # خيار الحذف/التعديل
        st.write("### الإدارة الحالية")
        for i, item in enumerate(st.session_state.data_list):
            col_a, col_b = st.columns([3, 1])
            col_a.write(f"{item['type']}: {item['name']}")
            if col_b.button(f"حذف", key=f"del_{i}"):
                st.session_state.data_list.pop(i)
                st.rerun()

# --- الفوتر ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>تطوير ريماس الدوسري | جامعة الأمير سطام بن عبدالعزيز</p>", unsafe_allow_html=True)
