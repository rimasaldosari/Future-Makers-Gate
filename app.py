import streamlit as st
import google.generativeai as genai
from datetime import datetime
import pandas as pd

# 1. إعدادات الصفحة والهوية الاحترافية
st.set_page_config(
    page_title="بوصلة الهاكثونات | ريماس الدوسري",
    page_icon="🎯",
    layout="wide"
)

# 2. كود CSS المطور
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
    .badge-timer {
        background-color: #fff7ed;
        color: #9a3412;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8rem;
    }
    .success-banner {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    /* تنسيق زر لينكد إن */
    .linkedin-btn {
        display: inline-flex;
        align-items: center;
        background-color: #0077b5;
        color: white !important;
        padding: 10px 20px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
        transition: 0.3s;
    }
    .linkedin-btn:hover {
        background-color: #005a87;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- العنوان الرئيسي ---
st.title("🚀 بوصلة الهاكثونات الذكية")
st.markdown("#### منصة الابتكار المتكاملة - تطوير المهندسة ريماس الدوسري")

# 3. نظام التبويبات
tab_hacks, tab_ai_chat, tab_ai_critic, tab_teams, tab_tools, tab_success, tab_admin = st.tabs([
    "🔥 الهاكثونات", "💬 مساعد البوصلة", "🧠 محلل الأفكار", "👥 صانع الفرق", "🎒 الحقيبة", "🏆 النجاحات", "🔐 الإدارة"
])

# --- 1. الهاكثونات ---
with tab_hacks:
    st.subheader("الهاكثونات المتاحة حالياً")
    hacks_data = [
        {"name": "هاكثون الطاقة المتجددة", "date": "2026-06-10", "loc": "الرياض", "likes": 42},
        {"name": "تحدي الابتكار السيبراني", "date": "2026-04-20", "loc": "الخرج"}
    ]
    for h in hacks_data:
        end_date = datetime.strptime(h['date'], "%Y-%m-%d").date()
        days_left = (end_date - datetime.now().date()).days
        if days_left >= 0:
            st.markdown(f"""
                <div class="hack-card">
                    <span class="badge-timer">⏳ فرصة أخيرة: متبقي {days_left} أيام</span>
                    <h3>{h['name']}</h3>
                    <p>📍 {h['loc']} | 📅 ينتهي في: {h['date']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"❤️ تصويت جماعي ({h.get('likes', 0)})", key=h['name']):
                st.toast(f"تم تسجيل إعجابك بـ {h['name']}")

# --- 2. الشات بوت ---
with tab_ai_chat:
    st.subheader("💬 اسألي مساعد ريماس الذكي")
    if "messages" not in st.session_state: st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
    if p := st.chat_input("كيف أقدر أساعدك؟"):
        st.session_state.messages.append({"role": "user", "content": p})
        with st.chat_message("user"): st.markdown(p)
        with st.chat_message("assistant"):
            response = f"أهلاً بك! بصفتي مساعد المهندسة ريماس، سؤالك عن '{p}' محل اهتمامنا."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- 3. محلل الأفكار ---
with tab_ai_critic:
    st.subheader("🧠 قيم فكرتك")
    idea = st.text_area("اكتبي فكرتك هنا:")
    if st.button("حلل فكرتي 🚀"):
        st.info("تحليل ذكي: فكرة ممتازة! حاولي ربطها برؤية 2030 لزيادة فرص الفوز.")

# --- 4. صانع الفرق ---
with tab_teams:
    st.subheader("👥 ابحث عن فريق")
    col_x, col_y = st.columns(2)
    with col_x:
        st.text_input("الاسم:")
        st.multiselect("المهارات:", ["Python", "UI/UX", "AI"])
        st.button("تسجيل اهتمام")
    with col_y:
        st.info("سارة (UI/UX) - متاحة للتعاون")

# --- 5. حقيبة الهاكثون ---
with tab_tools:
    st.subheader("🎒 أدواتك للنجاح")
    st.markdown("- **التصميم:** Figma\n- **البرمجة:** GitHub & Streamlit\n- **الذكاء:** Gemini API")

# --- 6. قصص النجاح (مع زر LinkedIn) ---
with tab_success:
    st.subheader("🏆 بصمة ريماس في الابتكار")
    st.markdown("""
        <div class="success-banner">
            <h4>🌟 إنجاز معسكر IBM</h4>
            <p>تطوير وكلاء ذكاء اصطناعي متميزين.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # زر لينكد إن لفتح التطبيق مباشرة
    st.markdown("""
        <a href="linkedin://in/rimas-aldosari" class="linkedin-btn">
            <span>🔗 توثيق الإنجاز على LinkedIn</span>
        </a>
    """, unsafe_allow_html=True)

# --- 7. الإدارة ---
with tab_admin:
    st.subheader("🔐 لوحة التحكم")
    pwd = st.text_input("كلمة المرور:", type="password")
    if pwd == "Remas2026":
        st.success("أهلاً ريماس!")
        with st.form("admin_form"):
            st.text_input("اسم الهاكثون")
            st.form_submit_button("إضافة")

# --- الفوتر مع رابط LinkedIn الذكي ---
st.markdown("---")
st.markdown(f"""
    <div style="text-align: center;">
        <p style="color: #888;">تم التطوير بواسطة ريماس الدوسري | جامعة الأمير سطام بن عبدالعزيز</p>
        <a href="linkedin://in/rimas-aldosari" style="text-decoration: none; color: #0077b5; font-weight: bold;">
            LinkedIn Profile 🔗
        </a>
    </div>
""", unsafe_allow_html=True)
