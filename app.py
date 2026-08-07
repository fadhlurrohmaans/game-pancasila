import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Nusantara Gem Crush: Pancasila Quest",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling CSS Streamlit untuk Tampilan Layar Penuh (Full Screen Mobile)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 0.2rem !important;
        padding-right: 0.2rem !important;
        max-width: 100% !important;
    }
    .main {
        background: linear-gradient(135deg, #1f0003 0%, #0d0001 100%);
    }
    iframe {
        border-radius: 16px;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# Single Bundle Engine HTML5 + CSS + JavaScript (Mobile Responsive & Auto-Match Cascade)
game_html = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<style>
    * {
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        user-select: none;
        -webkit-user-select: none;
        -webkit-touch-callout: none;
        touch-action: manipulation;
    }
    html, body {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }
    body {
        padding: 8px;
        background: linear-gradient(135deg, #4a0000, #1a0000);
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
    }
    .card {
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(255, 215, 0, 0.4);
        border-radius: 16px;
        padding: 16px;
        width: 100%;
        max-width: 480px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.7);
    }
    h2 { 
        color: #ffd700; 
        margin-top: 0; 
        font-size: clamp(20px, 5vw, 26px);
        text-shadow: 0 2px 6px rgba(0,0,0,0.6); 
    }
    
    /* Stats Bar Mobile Friendly */
    .stats-bar {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 4px;
        width: 100%;
        max-width: 480px;
        background: rgba(0,0,0,0.65);
        padding: 8px 4px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    .stat-item { text-align: center; }
    .stat-title { font-size: 9px; color: #ffd700; font-weight: bold; text-transform: uppercase; }
    .stat-value { font-size: 12px; font-weight: bold; white-space: nowrap; }

    /* Gem Grid Flexible & Responsive */
    #grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 6px;
        width: 100%;
        max-width: 480px;
        background: rgba(15, 5, 5, 0.85);
        padding: 8px;
        border-radius: 16px;
        border: 2px solid #ffd700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.25), inset 0 0 15px rgba(0,0,0,0.8);
    }

    /* === BASE PERMATA / TILE STYLING === */
    .tile {
        width: 100%;
        aspect-ratio: 1 / 1;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: clamp(18px, 5.5vw, 26px);
        cursor: pointer;
        transition: transform 0.2s ease, opacity 0.2s ease, box-shadow 0.15s, filter 0.15s;
        border: 1.5px solid rgba(255, 255, 255, 0.35);
        box-shadow: inset -2px -3px 5px rgba(0,0,0,0.6), inset 2px 2px 4px rgba(255,255,255,0.6), 0 3px 6px rgba(0,0,0,0.4);
        position: relative;
        overflow: hidden;
    }

    /* Pantulan Kilau Kristal pada Permata */
    .tile::before {
        content: '';
        position: absolute;
        top: 2px;
        left: 3px;
        right: 3px;
        height: 38%;
        background: linear-gradient(to bottom, rgba(255,255,255,0.55), rgba(255,255,255,0.05));
        border-radius: 6px 6px 100% 100%;
        pointer-events: none;
    }

    .tile:active {
        transform: scale(0.92);
    }

    /* Efek Permata Terpilih */
    .tile.selected {
        border: 2px solid #ffffff !important;
        transform: scale(1.12);
        box-shadow: 0 0 18px #ffd700, inset 0 0 8px #ffffff !important;
        z-index: 10;
        animation: pulse-gem 0.8s infinite alternate;
    }

    /* Animasi Permata Menghilang ketika Match */
    .tile.matched-pop {
        transform: scale(0) rotate(180deg) !important;
        opacity: 0 !important;
        filter: brightness(2) !important;
    }

    @keyframes pulse-gem {
        0% { filter: brightness(1); transform: scale(1.08); }
        100% { filter: brightness(1.35); transform: scale(1.15); }
    }

    /* WARNA PERMATA PANCASILA */
    .gem-topaz { background: linear-gradient(135deg, #ffe066, #d4af37, #8a7300); }
    .gem-sapphire { background: linear-gradient(135deg, #4dabf7, #1971c2, #0c365e); }
    .gem-emerald { background: linear-gradient(135deg, #51cf66, #2b8a3e, #123b1a); }
    .gem-ruby { background: linear-gradient(135deg, #ff6b6b, #c92a2a, #5c0b0b); }
    .gem-amber { background: linear-gradient(135deg, #ffc078, #d9480f, #7a2200); }
    .gem-amethyst { background: linear-gradient(135deg, #cc5de8, #862e9c, #3b0d48); }

    /* Quiz Modal Overlay */
    .modal-overlay {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.94);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 16px;
        z-index: 100;
    }
    .timer-bar-container {
        width: 100%;
        height: 6px;
        background: rgba(255,255,255,0.2);
        border-radius: 3px;
        overflow: hidden;
        margin-bottom: 12px;
    }
    .timer-bar { height: 100%; background: #ffd700; width: 100%; }
    
    .btn {
        background: linear-gradient(45deg, #d32f2f, #b71c1c);
        color: white; border: 1px solid #ffd700;
        padding: 12px 20px; font-size: 15px; font-weight: bold;
        border-radius: 25px; cursor: pointer; transition: all 0.2s;
        margin: 6px;
        width: 100%;
        max-width: 300px;
    }
    .btn:active { transform: scale(0.96); }
    .btn-diff { background: rgba(255,255,255,0.1); width: 100%; max-width: 290px; }
    .btn-diff.selected { background: #ffd700; color: #800000; font-weight: bold; }

    .opt-btn {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white; padding: 12px; border-radius: 10px;
        text-align: left; font-size: 13px; cursor: pointer; margin-bottom: 8px;
        width: 100%; transition: all 0.2s;
    }
    .opt-btn:active { background: rgba(255, 215, 0, 0.3); border-color: #ffd700; }
    .opt-btn.correct { background: #2e7d32 !important; }
    .opt-btn.wrong { background: #c62828 !important; }

    .hidden { display: none !important; }
</style>
</head>
<body>

<!-- SCREEN 1: START & DIFFICULTY -->
<div class="card" id="screen-start">
    <h2>🦅 Nusantara Gem Crush</h2>
    <p style="font-size: 12px; color: #ffe066; margin-bottom: 12px;">Permata Pancasila Quest</p>
    
    <div style="margin: 10px 0;">
        <button class="btn btn-diff selected" onclick="setDiff('mudah', this)">🟢 Mode Normal (25 Langkah | 3 ❤️)</button><br>
        <button class="btn btn-diff" onclick="setDiff('tinggi', this)">🔴 Mode Tantangan (15 Langkah | 2 ❤️)</button>
    </div>

    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 10px; font-size: 11px; margin-bottom: 14px; text-align: left; border: 1px solid rgba(255, 215, 0, 0.2);">
        ⏱️ <b>Batasan Waktu Level & Soal:</b><br>
        • Level 1: <b>5 Menit</b> (Target: 5 Soal | 60s/soal)<br>
        • Level 2: <b>4 Menit</b> (Target: 8 Soal | 30s/soal)<br>
        • Level 3: <b>3 Menit</b> (Target: 10 Soal | 18s/soal)<br>
        ⚠️ Waktu Habis / Nyawa Habis / Langkah Habis = <b>GAME OVER</b>!
    </div>

    <button class="btn" style="font-size: 16px;" onclick="startGame()">Mulai Petualangan 🚀</button>
</div>

<!-- SCREEN 2: GAME BOARD -->
<div id="screen-game" class="hidden" style="display:flex; flex-direction:column; align-items:center; width: 100%;">
    <div class="stats-bar">
        <div class="stat-item">
            <div class="stat-title">Nyawa</div>
            <div class="stat-value" id="val-lives" style="color:#ff4d4d;">❤️❤️❤️</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Lvl</div>
            <div class="stat-value" id="val-level" style="color:#ffd700;">1</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Waktu</div>
            <div class="stat-value" id="val-level-time" style="color:#ff9f43;">05:00</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Skor</div>
            <div class="stat-value" id="val-score">0</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Moves</div>
            <div class="stat-value" id="val-moves">25</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Target</div>
            <div class="stat-value" id="val-target" style="color:#4caf50;">0/5</div>
        </div>
    </div>

    <div id="grid"></div>
</div>

<!-- QUIZ MODAL OVERLAY -->
<div class="modal-overlay hidden" id="quiz-modal">
    <div style="width: 100%; max-width: 440px; text-align: center;">
        <div style="font-size: 11px; color: #ffd700; font-weight: bold;" id="modal-tag">CHALLENGE PANCASILA</div>
        <div class="timer-bar-container"><div class="timer-bar" id="timer-bar"></div></div>
        <h3 id="quiz-question" style="font-size: 14px; margin: 10px 0 15px 0; min-height: 40px; line-height: 1.4;">Pertanyaan...</h3>
        <div id="quiz-options"></div>
    </div>
</div>

<!-- SCREEN 3: LEVEL COMPLETE -->
<div class="card hidden" id="screen-level-win">
    <h2>🎉 Level Selesai!</h2>
    <p id="win-desc" style="font-size: 13px;">Selamat! Kamu berhasil menuntaskan tantangan permata level ini tepat waktu.</p>
    <div style="font-size: 30px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="win-score">0 Poin</div>
    <button class="btn" id="btn-next-lvl" onclick="nextLevel()">Lanjut Level Berikutnya ➡️</button>
</div>

<!-- SCREEN 4: GAME OVER / TAMAT -->
<div class="card hidden" id="screen-end">
    <h2 id="end-title">💥 GAME OVER</h2>
    <p id="end-desc" style="font-size: 13px; color: #ff6b6b; font-weight: bold;">Gagal menyelesaikan tantangan!</p>
    <div style="font-size: 32px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="final-score">0 Poin</div>
    <div style="font-weight: bold; color: #4caf50; font-size: 15px; margin-bottom: 15px;" id="final-rank"></div>
    <button class="btn" onclick="resetGame()">Main Lagi 🔄</button>
</div>

<script>
    const width = 6;
    
    // Simbol Permata Pancasila
    const gems = ['🌟', '⛓️', '🌳', '🐂', '🌾', '🦅'];
    const gemClasses = ['gem-topaz', 'gem-sapphire', 'gem-emerald', 'gem-ruby', 'gem-amber', 'gem-amethyst'];

    // Waktu Level dalam detik (Lvl 1: 5m/300s, Lvl 2: 4m/240s, Lvl 3: 3m/180s)
    const levelTimeLimits = { 1: 300, 2: 240, 3: 180 };

    // Waktu per Soal Kuis dalam detik (Lvl 1: 60s, Lvl 2: 30s, Lvl 3: 18s)
    const questionTimeLimits = { 1: 60, 2: 30, 3: 18 };

    // Database Soal Pancasila per Level
    const questionsDB = {
        1: [
            { q: "Sila Pertama Pancasila disimbolkan dengan Permata Bintang...", opt: ["Topaz Emas", "Rantai Emas", "Pohon Beringin", "Kepala Banteng"], ans: 0 },
            { q: "Pohon Beringin melambangkan Sila ke-...", opt: ["Sila 1", "Sila 2", "Sila 3", "Sila 4"], ans: 2 },
            { q: "Bunyi Sila ke-2 adalah...", opt: ["Ketuhanan Yang Maha Esa", "Kemanusiaan yang adil dan beradab", "Persatuan Indonesia", "Keadilan Sosial"], ans: 1 },
            { q: "Simbol Padi dan Kapas melambangkan Sila ke-...", opt: ["Ketiga", "Keempat", "Kelima", "Kedua"], ans: 2 },
            { q: "Jumlah bulu pada sayap Burung Garuda Pancasila adalah...", opt: ["17", "8", "45", "19"], ans: 0 }
        ],
        2: [
            { q: "Menghormati orang lain yang sedang beribadah adalah pengamalan Sila ke-...", opt: ["Sila 1", "Sila 2", "Sila 3", "Sila 4"], ans: 0 },
            { q: "Melakukan musyawarah mufakat untuk mengambil keputusan bersama adalah nilai Sila...", opt: ["Sila 2", "Sila 3", "Sila 4", "Sila 5"], ans: 2 },
            { q: "Gotong royong dan menjaga persatuan bangsa mencerminkan Sila ke-...", opt: ["Sila 1", "Sila 2", "Sila 3", "Sila 5"], ans: 2 },
            { q: "Menjenguk teman sakit dan saling mencintai sesama manusia adalah Sila ke-...", opt: ["Sila 1", "Sila 2", "Sila 4", "Sila 5"], ans: 1 },
            { q: "Sikap adil dan menghargai hak-hak orang lain sesuai dengan Sila...", opt: ["Sila 2", "Sila 3", "Sila 4", "Sila 5"], ans: 3 },
            { q: "Bangga menggunakan bahasa nasional Indonesia merupakan wujud Sila ke-...", opt: ["Sila 1", "Sila 3", "Sila 4", "Sila 5"], ans: 1 },
            { q: "Suka bekerja keras dan tidak bergaya hidup mewah merupakan pengamalan Sila ke-...", opt: ["Sila 2", "Sila 3", "Sila 4", "Sila 5"], ans: 3 },
            { q: "Menjaga keseimbangan antara hak dan kewajiban merupakan sikap Sila ke-...", opt: ["Sila 2", "Sila 3", "Sila 4", "Sila 5"], ans: 3 }
        ],
        3: [
            { q: "Pancasila secara resmi disahkan sebagai Dasar Negara pada tanggal...", opt: ["17 Agustus 1945", "18 Agustus 1945", "1 Juni 1945", "22 Juni 1945"], ans: 1 },
            { q: "Istilah Pancasila pertama kali diusulkan oleh Ir. Soekarno pada tanggal...", opt: ["29 Mei 1945", "1 Juni 1945", "22 Juni 1945", "18 Agustus 1945"], ans: 1 },
            { q: "Semboyan 'Bhinneka Tunggal Ika' diambil dari Kitab Sutasoma karya...", opt: ["Mpu Prapanca", "Mpu Tantular", "Mpu Walmiki", "Mpu Sedah"], ans: 1 },
            { q: "Rumusan awal Pancasila oleh Panitia Sembilan tertuang dalam...", opt: ["Piagam Jakarta", "Trikora", "Dekrit Presiden", "UUD 1945"], ans: 0 },
            { q: "Pancasila sebagai 'Ideologi Terbuka' bermakna...", opt: ["Bebas diubah kapan saja", "Dapat menyesuaikan zaman tanpa mengubah nilai dasar", "Menerima semua budaya asing", "Tidak memiliki hukum mengikat"], ans: 1 },
            { q: "Sidang BPUPKI Pertama berfokus membahas...", opt: ["Teknis Proklamasi", "Rumusan Dasar Negara", "Pemilihan Presiden", "Wilayah Negara"], ans: 1 },
            { q: "Kedudukan Pancasila sebagai 'Sumber dari segala sumber hukum' ditetapkan dalam...", opt: ["Ketetapan MPR", "UUD 1945", "Keputusan Presiden", "Peraturan Pemerintah"], ans: 0 },
            { q: "Penetapan Hari Lahir Pancasila diperingati setiap tanggal...", opt: ["1 Juni", "17 Agustus", "1 Oktober", "28 Oktober"], ans: 0 },
            { q: "Tokoh yang menyampaikan usulan Dasar Negara selain Ir. Soekarno adalah...", opt: ["Moh. Yamin & Dr. Soepomo", "Sutan Sjahrir & Tan Malaka", "Moh. Hatta & Bung Tomo", "Ki Hajar Dewantara"], ans: 0 },
            { q: "Panitia Sembilan dibentuk setelah sidang BPUPKI Pertama untuk...", opt: ["Menyusun Teks Proklamasi", "Menyempurnakan rumusan Dasar Negara", "Memilih Presiden & Wapres", "Membentuk TNI"], ans: 1 }
        ]
    };

    // Game Variables
    let selectedDiff = 'mudah';
    let timePerQuestion = 60;
    let initialMoves = 25;
    let maxLives = 3;
    
    let currentLevel = 1;
    let score = 0;
    let moves = 25;
    let lives = 3;
    let questionsAnswered = 0;
    let targetQuestions = 5;
    
    let levelTimeLeft = 300;
    let levelTimerInterval = null;
    let quizTimerInterval = null;

    let grid = [];
    let board = document.getElementById('grid');
    let selectedTile = null;
    let isProcessing = false;

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    function setDiff(diff, btn) {
        selectedDiff = diff;
        document.querySelectorAll('.btn-diff').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');

        if (diff === 'mudah') { initialMoves = 25; maxLives = 3; }
        else if (diff === 'tinggi') { initialMoves = 15; maxLives = 2; }
    }

    function formatTime(seconds) {
        let mins = Math.floor(seconds / 60);
        let secs = seconds % 60;
        return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }

    function applyGemStyle(tile) {
        const symbol = tile.innerText;
        const index = gems.indexOf(symbol);
        
        gemClasses.forEach(cls => tile.classList.remove(cls));
        
        if (index !== -1) {
            tile.classList.add(gemClasses[index]);
        }
    }

    function startGame() {
        currentLevel = 1;
        score = 0;
        lives = maxLives;
        showScreen('screen-game');
        initLevel();
    }

    function initLevel() {
        moves = initialMoves;
        questionsAnswered = 0;
        
        if (currentLevel === 1) targetQuestions = 5;
        else if (currentLevel === 2) targetQuestions = 8;
        else if (currentLevel === 3) targetQuestions = 10;

        timePerQuestion = questionTimeLimits[currentLevel];
        levelTimeLeft = levelTimeLimits[currentLevel];
        
        startLevelTimer();
        updateUI();
        createBoard();
    }

    function startLevelTimer() {
        clearInterval(levelTimerInterval);
        levelTimerInterval = setInterval(() => {
            levelTimeLeft--;
            document.getElementById('val-level-time').innerText = formatTime(levelTimeLeft);

            if (levelTimeLeft <= 0) {
                clearInterval(levelTimerInterval);
                clearInterval(quizTimerInterval);
                document.getElementById('quiz-modal').classList.add('hidden');
                gameOver("⏳ Waktu Level Habis! Kamu tidak berhasil menyelesaikan level tepat waktu.");
            }
        }, 1000);
    }

    function updateUI() {
        document.getElementById('val-level').innerText = currentLevel;
        document.getElementById('val-score').innerText = score;
        document.getElementById('val-moves').innerText = moves;
        document.getElementById('val-target').innerText = `${questionsAnswered}/${targetQuestions}`;
        document.getElementById('val-level-time').innerText = formatTime(levelTimeLeft);
        
        let heartStr = "";
        for (let i = 0; i < maxLives; i++) {
            if (i < lives) heartStr += "❤️";
            else heartStr += "🖤";
        }
        document.getElementById('val-lives').innerText = heartStr;
    }

    /* MATCH-3 BOARD ENGINE */
    function createBoard() {
        grid = [];
        board.innerHTML = '';
        for (let i = 0; i < width * width; i++) {
            const tile = document.createElement('div');
            tile.classList.add('tile');
            tile.setAttribute('id', i);
            let randomGem = gems[Math.floor(Math.random() * gems.length)];
            tile.innerText = randomGem;
            tile.addEventListener('click', selectTile);
            applyGemStyle(tile);
            board.appendChild(tile);
            grid.push(tile);
        }
        checkMatchesSilently();
    }

    async function selectTile() {
        if (isProcessing || moves <= 0 || lives <= 0 || levelTimeLeft <= 0) return;

        if (!selectedTile) {
            selectedTile = this;
            selectedTile.classList.add('selected');
        } else {
            let firstTile = selectedTile;
            let secondTile = this;
            let firstId = parseInt(firstTile.id);
            let secondId = parseInt(secondTile.id);

            selectedTile.classList.remove('selected');
            selectedTile = null;

            let validMoves = [
                firstId - 1, firstId + 1,
                firstId - width, firstId + width
            ];

            if (firstId % width === 0 && secondId === firstId - 1) validMoves = validMoves.filter(x => x !== secondId);
            if ((firstId + 1) % width === 0 && secondId === firstId + 1) validMoves = validMoves.filter(x => x !== secondId);

            if (validMoves.includes(secondId)) {
                isProcessing = true;
                swapGems(firstTile, secondTile);

                let matchInfo = findAndMarkMatches();

                if (matchInfo.matchedIndices.length === 0) {
                    // Jika tidak ada match, kembalikan permata ke posisi semula
                    await sleep(200);
                    swapGems(firstTile, secondTile);
                    isProcessing = false;
                } else {
                    // Move Valid!
                    moves--;
                    updateUI();
                    await handleCascadeAndQuiz(matchInfo);
                }
            }
        }
    }

    function swapGems(tile1, tile2) {
        let temp = tile1.innerText;
        tile1.innerText = tile2.innerText;
        tile2.innerText = temp;
        applyGemStyle(tile1);
        applyGemStyle(tile2);
    }

    /* METODE AUTO-MATCH, AUTO-CLEAR & SKOR OTOMATIS */
    function findAndMarkMatches() {
        let matchedIndices = new Set();
        let matchedSymbol = null;

        // Cek Horisontal
        for (let r = 0; r < width; r++) {
            for (let c = 0; c < width - 2; c++) {
                let idx1 = r * width + c;
                let idx2 = r * width + (c + 1);
                let idx3 = r * width + (c + 2);
                let sym1 = grid[idx1].innerText;
                if (sym1 !== '' && sym1 === grid[idx2].innerText && sym1 === grid[idx3].innerText) {
                    matchedIndices.add(idx1);
                    matchedIndices.add(idx2);
                    matchedIndices.add(idx3);
                    matchedSymbol = sym1;
                }
            }
        }

        // Cek Vertikal
        for (let c = 0; c < width; c++) {
            for (let r = 0; r < width - 2; r++) {
                let idx1 = r * width + c;
                let idx2 = (r + 1) * width + c;
                let idx3 = (r + 2) * width + c;
                let sym1 = grid[idx1].innerText;
                if (sym1 !== '' && sym1 === grid[idx2].innerText && sym1 === grid[idx3].innerText) {
                    matchedIndices.add(idx1);
                    matchedIndices.add(idx2);
                    matchedIndices.add(idx3);
                    matchedSymbol = sym1;
                }
            }
        }

        return { matchedIndices: Array.from(matchedIndices), matchedSymbol };
    }

    function dropGems() {
        for (let c = 0; c < width; c++) {
            let colGems = [];
            for (let r = width - 1; r >= 0; r--) {
                let idx = r * width + c;
                if (grid[idx].innerText !== '') {
                    colGems.push(grid[idx].innerText);
                }
            }
            for (let r = width - 1; r >= 0; r--) {
                let idx = r * width + c;
                if (colGems.length > 0) {
                    grid[idx].innerText = colGems.shift();
                } else {
                    grid[idx].innerText = gems[Math.floor(Math.random() * gems.length)];
                }
                applyGemStyle(grid[idx]);
            }
        }
    }

    async function handleCascadeAndQuiz(initialMatchInfo) {
        let currentMatch = initialMatchInfo;
        let combo = 1;
        let mainMatchedSymbol = initialMatchInfo.matchedSymbol;

        while (currentMatch.matchedIndices.length > 0) {
            // 1. Animasi Menghilang & Tambah Skor
            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].classList.add('matched-pop');
            });

            // Tambah skor otomatis per permata (+30 poin per permata dikali Combo)
            let points = currentMatch.matchedIndices.length * 30 * combo;
            score += points;
            updateUI();

            await sleep(300); // Tunggu durasi animasi menghilang

            // Kosongkan Teks Permata yang Cocok
            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].innerText = '';
                grid[idx].classList.remove('matched-pop');
                applyGemStyle(grid[idx]);
            });

            await sleep(150);

            // 2. Permata di Atas Jatuh Mengisi Kotak Kosong
            dropGems();
            await sleep(250);

            // 3. Cek apakah ada pencocokan baru secara beruntun (Combo)
            currentMatch = findAndMarkMatches();
            if (currentMatch.matchedIndices.length > 0) {
                combo++;
            }
        }

        // Setelah semua permata yang cocok selesai dibersihkan & diisi:
        if (mainMatchedSymbol) {
            triggerQuiz(mainMatchedSymbol);
        } else {
            isProcessing = false;
        }
    }

    function checkMatchesSilently() {
        let matchInfo = findAndMarkMatches();
        while (matchInfo.matchedIndices.length > 0) {
            matchInfo.matchedIndices.forEach(idx => {
                grid[idx].innerText = gems[Math.floor(Math.random() * gems.length)];
                applyGemStyle(grid[idx]);
            });
            matchInfo = findAndMarkMatches();
        }
        score = 0;
        updateUI();
    }

    /* QUIZ SYSTEM */
    function triggerQuiz(symbol) {
        let qList = questionsDB[currentLevel];
        let randomQ = qList[Math.floor(Math.random() * qList.length)];

        document.getElementById('modal-tag').innerText = `MATCH PERMATA ${symbol}! JAWAB BENAR (${timePerQuestion}s) UNTUK BONUS SKOR + MOVES`;
        document.getElementById('quiz-question').innerText = randomQ.q;
        
        let optsDiv = document.getElementById('quiz-options');
        optsDiv.innerHTML = '';

        randomQ.opt.forEach((optText, idx) => {
            let btn = document.createElement('button');
            btn.className = 'opt-btn';
            btn.innerText = `${String.fromCharCode(65 + idx)}. ${optText}`;
            btn.onclick = () => handleQuizAnswer(idx === randomQ.ans, btn);
            optsDiv.appendChild(btn);
        });

        document.getElementById('quiz-modal').classList.remove('hidden');
        startQuizTimer();
    }

    function startQuizTimer() {
        let timerBar = document.getElementById('timer-bar');
        timerBar.style.width = '100%';
        let step = 100;
        let totalSteps = (timePerQuestion * 1000) / step;
        let currentStep = 0;

        clearInterval(quizTimerInterval);
        quizTimerInterval = setInterval(() => {
            currentStep++;
            let pct = Math.max(0, 100 - (currentStep / totalSteps) * 100);
            timerBar.style.width = pct + '%';

            if (pct <= 0) {
                clearInterval(quizTimerInterval);
                handleQuizAnswer(false, null);
            }
        }, step);
    }

    function handleQuizAnswer(isCorrect, btn) {
        clearInterval(quizTimerInterval);
        if (btn) btn.classList.add(isCorrect ? 'correct' : 'wrong');

        if (isCorrect) {
            score += 150;
            moves += 2;
            questionsAnswered++;
        } else {
            lives--;
        }

        updateUI();

        setTimeout(() => {
            document.getElementById('quiz-modal').classList.add('hidden');
            isProcessing = false;

            if (lives <= 0) {
                gameOver("💔 Nyawa Kamu Habis! Jawab soal kuis dengan lebih cermat.");
            } else if (questionsAnswered >= targetQuestions) {
                levelWin();
            } else if (moves <= 0) {
                gameOver("💥 Langkah Kamu Habis!");
            }
        }, 1000);
    }

    function levelWin() {
        clearInterval(levelTimerInterval);
        if (currentLevel < 3) {
            showScreen('screen-level-win');
            document.getElementById('win-score').innerText = `${score} Poin`;
            document.getElementById('btn-next-lvl').innerText = `Lanjut ke Level ${currentLevel + 1} ➡️`;
        } else {
            gameOver("SELAMAT! Kamu berhasil menamatkan seluruh Tantangan Permata Pancasila!", true);
        }
    }

    function nextLevel() {
        currentLevel++;
        showScreen('screen-game');
        initLevel();
    }

    function gameOver(msg, isVictory = false) {
        clearInterval(levelTimerInterval);
        clearInterval(quizTimerInterval);

        showScreen('screen-end');
        document.getElementById('end-title').innerText = isVictory ? "🏆 Champion Pancasila!" : "💥 GAME OVER";
        document.getElementById('end-desc').innerText = msg;
        document.getElementById('final-score').innerText = `${score} Poin`;

        let rank = "";
        if (score > 2500) rank = "🥇 Gelar: Duta Utama Garuda Pancasila";
        else if (score > 1500) rank = "🥈 Gelar: Pejuang Patriot Muda";
        else rank = "🥉 Gelar: Pertiwi Muda";

        document.getElementById('final-rank').innerText = rank;
    }

    function resetGame() {
        clearInterval(levelTimerInterval);
        clearInterval(quizTimerInterval);
        showScreen('screen-start');
    }

    function showScreen(screenId) {
        ['screen-start', 'screen-game', 'screen-level-win', 'screen-end'].forEach(id => {
            let el = document.getElementById(id);
            if(id === screenId) el.classList.remove('hidden');
            else el.classList.add('hidden');
        });
    }
</script>
</body>
</html>
"""

# Render Game di Streamlit
components.html(game_html, height=720, scrolling=False)
