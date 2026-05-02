from flask import Flask

app = Flask(__name__)

# الاستايل العام - قمة الفخامة والتنظيم
COMMON_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Reem+Kufi:wght@500;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

    :root {
        --primary: #00f2ff;
        --dark-bg: #020617;
        --card-bg: rgba(15, 23, 42, 0.85);
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
   
    /* نيفبار احترافي مقسم */
    nav {
        position: fixed;
        top: 0; left: 0; width: 100%;
        background: rgba(2, 6, 23, 0.95);
        backdrop-filter: blur(20px);
        padding: 15px 8%;
        display: flex;
        justify-content: space-between; /* هذا يفصل الاسم عن الروابط */
        align-items: center;
        z-index: 1000;
        border-bottom: 1px solid rgba(0, 242, 255, 0.1);
    }

    .logo {
        font-family: 'Reem Kufi', sans-serif;
        font-size: 28px;
        color: var(--primary);
        text-decoration: none;
        font-weight: 700;
        text-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
        letter-spacing: 1px;
    }

    .nav-links {
        display: flex;
        gap: 25px;
    }

    .nav-links a {
        color: #cbd5e1;
        text-decoration: none;
        font-weight: 700;
        transition: 0.3s ease;
        font-size: 16px;
        position: relative;
    }

    .nav-links a::after {
        content: '';
        position: absolute;
        width: 0; height: 2px;
        bottom: -5px; right: 0;
        background-color: var(--primary);
        transition: 0.3s;
    }

    .nav-links a:hover { color: var(--primary); }
    .nav-links a:hover::after { width: 100%; }

    .page-wrapper {
        padding-top: 120px;
        flex: 1;
        z-index: 1;
    }

    .section-hero {
        padding: 40px 20px;
        text-align: center;
    }

    .section-hero h1 {
        font-size: clamp(2.8rem, 8vw, 4.8rem);
        font-weight: 900;
        margin-bottom: 15px;
        background: linear-gradient(to bottom, #fff, var(--primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .card-container {
        padding: 30px 8%;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
    }

    .card {
        background: var(--card-bg);
        padding: 40px 30px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-align: center;
    }

    .card:hover {
        transform: translateY(-12px);
        border-color: var(--primary);
        box-shadow: 0 15px 35px rgba(0, 242, 255, 0.2);
    }

    .card .icon-box {
        font-size: 3rem;
        margin-bottom: 20px;
        display: inline-block;
    }

    .contact-list {
        max-width: 550px;
        margin: 40px auto;
        padding: 0 20px 100px;
    }

    .contact-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 30px;
        background: var(--card-bg);
        margin-bottom: 20px;
        border-radius: 18px;
        text-decoration: none;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        border: 1px solid rgba(255,255,255,0.05);
        transition: 0.3s;
    }

    .contact-item i { font-size: 1.6rem; }
    .contact-item span { display: flex; align-items: center; gap: 10px; }

    footer {
        padding: 40px;
        background: rgba(1, 4, 9, 0.95);
        text-align: center;
        border-top: 1px solid rgba(255,255,255,0.05);
        color: var(--text-gray);
        font-weight: bold;
    }

    #matrix-canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 0;
        opacity: 0.15;
    }

    @media (max-width: 768px) {
        nav { flex-direction: column; padding: 15px; gap: 15px; text-align: center; }
        .nav-links { gap: 15px; }
        .page-wrapper { padding-top: 160px; }
    }
