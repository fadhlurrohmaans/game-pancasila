import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Petualangan Garuda - Pancasila Arcade",
    page_icon="🦅",
    layout="centered"
)

st.title("🦅 Petualangan Garuda: Penjaga Pancasila")
st.caption("Game Arcade Klasik Edukasi Fungsi Pancasila — Siap Deploy di Streamlit!")

# Sidebar Informasi & Edukasi
with st.sidebar:
    st.header("🎮 Cara Bermain")
    st.markdown("""
    * **Gerak**: Gunakan **Panah Keyboard** atau **WASD**.
    * **Objektif**: Ambil 5 **Kristal Emas Pancasila** dan hindari **Musuh Merah (Hoaks/Disintegrasi)**.
    * **Kuis**: Jawab pertanyaan kuis fungsi Pancasila dengan menekan angka **1, 2, atau 3**.
    """)
    st.divider()
    st.header("📚 5 Fungsi Pancasila")
    st.markdown("""
    1. **Dasar Negara**: Landasan utama penyelenggaraan negara.
    2. **Pandangan Hidup**: Pedoman moral & perilaku sehari-hari.
    3. **Jiwa Bangsa**: Pemersatu sejak lahirnya Indonesia.
    4. **Sumber Hukum**: Cuan dari segala sumber hukum Indonesia.
    5. **Kepribadian Bangsa**: Ciri khas unik yang membedakan dari bangsa lain.
    """)

# Game Engine (HTML5/JS Canvas di dalam Streamlit)
game_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #0f0f19;
            color: #f0f0f0;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            padding: 10px;
        }
        canvas {
            border: 4px solid #ffffff;
            box-shadow: 0px 0px 20px rgba(255, 215, 0, 0.3);
            background-color: #0f0f19;
        }
    </style>
</head>
<body>

<canvas id="gameCanvas" width="760" height="520"></canvas>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Game State
let state = 'START'; // START, PLAY, QUIZ, GAMEOVER, WIN
let score = 0;
let hp = 3;
let activeQuiz = null;
let feedbackText = "";
let feedbackTimer = 0;

// Input Keys
const keys = {};
window.addEventListener("keydown", e => {
    keys[e.key] = true;
    handleQuizInput(e.key);
});
window.addEventListener("keyup", e => { keys[e.key] = false; });

// Player
const player = { x: 50, y: 240, w: 24, h: 24, speed: 4 };

// Enemies
const enemies = [
    { x: 180, y: 100, w: 20, h: 20, dx: 3, dy: 0 },
    { x: 380, y: 380, w: 20, h: 20, dx: -3, dy: 2 },
    { x: 580, y: 150, w: 20, h: 20, dx: 0, dy: 4 },
    { x: 280, y: 300, w: 20, h: 20, dx: 2, dy: -3 }
];

// Questions Data
const questions = [
    {
        sila: "Dasar Negara",
        q: "Pancasila jadi landasan utama mengatur penyelenggaraan negara. Fungsi ini adalah...",
        opts: ["1. Dasar Negara", "2. Pandangan Hidup", "3. Kepribadian Bangsa"],
        ans: 1
    },
    {
        sila: "Pandangan Hidup",
        q: "Pancasila jadi pedoman moral & petunjuk arah perilaku warga sehari-hari...",
        opts: ["1. Sumber Hukum", "2. Pandangan Hidup Bangsa", "3. Cita-cita Bangsa"],
        ans: 2
    },
    {
        sila: "Jiwa Bangsa",
        q: "Pancasila lahir bersamaan dengan bangsa Indonesia dan menyatukan rakyat...",
        opts: ["1. Kepribadian Bangsa", "2. Jiwa Bangsa Indonesia", "3. Perjanjian Luhur"],
        ans: 2
    },
    {
        sila: "Sumber Hukum",
        q: "Semua hukum di Indonesia tidak boleh bertentangan dengan Pancasila...",
        opts: ["1. Sumber dari Segala Sumber Hukum", "2. Ideologi Terbuka", "3. Dasar Negara"],
        ans: 1
    },
    {
        sila: "Kepribadian Bangsa",
        q: "Pancasila memberi ciri khas unik (gotong royong) yang bedakan dari bangsa lain...",
        opts: ["1. Cita-cita Bangsa", "2. Perjanjian Luhur", "3. Kepribadian Bangsa"],
        ans: 3
    }
];

