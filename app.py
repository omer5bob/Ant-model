import streamlit as st
from datetime import datetime

# إعدادات الصفحة ودعم الاتجاه من اليمين إلى اليسار (RTL) للعربية
st.set_page_config(
    page_title="ِANTS-WARN | نموذج النمل للإنذار",
    page_icon="🐜",
    layout="wide"
)

# تطبيق تنسيق CSS لدعم اللغة العربية وتنسيق الواجهة
st.markdown("""
    <style>
    body, div, p, span, label, input, select, textarea {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stCheckbox > label {
        direction: rtl !important;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border-right: 5px solid #ff4b4b;
    }
    .active-step {
        background-color: #d4edda;
        color: #155724;
        padding: 8px;
        border-radius: 5px;
        margin: 5px 0;
        border-right: 4px solid #28a745;
    }
    .inactive-step {
        background-color: #e2e3e5;
        color: #383d41;
        padding: 8px;
        border-radius: 5px;
        margin: 5px 0;
        border-right: 4px solid #6c757d;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق
st.title("🐜 نموذج النمل للإنذار ")
st.subheader("مُنشئ ومراجع الرسائل التحذيرية الأمنية")
st.caption("واجهة أولية عربية لإعداد الرسالة، فحص اكتمال عناصرها، وتوليد صياغة موجزة قابلة للمراجعة قبل الإرسال.")

st.divider()

# تقسيم الشاشة إلى عمودين (المدخلات والمخرجات)
col_input, col_preview = st.columns([3, 2])

with col_input:
    st.header("1. بيانات الرسالة")
    st.info("⚠️ أدخل الحد الأدنى الضروري من المعلومات التشغيلية. لا تُدخل بيانات شخصية غير لازمة.")
    
    # حقول إدخال البيانات
    جهة_مصدرة = st.text_input("الجهة المُصدرة", placeholder="مثال: الجهة المختصة")
    مخاطب = st.text_input("المخاطَب / الفئة المستهدفة", placeholder="مثال: جميع السكان في المنطقة")
    خطر = st.text_area("الخطر أو التهديد", placeholder="ما الخطر الذي ينبغي التحذير منه؟")
    مكان = st.text_input("المكان / المنطقة", placeholder="المنطقة أو نطاق الخطر")
    وقت = st.text_input("الوقت / الإطار الزمني", placeholder="الآن / من 20:00 إلى 22:00")
    اجراء = st.text_area("الإجراء المطلوب", placeholder="ماذا يجب على المتلقي أن يفعل الآن؟")
    حماية = st.text_input("مكان الحماية / السلوك الآمن", placeholder="مثال: الدخول إلى مكان آمن بعيداً عن النوافذ")
    سياق = st.text_area("السياق أو التوضيح الذي يمنع الالتباس والهلع", placeholder="معلومة مختصرة ضرورية لتفسير الخطر أو التصرف المطلوب")
    
    col_lang, col_update = st.columns(2)
    with col_lang:
        لغة = st.selectbox("اللغة", ["العربية", "English", "تعدد اللغات (Ar/En)"])
    with col_update:
        تحديث = st.text_input("رسالة انتهاء الخطر / التحديث", placeholder="متى وكيف سيتم إعلان انتهاء الخطر؟")

with col_preview:
    st.header("2. قائمة التحقق")
    st.caption("هذه القائمة تربط النموذج المقترح الأولى بعناصر الرسالة التحذيرية .")
    
    # احتساب نسبة الاكتمال تلقائياً بناءً على الحقول الممتلئة
     عناصر_التحقق = [جهة_مصدرة, مخاطب, خطر, مكان, وقت, اجراء, حماية, سياق]
    عناصر_مكتملة = sum(1 for item in عناصر_التحقق if item.strip() != "")
    نسبة_الاكتمال = int((عناصر_مكتملة / len(عناصر_التحقق)) * 100)
    
    # عرض نسبة الاكتمال
    st.subheader("اكتمال العناصر")
    st.progress(نسبة_الاكتمال / 100)
    if نسبة_الاكتمال == 100:
        st.success(f"مكتملة تماماً 🎉 ({نسبة_الاكتمال}%)")
    elif نسبة_الاكتمال > 0:
        st.warning(f"جاري الإعداد... ({نسبة_الاكتمال}%)")
    else:
        st.error(f"غير مكتملة ({نسبة_الاكتمال}%)")
        
    st.divider()
    
    # سلسلة تدفق نموذج النملة
    st.subheader("🔗 سلسلة النموذج")
    
    def get_step_style(val, title, prefix):
        if val.strip() != "":
            return f'<div class="active-step">✅ <b>{prefix}:</b> {title} (مكتمل)</div>'
        return f'<div class="inactive-step">❌ <b>{prefix}:</b> {title} (مطلوب)</div>'

    st.markdown(get_step_style(مخاطب, "المخاطَب", "من؟"), unsafe_allow_html=True)
    st.markdown(get_step_style(خطر, "الخطر", "ما الذي يحدث؟"), unsafe_allow_html=True)
    st.markdown(get_step_style(جهة_مصدرة, "المصدر", "من الجهة؟"), unsafe_allow_html=True)
    st.markdown(get_step_style(اجراء, "الفعل", "ماذا يفعل؟"), unsafe_allow_html=True)
    st.markdown(get_step_style(حماية, "الحماية", "أين يحتمي؟"), unsafe_allow_html=True)
    st.markdown(get_step_style(وقت, "الوقت", "متى؟"), unsafe_allow_html=True)
    st.markdown(get_step_style(سياق, "السياق", "لماذا / ما التوضيح؟"), unsafe_allow_html=True)
    st.markdown(get_step_style(تحديث, "التحديث", "متى ينتهي؟"), unsafe_allow_html=True)

    st.divider()

    # النص المقترح والإنشاء الآلي
    st.subheader("📄 النص المقترح المعاين")
    if عناصر_مكتملة > 0:
        نص_الرسالة = f"🚨 تحذير أمني عاجل من [{جهة_مصدرة if جهة_مصدرة else '...'}]\n"
        نص_الرسالة += f"إلى: [{مخاطب if مخاطب else '...'}]\n"
        نص_الرسالة += f"التهديد: {خطر if خطر else '...'}\n"
        نص_الرسالة += f"النطاق: {مكان if مكان else '...'}\n"
        نص_الرسالة += f"التوقيت: {وقت if وقت else '...'}\n"
        نص_الرسالة += f"الإجراء الفوري: {اجراء if اجراء else '...'}\n"
        نص_الرسالة += f"التوجيه الأمن: {حماية if حماية else '...'}\n"
        نص_الرسالة += f"ملاحظة: {سياق if سياق else '...'}\n"
        نص_الرسالة += f"التحديث القادم: {تحديث if تحديث else '...'}"
        
        st.text_area("معاينة البث البصري:", نص_الرسالة, height=200)
    else:
        st.info("أدخل البيانات الأساسية في اليمين لتوليد معاينة تلقائية للرسالة.")

    # أزرار التحكم التشغيلية
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        if st.button("📋 نسخ النص", use_container_width=True):
            st.toast("تم نسخ النص إلى الحافظة (محاكاة)")
    with col_b2:
        st.button("🖨️ حفظ PDF", use_container_width=True)
    with col_b3:
        if st.button("🗑️ مسح", use_container_width=True):
            st.rerun()

    st.divider()
    
    # سجل المراجعة السفلي
    st.subheader("📋 سجل المراجعة")
    st.text("حالة: مسودة")
    وقت_الحالي = datetime.now().strftime("%d/%m/%Y، %I:%M:%S %p")
    st.text(f"آخر فحص: {وقت_الحالي}")
    st.caption("🛑 النتيجة إرشادية ولا تُعد اعتماداً أمنياً أو تشغيلياً. لا يتم الإرسال الفعلي من هذه النسخة التجريبية.")