</style>
"""

MATRIX_SCRIPT = """
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
    function draw() {
        ctx.fillStyle = 'rgba(2, 6, 23, 0.1)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#00f2ff';
        ctx.font = fontSize + 'px monospace';
        for (let i = 0; i < drops.length; i++) {
            const text = letters.charAt(Math.floor(Math.random() * letters.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 45);
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
</script>
"""

NAVBAR = """
<nav>
    <a href="/" class="logo">ASSEM HAMID</a>
    <div class="nav-links">
        <a href="/">الرئيسية</a>
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
                    <div class="icon-box">🚀</div>
                    <h2 style="color: var(--primary); margin-bottom: 15px;">سرعة الأداء</h2>
                    <p>تطوير معالجات بيانات لحظية تضمن استجابة النظام بأقل من أجزاء من الثانية.</p>
                </div>
                <div class="card">
                    <div class="icon-box">🛡️</div>
                    <h2 style="color: var(--primary); margin-bottom: 15px;">حصانة سيبرانية</h2>
                    <p>تأمين شامل للبيانات ضد كافة أنواع التهديدات باستخدام بروتوكولات تشفير عالمية.</p>
                </div>
                <div class="card">
                    <div class="icon-box">💎</div>
                    <h2 style="color: var(--primary); margin-bottom: 15px;">واجهات ذكية</h2>
                    <p>تجربة مستخدم انسيابية تتكيف مع كافة الأجهزة اللوحية والذكية بدقة متناهية.</p>
                </div>
                <div class="card">
                    <div class="icon-box">🧠</div>
                    <h2 style="color: var(--primary); margin-bottom: 15px;">ذكاء برمجي</h2>
                    <p>بناء معماريات برمجية متطورة تتعلم وتتطور لتلبية احتياجات المستقبل الرقمي.</p>
                </div>
            </div>
        </div>
        {FOOTER}
        {MATRIX_SCRIPT}
    </body>
    </html>
    """

@app.route('/about')
def about():
    return f"""
    <html>
    <head><title>من أنا | عاصم حميد</title><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        <canvas id="matrix-canvas"></canvas>
        {NAVBAR}
        <div class="page-wrapper">
            <section class="section-hero">
                <h1>رؤية مهندس</h1>
                <p style="color: var(--primary);">التطور التقني العربي هو المستقبل العالمي</p>
            </section>
            <div style="padding: 0 10%;">
                <div class="card" style="max-width: 800px; margin: auto;">
                    <div class="icon-box">👔</div>
                    <h2 style="color: var(--primary); margin-bottom: 20px;"> الاحترافية التقنية</h2>
                    <p>أنا مبرمج متخصص في لغة Python، أركز على بناء أنظمة خلفية (Backend) قوية ومستقرة.</p>
                    <p style="margin-top:15px;">هدفي هو تحويل الرؤى الطموحة إلى واقع رقمي ملموس يتسم بالسرعة والأمان المطلق.</p>
                </div>
            </div>
        </div>
        {FOOTER}
        {MATRIX_SCRIPT}
    </body>
    </html>
    """

@app.route('/contact')
def contact():
    return f"""
    <html>
    <head><title>تواصل معي | عاصم حميد</title><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        <canvas id="matrix-canvas"></canvas>
        {NAVBAR}
        <div class="page-wrapper">
            <section class="section-hero">
                <h1>قنوات التواصل الرسمية</h1>
                <p style="color: var(--primary);">نحن هنا للاستماع إلى تطلعاتكم التقنية</p>
            </section>
            <div class="contact-list">
                <a href="https://wa.me/967783747282" class="contact-item" style="border-right: 5px solid #25d366;">
                    <span>✅ واتساب (WhatsApp)</span>
                    <i class="fab fa-whatsapp" style="color: #25d366;"></i>
                </a>
                <a href="tel:+967783787282" class="contact-item" style="border-right: 5px solid #3b82f6;">
                    <span>📞 اتصال هاتفي (Call)</span>
                    <i class="fas fa-phone-alt" style="color: #3b82f6;"></i>
                </a>
                <a href="mailto:aasssseemm5@gmail.com" class="contact-item" style="border-right: 5px solid #ea4335;">
                    <span>✉️ بريد إلكتروني (Email)</span>
                    <i class="fas fa-envelope" style="color: #ea4335;"></i>
                </a>
            </div>
        </div>
        {FOOTER}
        {MATRIX_SCRIPT}
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)