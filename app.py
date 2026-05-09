import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة ريماس للابتكار", layout="wide")

# CSS لتطابق الشكل مع الصورة image_8.png
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; font-family: 'Tajawal', sans-serif; }
    .event-card {
        background-color: #ffffff; border-radius: 15px; padding: 25px;
        margin-bottom: 20px; color: #000000; border-left: 10px solid #1e3a8a;
    }
    .status-badge { background-color: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 8px; font-weight: bold; float: right; }
    .card-header { color: #1e3a8a; font-size: 24px; font-weight: bold; margin-bottom: 10px; text-align: left; }
    .details-box { background-color: #f3f4f6; padding: 15px; border-radius: 10px; color: #374151; text-align: right; margin-top: 10px; }
    .reg-button { background-color: #1e3a8a; color: white !important; padding: 8px 25px; border-radius: 8px; text-decoration: none; display: inline-block; margin-top: 15px; }
    .linkedin-link { background-color: #0077b5; color: white !important; padding: 10px; border-radius: 5px; text-decoration: none; display: block; text-align: center; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 1. البيانات الأصلية من جدولك image_9.png مع إضافة الأوصاف
if 'events_df' not in st.session_state:
    data = [
        {"الاسم": "هاكثون بلاك هات", "الجهة": "الاتحاد السعودي", "التخصص": "أمن سيبراني", "الموقع": "الرياض", "الرابط": "https://blackhatsaudi.com", "الوصف": "أكبر فعالية تقنية في المنطقة لتبادل الخبرات ومواجهة تحديات الأمن السيبراني العالمية."},
        {"الاسم": "معسكرات طويق", "الجهة": "أكاديمية طويق", "التخصص": "ذكاء اصطناعي", "الموقع": "الرياض", "الرابط": "https://tuwaiq.edu.sa", "الوصف": "معسكرات احترافية مكثفة لتأهيل الكوادر الوطنية في مجالات البرمجة والذكاء الاصطناعي."},
        {"الاسم": "هاكثون الدرعية", "الجهة": "هيئة تطوير الدرعية", "التخصص": "تراث وتقنية", "الموقع": "الدرعية", "الرابط": "https://dgda.gov.sa", "الوصف": "ابتكار حلول تقنية تجمع بين العراقة والتكنولوجيا الحديثة لخدمة زوار المنطقة التاريخية."},
        {"الاسم": "هاكثون سطام", "الجهة": "جامعة سطام", "التخصص": "الكل", "الموقع": "الخرج", "الرابط": "https://psau.edu.sa", "الوصف": "ملتقى ابتكاري لطلاب ومنسوبي جامعة سطام لتقديم حلول ذكية تخدم البيئة الجامعية."},
        {"الاسم": "معسكر الابتكار", "الجهة": "مبادرات الابتكار", "التخصص": "ابتكار وتقنية", "الموقع": "عام", "الرابط": "https://innovation.sa", "الوصف": "رحلة تعليمية من الفكرة إلى النموذج الأولي باستخدام أدوات الابتكار العالمية."},
        {"الاسم": "هاكثون الحج", "الجهة": "مركز الدراسات", "التخصص": "تقنية وخدمات", "الموقع": "جدة", "الرابط": "https://hajhackathon.sa", "الوصف": "تطوير حلول تقنية مبتكرة لتسهيل رحلة ضيوف الرحمن وتحسين الخدمات."}
    ]
    st.session_state.events_df = pd.DataFrame(data)

# القائمة الجانبية (الفلترة والتحكم)
with st.sidebar:
    st.markdown("### 🛠️ لوحة التحكم")
    edit_mode = st.toggle("تفعيل وضع المحرر")
    
    st.markdown("---")
    st.markdown("### 🔍 تصفية سريعة")
    # هذه الفلاتر الآن تعمل فعلياً وتغير النتائج
    f_loc = st.selectbox("حسب المدينة:", ["الكل"] + list(st.session_state.events_df['الموقع'].unique()))
    f_major = st.selectbox("حسب التخصص:", ["الكل"] + list(st.session_state.events_df['التخصص'].unique()))
    
    st.markdown("---")
    st.write("**تطوير:** ريماس الدوسري")
    st.markdown(f'<a href="https://www.linkedin.com/in/rimas-aldosari" class="linkedin-link">LinkedIn Profile 🔗</a>', unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<h1 style="color: #58a6ff; text-align: center;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# ميزة التعديل
if edit_mode:
    st.info("💡 يمكنك إضافة وصف لكل هاكثون أو تغيير الروابط من الجدول أدناه:")
    st.session_state.events_df = st.data_editor(st.session_state.events_df, num_rows="dynamic")

# تطبيق الفلترة على البيانات المعروضة
df_to_show = st.session_state.events_df.copy()
if f_loc != "الكل":
    df_to_show = df_to_show[df_to_show['الموقع'] == f_loc]
if f_major != "الكل":
    df_to_show = df_to_show[df_to_show['التخصص'] == f_major]

# قسم قيم فكرتك (مع أيقونة لمبة تفاعلية)
with st.expander("💡 أيقونة: قيم فكرتك للهاكثون"):
    st.markdown("### 📊 محلل الابتكار")
    idea_name = st.text_input("ما هو اسم فكرتك؟")
    target_hack = st.selectbox("اختر الهاكثون المستهدف:", df_to_show['الاسم'].unique())
    if st.button("تحليل الفكرة الآن"):
        st.balloons()
        st.success(f"فكرة '{idea_name}' رائعة! تتماشى مع رؤية {target_hack}. ننصحك يا ريماس بالتركيز على واجهة المستخدم (UI/UX) كما في مشروعك السابق.")

# عرض الكروت بناءً على الفلترة والوصف
for _, row in df_to_show.iterrows():
    st.markdown(f"""
    <div class="event-card">
        <div class="status-badge">✅ متاح للتسجيل</div>
        <div class="card-header">{row['الاسم']}</div>
        <div style="color: #4b5563; margin-bottom: 10px;">
            📍 {row['الموقع']} | 🏢 {row['الجهة']} | 🎯 {row['التخصص']}
        </div>
        <div class="details-box">
            <b>📝 وصف الفعالية:</b><br>{row['الوصف']}
        </div>
        <a href="{row['الرابط']}" target="_blank" class="reg-button">🔗 سجل الآن</a>
    </div>
    """, unsafe_allow_html=True)
