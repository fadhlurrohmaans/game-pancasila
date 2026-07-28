import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Petualangan Garuda - Pancasila Arcade",
    page_icon="🦅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS Streamlit agar tampil full & rapi di layar HP
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        max-width: 850px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🦅 Petualangan Garuda: Penjaga Pancasila")

# Engine Game HTML5 + Cyber Arcade Graphics + Touch Controls
game_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <style>
        * {
            box-sizing: border-box;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        body {
            background-color: #0b0c10;
            color: #66fcf1;
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            padding: 5px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .canvas-container {
            position: relative;
            width: 100%;
            max-width: 780px;
        }
        canvas {
            width: 100%;
            height: auto;
            border: 3px solid #45f3ff;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(69, 243, 255, 0.4);
            background: #0d0e15;
            display: block;
        }
        /* Virtual Controller (Touch Pad Android) */
        .controls-wrapper {
            width: 100%;
            max-width: 780px;
            margin-top: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #1f2833;
            padding: 10px;
            border-radius: 12px;
            border: 1px solid #45f3ff;
        }
        .dpad {
            display: grid;
            grid-template-columns: repeat(3, 50px);
            grid-template-rows: repeat(3, 50px);
            gap: 4px;
        }
        .btn-ctrl {
            background: #0b0c10;
            border: 2px solid #45f3ff;
            color: #45f3ff;
            font-size: 20px;
            font-weight: bold;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 0 #1f2833;
            active { background: #45f3ff; color: #000; }
        }
        .btn-ctrl:active {
            transform: translateY(2px);
            background: #45f3ff;
            color: #0b0c10;
        }
        .action-buttons {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
        }
        .btn-quiz {
            width: 60px;
            height: 60px;
            background: #c5a059;
            border: 2px solid #fff;
            color: #000;
            font-size: 22px;
            font-weight: bold;
            border-radius: 50%;
            box-shadow: 0 4px 10px rgba(255, 215, 0, 0.4);
        }
        .btn-quiz:active {
            transform: scale(0.92);
            background: #fff;
        }
        .btn-space {
            width: 130px;
            height: 50px;
            background: #ff0055;
            border: 2px solid #fff;
            color: #fff;
            font-size: 14px;
            font-weight: bold;
            border-radius: 8px;
            text-shadow: 0 0 5px #000;
        }
        .btn-space:active { background: #ff6699; }
    </style>
</head>
<body>

<div class="canvas-container">
    <canvas id="gameCanvas" width="800" height="500"></canvas>
</div>

<!-- On-Screen Virtual Controls untuk Mobile Android -->
<div class="controls-wrapper">
    <!-- D-PAD / Panah Arah -->
    <div class="dpad">
        <div></div>
        <button class="btn-ctrl" id="btnUp">⬆️</button>
        <div></div>
        <button class="btn-ctrl" id="btnLeft">⬅️</button>
        <div></div>
        <button class="btn-ctrl" id="btnRight">➡️</button>
        <div></div>
        <button class="btn-ctrl" id="btnDown">⬇️</button>
        <div></div>
    </div>

    <!-- Tombol Aksi & Kuis -->
    <div class="action-buttons">
        <button class="btn-quiz" id="btn1">1</button>
        <button class="btn-quiz" id="btn2">2</button>
        <button class="btn-quiz" id="btn3">3</button>
        <br>
        <button class="btn-space" id="btnAction">Mulai / Spasi</button>
    </div>
</div>

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

// Directional State (Mobile Touch Friendly)
const moveDir = { up: false, down: false, left: false, right: false };

// Player Garuda
const player = { x: 50, y: 230, w: 32, h: 32, speed: 4 };

// Musuh (Hoaks / Disintegrasi)
const enemies = [
    { x: 220, y: 100, w: 26, h: 26, dx: 3.5, dy: 0, label: "HOAX" },
    { x: 420, y: 380, w: 26, h: 26, dx: -3, dy: 2.5, label: "FITNAH" },
    { x: 620, y: 150, w: 26, h: 26, dx: 0, dy: 4, label: "DISAGRE" },
    { x: 300, y: 280, w: 26, h: 26, dx: 2.5, dy: -3, label: "HOAX" }
];

// Soal Edukasi Pancasila
const questions = [
    {
        sila: "1. Dasar Negara",
        symbol: "⭐",
        q: "Landasan utama dalam mengatur penyelenggaraan seluruh pemerintahan negara:",
        opts: ["1. Dasar Negara", "2. Pandangan Hidup", "3. Perjanjian Luhur"],
        ans: 1
    },
    {
        sila: "2. Pandangan Hidup",
        symbol: "⛓️",
        q: "Pedoman moral & petunjuk arah perilaku seluruh rakyat sehari-hari:",
        opts: ["1. Sumber Hukum", "2. Pandangan Hidup", "3. Cita-cita Bangsa"],
        ans: 2
    },
    {
        sila: "3. Jiwa Bangsa",
        symbol: "🌳",
        q: "Lahir bersamaan dengan keberadaan bangsa dan menjaga persatuan Indonesia:",
        opts: ["1. Kepribadian Bangsa", "2. Jiwa Bangsa", "3. Sumber Hukum"],
        ans: 2
    },
    {
        sila: "4. Sumber Hukum",
        symbol: "🐂",
        q: "Setiap hukum/UU di Indonesia wajib berlandaskan dan tidak bertentangan dengan:",
        opts: ["1. Sumber Segala Hukum", "2. Ideologi Terbuka", "3. Doktrin Politik"],
        ans: 1
    },
    {
        sila: "5. Kepribadian Bangsa",
        symbol: "🌾",
        q: "Memberikan ciri khas unik (gotong royong) yang membedakan dengan bangsa lain:",
        opts: ["1. Cita-cita Bangsa", "2. Perjanjian Luhur", "3. Kepribadian Bangsa"],
        ans: 3
    }
];

// Kristal Sila
const crystalPositions = [
    {x: 200, y: 90}, {x: 650, y: 100}, {x: 150, y: 400}, {x: 650, y: 400}, {x: 400, y: 230}
];
const crystals = crystalPositions.map((pos, idx) => ({
    x: pos.x, y: pos.y, w: 28, h: 28, collected: false, q: questions[idx]
}));

// Keyboard Event Handlers
const keys = {};
window.addEventListener("keydown", e => {
    keys[e.key] = true;
    handleInput(e.key);
});
window.addEventListener("keyup", e => { keys[e.key] = false; });

// Touch / Mobile Event Listener Binding
function bindTouchBtn(btnId, actionStart, actionEnd) {
    const el = document.getElementById(btnId);
    el.addEventListener("touchstart", (e) => { e.preventDefault(); actionStart(); });
    el.addEventListener("touchend", (e) => { e.preventDefault(); if(actionEnd) actionEnd(); });
    el.addEventListener("mousedown", (e) => { e.preventDefault(); actionStart(); });
    el.addEventListener("mouseup", (e) => { e.preventDefault(); if(actionEnd) actionEnd(); });
}

bindTouchBtn("btnUp", () => moveDir.up = true, () => moveDir.up = false);
bindTouchBtn("btnDown", () => moveDir.down = true, () => moveDir.down = false);
bindTouchBtn("btnLeft", () => moveDir.left = true, () => moveDir.left = false);
bindTouchBtn("btnRight", () => moveDir.right = true, () => moveDir.right = false);

bindTouchBtn("btn1", () => handleInput('1'));
bindTouchBtn("btn2", () => handleInput('2'));
bindTouchBtn("btn3", () => handleInput('3'));
bindTouchBtn("btnAction", () => handleInput(' '));

function handleInput(key) {
    if ((state === 'START') && (key === ' ' || key === 'Spacebar')) {
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
                feedbackText = "BENAR! Kekuatan Sila Berhasil Diaktifkan! ✨";
            } else {
                hp -= 1;
                feedbackText = "SALAH! Jiwa Pancasila Melemahi! 💔";
            }
            feedbackTimer = 90;
            state = 'PLAY';

            if (crystals.every(c => c.collected)) state = 'WIN';
            else if (hp <= 0) state = 'GAMEOVER';
        }
    } else if ((state === 'GAMEOVER' || state === 'WIN') && (key === 'r' || key === 'R' || key === ' ')) {
        resetGame();
    }
}

function resetGame() {
    player.x = 50; player.y = 230;
    score = 0; hp = 3;
    crystals.forEach(c => c.collected = false);
    state = 'PLAY';
}

function update() {
    if (state === 'PLAY') {
        // Player Movement (Keyboard & Virtual Touch D-Pad)
        if (keys['ArrowLeft'] || keys['a'] || moveDir.left) player.x -= player.speed;
        if (keys['ArrowRight'] || keys['d'] || moveDir.right) player.x += player.speed;
        if (keys['ArrowUp'] || keys['w'] || moveDir.up) player.y -= player.speed;
        if (keys['ArrowDown'] || keys['s'] || moveDir.down) player.y += player.speed;

        // Batas Layar Arena
        player.x = Math.max(15, Math.min(canvas.width - 45, player.x));
        player.y = Math.max(55, Math.min(canvas.height - 45, player.y));

        // Pergerakan Musuh
        enemies.forEach(e => {
            e.x += e.dx; e.y += e.dy;
            if (e.x <= 15 || e.x >= canvas.width - 40) e.dx *= -1;
            if (e.y <= 55 || e.y >= canvas.height - 40) e.dy *= -1;

            // Tabrakan Musuh
            if (player.x < e.x + e.w && player.x + player.w > e.x &&
                player.y < e.y + e.h && player.y + player.h > e.y) {
                hp -= 1;
                player.x = 50; player.y = 230;
                feedbackText = "⚠️ Terkena Serangan " + e.label + "! HP -1";
                feedbackTimer = 70;
                if (hp <= 0) state = 'GAMEOVER';
            }
        });

        // Tabrakan Kristal
        crystals.forEach(c => {
            if (!c.collected && player.x < c.x + c.w && player.x + player.w > c.x &&
                player.y < c.y + c.h && player.y + player.h > c.y) {
                activeQuiz = c;
                state = 'QUIZ';
            }
        });
    }
}

// Draw Pixel Art / Cyber Graphics
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Grid Cyber Background
    ctx.strokeStyle = "rgba(69, 243, 255, 0.05)";
    ctx.lineWidth = 1;
    for (let x = 0; x < canvas.width; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
    }
    for (let y = 0; y < canvas.height; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
    }

    if (state === 'START') {
        // Layar Judul Arcade
        ctx.fillStyle = "#FFD700";
        ctx.font = "bold 34px 'Courier New'";
        ctx.textAlign = "center";
        ctx.fillText("PETUALANGAN GARUDA", canvas.width/2, 170);
        
        ctx.fillStyle = "#45f3ff";
        ctx.font = "bold 18px 'Courier New'";
        ctx.fillText("🛡️ PENJAGA FUNGSI PANCASILA 🛡️", canvas.width/2, 220);

        ctx.fillStyle = "#ffffff";
        ctx.font = "16px 'Courier New'";
        ctx.fillText("Tekan [MULAI] atau SPASI untuk Memulai", canvas.width/2, 330);
        ctx.font = "13px 'Courier New'";
        ctx.fillText("Gunakan D-Pad Virtual di bawah untuk bergerak!", canvas.width/2, 370);
    } 
    else if (state === 'PLAY' || state === 'QUIZ' || state === 'GAMEOVER' || state === 'WIN') {
        // Top Neon HUD
        ctx.fillStyle = "#1f2833";
        ctx.fillRect(10, 8, canvas.width - 20, 38);
        ctx.strokeStyle = "#45f3ff";
        ctx.lineWidth = 2;
        ctx.strokeRect(10, 8, canvas.width - 20, 38);

        ctx.textAlign = "left";
        ctx.fillStyle = "#FFD700";
        ctx.font = "bold 16px 'Courier New'";
        ctx.fillText("SKOR: " + score, 25, 33);

        ctx.fillStyle = "#ff0055";
        ctx.fillText("HP: " + "❤️".repeat(Math.max(0, hp)), 300, 33);

        ctx.fillStyle = "#00ff66";
        const collectedCount = crystals.filter(c => c.collected).length;
        ctx.fillText("KRISTAL: " + collectedCount + "/5", 610, 33);

        // Border Arena Oyun
        ctx.strokeStyle = "#ff0055";
        ctx.lineWidth = 3;
        ctx.strokeRect(10, 50, canvas.width - 20, canvas.height - 60);

        // Render Kristal Pancasila (Glow & Icon)
        crystals.forEach(c => {
            if (!c.collected) {
                ctx.shadowBlur = 15;
                ctx.shadowColor = "#FFD700";
                ctx.fillStyle = "#FFD700";
                ctx.beginPath();
                ctx.arc(c.x + c.w/2, c.y + c.h/2, 14, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;

                // Simbol Sila
                ctx.fillStyle = "#000";
                ctx.font = "14px Arial";
                ctx.textAlign = "center";
                ctx.fillText(c.q.symbol, c.x + c.w/2, c.y + c.h/2 + 5);
            }
        });

        // Render Musuh (Pixel Monster Red/Purple Glow)
        enemies.forEach(e => {
            ctx.shadowBlur = 10;
            ctx.shadowColor = "#ff0055";
            ctx.fillStyle = "#ff0055";
            ctx.fillRect(e.x, e.y, e.w, e.h);
            ctx.shadowBlur = 0;

            // Label Hoaks
            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 10px 'Courier New'";
            ctx.textAlign = "center";
            ctx.fillText(e.label, e.x + e.w/2, e.y - 4);
        });

        // Render Player (Garuda Kesatria)
        ctx.shadowBlur = 12;
        ctx.shadowColor = "#00ff66";
        ctx.fillStyle = "#00ff66";
        ctx.fillRect(player.x, player.y, player.w, player.h);
        
        // Perisai Garuda
        ctx.fillStyle = "#ff0055";
        ctx.fillRect(player.x + 8, player.y + 8, 16, 16);
        ctx.fillStyle = "#ffffff";
        ctx.fillRect(player.x + 12, player.y + 12, 8, 8);
        ctx.shadowBlur = 0;

        // Feedback Notifikasi Teks
        if (feedbackTimer > 0) {
            ctx.fillStyle = "#FFD700";
            ctx.font = "bold 15px 'Courier New'";
            ctx.textAlign = "center";
            ctx.fillText(feedbackText, canvas.width/2, canvas.height - 20);
            feedbackTimer--;
        }

        // Popup Modal Kuis
        if (state === 'QUIZ' && activeQuiz) {
            ctx.fillStyle = "rgba(11, 12, 16, 0.95)";
            ctx.fillRect(40, 70, canvas.width - 80, 360);
            ctx.strokeStyle = "#FFD700";
            ctx.lineWidth = 3;
            ctx.strokeRect(40, 70, canvas.width - 80, 360);

            ctx.textAlign = "left";
            ctx.fillStyle = "#FFD700";
            ctx.font = "bold 20px 'Courier New'";
            ctx.fillText("📜 UJIAN SILA: " + activeQuiz.q.sila, 60, 110);

            ctx.fillStyle = "#ffffff";
            ctx.font = "14px 'Courier New'";
            ctx.fillText(activeQuiz.q.q, 60, 155);

            activeQuiz.q.opts.forEach((opt, idx) => {
                ctx.fillStyle = "#45f3ff";
                ctx.font = "bold 16px 'Courier New'";
                ctx.fillText(opt, 80, 220 + (idx * 45));
            });

            ctx.fillStyle = "#FFD700";
            ctx.font = "13px 'Courier New'";
            ctx.fillText("Tekan tombol [1], [2], atau [3] di bawah untuk menjawab!", 60, 390);
        }

        // Layar Game Over
        if (state === 'GAMEOVER') {
            ctx.fillStyle = "rgba(11, 12, 16, 0.9)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.textAlign = "center";
            ctx.fillStyle = "#ff0055";
            ctx.font = "bold 38px 'Courier New'";
            ctx.fillText("GAME OVER", canvas.width/2, 200);
            ctx.fillStyle = "#ffffff";
            ctx.font = "16px 'Courier New'";
            ctx.fillText("Nilai-nilai Pancasila Terancam Hoaks!", canvas.width/2, 250);
            ctx.fillText("Tekan tombol [MULAI] atau [R] untuk Coba Lagi", canvas.width/2, 320);
        }

        // Layar Menang (Win)
        if (state === 'WIN') {
            ctx.fillStyle = "rgba(11, 12, 16, 0.9)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.textAlign = "center";
            ctx.fillStyle = "#FFD700";
            ctx.font = "bold 34px 'Courier New'";
            ctx.fillText("🏆 KEMENANGAN MUTLAK! 🏆", canvas.width/2, 200);
            ctx.fillStyle = "#45f3ff";
            ctx.font = "16px 'Courier New'";
            ctx.fillText("Kamu Berhasil Menjaga Fungsi Pancasila! Skor: " + score, canvas.width/2, 250);
            ctx.fillText("Tekan tombol [MULAI] atau [R] untuk Main Lagi", canvas.width/2, 320);
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
components.html(game_code, height=690)
