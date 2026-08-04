import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Nusantara Gem Crush: Pancasila Quest",
    page_icon="🦅",
    layout="centered"
)

# Custom Styling Background Streamlit
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1f0003 0%, #0d0001 100%);
    }
    .stAppHeader { background-color: transparent; }
    </style>
""", unsafe_allow_html=True)

st.title("🦅 Nusantara Gem Crush: Pancasila Quest")
st.caption("Cocokkan Permata Pancasila & Jawab Kuis Sebelum Waktu Level Habis!")

# Single Bundle Engine HTML5 + CSS + JavaScript
game_html = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<style>
    * {
        box-sizing: border-box;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        user-select: none;
    }
    body {
        margin: 0;
        padding: 10px;
        background: linear-gradient(135deg, #4a0000, #1a0000);
        color: white;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        min-height: 660px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
    }
    .card {
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(255, 215, 0, 0.4);
        border-radius: 16px;
        padding: 20px;
        width: 100%;
        max-width: 520px;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    h2 { color: #ffd700; margin-top: 0; text-shadow: 0 2px 6px rgba(0,0,0,0.6); }
    
    /* Stats Bar */
    .stats-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        max-width: 500px;
        background: rgba(0,0,0,0.6);
        padding: 8px 10px;
        border-radius: 12px;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    .stat-item { text-align: center; flex: 1; }
    .stat-title { font-size: 10px; color: #ffd700; font-weight: bold; text-transform: uppercase; }
    .stat-value { font-size: 14px; font-weight: bold; }

    /* Gem Grid */
    #grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        grid-gap: 8px;
        background: rgba(15, 5, 5, 0.8);
        padding: 12px;
        border-radius: 18px;
        border: 2px solid #ffd700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.25), inset 0 0 15px rgba(0,0,0,0.8);
    }

    /* === BASE PERMATA / TILE STYLING === */
    .tile {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s, filter 0.2s;
        border: 2px solid rgba(255, 255, 255, 0.35);
        box-shadow: inset -2px -3px 6px rgba(0,0,0,0.6), inset 2px 2px 5px rgba(255,255,255,0.6), 0 4px 8px rgba(0,0,0,0.5);
        position: relative;
        overflow: hidden;
    }

    /* Pantulan Kilau Kristal pada Permata */
    .tile::before {
        content: '';
        position: absolute;
        top: 2px;
        left: 4px;
        right: 4px;
        height: 38%;
        background: linear-gradient(to bottom, rgba(255,255,255,0.55), rgba(255,255,255,0.05));
        border-radius: 8px 8px 100% 100%;
        pointer-events: none;
    }

    .tile:hover {
        transform: scale(1.12);
        filter: brightness(1.2);
        z-index: 5;
    }

    /* Efek Permata Terpilih */
    .tile.selected {
        border: 3px solid #ffffff !important;
        transform: scale(1.18);
        box-shadow: 0 0 20px #ffd700, inset 0 0 10px #ffffff !important;
        z-index: 10;
        animation: pulse-gem 0.8s infinite alternate;
    }

    @keyframes pulse-gem {
        0% { filter: brightness(1); transform: scale(1.15); }
        100% { filter: brightness(1.35); transform: scale(1.22); }
    }

    /* === WARNA & EFEK KHUSUS SETIAP PERMATA PANCASILA === */
    .gem-topaz { 
        background: linear-gradient(135deg, #ffe066, #d4af37, #8a7300); 
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.7), inset -2px -3px 6px rgba(0,0,0,0.6), inset 2px 2px 5px rgba(255,255,255,0.8);
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    .gem-sapphire { 
        background: linear-gradient(135deg, #4dabf7, #1971c2, #0c365e); 
        box-shadow: 0 0 10px rgba(25, 113, 194, 0.7), inset -2px -3px 6px rgba(0,0,0,0.6), inset 2px 2px 5px rgba(255,255,255,0.8);
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    .gem-emerald { 
        background: linear-gradient(135deg, #51cf66, #2b8a3e, #123b1a); 
        box-shadow: 0 0 10px rgba(43, 138, 62, 0.7), inset -2px -3px 6px rgba(0,0,0,0.6), inset 2px 2px 5px rgba(255,255,255,0.8);
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    .gem-ruby { 
        background: linear-gradient(135deg, #ff6b6b, #c92a2a, #5c0b0b); 
        box-shadow: 0 0 10px rgba(201, 42, 42, 0.7), inset -2px -3px 6px rgba(0,0,0,0.6), inset 2px 2px 5px rgba(255,255,255,0.8);
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    .gem-amber { 
        background: linear-gradient(135deg, #ffc078, #d9480f, #7a2200); 
        box-shadow: 0 0 10px rgba(217, 72, 15, 0.7), inset -2px -3px 6px rgba(0,0,0,0.6), inset 2px 2px 5px rgba(255,255,255,0.8);
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    .gem-amethyst { 
        background: linear-gradient(135deg, #cc5de8, #862e9c, #3b0d48); 
        box-shadow: 0 0 10px rgba(134, 46, 156, 0.7), inset -2px -3px 6px rgba(0,0,0,0.6), inset 2px 2px 5px rgba(255,255,255,0.8);
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }

    /* Quiz Modal Overlay */
    .modal-overlay {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.93);
        border-radius: 16px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
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
        padding: 10px 20px; font-size: 15px; font-weight: bold;
        border-radius: 25px; cursor: pointer; transition: all 0.2s;
        margin: 5px;
    }
    .btn:hover { transform: translateY(-2px); background: linear-gradient(45deg, #f44336, #d32f2f); }
    .btn-diff { background: rgba(255,255,255,0.1); width: 100%; max-width: 270px; }
    .btn-diff.selected { background: #ffd700; color: #800000; font-weight: bold; }

    .opt-btn {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white; padding: 10px 12px; border-radius: 10px;
        text-align: left; font-size: 14px; cursor: pointer; margin-bottom: 8px;
        width: 100%; transition: all 0.2s;
    }
    .opt-btn:hover { background: rgba(255, 215, 0, 0.3); border-color: #ffd700; }
    .opt-btn.correct { background: #2e7d32 !important; }
    .opt-btn.wrong { background: #c62828 !important; }

    .hidden { display: none !important; }
</style>
</head>
<body>

<!-- SCREEN 1: START & DIFFICULTY -->
<div class="card" id="screen-start">
    <h2>🦅 Nusantara Gem Crush</h2>
    <p style="font-size: 13px; color: #ffe066;">Permata Pancasila Quest</p>
    
    <div style="margin: 10px 0;">
        <button class="btn btn-diff selected" onclick="setDiff('mudah', this)">🟢 Mode Normal (25 Langkah | 3 ❤️)</button><br>
        <button class="btn btn-diff" onclick="setDiff('tinggi', this)">🔴 Mode Tantangan (15 Langkah | 2 ❤️)</button>
    </div>

    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 10px; font-size: 12px; margin-bottom: 12px; text-align: left; border: 1px solid rgba(255, 215, 0, 0.2);">
        💎 <b>Batasan Waktu Level & Soal:</b><br>
        • Level 1: <b>5 Menit</b> (Target: 5 Soal | 60s/soal)<br>
        • Level 2: <b>4 Menit</b> (Target: 8 Soal | 30s/soal)<br>
        • Level 3: <b>3 Menit</b> (Target: 10 Soal | 18s/soal)<br>
        ⚠️ Waktu Habis / Nyawa Habis / Langkah Habis = <b>GAME OVER</b>!
    </div>

    <button class="btn" style="width: 80%; font-size: 17px;" onclick="startGame()">Mulai Petualangan 🚀</button>
</div>

<!-- SCREEN 2: GAME BOARD -->
<div id="screen-game" class="hidden" style="display:flex; flex-direction:column; align-items:center;">
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
            <div class="stat-title">Waktu Level</div>
            <div class="stat-value" id="val-level-time" style="color:#ff9f43;">05:00</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Skor</div>
            <div class="stat-value" id="val-score">0</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Langkah</div>
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
    <div style="width: 100%; max-width: 450px; text-align: center;">
        <div style="font-size: 12px; color: #ffd700; font-weight: bold;" id="modal-tag">CHALLENGE PANCASILA</div>
        <div class="timer-bar-container"><div class="timer-bar" id="timer-bar"></div></div>
        <h3 id="quiz-question" style="font-size: 15px; margin: 10px 0 15px 0; min-height: 45px;">Pertanyaan...</h3>
        <div id="quiz-options"></div>
    </div>
</div>

<!-- SCREEN 3: LEVEL COMPLETE -->
<div class="card hidden" id="screen-level-win">
    <h2>🎉 Level Selesai!</h2>
    <p id="win-desc">Selamat! Kamu berhasil menuntaskan tantangan permata level ini tepat waktu.</p>
    <div style="font-size: 32px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="win-score">0 Poin</div>
    <button class="btn" id="btn-next-lvl" onclick="nextLevel()">Lanjut Level Berikutnya ➡️</button>
</div>

<!-- SCREEN 4: GAME OVER / TAMAT -->
<div class="card hidden" id="screen-end">
    <h2 id="end-title">💥 GAME OVER</h2>
    <p id="end-desc" style="font-size: 14px; color: #ff6b6b; font-weight: bold;">Gagal menyelesaikan tantangan!</p>
    <div style="font-size: 36px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="final-score">0 Poin</div>
    <div style="font-weight: bold; color: #4caf50; font-size: 16px; margin-bottom: 15px;" id="final-rank"></div>
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
        
        // Bersihkan kelas permata terdahulu
        gemClasses.forEach(cls => tile.classList.remove(cls));
        
        // Terapkan kelas permata baru
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

    /* MATCH-3 LOGIC */
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

    function selectTile() {
        if (isProcessing || moves <= 0 || lives <= 0 || levelTimeLeft <= 0) return;

        if (!selectedTile) {
            selectedTile = this;
            selectedTile.classList.add('selected');
        } else {
            let firstId = parseInt(selectedTile.id);
            let secondId = parseInt(this.id);

            let validMoves = [
                firstId - 1, firstId + 1,
                firstId - width, firstId + width
            ];

            if (firstId % width === 0 && secondId === firstId - 1) validMoves = validMoves.filter(x => x !== secondId);
            if ((firstId + 1) % width === 0 && secondId === firstId + 1) validMoves = validMoves.filter(x => x !== secondId);

            if (validMoves.includes(secondId)) {
                swapGems(selectedTile, this);
                
                moves--;
                updateUI();
                
                setTimeout(() => {
                    let matchSymbol = checkAndClearMatches();
                    if (!matchSymbol) {
                        swapGems(selectedTile, this);
                        updateUI();

                        if (moves <= 0) {
                            gameOver("💥 Langkah Kamu Habis! Hati-hati menukar permata tanpa match.");
                        }
                    } else {
                        triggerQuiz(matchSymbol);
                    }
                    if (selectedTile) selectedTile.classList.remove('selected');
                    selectedTile = null;
                }, 200);

            } else {
                selectedTile.classList.remove('selected');
                selectedTile = this;
                selectedTile.classList.add('selected');
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

    function checkAndClearMatches() {
        let matchedSymbol = null;

        // Cek Horisontal
        for (let i = 0; i < width * width; i++) {
            if (i % width < width - 2) {
                let row = [i, i+1, i+2];
                let decided = grid[i].innerText;
                if (decided !== '' && row.every(idx => grid[idx].innerText === decided)) {
                    row.forEach(idx => {
                        grid[idx].innerText = '';
                        applyGemStyle(grid[idx]);
                    });
                    score += 50;
                    matchedSymbol = decided;
                }
            }
        }

        // Cek Vertikal
        for (let i = 0; i < width * (width - 2); i++) {
            let col = [i, i+width, i+width*2];
            let decided = grid[i].innerText;
            if (decided !== '' && col.every(idx => grid[idx].innerText === decided)) {
                col.forEach(idx => {
                    grid[idx].innerText = '';
                    applyGemStyle(grid[idx]);
                });
                score += 50;
                matchedSymbol = decided;
            }
        }

        return matchedSymbol;
    }

    function fillBoard() {
        for (let i = 0; i < width * width; i++) {
            if (grid[i].innerText === '') {
                for (let k = i; k >= width; k -= width) {
                    grid[k].innerText = grid[k - width].innerText;
                    applyGemStyle(grid[k]);
                }
                grid[i % width].innerText = gems[Math.floor(Math.random() * gems.length)];
                applyGemStyle(grid[i % width]);
            }
        }
    }

    function checkMatchesSilently() {
        while (checkAndClearMatches()) {
            for (let i = 0; i < width * width; i++) {
                if (grid[i].innerText === '') {
                    grid[i].innerText = gems[Math.floor(Math.random() * gems.length)];
                    applyGemStyle(grid[i]);
                }
            }
        }
        score = 0;
        updateUI();
    }

    /* QUIZ SYSTEM */
    function triggerQuiz(symbol) {
        isProcessing = true;
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
            fillBoard();
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
components.html(game_html, height=670, scrolling=False)

# Panduan Petualangan
with st.expander("💎 Koleksi Permata Pancasila & Aturan Game"):
    st.write("""
    - **Tipe Permata Pancasila:**
      - 🌟 **Topaz Emas:** Bintang Pancasila (Sila 1)
      - ⛓️ **Safir Biru:** Rantai Pancasila (Sila 2)
      - 🌳 **Zamrud Hijau:** Pohon Beringin (Sila 3)
      - 🐂 **Rubi Merah:** Kepala Banteng (Sila 4)
      - 🌾 **Amber Oranye:** Padi & Kapas (Sila 5)
      - 🦅 **Ametis Ungu:** Lambang Garuda Pancasila
    - **Batasan Waktu Level & Soal:**
      - **Level 1:** ⏳ 5 Menit — Target: **5 Soal** (60 Detik/soal)
      - **Level 2:** ⏳ 4 Menit — Target: **8 Soal** (30 Detik/soal)
      - **Level 3:** ⏳ 3 Menit — Target: **10 Soal** (18 Detik/soal)
    """)
