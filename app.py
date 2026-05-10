import streamlit as st
import pandas as pd
import random

# =========================================
# 1. إعدادات الصفحة المتقدمة
# =========================================
st.set_page_config(
    page_title="بوصلة الهاكثونات | ريماس الدوسري",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# 2. CSS الاحترافي (إخفاء الأدوات + تحسين الألوان + إخفاء السفلي)
# =========================================
st.markdown("""
<style>
    /* إخفاء شريط الحساب العلوي والسفلي تماماً */
    #MainMenu, header, footer { visibility: hidden; }
    [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stStatusWidget"] { display: none !important; }
    .stDeployButton { display:none !important; }

    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .stApp { background-color: #f0f4f8; }

    /* تحسين الإحصائيات */
    .stats-card {
        background: white; padding: 25px; border-radius: 20px; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-bottom: 5px solid #1e3a8a;
        transition: transform 0.3s ease;
    }
    .stats-card:hover { transform: translateY(-5px); }
    .stats-card h2 { color: #1e3a8a !important; font-size: 35px; margin: 0; }
    .stats-card p { color: #64748b !important; font-weight: 600; margin-top: 5px; }

    /* صناديق الأدوات الذكية */
    .ai-card {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        padding: 20px; border-radius: 15px; border-right: 6px solid #3b82f6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin: 10px 0;
    }
    .ai-card h3 { color: #1e3a8a !important; font-size: 20px; }

    /* كروت الهاكثونات المطورة */
    .hack-item {
        background: white; padding: 30px; border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06); margin-bottom: 25px;
        border-right: 10px solid #1e3a8a; position: relative;
    }
    .hack-item h2 { color: #0f172a !important; margin-bottom: 15px; font-weight: 700; }
    
    .info-tag {
        display: inline-block; background: #e2e8f0; color: #1e293b;
        padding: 4px 12px; border-radius: 6px; font-size: 14px; margin-left: 8px;
        margin-bottom: 10px; font-weight: 600;
    }

    .desc-area {
        background: #f8fafc; padding: 18px; border-radius: 12px;
        border: 1px solid #e2e8f0; color: #334155 !important; line-height: 1.6;
    }

    .status-badge-active {
        background-color: #dcfce7; color: #15803d; padding: 6px 15px;
        border-radius: 50px; font-weight: bold; font-size: 13px;
        position: absolute; left: 20px; top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# =========================================
# 3. جلب ومعالجة البيانات
# =========================================
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRoHDmJwadCVmFXscpcFpsa4KAmxtjp6z-Ch5tOerG-5ztT6ysJho-RPfvBpX5QzMLnoDXfisRGYHuA/pub?gid=0&single=true&output=csv"

@st.cache_data(ttl=10)
def get_data():
    try:
        data = pd.read_csv(SHEET_URL)
        data.columns = data.columns.str.strip()
        # تنظيف البيانات من القيم المفقودة لنصوص افتراضية
        data = data.fillna("غير محدد")
        return data
    except:
        return None

df = get_data()

# =========================================
# 4. واجهة المستخدم (UI)
# =========================================
st.markdown('<h1 style="text-align:center; color:#1e3a8a; font-size:45px; margin-bottom:10px;">🚀 بوصلة الهاكثونات</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#64748b; font-size:18px; margin-bottom:40px;">وجهتك الأولى لاكتشاف فرص الابتكار في المملكة</p>', unsafe_allow_html=True)

# شريط البحث
search_query = st.text_input("", placeholder="🔍 ابحثي عن اسم الهاكثون، المدينة، أو الجهة المنظمة...")

if df is not None:
    # قسم الإحصائيات
    s1, s2, s3 = st.columns(3)
    with s1: st.markdown(f'<div class="stats-card"><h2>{len(df)}</h2><p>فرصة تقنية</p></div>', unsafe_allow_html=True)
    with s2: st.markdown(f'<div class="stats-card"><h2>{df["Location"].nunique()}</h2><p>مدينة</p></div>', unsafe_allow_html=True)
    with s3: st.markdown(f'<div class="stats-card"><h2>{df["major"].nunique()}</h2><p>تخصص</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # قسم أدوات الابتكار
    col_ai_1, col_ai_2 = st.columns(2)
    with col_ai_1:
        st.markdown('<div class="ai-card"><h3>💡 مولد الأفكار الذكي</h3><p style="color:#64748b;">هل تبحثين عن إلهام؟ دعي الذكاء الاصطناعي يقترح عليكِ</p></div>', unsafe_allow_html=True)
        if st.button("✨ ولّد فكرة مشروع"):
            st.success(random.choice([
                "منصة AI لتحليل هدر الطعام في المطاعم",
                "تطبيق واقع معزز (AR) للجولات السياحية في الرياض",
                "نظام ذكي للتنبؤ بالأعطال في خطوط الإنتاج",
                "منصة لربط المبدعين السعوديين بالمستثمرين عالمياً"
            ]))
            
    with col_ai_2:
        st.markdown('<div class="ai-card"><h3>👥 مقترح أسماء الفرق</h3><p style="color:#64748b;">اختاري اسماً يعكس قوة فريقك في المنافسة</p></div>', unsafe_allow_html=True)
        if st.button("🎲 اقترح اسم فريق"):
            st.info(random.choice(["Digital Knights", "Vision 2030 Coders", "Saudi Tech Titans", "Infinity Devs"]))

    # القائمة الجانبية
    with st.sidebar:
        st.markdown(f"<h2 style='text-align:center;'>👋 أهلاً ريماس</h2>", unsafe_allow_html=True)
        st.markdown("---")
        st.link_button("💼 حسابي على LinkedIn", "https://www.linkedin.com/in/rimas-aldosari-656a23375", use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.subheader("📍 تصفية حسب")
        loc_filter = st.selectbox("المدينة", ["الكل"] + sorted(df['Location'].unique().tolist()))
        major_filter = st.selectbox("التخصص", ["الكل"] + sorted(df['major'].unique().tolist()))

    # فلترة النتائج
    results = df.copy()
    if search_query:
        results = results[results.astype(str).apply(lambda x: x.str.contains(search_query, case=False).any(), axis=1)]
    if loc_filter != "الكل":
        results = results[results['Location'] == loc_filter]
    if major_filter != "الكل":
        results = results[results['major'] == major_filter]

    st.markdown("---")
    
    # عرض الهاكثونات
    if results.empty:
        st.warning("لا توجد نتائج تطابق بحثك، جربي كلمات أخرى.")
    else:
        for _, row in results.iterrows():
            with st.container():
                st.markdown(f"""
                <div class="hack-item">
                    <div class="status-badge-active">✅ متاح</div>
                    <h2>{row['Name']}</h2>
                    <div>
                        <span class="info-tag">📍 {row['Location']}</span>
                        <span class="info-tag">🏢 {row['Organizaion']}</span>
                        <span class="info-tag">🎯 {row['major']}</span>
                        <span class="info-tag">📅 {row['Data']}</span>
                    </div>
                    <div class="desc-area">
                        <b>وصف الفرصة:</b><br>{row['Description']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # زر التسجيل
                link = str(row['Link']).strip()
                if link != "غير محدد" and len(link) > 5:
                    final_link = link if link.startswith('http') else f"https://{link}"
                    st.link_button(f"🔗 سجل الآن في {row['Name']}", final_link, use_container_width=False)
                st.markdown("<br><br>", unsafe_allow_html=True)
