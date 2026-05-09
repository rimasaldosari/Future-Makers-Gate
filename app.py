import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

# 3. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #f8fafc; }
    
    .hack-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #1e3a8a;
        position: relative;
    }
    
    /* أوسمة الحالة */
    .status-available { background-color: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 8px; font-weight: bold; font-size: 14px; float: left; }
    .status-expired { background-color: #fee2e2; color: #991b1b; padding: 5px 12px; border-radius: 8px; font-weight: bold; font-size: 14px; float: left; }
    
    .info-line { font-size: 16px; margin: 8px 0; color: #1e293b; }
    .info-label { color: #1e3a8a; font-weight: bold; }
    
    .description-box {
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #0f172a;
        margin-top: 15px;
        border-right: 4px solid #94a3b8;
    }
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

st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 5. قسم "قيم فكرتك"
with st.expander("💡 أيقونة: قيم فكرتك للهاكثون"):
    st.markdown("<h3 style='color:#1e3a8a;'>📊 محلل الابتكار الشخصي</h3>", unsafe_allow_html=True)
    user_idea = st.text_input("ما هي فكرتك الجديدة؟", placeholder="اكتبي فكرتك هنا...")
    if df is not None:
        target_h = st.selectbox("اختر الهاكثون المستهدف لفكرتك:", df['Name'].unique())
        if st.button("تحليل الفكرة"):
            if user_idea:
                st.balloons()
                st.success(f"فكرة '{user_idea}' رائعة ومناسبة لـ {target_h}! مهاراتك يا ريماس في UI/UX ستجعلها مميزة.")

# 6. القائمة الجانبية
with st.sidebar:
    st.markdown("<div style='text-align:center;'><b>تطوير المهندسة:</b><br>ريماس الدوسري</div>", unsafe_allow_html=True)
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/rimas-aldosari-656a23375")
    st.markdown("---")
    if df is not None:
        sel_loc = st.selectbox("📍 ابحث حسب المدينة:", ["الكل"] + sorted(df['Location'].dropna().unique().tolist()))
        sel_major = st.selectbox("🎯 ابحث حسب التخصص:", ["الكل"] + sorted(df['major'].dropna().unique().tolist()))

# 7. عرض النتائج
if df is not None:
    # ترتيب البيانات ليظهر "متاح" أولاً
    filt_df = df.copy()
    if sel_loc != "الكل": filt_df = filt_df[filt_df['Location'] == sel_loc]
    if sel_major != "الكل": filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        # تحديد الحالة بناءً على التاريخ أو النص
        status = str(row.get('Data', '')).strip()
        is_expired = "2026" not in status and "متاح" not in status and "قريبا" not in status # معيار بسيط للتوضيح
        
        # يمكنك جعلها أدق لو أضفتِ عمود "الحالة" في الجدول
        status_class = "status-expired" if "منتهي" in status else "status-available"
        status_text = "🚫 انتهى" if "منتهي" in status else "✅ متاح"

        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <div class="{status_class}">{status_text}</div>
                <h2 style='color: #1e40af; margin-top:0;'>{row.get('Name', 'نشاط تقني')}</h2>
                <div class="info-line"><span class="info-label">📍 المدينة:</span> {row.get('Location', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🏢 الجهة:</span> {row.get('Organizaion', 'غير محدد')}</div>
                <div class="info-line"><span class="info-label">🎯 التخصص:</span> {row.get('major', 'عام')}</div>
                <div class="info-line"><span class="info-label">📅 التاريخ:</span> {row.get('Data', 'قريباً')}</div>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b><br>{row.get('Description', 'لا يوجد وصف حالياً.')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            link = str(row.get('Link', '')).strip()
            if link and link != 'nan' and "منتهي" not in status:
                actual_link = link if link.startswith('http') else f"https://{link}"
                st.link_button(f"🔗 سجل الآن في {row.get('Name')}", actual_link)
            st.markdown("<br>", unsafe_allow_html=True)
