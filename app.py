import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات والمعسكرات", layout="wide")

# تصميم CSS مطابق لصورة تطبيقك مع تحسين الوضوح
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; font-family: 'Tajawal', sans-serif; }
    .event-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        color: #000000;
        border-left: 10px solid #1e3a8a;
    }
    .status-badge { background-color: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 8px; font-weight: bold; float: right; }
    .card-header { color: #1e3a8a; font-size: 24px; font-weight: bold; margin-bottom: 10px; text-align: left; }
    .info-row { color: #4b5563; margin-bottom: 15px; font-size: 16px; text-align: left; }
    .details-box { background-color: #f3f4f6; padding: 15px; border-radius: 10px; color: #374151; text-align: right; }
    .reg-button { background-color: #1e3a8a; color: white !important; padding: 8px 25px; border-radius: 8px; text-decoration: none; display: inline-block; margin-top: 15px; }
    .linkedin-link { background-color: #0077b5; color: white !important; padding: 10px; border-radius: 5px; text-decoration: none; display: block; text-align: center; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# البيانات كاملة كما وردت في جدولك (image_9.png)
events = [
    {"name": "هاكثون بلاك هات", "org": "الاتحاد السعودي", "major": "أمن سيبراني", "date": "ديسمبر 2026", "link": "https://blackhatsaudi.com", "loc": "الرياض"},
    {"name": "معسكرات طويق", "org": "أكاديمية طويق", "major": "ذكاء اصطناعي", "date": "متاح الآن", "link": "https://tuwaiq.edu.sa", "loc": "الرياض"},
    {"name": "هاكثون البيانات", "org": "الهيئة العامة للإحصاء", "major": "علوم بيانات", "date": "متاح الآن", "link": "https://www.gastat.gov.sa", "loc": "الرياض"},
    {"name": "معسكر الابتكار", "org": "مبادرات الابتكار", "major": "ابتكار وتقنية", "date": "مايو 2026", "link": "https://3502354586459", "loc": "عام"},
    {"name": "هاكثون الصناعة", "org": "صندوق التنمية الصناعية", "major": "هندسة وتقنية", "date": "قريباً 2026", "link": "https://www.sidf.gov.sa", "loc": "الرياض"},
    {"name": "برنامج نخب", "org": "صندوق التنمية الصناعية", "major": "هندسة", "date": "متاح الآن", "link": "https://www.sidf.gov.sa", "loc": "عام"},
    {"name": "هاكثون سطام", "org": "جامعة سطام", "major": "الكل", "date": "مايو 2026", "link": "https://psau.edu.sa", "loc": "سطام"},
    {"name": "هاكثون الحج", "org": "مركز الدراسات والبحوث", "major": "تقنية وخدمات", "date": "أغسطس 2026", "link": "https://hajhackathon.sa", "loc": "جدة"},
    {"name": "هاكثون نيوم", "org": "شركة نيوم", "major": "استدامة وتقنية", "date": "أكتوبر 2026", "link": "https://www.neom.com", "loc": "نيوم"},
    {"name": "هاكثون الدرعية", "org": "هيئة تطوير الدرعية", "major": "تراث وتقنية", "date": "سبتمبر 2026", "link": "https://dgda.gov.sa", "loc": "الدرعية"},
    {"name": "هاكثون سيسكو العالمي", "org": "Cisco", "major": "شبكات وأمن", "date": "متاح الآن", "link": "https://www.cisco.com", "loc": "عن بعد"}
]

col_side, col_main = st.columns([1, 3])

with col_side:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### 🔍 تصفية سريعة")
    st.selectbox("حسب التخصص:", ["الكل"] + list(set(e['major'] for e in events)))
    st.selectbox("حسب المدينة:", ["الكل"] + list(set(e['loc'] for e in events)))
    st.markdown("---")
    st.markdown(f"**تطوير:**\n\nريماس الدوسري")
    st.markdown('<a href="https://www.linkedin.com/in/rimas-aldosari" class="linkedin-link">LinkedIn Profile 🔗</a>', unsafe_allow_html=True)

with col_main:
    st.markdown('<h1 style="color: #58a6ff; text-align: center;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)
    
    for ev in events:
        st.markdown(f"""
        <div class="event-card">
            <div class="status-badge">✅ متاح</div>
            <div class="card-header">{ev['name']}</div>
            <div class="info-row">
                📍 {ev['loc']} | 🏢 {ev['org']} | 🎯 {ev['major']} | 📅 {ev['date']}
            </div>
            <div class="details-box">
                <b>🔗 رابط التقديم:</b> {ev['link']}
            </div>
            <a href="{ev['link']}" class="reg-button">🔗 سجل الآن</a>
        </div>
        """, unsafe_allow_html=True)
