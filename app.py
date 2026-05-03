from flask import Flask,send_from_direktoryimport os

app = Flask(__name__)

# استايل "السيادة التقنية" - هندسة تفوق التوقعات
COMMON_STYLE = """
<link rel="manifest" href="/manifest.json">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Orbitron:wght@400;900&family=Lexend:wght@300;600&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css');

    :root {
        --primary: #00f2ff;
        --secondary: #bc13fe;
        --bg: #030712;
        --glass-bg: rgba(17, 24, 39, 0.7);
        --border-color: rgba(0, 242, 255, 0.2);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

    body {
        background-color: var(--bg);
        color: #f8fafc;
        direction: rtl;
        font-family: 'Cairo', sans-serif;
        overflow-x: hidden;
        min-height: 100vh;
        scroll-behavior: smooth;
    }

    /* نيفبار "المستقبل" */
    nav {
        position: fixed;
        top: 0; left: 0; width: 100%;
        background: rgba(3, 7, 18, 0.85);
        backdrop-filter: blur(25px) saturate(180%);
        padding: 15px 10%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10000;
        border-bottom: 1px solid var(--border-color);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    .logo {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: #fff;
        text-decoration: none;
        letter-spacing: 2px;
        background: linear-gradient(to right, #fff, var(--primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px var(--primary));
    }

    .nav-links { display: flex; gap: 20px; }
    .nav-links a {
        color: #cbd5e1;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.95rem;
        padding: 10px 18px;
        border-radius: 12px;
        transition: 0.4s;
        border: 1px solid transparent;
    }

    .nav-links a:hover {
        background: rgba(0, 242, 255, 0.08);
        border-color: var(--primary);
        color: var(--primary);
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
    }

    /* قسم الهيرو العملاق */
    .page-container {
        padding-top: 140px;
        position: relative;
        z-index: 5;
    }

    .hero-section {
        text-align: center;
        padding: 80px 20px;
        animation: fadeIn 1.5s ease-out;
    }

    @keyframes fadeIn { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

    .hero-section h1 {
        font-size: clamp(3rem, 12vw, 7rem);
        font-weight: 900;
        margin-bottom: 20px;
        line-height: 1;
        background: linear-gradient(135deg, #fff, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 30px rgba(0, 242, 255, 0.3));
    }

    .hero-section p {
        font-size: 1.5rem;
        color: #94a3b8;
        font-weight: 600;
        letter-spacing: 4px;
        text-transform: uppercase;
    }

    /* شبكة القدرات الفنية */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 35px;
        padding: 60px 10%;
    }

    .feature-card {
        background: var(--glass-bg);
        border-radius: 40px;
        padding: 60px 40px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center;
        transition: 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .feature-card:hover {
        transform: translateY(-20px) rotateX(10deg);
        border-color: var(--primary);
        box-shadow: 0 40px 80px rgba(0,0,0,0.8), 0 0 30px rgba(0, 242, 255, 0.1);
    }

    .feature-card i {
        font-size: 4.5rem;
        margin-bottom: 30px;
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(0, 242, 255, 0.5));
    }

    .feature-card h3 { font-size: 2rem; margin-bottom: 20px; font-weight: 900; color: #fff; }
    .feature-card p { font-size: 1.1rem; color: #94a3b8; line-height: 1.8; }

    /* قسم الأرقام السيادي */
    .data-stats {
        display: flex;
        justify-content: center;
        gap: 80px;
        padding: 80px 10%;
        background: rgba(0,0,0,0.4);
        flex-wrap: wrap;
    }

    .stat-box { text-align: center; }
    .stat-box h2 { font-size: 4rem; font-family: 'Orbitron'; color: var(--primary); text-shadow: 0 0 20px var(--primary); }
    .stat-box span { font-size: 1rem; color: #64748b; font-weight: 900; }

    /* نظام تواصل النخبة */
    .contact-wrapper {
        max-width: 800px;
        margin: 80px auto;
        padding: 0 25px 120px;
    }

    .contact-link {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 30px 45px;
        background: rgba(255, 255, 255, 0.03);
        margin-bottom: 30px;
        border-radius: 30px;
        text-decoration: none;
        color: white;
        font-weight: 900;
        font-size: 1.4rem;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.5s;
    }

    .contact-link:hover {
        background: rgba(0, 242, 255, 0.12);
        transform: scale(1.05);
        border-color: var(--primary);
    }

    footer {
        padding: 80px;
        text-align: center;
        background: #000;
        color: #475569;
        font-size: 1rem;
        font-family: 'Lexend', sans-serif;
        border-top: 1px solid rgba(255,255,255,0.05);
        letter-spacing: 2px;
    }

    /* الماتريكس الذري المتطور */
    #matrix-canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: 1;
        opacity: 0.25;
    }

    /* هندسة الجوال - لا تشابك بعد اليوم */
    @media (max-width: 900px) {
        nav { flex-direction: column; padding: 20px; gap: 15px; }
        .nav-links { gap: 10px; flex-wrap: wrap; justify-content: center; }
        .nav-links a { font-size: 0.8rem; padding: 8px 12px; }
        .page-container { padding-top: 220px; }
        .hero-section h1 { font-size: 3.5rem; }
    }
</style>
"""