// Crystals
const crystalPositions = [
    {x: 180, y: 80}, {x: 600, y: 90}, {x: 120, y: 420}, {x: 620, y: 420}, {x: 370, y: 240}
];
const crystals = crystalPositions.map((pos, idx) => ({
    x: pos.x, y: pos.y, w: 18, h: 18, collected: false, q: questions[idx]
}));

function handleQuizInput(key) {
    if (state === 'START' && key === ' ') {
        state = 'PLAY';
    } else if (state === 'QUIZ' && activeQuiz) {
        let choice = 0;
        if (key === '1') choice = 1;
        if (key === '2') choice = 2;
        if (key === '3') choice = 3;

        if (choice > 0) {
            if (choice === activeQuiz.q.ans) {
                score += 100;
                activeQuiz.collected = true;
                feedbackText = "BENAR! Kekuatan Sila Diaktifkan!";
            } else {
                hp -= 1;
                feedbackText = "SALAH! Pemahaman Jiwa Pancasila Melemahi!";
            }
            feedbackTimer = 90;
            state = 'PLAY';

            if (crystals.every(c => c.collected)) state = 'WIN';
            else if (hp <= 0) state = 'GAMEOVER';
        }
    } else if ((state === 'GAMEOVER' || state === 'WIN') && (key === 'r' || key === 'R')) {
        resetGame();
    }
}

function resetGame() {
    player.x = 50; player.y = 240;
    score = 0; hp = 3;
    crystals.forEach(c => c.collected = false);
    state = 'PLAY';
}

