import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Layar Streamlit Mode Wide / Full
st.set_page_config(
    page_title="Mancing Pancasila - Arcade SMP",
    page_icon="🎣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS Streamlit untuk Tampilan Layar Penuh
st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.2rem !important;
        padding-right: 0.2rem !important;
        max-width: 100% !important;
    }
    body {
        background-color: #050b14;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Engine Game HTML5 + Canvas + System Nyawa + Soal SMP
game_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        * {
            box-sizing: border-box;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }
        body {
            background: #050b14;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow: hidden;
        }
        .game-wrapper {
            position: relative;
            width: 100vw;
            height: 100vh;
            max-width: 1200px;
            max-height: 900px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        canvas {
            width: 100%;
            height: 100%;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
            background: #000;
            display: block;
        }
        .touch-controls {
            position: absolute;
            bottom: 20px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-between;
            padding: 0 25px;
            pointer-events: none;
            z-index: 10;
        }
        .btn-touch {
            pointer-events: auto;
            background: linear-gradient(135deg, #00d2ff, #0066ff);
            border: 2px solid #ffffff;
            color: #ffffff;
            font-weight: bold;
            font-size: 18px;
            padding: 16px 32px;
            border-radius: 50px;
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.5);
            transition: transform 0.1s, background 0.2s;
            cursor: pointer;
        }
        .btn-touch:active {
            transform: scale(0.92);
            background: linear-gradient(135deg, #00ffcc, #0099ff);
        }
        .btn-reel {
            background: linear-gradient(135deg, #ff0055, #ff6600);
            box-shadow: 0 6px 20px rgba(255, 0, 85, 0.5);
            display: none;
        }
        .quiz-overlay {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 92%;
            max-width: 580px;
            background: rgba(8, 16, 32, 0.96);
            border: 2px solid #FFD700;
            border-radius: 16px;
            padding: 20px 24px;
            box-shadow: 0 0 35px rgba(255, 215, 0, 0.5);
            display: none;
            flex-direction: column;
            gap: 12px;
            z-index: 20;
            backdrop-filter: blur(10px);
        }
        .quiz-btn {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid #00d2ff;
            color: #fff;
            padding: 12px 16px;
            border-radius: 10px;
            font-size: 15px;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s;
        }
        .quiz-btn:hover {
            background: rgba(0, 210, 255, 0.2);
            border-color: #00ffcc;
        }
        .quiz-btn:active {
            background: #00d2ff;
            color: #000;
            font-weight: bold;
        }
        .fish-caught-card {
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.15), rgba(0, 212, 255, 0.15));
            border: 1px dashed #FFD700;
            border-radius: 10px;
            padding: 10px 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
    </style>
</head>
<body>

<div class="game-wrapper">
    <canvas id="fishCanvas" width="1000" height="650"></canvas>
    
    <div class="touch-controls">
        <button class="btn-touch" id="btnCast">🎣 LEMPAR KAIL</button>
        <button class="btn-touch btn-reel" id="btnReel">🌀 TARIK (HOLD)</button>
    </div>

    <div class="quiz-overlay" id="quizBox">
        <div class="fish-caught-card">
            <div>
                <span style="color:#FFD700; font-size:12px; font-weight:bold; letter-spacing:1px;">🐟 IKAN UDAH DIPATUK! JAWAB DULU:</span>
                <h4 id="fishName" style="margin:2px 0 0 0; color:#fff; font-size:18px;">Ikan Mas Pancasila</h4>
            </div>
            <span id="fishWeight" style="color:#00ffcc; font-weight:bold; font-size:16px;">3.5 kg</span>
        </div>
        <p id="quizQuestion" style="font-size:15px; line-height:1.4; color:#e0e0e0; margin: 4px 0; font-weight:500;"></p>
        <div id="quizOptions" style="display:flex; flex-direction:column; gap:8px;"></div>
    </div>
</div>

<script>
const canvas = document.getElementById("fishCanvas");
const ctx = canvas.getContext("2d");

function resizeCanvas() {
    canvas.width = 1000;
    canvas.height = 650;
}
resizeCanvas();

// Status Game
let state = 'MENU'; // MENU, WAITING, STRIKE, REELING, FISH_JUMPING, QUIZ, LEVEL_WIN, VICTORY, GAMEOVER
let difficulty = 'MUDAH';
let currentLevel = 1;
let score = 0;
let lives = 3; // SISTEM NYAWA
let caughtInLevel = 0;

const diffSettings = {
    'MUDAH': { tensionDrop: 0.3, tensionGain: 0.8, fishPower: 0.4 },
    'SEDANG': { tensionDrop: 0.5, tensionGain: 1.1, fishPower: 0.7 },
    'TINGGI': { tensionDrop: 0.8, tensionGain: 1.5, fishPower: 1.1 }
};

const levelTargets = { 1: 3, 2: 4, 3: 5 };
const levelNames = { 1: "Danau Pancasila", 2: "Sungai Nusantara", 3: "Laut Garuda" };

// Mekanik Memancing
let bobber = { x: 500, y: 380, active: false };
let tension = 50;
let reelProgress = 0;
let isReeling = false;
let biteTimer = 0;

// Efek Visual
let particles = [];
let ripples = [];
let screenShake = 0;
let strikePulse = 0;
let messageNotice = { text: "", timer: 0, color: "#ff0055" };

// Animasi Lompatan Ikan
let jumpingFish = {
    active: false,
    x: 0, y: 0,
    startX: 0, startY: 0,
    endX: 180, endY: 480,
    progress: 0,
    species: "",
    weight: "0 kg",
    color: "#FFD700"
};

let waveOffset = 0;
let currentQuestion = null;

// Nama Ikan Unik per Level
const fishSpecies = {
    1: ["Ikan Mas Bintang", "Ikan Gurame Toleransi", "Ikan Nila Rantai Emas"],
    2: ["Ikan Patin Pohon Beringin", "Ikan Baung Musyawarah", "Ikan Arwana Gotong Royong"],
    3: ["Ikan Kakap Kepala Banteng", "Ikan Tuna Padi Kapas", "Ikan Marlin Garuda Muda"]
};

// SOAL-SOAL PANCASILA UNTUK ANAK SMP (Bahasa Mudah & Relevan)
const questions = [
    {
        q: "Saat ada teman beda agama yang mau beribadah, sikap kita yang paling tepat sesuai Sila ke-1 adalah...",
        opts: ["A. Menghormati dan tidak mengganggunya", "B. Menyuruhnya cepat selesai", "C. Mengajaknya main game saat itu juga"],
        ans: 0
    },
    {
        q: "Membantu teman yang jatuh dari sepeda tanpa membeda-bedakan kaya atau miskin adalah pengamalan Sila ke-...",
        opts: ["A. Sila Ke-1 (Ketuhanan)", "B. Sila Ke-2 (Kemanusiaan)", "C. Sila Ke-3 (Persatuan)"],
        ans: 1
    },
    {
        q: "Di sekolahmu ada murid dari berbagai daerah dan suku. Kita tetap harus rukun dan kompak. Ini sesuai nilai Sila ke-...",
        opts: ["A. Sila Ke-3 (Persatuan Indonesia)", "B. Sila Ke-4 (Kerakyatan)", "C. Sila Ke-5 (Keadilan Sosial)"],
        ans: 0
    },
    {
        q: "Saat menentukan ketua OSIS atau tempat piknik kelas, keputusan diambil lewat diskusi bersama. Diskusi ini disebut...",
        opts: ["A. Kerja kelompok", "B. Musyawarah mufakat", "C. Ronda malam"],
        ans: 1
    },
    {
        q: "Suka menabung, hemat, dan tidak boros jajan di kantin merupakan contoh perilaku sederhana Sila ke-...",
        opts: ["A. Sila Ke-3", "B. Sila Ke-4", "C. Sila Ke-5"],
        ans: 2
    },
    {
        q: "Pancasila dipakai sebagai 'kompas' atau pedoman bertindak dalam kehidupan sehari-hari. Ini fungsi Pancasila sebagai...",
        opts: ["A. Pandangan Hidup Bangsa", "B. Dasar Negara", "C. Alat Olahraga"],
        ans: 0
    },
    {
        q: "Pancasila adalah pondasi utama dalam mengatur pemerintahan dan tata negara Indonesia. Fungsi ini disebut...",
        opts: ["A. Dasar Negara", "B. Perjanjian Internasional", "C. Lambang Daerah"],
        ans: 0
    },
    {
        q: "Kebiasaan gotong royong dan ramah tamah membuat bangsa Indonesia punya ciri khas unik. Ini menunjukkan Pancasila sebagai...",
        opts: ["A. Kepribadian Bangsa", "B. Lagu Kebangsaan", "C. Tata Tertib Sekolah"],
        ans: 0
    },
    {
        q: "Semua hukum dan aturan perundang-undangan di Indonesia tidak boleh bertentangan dengan Pancasila. Artinya Pancasila sebagai...",
        opts: ["A. Sumber dari Segala Sumber Hukum", "B. Buku Teks Pelajaran", "C. Slogan Parade"],
        ans: 0
    },
    {
        q: "Simbol 'Rantai Emas' pada dada burung Garuda melambangkan Sila ke-...",
        opts: ["A. Sila Ke-1 (Ketuhanan)", "B. Sila Ke-2 (Kemanusiaan)", "C. Sila Ke-3 (Persatuan)"],
        ans: 1
    },
    {
        q: "Simbol 'Pohon Beringin' yang teduh dan punya akar kuat melambangkan...",
        opts: ["A. Persatuan Indonesia (Sila ke-3)", "B. Keadilan Sosial (Sila ke-5)", "C. Ketuhanan (Sila ke-1)"],
        ans: 0
    },
    {
        q: "Kenapa Kepala Banteng dijadikan simbol Sila ke-4?",
        opts: ["A. Karena banteng hewan yang suka berkumpul dan bermusyawarah", "B. Karena banteng hewan yang paling cepat lari", "C. Karena banteng suka makan rumput"],
        ans: 0
    },
    {
        q: "Simbol Padi dan Kapas pada Sila ke-5 melambangkan kebutuhan dasar manusia, yaitu...",
        opts: ["A. Pangan (Makanan) dan Sandang (Pakaian)", "B. Rumah Mewah dan Mobil", "C. Smartphone dan Kuota"],
        ans: 0
    }
];

// Touch & Click Controls
const btnCast = document.getElementById("btnCast");
const btnReel = document.getElementById("btnReel");
const quizBox = document.getElementById("quizBox");

btnCast.addEventListener("click", castLine);

function startReel(e) { if(e) e.preventDefault(); isReeling = true; }
function stopReel(e) { if(e) e.preventDefault(); isReeling = false; }

btnReel.addEventListener("touchstart", startReel);
btnReel.addEventListener("touchend", stopReel);
btnReel.addEventListener("mousedown", startReel);
btnReel.addEventListener("mouseup", stopReel);

window.addEventListener("keydown", (e) => {
    if (e.code === "Space") {
        if (state === 'CASTING' || state === 'WAITING') return;
        if (state === 'STRIKE') startReelingMechanic();
        if (state === 'REELING') isReeling = true;
    }
});
window.addEventListener("keyup", (e) => {
    if (e.code === "Space") isReeling = false;
});

function triggerNotice(msg, color = "#ff0055") {
    messageNotice.text = msg;
    messageNotice.timer = 100;
    messageNotice.color = color;
}

function triggerSplash(x, y, count = 25) {
    for (let i = 0; i < count; i++) {
        particles.push({
            x: x, y: y,
            vx: (Math.random() - 0.5) * 8,
            vy: -Math.random() * 9 - 2,
            size: Math.random() * 4 + 2,
            alpha: 1,
            color: Math.random() > 0.4 ? '#00d2ff' : '#ffffff'
        });
    }
}

function triggerRipple(x, y) {
    ripples.push({ x: x, y: y, radius: 5, maxRadius: 40, alpha: 1 });
}

function castLine() {
    if (state === 'MENU' || state === 'LEVEL_WIN' || state === 'VICTORY' || state === 'GAMEOVER') {
        if (state === 'GAMEOVER' || state === 'VICTORY') {
            lives = 3;
            score = 0;
            currentLevel = 1;
            caughtInLevel = 0;
        }
        state = 'WAITING';
        resetFishingState();
    } else if (state === 'WAITING' && !bobber.active) {
        bobber.active = true;
        bobber.x = 450 + Math.random() * 200;
        bobber.y = 350 + Math.random() * 100;
        triggerSplash(bobber.x, bobber.y, 15);
        triggerRipple(bobber.x, bobber.y);
        biteTimer = 90 + Math.floor(Math.random() * 120);
        btnCast.style.display = "none";
    }
}

function resetFishingState() {
    bobber.active = false;
    tension = 50;
    reelProgress = 0;
    jumpingFish.active = false;
    btnCast.style.display = "block";
    btnCast.innerText = "🎣 LEMPAR KAIL";
    btnReel.style.display = "none";
    quizBox.style.display = "none";
}

function startReelingMechanic() {
    state = 'REELING';
    btnReel.style.display = "block";
    btnCast.style.display = "none";
    triggerSplash(bobber.x, bobber.y, 20);
}

function loseLife(reasonText) {
    lives--;
    screenShake = 18;
    triggerNotice(reasonText, "#ff0055");

    if (lives <= 0) {
        state = 'GAMEOVER';
        btnReel.style.display = "none";
        btnCast.style.display = "none";
    } else {
        state = 'WAITING';
        resetFishingState();
    }
}

function startFishJumpingAnim() {
    state = 'FISH_JUMPING';
    btnReel.style.display = "none";
    
    jumpingFish.active = true;
    jumpingFish.startX = bobber.x;
    jumpingFish.startY = bobber.y;
    jumpingFish.progress = 0;
    
    const speciesList = fishSpecies[currentLevel];
    jumpingFish.species = speciesList[Math.floor(Math.random() * speciesList.length)];
    jumpingFish.weight = (1.5 + Math.random() * 3.2).toFixed(1) + " kg";
    jumpingFish.color = currentLevel === 1 ? '#FFD700' : (currentLevel === 2 ? '#00ffcc' : '#ff0055');

    triggerSplash(bobber.x, bobber.y, 35);
    screenShake = 12;
}

function triggerQuiz() {
    state = 'QUIZ';
    document.getElementById("fishName").innerText = jumpingFish.species;
    document.getElementById("fishWeight").innerText = jumpingFish.weight;

    currentQuestion = questions[Math.floor(Math.random() * questions.length)];
    document.getElementById("quizQuestion").innerText = currentQuestion.q;
    
    const optsContainer = document.getElementById("quizOptions");
    optsContainer.innerHTML = "";
    
    currentQuestion.opts.forEach((opt, idx) => {
        const btn = document.createElement("button");
        btn.className = "quiz-btn";
        btn.innerText = opt;
        btn.onclick = () => answerQuiz(idx);
        optsContainer.appendChild(btn);
    });
    
    quizBox.style.display = "flex";
}

function answerQuiz(selectedIndex) {
    quizBox.style.display = "none";
    if (selectedIndex === currentQuestion.ans) {
        score += 150;
        caughtInLevel++;
        triggerNotice(" Jawaban Benar! +150 Poin", "#00ff66");

        if (caughtInLevel >= levelTargets[currentLevel]) {
            if (currentLevel < 3) {
                state = 'LEVEL_WIN';
            } else {
                state = 'VICTORY';
            }
        } else {
            state = 'WAITING';
            resetFishingState();
        }
    } else {
        loseLife("❌ Jawaban Salah! Ikan Lepas & Nyawa -1");
    }
}

// Logic Updates
function update() {
    waveOffset += 0.03;
    if (screenShake > 0) screenShake *= 0.88;
    if (messageNotice.timer > 0) messageNotice.timer--;

    // Update Particles
    for (let i = particles.length - 1; i >= 0; i--) {
        let p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.35;
        p.alpha -= 0.025;
        if (p.alpha <= 0) particles.splice(i, 1);
    }

    // Update Ripples
    for (let i = ripples.length - 1; i >= 0; i--) {
        let r = ripples[i];
        r.radius += 0.8;
        r.alpha -= 0.015;
        if (r.alpha <= 0) ripples.splice(i, 1);
    }

    // Waiting & Strike Logic
    if (state === 'WAITING' && bobber.active) {
        biteTimer--;
        if (biteTimer <= 0) {
            state = 'STRIKE';
            screenShake = 15;
            triggerSplash(bobber.x, bobber.y, 30);
            triggerRipple(bobber.x, bobber.y);
            
            btnCast.style.display = "block";
            btnCast.innerText = "⚡ STRIKE! TEKAN UNTUK TARIK!";
            btnCast.onclick = () => {
                btnCast.onclick = castLine;
                startReelingMechanic();
            };
        }
    }

    // Reeling Physics
    if (state === 'REELING') {
        const cfg = diffSettings[difficulty];
        if (isReeling) tension += cfg.tensionGain;
        else tension -= cfg.tensionDrop;

        tension += (Math.random() - 0.45) * cfg.fishPower * 2.8;

        if (tension >= 35 && tension <= 75) {
            reelProgress += 0.4;
            if (Math.random() > 0.7) triggerRipple(bobber.x, bobber.y);
        }

        // Tali Putus / Kendur -> Ikan Lepas & Nyawa Berkurang
        if (tension > 98 || tension < 5) {
            triggerSplash(bobber.x, bobber.y, 25);
            loseLife("💦 Senar Putus / Kendur! Ikan Lepas (-1 Nyawa)");
        }

        if (reelProgress >= 100) {
            startFishJumpingAnim();
        }
    }

    // Jumping Fish Animation Arc
    if (state === 'FISH_JUMPING') {
        jumpingFish.progress += 0.025;
        let t = jumpingFish.progress;
        
        jumpingFish.x = (1 - t) * jumpingFish.startX + t * jumpingFish.endX;
        let directY = (1 - t) * jumpingFish.startY + t * jumpingFish.endY;
        jumpingFish.y = directY - Math.sin(t * Math.PI) * 160;

        if (Math.random() > 0.4) {
            particles.push({
                x: jumpingFish.x, y: jumpingFish.y,
                vx: (Math.random() - 0.5) * 3, vy: (Math.random() - 0.5) * 3,
                size: Math.random() * 3 + 2, alpha: 1, color: '#FFD700'
            });
        }

        if (t >= 1) {
            triggerSplash(jumpingFish.endX, jumpingFish.endY, 20);
            triggerQuiz();
        }
    }
}

// Visual Ikan
function drawFishGraphic(ctx, x, y, scale = 1, angle = 0, color = "#FFD700") {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(angle);
    ctx.scale(scale, scale);

    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.ellipse(0, 0, 30, 16, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 1.5;
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(-25, 0);
    ctx.lineTo(-42, -14);
    ctx.lineTo(-38, 0);
    ctx.lineTo(-42, 14);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(-2, -14);
    ctx.lineTo(6, -24);
    ctx.lineTo(12, -12);
    ctx.fill();

    ctx.fillStyle = "#ffffff";
    ctx.beginPath();
    ctx.arc(16, -4, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = "#000000";
    ctx.beginPath();
    ctx.arc(17, -4, 2, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();
}

// Render Utama
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.save();
    if (screenShake > 0.5) {
        let shakeX = (Math.random() - 0.5) * screenShake;
        let shakeY = (Math.random() - 0.5) * screenShake;
        ctx.translate(shakeX, shakeY);
    }

    // Sky
    let skyGrad = ctx.createLinearGradient(0, 0, 0, 300);
    if (currentLevel === 1) {
        skyGrad.addColorStop(0, '#1a0b2e'); skyGrad.addColorStop(0.6, '#8c2f5e'); skyGrad.addColorStop(1, '#f8664b');
    } else if (currentLevel === 2) {
        skyGrad.addColorStop(0, '#0f2027'); skyGrad.addColorStop(0.6, '#203a43'); skyGrad.addColorStop(1, '#2c5364');
    } else {
        skyGrad.addColorStop(0, '#050515'); skyGrad.addColorStop(0.6, '#0a1128'); skyGrad.addColorStop(1, '#1c2541');
    }
    ctx.fillStyle = skyGrad;
    ctx.fillRect(0, 0, canvas.width, 300);

    ctx.fillStyle = "rgba(255, 230, 150, 0.6)";
    ctx.beginPath();
    ctx.arc(800, 140, 40, 0, Math.PI * 2);
    ctx.fill();

    // Water
    let waterGrad = ctx.createLinearGradient(0, 300, 0, canvas.height);
    waterGrad.addColorStop(0, 'rgba(0, 105, 148, 0.9)');
    waterGrad.addColorStop(0.5, 'rgba(0, 55, 90, 0.95)');
    waterGrad.addColorStop(1, 'rgba(2, 20, 40, 1)');
    ctx.fillStyle = waterGrad;

    ctx.beginPath();
    ctx.moveTo(0, 300);
    for (let x = 0; x <= canvas.width; x += 20) {
        let y = 300 + Math.sin(x * 0.015 + waveOffset) * 6;
        ctx.lineTo(x, y);
    }
    ctx.lineTo(canvas.width, canvas.height);
    ctx.lineTo(0, canvas.height);
    ctx.closePath();
    ctx.fill();

    // Ripples
    ripples.forEach(r => {
        ctx.strokeStyle = `rgba(255, 255, 255, ${r.alpha})`;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.ellipse(r.x, r.y, r.radius * 1.8, r.radius * 0.6, 0, 0, Math.PI * 2);
        ctx.stroke();
    });

    // Dock & Rod
    ctx.fillStyle = "#2c1d11"; ctx.fillRect(0, 480, 220, 170);
    ctx.fillStyle = "#1e130a"; ctx.fillRect(0, 510, 220, 10);

    ctx.strokeStyle = "#d4af37";
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(80, 520);
    
    let rodTipX = 320;
    let rodTipY = 220 + (state === 'REELING' ? (tension * 0.8) : 0);
    ctx.quadraticCurveTo(200, 350, rodTipX, rodTipY);
    ctx.stroke();

    // Senar
    if (bobber.active || state === 'REELING' || state === 'STRIKE') {
        ctx.strokeStyle = "rgba(255, 255, 255, 0.75)";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(rodTipX, rodTipY);
        ctx.lineTo(bobber.x, bobber.y);
        ctx.stroke();

        let bobY = bobber.y + (state === 'STRIKE' ? Math.sin(waveOffset * 15) * 10 : 0);
        ctx.fillStyle = "#ff0000";
        ctx.beginPath();
        ctx.arc(bobber.x, bobY, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#ffffff";
        ctx.fillRect(bobber.x - 6, bobY - 2, 12, 4);
    }

    // Particles
    particles.forEach(p => {
        ctx.save();
        ctx.globalAlpha = p.alpha;
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
    });

    // Jumping Fish
    if (state === 'FISH_JUMPING' && jumpingFish.active) {
        let angle = Math.atan2(jumpingFish.y - bobber.y, jumpingFish.x - bobber.x);
        drawFishGraphic(ctx, jumpingFish.x, jumpingFish.y, 1.2, angle, jumpingFish.color);
    }

    // STRIKE Banner
    if (state === 'STRIKE') {
        strikePulse += 0.1;
        let scale = 1 + Math.sin(strikePulse * 3) * 0.15;
        
        ctx.save();
        ctx.translate(canvas.width/2, 180);
        ctx.scale(scale, scale);
        
        ctx.shadowBlur = 20;
        ctx.shadowColor = "#ff0055";
        ctx.fillStyle = "#ff0055";
        ctx.font = "900 48px 'Segoe UI', sans-serif";
        ctx.textAlign = "center";
        ctx.fillText("⚡ STRIKE! ⚡", 0, 0);
        ctx.fillStyle = "#FFD700";
        ctx.font = "bold 20px 'Segoe UI', sans-serif";
        ctx.fillText("SEGERA TEKAN TOMBOL TARIK!", 0, 40);
        ctx.restore();
    }

    // Tension Meter
    if (state === 'REELING') {
        ctx.fillStyle = "rgba(8, 16, 32, 0.85)";
        ctx.fillRect(350, 40, 300, 110);
        ctx.strokeStyle = "#00d2ff";
        ctx.lineWidth = 1.5;
        ctx.strokeRect(350, 40, 300, 110);

        ctx.fillStyle = "#fff";
        ctx.font = "12px sans-serif";
        ctx.textAlign = "left";
        ctx.fillText("KETEGANGAN SENAR (Tahan tombol di Hijau!)", 360, 60);

        ctx.fillStyle = "#222";
        ctx.fillRect(360, 68, 280, 20);

        ctx.fillStyle = "#00ff66";
        ctx.fillRect(360 + (35 * 2.8), 68, (40 * 2.8), 20);

        ctx.fillStyle = tension > 75 || tension < 35 ? "#ff0055" : "#ffffff";
        ctx.fillRect(360 + (tension * 2.8) - 3, 64, 6, 28);

        ctx.fillStyle = "#fff";
        ctx.fillText("JARAK IKAN: " + Math.floor(reelProgress) + "%", 360, 108);
        ctx.fillStyle = "#222";
        ctx.fillRect(360, 115, 280, 12);
        ctx.fillStyle = "#00d2ff";
        ctx.fillRect(360, 115, (reelProgress * 2.8), 12);
    }

    // Notice Overlay Text
    if (messageNotice.timer > 0) {
        ctx.save();
        ctx.fillStyle = messageNotice.color;
        ctx.font = "bold 22px 'Segoe UI', sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(messageNotice.text, canvas.width/2, 240);
        ctx.restore();
    }

    // TOP HUD BAR (Termasuk Tampilan NYAWA ❤️)
    ctx.fillStyle = "rgba(10, 20, 35, 0.88)";
    ctx.fillRect(15, 12, canvas.width - 30, 48);
    ctx.strokeStyle = "rgba(255, 255, 255, 0.2)";
    ctx.strokeRect(15, 12, canvas.width - 30, 48);

    ctx.font = "bold 15px 'Segoe UI', sans-serif";
    
    // Level
    ctx.fillStyle = "#00ffcc";
    ctx.textAlign = "left";
    ctx.fillText("📍 " + levelNames[currentLevel], 28, 42);

    // Nyawa (Hearts)
    ctx.fillStyle = "#ff3366";
    let heartIcons = "❤️".repeat(Math.max(0, lives));
    ctx.fillText("NYAWA: " + (heartIcons || "💀"), 220, 42);

    // Skor
    ctx.fillStyle = "#FFD700";
    ctx.fillText("SKOR: " + score, 420, 42);

    // Target Ikan
    ctx.fillStyle = "#ffffff";
    ctx.fillText("IKAN: " + caughtInLevel + "/" + levelTargets[currentLevel], 600, 42);

    // Kesulitan
    ctx.fillStyle = "#ff9900";
    ctx.fillText("LEVEL: " + difficulty, 780, 42);

    // Overlays Menu
    if (state === 'MENU') {
        ctx.fillStyle = "rgba(5, 11, 20, 0.92)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.textAlign = "center";
        ctx.fillStyle = "#00d2ff";
        ctx.font = "bold 38px sans-serif";
        ctx.fillText("🎣 MANCING PANCASILA 🎣", canvas.width/2, 170);

        ctx.fillStyle = "#e0e0e0";
        ctx.font = "16px sans-serif";
        ctx.fillText("Pilih Tingkat Kesulitan Memancing:", canvas.width/2, 230);

        drawCanvasBtn(canvas.width/2 - 220, 270, 130, 45, "MUDAH", difficulty === 'MUDAH' ? '#00ff66' : '#222');
        drawCanvasBtn(canvas.width/2 - 65, 270, 130, 45, "SEDANG", difficulty === 'SEDANG' ? '#FFD700' : '#222');
        drawCanvasBtn(canvas.width/2 + 90, 270, 130, 45, "TINGGI", difficulty === 'TINGGI' ? '#ff0055' : '#222');

        ctx.fillStyle = "#ffffff";
        ctx.font = "15px sans-serif";
        ctx.fillText("Sistem Game: Kamu punya 3 Nyawa (❤️). Hati-hati jangan sampai senar putus / salah jawab!", canvas.width/2, 380);
        ctx.fillText("Tekan [LEMPAR KAIL] di bawah untuk mulai memancing!", canvas.width/2, 410);
    }

    if (state === 'GAMEOVER') {
        ctx.fillStyle = "rgba(15, 5, 10, 0.94)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.textAlign = "center";
        
        ctx.fillStyle = "#ff0055";
        ctx.font = "bold 42px sans-serif";
        ctx.fillText("💀 GAME OVER! 💀", canvas.width/2, 210);
        
        ctx.fillStyle = "#ffffff";
        ctx.font = "18px sans-serif";
        ctx.fillText("Nyawamu telah habis! Ikan-ikan berhasil meloloskan diri.", canvas.width/2, 270);
        ctx.fillText("Total Skor Akhir Kamu: " + score, canvas.width/2, 310);
        
        drawCanvasBtn(canvas.width/2 - 100, 360, 200, 50, "🔄 COBA LAGI", "#ff0055");
    }

    if (state === 'LEVEL_WIN') {
        ctx.fillStyle = "rgba(5, 11, 20, 0.92)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.textAlign = "center";
        ctx.fillStyle = "#00ff66";
        ctx.font = "bold 32px sans-serif";
        ctx.fillText("🎉 STAGE " + currentLevel + " SELESAI! 🎉", canvas.width/2, 230);
        ctx.fillStyle = "#ffffff";
        ctx.font = "18px sans-serif";
        ctx.fillText("Mantap! Kamu berhasil menangkap semua ikan di lokasi ini!", canvas.width/2, 280);
        
        drawCanvasBtn(canvas.width/2 - 100, 340, 200, 50, "LANJUT LEVEL " + (currentLevel+1), "#00d2ff");
    }

    if (state === 'VICTORY') {
        ctx.fillStyle = "rgba(5, 11, 20, 0.95)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.textAlign = "center";
        ctx.fillStyle = "#FFD700";
        ctx.font = "bold 36px sans-serif";
        ctx.fillText("🏆 PEMANCING PANCASILA SEJATI! 🏆", canvas.width/2, 220);
        ctx.fillStyle = "#ffffff";
        ctx.font = "18px sans-serif";
        ctx.fillText("Hebat! Kamu menguasai lokasi mancing & paham nilai Pancasila! Total Skor: " + score, canvas.width/2, 280);
        
        drawCanvasBtn(canvas.width/2 - 100, 350, 200, 50, "MAIN LAGI", "#00ff66");
    }

    ctx.restore();
}

function drawCanvasBtn(x, y, w, h, text, bg) {
    ctx.fillStyle = bg;
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 1.5;
    ctx.strokeRect(x, y, w, h);
    ctx.fillStyle = "#ffffff";
    ctx.font = "bold 14px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(text, x + w/2, y + h/2 + 5);
}

// Event Klik Menu / Game Over
canvas.addEventListener("click", (e) => {
    const rect = canvas.getBoundingClientRect();
    const clickX = (e.clientX - rect.left) * (canvas.width / rect.width);
    const clickY = (e.clientY - rect.top) * (canvas.height / rect.height);

    if (state === 'MENU') {
        if (clickY >= 270 && clickY <= 315) {
            if (clickX >= canvas.width/2 - 220 && clickX <= canvas.width/2 - 90) difficulty = 'MUDAH';
            if (clickX >= canvas.width/2 - 65 && clickX <= canvas.width/2 + 65) difficulty = 'SEDANG';
            if (clickX >= canvas.width/2 + 90 && clickX <= canvas.width/2 + 220) difficulty = 'TINGGI';
        }
    } else if (state === 'GAMEOVER') {
        if (clickX >= canvas.width/2 - 100 && clickX <= canvas.width/2 + 100 && clickY >= 360 && clickY <= 410) {
            lives = 3;
            score = 0;
            currentLevel = 1;
            caughtInLevel = 0;
            state = 'MENU';
            resetFishingState();
        }
    } else if (state === 'LEVEL_WIN') {
        if (clickX >= canvas.width/2 - 100 && clickX <= canvas.width/2 + 100 && clickY >= 340 && clickY <= 390) {
            currentLevel++;
            caughtInLevel = 0;
            state = 'WAITING';
            resetFishingState();
        }
    } else if (state === 'VICTORY') {
        if (clickX >= canvas.width/2 - 100 && clickX <= canvas.width/2 + 100 && clickY >= 350 && clickY <= 400) {
            currentLevel = 1;
            caughtInLevel = 0;
            score = 0;
            lives = 3;
            state = 'MENU';
            resetFishingState();
        }
    }
});

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

gameLoop();
</script>

</body>
</html>
"""

# Render Game ke Streamlit
components.html(game_code, height=720, scrolling=False)
