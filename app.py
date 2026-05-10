import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة - (تم التأكد من صحة السطر لمنع AttributeError)
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات (الرابط المباشر من جدولك)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

# 3. تصميم الواجهة (CSS) - حل مشكلة اللون الأبيض وتنسيق الكروت
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #f0f2f6; }
    
    /* تصميم الكرت */
    .hack-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #1e3a8a;
        color: #1e293b !important;
    }
    
    /* لون العناوين والنصوص لضمان الوضوح */
    .hack-card h2 { color: #1e40af !important; margin-top:0; }
    .info-line { font-size: 16px; margin: 8px 0; color: #1e293b !important; }
    .info-label { color: #1e3a8a !important; font-weight: bold; }
    
    /* صندوق الوصف الرمادي */
    .description-box {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #334155 !important;
        margin-top: 15px;
        border: 1px solid #e2e8f0;
    }
    
    /* وسام الحالة (متاح/منتهي) */
    .badge { padding: 5px 12px; border-radius: 8px; font-weight: bold; font-size: 12px; float: left; }
    .badge-green { background-color: #dcfce7; color: #166534; }
    .badge-red { background-color: #fee2e2; color: #991b1b; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(ttl=5)
def load_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        return data
    except:
        return None

df = load_data()

# العنوان الرئيسي
st.markdown('<h1 style="text-align:center; color:#1e3a8a; margin-bottom:30px;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 4. قسم "قيم فكرتك" - بتصميم واضح جداً
with st.expander("💡 أيقونة: قيم فكرتك للهاكثون"):
    st.markdown("<div style='color:#1e3a8a; font-weight:bold; font-size:20px;'>📊 محلل الابتكار الشخصي</div>", unsafe_allow_html=True)
    idea = st.text_input("ما هي فكرتك الجديدة؟", key="idea_input")
    if df is not None:
        target = st.selectbox("اختر الهاكثون المستهدف:", df['Name'].unique())
        if st.button("تحليل الفكرة"):
            if idea:
                st.balloons()
                st.success(f"فكرة '{idea}' رهيبة يا ريماس! الهاكثون {target} ينتظرك.")

# 5. القائمة الجانبية
with st.sidebar:
    st.markdown("<div style='text-align:center; color:white; background:#1e3a8a; padding:10px; border-radius:10px;'><b>تطوير المهندسة:</b><br>ريماس الدوسري</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("🔗 حسابي على LinkedIn", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 حسب المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 حسب التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 6. عرض النتائج
if df is not None:
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        # فحص الحالة
        status_val = str(row.get('Data', ''))
        is_expired = "منتهي" in status_val
        badge_class = "badge-red" if is_expired else "badge-green"
        badge_text = "🚫 انتهى" if is_expired else "✅ متاح"
        
        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <div class="badge {badge_class}">{badge_text}</div>
                <h2>{row.get('Name', 'نشاط تقني')}</h2>
                <div class="info-line"><span class="info-label">📍 المدينة:</span> {row.get('Location', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🎯 التخصص:</span> {row.get('major', 'عام')}</div>
                <div class="info-line"><span class="info-label">📅 التاريخ:</span> {row.get('Data', 'قريباً')}</div>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b><br>{row.get('Description', 'تحدي تقني مميز ينتظر المبدعين.')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # عرض زر التسجيل فقط إذا لم تكن منتهية وكان الرابط موجوداً
            link = str(row.get('Link', '')).strip()
            if link and link != 'nan' and not is_expired:
                actual_link = link if link.startswith('http') else f"https://{link}"
                st.link_button(f"🔗 سجل الآن في {row.get('Name')}", actual_link)
            elif is_expired:
                st.button("تم إغلاق التسجيل", disabled=True)
            st.markdown("<br>", unsafe_allow_html=True)
