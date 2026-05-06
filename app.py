import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="بوصلة الهاكثونات | ريماس الدوسري", page_icon="🚀", layout="wide")

# 2. رابط جدول البيانات
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?output=csv"

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
    }
    .info-line { font-size: 16px; margin: 5px 0; color: #475569; }
    .info-label { color: #1e3a8a; font-weight: bold; }
    .description-box {
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #334155;
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

@st.cache_data(ttl=5) # تحديث سريع جداً للتجربة
def load_data():
    try:
        # قراءة البيانات مع معالجة المسافات في الأعمدة والصفوف
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        # تنظيف كل النصوص في الجدول من المسافات الزائدة
        data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        return data
    except:
        return None

df = load_data()

# 4. العنوان الرئيسي والقائمة الجانبية
st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🔍 تصفية</h2>", unsafe_allow_html=True)
    if df is not None:
        majors = ["الكل"] + sorted(df['major'].dropna().unique().tolist())
        sel_major = st.selectbox("حسب التخصص:", majors)
    st.markdown("---")
    st.write("تطوير المهندسة: ريماس الدوسري")

# 5. عرض البطاقات
if df is not None:
    filt_df = df.copy()
    if sel_major != "الكل":
        filt_df = filt_df[filt_df['major'] == sel_major]

    for _, row in filt_df.iterrows():
        # استخدام دالة get للتأكد من قراءة القيمة حتى لو كان هناك خطأ في الاسم
        name = row.get('Name', 'نشاط تقني')
        org = row.get('Organizaion', 'غير محدد')
        loc = row.get('Location', 'عام')
        major = row.get('major', 'تقني')
        date = row.get('Data', 'قريباً')
        desc = row.get('Description', 'لا يوجد وصف حالياً.')
        link = str(row.get('Link', '')).strip()

        # تجاوز الصفوف الفارغة تماماً
        if pd.isna(name) or name == '':
            continue

        with st.container():
            st.markdown(f"""
            <div class="hack-card">
                <h2 style='color: #1e40af; margin-top:0;'>{name}</h2>
                <div class="info-line"><span class="info-label">📍 المدينة:</span> {loc}</div>
                <div class="info-line"><span class="info-label">🏢 الجهة:</span> {org}</div>
                <div class="info-line"><span class="info-label">🎯 التخصص:</span> {major}</div>
                <div class="info-line"><span class="info-label">📅 التاريخ:</span> {date}</div>
                <div class="description-box">
                    📝 <b>عن الفرصة:</b><br>{desc}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # معالجة الرابط وظهوره كزر
            if link and link != 'nan' and len(link) > 5:
                actual_link = link if link.startswith('http') else f"https://{link}"
                st.link_button(f"🔗 سجل الآن في {name}", actual_link)
            else:
                st.info("ℹ️ رابط التسجيل سيتم تحديثه قريباً")
            
            st.markdown("<br>", unsafe_allow_html=True)
else:
    st.error("تأكدي من أن الجدول منشور على الويب بصيغة CSV")