MATRIX_SCRIPT = """
<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
   
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;
   
    const chars = '0101010101010101';
    const fontSize = 20;
    const columns = width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
        ctx.fillStyle = 'rgba(3, 7, 18, 0.15)';
        ctx.fillRect(0, 0, width, height);
       
        ctx.fillStyle = '#00f2ff';
        ctx.font = fontSize + 'px monospace';
       
        for (let i = 0; i < drops.length; i++) {
            const text = chars.charAt(Math.floor(Math.random() * chars.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
           
            if (drops[i] * fontSize > height && Math.random() > 0.98) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    setInterval(draw, 35);
</script>
"""

NAVBAR = """
<nav>
    <a href="/" class="logo">ASSEM HAMID</a>
    <div class="nav-links">
        <a href="/"><i class="fas fa-layer-group"></i> الرئيسية</a>
        <a href="/about"><i class="fas fa-fingerprint"></i> من أنا</a>
        <a href="/contact"><i class="fas fa-headset"></i> تواصل معي</a>
    </div>
</nav>
"""

@app.route('/')
def index():
    return f"""
    <html>
    <head><title>The Masterpiece | Assem Hamid</title><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        <canvas id="matrix-canvas"></canvas>
        {NAVBAR}
        <div class="page-container">
            <section class="hero-section">
                <p>Advanced Systems Architecture</p>
                <h1>عاصم حميد</h1>
            </section>
           
            <div class="data-stats">
                <div class="stat-box"><h2>0.00ms</h2><span>Latency</span></div>
                <div class="stat-box"><h2>100%</h2><span>Uptime</span></div>
                <div class="stat-box"><h2>AI-Gen</h2><span>Logic</span></div>
            </div>

            <div class="features-grid">
                <div class="feature-card"><i class="fas fa-bolt-lightning"></i><h3>سرعة استجابه عاليه🚀</h3><p>برمجة الأنظمة عالية الكثافة التي تتعامل مع ملايين الطلبات في أجزاء من الثانية دون أدنى تأخير.</p></div>
                <div class="feature-card"><i class="fas fa-shield-cat"></i><h3>حصانة سيبرانيه🔒</h3><p>تطبيق معايير التشفير اللامركزي وحماية الجدار الناري الذكي ضد كافة أنواع الاختراقات العالمية.</p></div>
                <div class="feature-card"><i class="fas fa-wand-magic-sparkles"></i><h3>واجهات خاصه💎</h3><p>تجربة مستخدم تتخطى المألوف، حيث يتفاعل التصميم مع تطلعات المستخدم في كل ضغطة زر.</p></div>
                <div class="feature-card"><i class="fas fa-brain-circuit"></i><h3>ذكاء اصطناعي🧠</h3><p>دمج وحدات تعلم آلي متقدمة تقوم بتحليل البيانات استباقياً لضمان استقرار النظام للأبد.</p></div>
            </div>
        </div>
        <footer> (3V) تطوير المهندس عاصم حميد © 2026 </footer>
        {MATRIX_SCRIPT}
    </body>
    </html>
    """

@app.route('/about')
def about():
    return f"""
    <html>
    <head><title>الرؤية الاستراتيجية | عاصم حميد</title><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        <canvas id="matrix-canvas"></canvas>
        {NAVBAR}
        <div class="page-container">
            <section class="hero-section"><h1>رؤية النخبة</h1><p>Arab Technology</p></section>
            <div style="padding: 0 10% 100px;">
                <div class="feature-card" style="max-width: 900px; margin: auto;">
                    <i class="fas fa-gem"></i>
                    <h2 style="color: #fff; font-size: 2.5rem; margin-bottom: 30px;">الاحترافية التقنية</h2>
                    <p style="font-size: 1.4rem; line-height: 2.2;"> أهدف إلى خلق بيئة تقنية عربية تتفوق على الحلول الغربية في الأمان والذكاء والسرعة.</p>
                </div>
            </div>
        </div>
        <footer>(3V) تطوير المهندس عاصم حميد © 2026</footer>
        {MATRIX_SCRIPT}
    </body>
    </html>
    """

@app.route('/contact')
def contact():
    return f"""
    <html>
    <head><title>قنوات الارتباط | عاصم حميد</title><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8">{COMMON_STYLE}</head>
    <body>
        <canvas id="matrix-canvas"></canvas>
        {NAVBAR}
        <div class="page-container">
            <section class="hero-section"><h1>قنوات التواصل المباشره📲</h1><p>قنوات تواصل آمنة ومباشرة</p></section>
            <div class="contact-wrapper">
                <a href="https://wa.me/967783747282" class="contact-link" style="border-right: 12px solid #25d366;">
                    <span><i class="fab fa-whatsapp"></i> واتساب🟢</span>
                    <i class="fas fa-check-double" style="color: #25d366;"></i>
                </a>
                <a href="tel:+967783787282" class="contact-link" style="border-right: 12px solid #3b82f6;">
                    <span><i class="fas fa-phone-flip"></i> اتصال هاتفي📞<span>
                    <i class="fas fa-signal" style="color: #3b82f6;"></i>
                </a>
                <a href="mailto:aasssseemm5@gmail.com" class="contact-link" style="border-right: 12px solid #ea4335;">
                    <span><i class="fas fa-envelope-open"></i> بريد إلكتروني📩</span>
                    <i class="fas fa-paper-plane" style="color: #ea4335;"></i>
                </a>
            </div>
        </div>
        <footer>(3V) تطوير المهندس عاصم حميد © 2026</footer>
        {MATRIX_SCRIPT}
    </body>
    </html>
    """
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(os.getcwd(), 'manifest.json')

if __name__ == '__main__':
    app.run(debug=True)
    