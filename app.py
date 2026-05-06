import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="منصة هاكثونات ومعسكرات المستقبل",
    page_icon="🚀",
    layout="wide"
)

# 2. تصميم الواجهة (CSS) لدعم اللغة العربية وتجميل الشكل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        margin-bottom: 15px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. رابط جدول بياناتك (CSV)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQG6e9dLydAAngT_ZzYXW2khBDqFVhWEzR_-eufO3jaFB2XYBudVWns9gxYkTmad1pE9-0QVQw8ZCw0/pub?output=csv"

# 4. دالة جلب البيانات
@st.cache_data(ttl=60) # يحدث البيانات كل دقيقة إذا تم تغيير الجدول
def get_data():
    return pd.read_csv(SHEET_URL)

try:
    df = get_data()

    # 5. واجهة الموقع
    st.title("🚀 بوصلة الهاكثونات والمعسكرات التقنية")
    st.write("دليلك الشامل لأحدث الفرص في المملكة وجامعة سطام.")

    # 6. قسم الفلترة في القائمة الجانبية
    st.sidebar.header("🔍 فلاتر البحث")
    
    # فلتر التخصص
    all_majors = ["الكل"] + sorted(df['major'].unique().tolist())
    selected_major = st.sidebar.selectbox("اختر التخصص:", all_majors)

    # فلتر الموقع
    all_locations = ["الكل"] + sorted(df['Location'].unique().tolist())
    selected_location = st.sidebar.selectbox("المنطقة أو الجامعة:", all_locations)

    # تطبيق الفلترة
    filtered_df = df.copy()
    if selected_major != "الكل":
        filtered_df = filtered_df[filtered_df['major'] == selected_major]
    if selected_location != "الكل":
        filtered_df = filtered_df[filtered_df['Location'] == selected_location]

    # 7. عرض النتائج
    st.subheader(f"الفرص المتاحة ({len(filtered_df)})")

    for index, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="card">
                <h3 style="color: #007bff; margin-bottom: 10px;">{row['Name']}</h3>
                <p>🏢 <b>الجهة:</b> {row['Organizaion']}</p>
                <p>🎯 <b>التخصص:</b> {row['major']}</p>
                <p>📅 <b>التاريخ:</b> {row['Data']}</p>
                <p>📍 <b>الموقع:</b> {row['Location']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # زر الرابط
            st.link_button(f"🔗 تفاصيل التسجيل في {row['Name']}", str(row['Link']))
            st.write("") # مسافة بسيطة

except Exception as e:
    st.error("جاري تجهيز البيانات... تأكد من نشر جدول البيانات كـ CSV")
