import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات المباشر
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?output=csv"

# 3. رابط لينكد إن المباشر (الأكثر ضماناً)
LINKEDIN_PROFILE_URL = "https://www.linkedin.com/in/rimas-aldosari-656a23375"

# 4. تصميم الواجهة (CSS) المحدث للألوان ووضوح النص
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
    }
    .info-line { font-size: 16px; margin: 8px 0; color: #1f2937; } /* لون داكن للنص */
    .info-label { color: #1d4ed8; font-weight: bold; } /* لون أزرق جذاب للتسميات */
    .description-box {
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #374151; /* لون داكن للوصف */
        margin-top: 15px;
        border-right: 4px solid #94a3b8;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #1e3a8a !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# دالة تحميل البيانات مع معالجة الأخطاء
@st.cache_data(ttl=5)
def load_data():
    try:
        # قراءة البيانات مع الترميز وتنظيف أسماء الأعمدة
        data = pd.read_csv(SHEET_URL, on_bad_lines='skip')
        data.columns = data.columns.str.strip()
        # تنظيف البيانات داخل الخلايا أيضاً
        data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        return data
    except Exception as e:
        st.error(f"حدث خطأ في تحميل البيانات: {e}")
        return None

df = load_data()

# 5. العنوان الرئيسي
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

# 6. القائمة الجانبية (البحث والفلترة)
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🔍 خيارات البحث</h2>", unsafe_allow_html=True)
    
    sel_major = "الكل"
    sel_loc = "الكل"
    
    if df is not None:
        # التخصص أولاً
        if 'major' in df.columns:
            all_majors = ["الكل"] + sorted(df['major'].dropna().unique().tolist())
            sel_major = st.selectbox("🎯 ابحث حسب التخصص:", all_majors)
        
        # المدينة ثانياً (تحت التخصص)
        if 'Location' in df.columns:
            all_locations = ["الكل"] + sorted(df['Location'].dropna().unique().tolist())
            sel_loc = st.selectbox("📍 ابحث حسب المدينة:", all_locations)
    
    st.markdown("---")
    st.markdown("<div style='text-align:center;'><b>تطوير:</b><br>ريماس الدوسري</div>", unsafe_allow_html=True)
    
    # الزر باستخدام الرابط المباشر
    st.link_button("🔗 LinkedIn Profile", LINKEDIN_PROFILE_URL)

# 7. عرض النتائج ومعالجة الفلاتر
if df is not None:
    filt_df = df.copy()
    if sel_major != "الكل":
        filt_df = filt_df[filt_df['major'] == sel_major]
    if sel_loc != "الكل":
        filt_df = filt_df[filt_df['Location'] == sel_loc]

    if filt_df.empty:
        st.warning("لا توجد نتائج تطابق بحثك حالياً.")
    else:
        for _, row in filt_df.iterrows():
            name = row.get('Name', 'نشاط تقني')
            # التأكد من وجود اسم للنشاط
            if pd.isna(name) or str(name).strip() == '': continue
            
            with st.container():
                st.markdown(f"""
                <div class="hack-card">
                    <h2 style='color: #1e40af; margin-top:0;'>{name}</h2>
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
                if link and link != 'nan' and len(link) > 5:
                    actual_link = link if link.startswith('http') else f"https://{link}"
                    st.link_button(f"🔗 سجل الآن", actual_link)
                st.markdown("<br>", unsafe_allow_html=True)
else:
    st.error("لم يتم العثور على بيانات. تأكدي من أن الجدول متاح للجميع كـ CSV.")
