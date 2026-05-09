import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="بوصلة ريماس للابتكار", layout="wide")

# CSS مطابق تماماً لصورتك (image_8.png) مع تحسينات للوضوح
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; font-family: 'Tajawal', sans-serif; }
    .event-card {
        background-color: #ffffff; border-radius: 15px; padding: 25px;
        margin-bottom: 20px; color: #000000; border-left: 10px solid #1e3a8a;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .status-badge { background-color: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 8px; font-weight: bold; float: right; }
    .expired-badge { background-color: #fee2e2; color: #991b1b; padding: 5px 12px; border-radius: 8px; font-weight: bold; float: right; }
    .card-header { color: #1e3a8a; font-size: 24px; font-weight: bold; margin-bottom: 10px; text-align: left; }
    .details-box { background-color: #f3f4f6; padding: 15px; border-radius: 10px; color: #374151; text-align: right; margin-top: 10px; }
    .reg-button { background-color: #1e3a8a; color: white !important; padding: 8px 25px; border-radius: 8px; text-decoration: none; display: inline-block; margin-top: 15px; }
    .linkedin-link { background-color: #0077b5; color: white !important; padding: 10px; border-radius: 5px; text-decoration: none; display: block; text-align: center; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- الربط مع جدول بيانات Google Sheets (image_9.png) ---
# ملاحظة: استبدلي الرابط التالي برابط ملفك الحقيقي بعد تفعيل المشاركة
SHEET_URL = "https://docs.google.com/spreadsheets/d/your_sheet_id/export?format=csv"

@st.cache_data(ttl=600) # تحديث البيانات كل 10 دقائق تلقائياً
def load_data():
    try:
        # قراءة البيانات مباشرة من جدولك
        return pd.read_csv(SHEET_URL)
    except:
        # بيانات احتياطية في حال تعذر الاتصال بالجدول
        return pd.DataFrame([
            {"الاسم": "هاكثون بلاك هات", "الحالة": "متاح", "الموقع": "الرياض", "التخصص": "أمن سيبراني", "الرابط": "https://blackhatsaudi.com", "الوصف": "أكبر فعالية تقنية في المنطقة لمواجهة تحديات الأمن السيبراني."},
            {"الاسم": "معسكرات طويق", "الحالة": "متاح", "الموقع": "الرياض", "التخصص": "ذكاء اصطناعي", "الرابط": "https://tuwaiq.edu.sa", "الوصف": "معسكرات احترافية مكثفة لتأهيل الكوادر الوطنية."},
            {"الاسم": "هاكثون الدرعية", "الحالة": "متاح", "الموقع": "الدرعية", "التخصص": "تراث وتقنية", "الرابط": "https://dgda.gov.sa", "الوصف": "ابتكار حلول تقنية تجمع بين العراقة والتكنولوجيا الحديثة."},
            {"الاسم": "هاكثون الابتكار الرقمي", "الحالة": "منتهي", "الموقع": "الخرج", "التخصص": "الكل", "الرابط": "https://psau.edu.sa", "الوصف": "الهاكثون الذي شاركتِ فيه بمشروع SattamAI في جامعة سطام."},
            {"الاسم": "معسكر IBM للوكلاء", "الحالة": "منتهي", "الموقع": "عن بعد", "التخصص": "ذكاء اصطناعي", "الرابط": "https://skillsbuild.org", "الوصف": "معسكر Unleashing the Power of AI Agents الذي أتممتِه بنجاح."}
        ])

df = load_data()

# --- التصميم الرئيسي للموقع ---
col_side, col_main = st.columns([1, 4])

with col_side:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("**تطوير:**")
    st.markdown("### ريماس الدوسري")
    st.markdown(f'<a href="https://www.linkedin.com/in/rimas-aldosari" class="linkedin-link">LinkedIn Profile 🔗</a>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("💡 **نصيحة:** يتم تحديث هذه البيانات تلقائياً من جدول البيانات الخاص بكِ.")

with col_main:
    st.markdown('<h1 style="color: #58a6ff; text-align: center;">🚀 بوصلة الهاكثونات والمعسكرات</h1>', unsafe_allow_html=True)
    
    # قسم قيم فكرتك
    with st.expander("💡 أيقونة: قيم فكرتك للهاكثون"):
        st.markdown("### 📊 محلل الابتكار الشخصي")
        idea_name = st.text_input("ما هي فكرتك الجديدة؟")
        target_h = st.selectbox("اختر الهاكثون المستهدف:", df['الاسم'].unique())
        if st.button("تحليل الفكرة"):
            st.balloons()
            st.success(f"فكرة '{idea_name}' ممتازة ومناسبة جداً لـ {target_h}! تذكري استخدام مهاراتك في UI/UX لتبرز الفكرة.")

    # عرض الفعاليات (المتاحة ثم المنتهية)
    st.markdown("---")
    
    # فرز البيانات لعرض المتاح أولاً
    df_sorted = df.sort_values(by="الحالة", ascending=False)
    
    for _, row in df_sorted.iterrows():
        is_expired = row['الحالة'] == "منتهي"
        status_class = "expired-badge" if is_expired else "status-badge"
        status_text = "🚫 انتهى التقديم" if is_expired else "✅ متاح للتسجيل"
        
        st.markdown(f"""
        <div class="event-card">
            <div class="{status_class}">{status_text}</div>
            <div class="card-header">{row['الاسم']}</div>
            <div style="color: #4b5563; margin-bottom: 10px;">
                📍 {row['الموقع']} | 🎯 {row['التخصص']}
            </div>
            <div class="details-box">
                <b>📝 الوصف:</b> {row['الوصف']}
            </div>
            {f'<a href="{row["الرابط"]}" target="_blank" class="reg-button">🔗 سجل الآن</a>' if not is_expired else ""}
        </div>
        """, unsafe_allow_html=True)
