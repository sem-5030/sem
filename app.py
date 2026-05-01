from flask import Flask

app = Flask(__name__)

# الاستايل العام والفخامة البصرية
COMMON_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Reem+Kufi:wght@500;700&display=swap');

    :root {
        --primary: #00f2ff;
        --dark-bg: #020617;
        --card-bg: rgba(15, 23, 42, 0.8);
        --text-gray: #94a3b8;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
        background-color: var(--dark-bg);
        color: white;
        direction: rtl;
        font-family: 'Cairo', sans-serif;
        overflow-x: hidden;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }

    /* نيفبار زجاجي ثابت */
    nav {
        position: fixed;
        top: 0; left: 0; width: 100%;
        background: rgba(2, 6, 23, 0.9);
        backdrop-filter: blur(15px);
        padding: 20px 8%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 1000;
        border-bottom: 1px solid rgba(0, 242, 255, 0.1);
    }

    .logo {
        font-family: 'Reem Kufi', sans-serif;
        font-size: 26px;
        color: white;
        text-decoration: none;
        text-shadow: 0 0 10px var(--primary);
    }

    .nav-links a {
        color: #cbd5e1;
        text-decoration: none;
        margin-right: 25px;
        font-weight: 700;
        transition: 0.3s;
    }

    .nav-links a:hover { color: var(--primary); }

    /* حاوي المحتوى لضمان عدم التداخل مع النيفبار */
    .page-wrapper {
        padding-top: 120px; /* مسافة لضمان ظهور المحتوى تحت النيفبار */
        flex: 1;
    }

    .section-hero {
        padding: 60px 20px;
        text-align: center;
    }

    .section-hero h1 {
        font-size: 4.5rem;
        font-weight: 900;
        margin-bottom: 20px;
        background: linear-gradient(to bottom, #fff, var(--primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .card-container {
        padding: 50px 8%;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
    }

    .card {
        background: var(--card-bg);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: 0.4s;
        text-align: center;
    }

    .card:hover {
        transform: translateY(-10px);
        border-color: var(--primary);
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.1);
    }

    .contact-list {
        max-width: 600px;
        margin: 50px auto;
        padding-bottom: 100px; /* جعل الصفحة أطول */
    }

    .contact-item {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background: var(--card-bg);
        margin-bottom: 20px;
        border-radius: 15px;
        text-decoration: none;
        color: white;
        font-weight: 700;
        font-size: 1.2rem;
        border: 1px solid rgba(255,255,255,0.05);
        transition: 0.3s;
    }

    .contact-item:hover { background: rgba(0, 242, 255, 0.1); transform: scale(1.02); }

    /* فوتر رسمي وموحد */
    footer {
        padding: 40px;
        background: #010409;
        text-align: center;
        border-top: 1px solid rgba(255,255,255,0.05);
        color: var(--text-gray);
        font-weight: bold;
    }

    /* خلفية الماتريكس (للرئيسية فقط) */
    #matrix-canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: -1;
        opacity: 0.15;
    }
</style>
"""

NAVBAR = """
<nav>
    <a href="/" class="logo">ASSEM Hamid</a>
    <div class="nav-links">
        <a href="/">الصفحة الرئيسية</a>
        <a href="/about">من أنا</a>
        <a href="/contact">تواصل معي</a>
    </div>
</nav>
"""

FOOTER = "<footer>جميع الحقوق محفوظة لدى المبرمج عاصم حميد © 2026</footer>"

@app.route('/')
def index():
    return f"""
    <html>
    <head><title>ASSEM Hamid | الرئيسية</title><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        <canvas id="matrix-canvas"></canvas>
        {NAVBAR}
        <div class="page-wrapper">
            <section class="section-hero">
                <h1>عاصم حميد</h1>
                <p style="font-size: 1.8rem; color: var(--primary);">هندسة الأنظمة البرمجية فائقة الأداء</p>
            </section>
            <div class="card-container">
                <div class="card">
                    <h2 style="color: var(--primary); margin-bottom: 15px;">🚀 سرعة الأداء</h2>
                    <p>تطوير معالجات بيانات لحظية تضمن استجابة النظام بأقل من أجزاء من الثانية.</p>
                </div>
                <div class="card">
                    <h2 style="color: var(--primary); margin-bottom: 15px;">🛡️ حصانة سيبرانية</h2>
                    <p>تأمين شامل للبيانات ضد كافة أنواع التهديدات باستخدام بروتوكولات تشفير عالمية.</p>
                </div>
                <div class="card">
                    <h2 style="color: var(--primary); margin-bottom: 15px;">💎 واجهات ذكية</h2>
                    <p>تجربة مستخدم انسيابية تتكيف مع كافة الأجهزة اللوحية والذكية بدقة متناهية.</p>
                </div>
            </div>
        </div>
        {FOOTER}
        <script>
            const canvas = document.getElementById('matrix-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            const letters = '01';
            const fontSize = 16;
            const columns = canvas.width / fontSize;
            const drops = [];
            for (let i = 0; i < columns; i++) drops[i] = 1;
            function draw() {{
                ctx.fillStyle = 'rgba(2, 6, 23, 0.1)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#00f2ff';
                ctx.font = fontSize + 'px monospace';
                for (let i = 0; i < drops.length; i++) {{
                    const text = letters.charAt(Math.floor(Math.random() * letters.length));
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                    drops[i]++;
                }}
            }}
            setInterval(draw, 33);
        </script>
    </body>
    </html>
    """

@app.route('/about')
def about():
    return f"""
    <html>
    <head><title>من أنا | عاصم حميد</title><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        {NAVBAR}
        <div class="page-wrapper">
            <section class="section-hero">
                <h1>رؤية مهندس</h1>
                <p style="color: var(--primary);">التطور التقني العربي هوا المستقبل العالمي</p>
            </section>
            <div style="padding: 0 10%;">
                <div class="card" style="max-width: 800px; margin: auto;">
                    <h2 style="color: var(--primary); margin-bottom: 20px;"> الاحترافيه التقنيه</h2>
                    <p>أنا مبرمج متخصص في لغة Python، أركز على بناء أنظمة خلفية (Backend) قوية ومستقرة. هدفي هو تحويل الرؤى الطموحة إلى واقع رقمي ملموس يتسم بالسرعة والأمان المطلق.</p>
                </div>
            </div>
        </div>
        {FOOTER}
    </body>
    </html>
    """

@app.route('/contact')
def contact():
    return f"""
    <html>
    <head><title>تواصل معي | عاصم حميد</title><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        {NAVBAR}
        <div class="page-wrapper">
            <section class="section-hero">
                <h1>قنوات التواصل الرسمية</h1>
                <p style="color: var(--primary);">نحن هنا للاستماع إلى تطلعاتكم التقنية</p>
            </section>
            <div class="contact-list">
                <a href="https://wa.me/967783747282" class="contact-item" style="border-right: 5px solid #25d366;">واتساب مباشر (WhatsApp)</a>
                <a href="tel:+967783787282" class="contact-item" style="border-right: 5px solid #3b82f6;">اتصال هاتفي (Call Now)</a>
                <a href="mailto:aasssseemm5@gmail.com" class="contact-item" style="border-right: 5px solid #ea4335;">بريد إلكتروني (Email Me)</a>
            </div>
        </div>
        {FOOTER}
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)