function update() {
    if (state === 'PLAY') {
        // Player Move
        if (keys['ArrowLeft'] || keys['a']) player.x -= player.speed;
        if (keys['ArrowRight'] || keys['d']) player.x += player.speed;
        if (keys['ArrowUp'] || keys['w']) player.y -= player.speed;
        if (keys['ArrowDown'] || keys['s']) player.y += player.speed;

        // Bounds
        player.x = Math.max(10, Math.min(canvas.width - 34, player.x));
        player.y = Math.max(40, Math.min(canvas.height - 34, player.y));

        // Enemies
        enemies.forEach(e => {
            e.x += e.dx; e.y += e.dy;
            if (e.x <= 10 || e.x >= canvas.width - 30) e.dx *= -1;
            if (e.y <= 40 || e.y >= canvas.height - 30) e.dy *= -1;

            // Collision Enemy
            if (player.x < e.x + e.w && player.x + player.w > e.x &&
                player.y < e.y + e.h && player.y + player.h > e.y) {
                hp -= 1;
                player.x = 50; player.y = 240;
                feedbackText = "Kena Serangan Hoaks! HP -1";
                feedbackTimer = 60;
                if (hp <= 0) state = 'GAMEOVER';
            }
        });

        // Collision Crystal
        crystals.forEach(c => {
            if (!c.collected && player.x < c.x + c.w && player.x + player.w > c.x &&
                player.y < c.y + c.h && player.y + player.h > c.y) {
                activeQuiz = c;
                state = 'QUIZ';
            }
        });
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (state === 'START') {
        ctx.fillStyle = "#FFD700";
        ctx.font = "bold 28px Courier New";
        ctx.fillText("PETUALANGAN GARUDA", 230, 200);
        
        ctx.fillStyle = "#ffffff";
        ctx.font = "16px Courier New";
        ctx.fillText("Penjaga Fungsi Pancasila", 270, 240);
        ctx.fillText("Tekan [SPASI] Untuk Memulai", 250, 340);
    } 
    else if (state === 'PLAY' || state === 'QUIZ' || state === 'GAMEOVER' || state === 'WIN') {
        // Top HUD Bar
        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 16px Courier New";
        ctx.fillText("Skor: " + score, 20, 25);
        ctx.fillStyle = "#dc143c";
        ctx.fillText("HP: " + "❤️ ".repeat(Math.max(0, hp)), 220, 25);
        ctx.fillStyle = "#FFD700";
        const collectedCount = crystals.filter(c => c.collected).length;
        ctx.fillText("Kristal: " + collectedCount + "/5", 580, 25);

        // Border Play Area
        ctx.strokeStyle = "#ffffff";
        ctx.strokeRect(10, 35, canvas.width - 20, canvas.height - 45);

        // Draw Crystals
        crystals.forEach(c => {
            if (!c.collected) {
                ctx.fillStyle = "#FFD700";
                ctx.fillRect(c.x, c.y, c.w, c.h);
            }
        });

        // Draw Enemies
        ctx.fillStyle = "#dc143c";
        enemies.forEach(e => ctx.fillRect(e.x, e.y, e.w, e.h));

        // Draw Player
        ctx.fillStyle = "#32cd32";
        ctx.fillRect(player.x, player.y, player.w, player.h);

        // Draw Feedback Message
        if (feedbackTimer > 0) {
            ctx.fillStyle = "#FFD700";
            ctx.font = "14px Courier New";
            ctx.fillText(feedbackText, 200, canvas.height - 15);
            feedbackTimer--;
        }

        // Quiz Modal Box
        if (state === 'QUIZ' && activeQuiz) {
            ctx.fillStyle = "rgba(30, 30, 50, 0.95)";
            ctx.fillRect(60, 80, canvas.width - 120, 320);
            ctx.strokeStyle = "#FFD700";
            ctx.lineWidth = 3;
            ctx.strokeRect(60, 80, canvas.width - 120, 320);

            ctx.fillStyle = "#FFD700";
            ctx.font = "bold 18px Courier New";
            ctx.fillText("UJIAN FUNGSI: " + activeQuiz.q.sila, 80, 120);

            ctx.fillStyle = "#ffffff";
            ctx.font = "13px Courier New";
            ctx.fillText(activeQuiz.q.q, 80, 160);

            activeQuiz.q.opts.forEach((opt, idx) => {
                ctx.fillStyle = "#32cd32";
                ctx.font = "bold 15px Courier New";
                ctx.fillText(opt, 100, 220 + (idx * 40));
            });

            ctx.fillStyle = "#FFD700";
            ctx.font = "12px Courier New";
            ctx.fillText("Tekan angka [1], [2], atau [3] pada keyboard!", 80, 370);
        }

        // Game Over Screen
        if (state === 'GAMEOVER') {
            ctx.fillStyle = "rgba(15, 15, 25, 0.85)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#dc143c";
            ctx.font = "bold 36px Courier New";
            ctx.fillText("GAME OVER", 280, 220);
            ctx.fillStyle = "#ffffff";
            ctx.font = "16px Courier New";
            ctx.fillText("Nilai-nilai Pancasila Terancam!", 230, 270);
            ctx.fillText("Tekan [R] untuk Mencoba Lagi", 240, 330);
        }

        // Win Screen
        if (state === 'WIN') {
            ctx.fillStyle = "rgba(15, 15, 25, 0.85)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#FFD700";
            ctx.font = "bold 32px Courier New";
            ctx.fillText("KEMENANGAN MUTLAK!", 210, 220);
            ctx.fillStyle = "#ffffff";
            ctx.font = "16px Courier New";
            ctx.fillText("Kamu Berhasil Menjaga Pancasila! Skor: " + score, 160, 270);
            ctx.fillText("Tekan [R] untuk Bermain Lagi", 240, 330);
        }
    }
}

function loop() {
    update();
    draw();
    requestAnimationFrame(loop);
}

loop();
</script>

</body>
</html>
"""

# Render Game ke Streamlit
components.html(game_code, height=560)