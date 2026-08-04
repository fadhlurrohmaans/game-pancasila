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
st.caption("Gunakan strategi terbaikmu! Menukar tanpa match akan mengurangi langkah, dan salah menjawab soal akan mengurangi nyawa.")

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
        background: linear-gradient(135deg, #600000, #2b0000);
        color: white;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.7);
        min-height: 640px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
    }
    .card {
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 16px;
        padding: 20px;
        width: 100%;
        max-width: 520px;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    h2 { color: #ffd700; margin-top: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
    
    /* Stats Bar */
    .stats-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        max-width: 490px;
        background: rgba(0,0,0,0.5);
        padding: 10px 12px;
        border-radius: 12px;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 215, 0, 0.2);
    }
    .stat-item { text-align: center; }
    .stat-title { font-size: 11px; color: #ffd700; font-weight: bold; text-transform: uppercase; }
    .stat-value { font-size: 16px; font-weight: bold; }

    /* Gem Grid */
    #grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        grid-gap: 6px;
        background: rgba(0, 0, 0, 0.5);
        padding: 10px;
        border-radius: 16px;
        border: 2px solid #ffd700;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.2);
    }
    .tile {
        width: 48px;
        height: 48px;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        cursor: pointer;
        transition: transform 0.2s, background 0.2s;
        border: 1px solid rgba(255,255,255,0.05);
    }
    .tile:hover { transform: scale(1.08); background: rgba(255, 255, 255, 0.2); }
    .tile.selected {
        border: 2px solid #ffd700;
        transform: scale(1.15);
        box-shadow: 0 0 12px #ffd700;
    }

    /* Quiz Modal Overlay */
    .modal-overlay {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.92);
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
    .btn-diff { background: rgba(255,255,255,0.1); width: 100%; max-width: 260px; }
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
    <p style="font-size: 13px;">Cocokkan Simbol Pancasila & Jawab Kuisnya!</p>
    
    <div style="margin: 15px 0;">
        <button class="btn btn-diff selected" onclick="setDiff('mudah', this)">🟢 Mudah (20s Soal | 25 Langkah | 3 ❤️)</button><br>
        <button class="btn btn-diff" onclick="setDiff('sedang', this)">🟡 Sedang (12s Soal | 20 Langkah | 3 ❤️)</button><br>
        <button class="btn btn-diff" onclick="setDiff('tinggi', this)">🔴 Tinggi (7s Soal | 15 Langkah | 2 ❤️)</button>
    </div>

    <div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px; font-size: 12px; margin-bottom: 15px; text-align: left;">
        ⚠️ <b>Aturan Baru:</b><br>
        • Menukar tanpa hasil match <u>TETAP mengurangi langkah</u>!<br>
        • Jawaban kuis salah / kehabisan waktu akan <u>mengurangi 1 Nyawa (❤️)</u>.<br>
        • Kehabisan langkah atau nyawa = <b>Game Over</b>.
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
    <p id="win-desc">Selamat! Kamu berhasil menuntaskan tantangan level ini.</p>
    <div style="font-size: 32px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="win-score">0 Poin</div>
    <button class="btn" id="btn-next-lvl" onclick="nextLevel()">Lanjut Level Berikutnya ➡️</button>
</div>

<!-- SCREEN 4: GAME OVER / TAMAT -->
<div class="card hidden" id="screen-end">
    <h2 id="end-title">💥 GAME OVER</h2>
    <p id="end-desc" style="font-size: 14px; color: #ff6b6b; font-weight: bold;">Kehabisan Langkah / Nyawa!</p>
    <div style="font-size: 36px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="final-score">0 Poin</div>
    <div style="font-weight: bold; color: #4caf50; font-size: 16px; margin-bottom: 15px;" id="final-rank"></div>
    <button class="btn" onclick="resetGame()">Main Lagi 🔄</button>
</div>

<script>
    const width = 6;
    const gems = ['⭐', '⛓️', '🌳', '🐂', '🌾', '🦅'];
    
    // Database Soal Pancasila per Level
    const questionsDB = {
        1: [
            { q: "Sila Pertama Pancasila disimbolkan dengan...", opt: ["Bintang Emas", "Rantai Emas", "Pohon Beringin", "Kepala Banteng"], ans: 0 },
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
            { q: "Suka bekerja keras dan tidak bergaya hidup mewah merupakan pengamalan Sila ke-...", opt: ["Sila 2", "Sila 3", "Sila 4", "Sila 5"], ans: 3 }
        ],
        3: [
            { q: "Pancasila secara resmi disahkan sebagai Dasar Negara pada tanggal...", opt: ["17 Agustus 1945", "18 Agustus 1945", "1 Juni 1945", "22 Juni 1945"], ans: 1 },
            { q: "Istilah Pancasila pertama kali diusulkan oleh Ir. Soekarno pada tanggal...", opt: ["29 Mei 1945", "1 Juni 1945", "22 Juni 1945", "18 Agustus 1945"], ans: 1 },
            { q: "Semboyan 'Bhinneka Tunggal Ika' diambil dari Kitab Sutasoma karya...", opt: ["Mpu Prapanca", "Mpu Tantular", "Mpu Walmiki", "Mpu Sedah"], ans: 1 },
            { q: "Rumusan awal Pancasila oleh Panitia Sembilan tertuang dalam...", opt: ["Piagam Jakarta", "Trikora", "Dekrit Presiden", "UUD 1945"], ans: 0 },
            { q: "Pancasila sebagai 'Ideologi Terbuka' bermakna...", opt: ["Bebas diubah kapan saja", "Dapat menyesuaikan zaman tanpa mengubah nilai dasar", "Menerima semua budaya asing", "Tidak memiliki hukum mengikat"], ans: 1 },
            { q: "Sidang BPUPKI Pertama berfokus membahas...", opt: ["Teknis Proklamasi", "Rumusan Dasar Negara", "Pemilihan Presiden", "Wilayah Negara"], ans: 1 },
            { q: "Kedudukan Pancasila sebagai 'Sumber dari segala sumber hukum' ditetapkan dalam...", opt: ["Ketetapan MPR", "UUD 1945", "Keputusan Presiden", "Peraturan Pemerintah"], ans: 0 },
            { q: "Penetapan Hari Lahir Pancasila diperingati setiap tanggal...", opt: ["1 Juni", "17 Agustus", "1 Oktober", "28 Oktober"], ans: 0 }
        ]
    };

    // Game Variables
    let selectedDiff = 'mudah';
    let timePerQuestion = 20;
    let initialMoves = 25;
    let maxLives = 3;
    
    let currentLevel = 1;
    let score = 0;
    let moves = 25;
    let lives = 3;
    let questionsAnswered = 0;
    let targetQuestions = 5;
    
    let grid = [];
    let board = document.getElementById('grid');
    let selectedTile = null;
    let isProcessing = false;
    let timerInterval = null;

    function setDiff(diff, btn) {
        selectedDiff = diff;
        document.querySelectorAll('.btn-diff').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');

        if (diff === 'mudah') { timePerQuestion = 20; initialMoves = 25; maxLives = 3; }
        else if (diff === 'sedang') { timePerQuestion = 12; initialMoves = 20; maxLives = 3; }
        else if (diff === 'tinggi') { timePerQuestion = 7; initialMoves = 15; maxLives = 2; }
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
        else if (currentLevel === 3) targetQuestions = 12;

        updateUI();
        createBoard();
    }

    function updateUI() {
        document.getElementById('val-level').innerText = currentLevel;
        document.getElementById('val-score').innerText = score;
        document.getElementById('val-moves').innerText = moves;
        document.getElementById('val-target').innerText = `${questionsAnswered}/${targetQuestions}`;
        
        // Render Hearts
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
            board.appendChild(tile);
            grid.push(tile);
        }
        checkMatchesSilently();
    }

    function selectTile() {
        if (isProcessing || moves <= 0 || lives <= 0) return;

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
                
                // LANGKAH SELALU BERKURANG KETIKA TUKAR
                moves--;
                updateUI();
                
                setTimeout(() => {
                    let matchSymbol = checkAndClearMatches();
                    if (!matchSymbol) {
                        // JIKA TIDAK MATCH: Kembalikan posisi permata, TAPI moves TIDAK dikembalikan!
                        swapGems(selectedTile, this);
                        updateUI();

                        // Cek jika langkah habis setelah swap gagal
                        if (moves <= 0) {
                            gameOver("💥 Langkah Kamu Habis! Hati-hati menukar permata tanpa match.");
                        }
                    } else {
                        // JIKA MATCH: Panggil Kuis!
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
    }

    function checkAndClearMatches() {
        let matchedSymbol = null;

        // Cek Horisontal
        for (let i = 0; i < width * width; i++) {
            if (i % width < width - 2) {
                let row = [i, i+1, i+2];
                let decided = grid[i].innerText;
                if (decided !== '' && row.every(idx => grid[idx].innerText === decided)) {
                    row.forEach(idx => grid[idx].innerText = '');
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
                col.forEach(idx => grid[idx].innerText = '');
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
                }
                grid[i % width].innerText = gems[Math.floor(Math.random() * gems.length)];
            }
        }
    }

    function checkMatchesSilently() {
        while (checkAndClearMatches()) {
            for (let i = 0; i < width * width; i++) {
                if (grid[i].innerText === '') grid[i].innerText = gems[Math.floor(Math.random() * gems.length)];
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

        document.getElementById('modal-tag').innerText = `MATCH ${symbol}! JAWAB BENAR UNTUK BONUS SKOR + MOVES`;
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

        clearInterval(timerInterval);
        timerInterval = setInterval(() => {
            currentStep++;
            let pct = Math.max(0, 100 - (currentStep / totalSteps) * 100);
            timerBar.style.width = pct + '%';

            if (pct <= 0) {
                clearInterval(timerInterval);
                handleQuizAnswer(false, null);
            }
        }, step);
    }

    function handleQuizAnswer(isCorrect, btn) {
        clearInterval(timerInterval);
        if (btn) btn.classList.add(isCorrect ? 'correct' : 'wrong');

        if (isCorrect) {
            score += 150;
            moves += 2; // Bonus +2 langkah jika benar
            questionsAnswered++;
        } else {
            lives--; // NYAWA BERKURANG JIKA SALAH / WAKTU HABIS
        }

        updateUI();

        setTimeout(() => {
            document.getElementById('quiz-modal').classList.add('hidden');
            fillBoard();
            isProcessing = false;

            // CEK SYARAT GAME OVER ATAU MENANG
            if (lives <= 0) {
                gameOver("💔 Nyawa Kamu Habis! Jawab soal kuis dengan lebih teliti.");
            } else if (questionsAnswered >= targetQuestions) {
                levelWin();
            } else if (moves <= 0) {
                gameOver("💥 Langkah Kamu Habis!");
            }
        }, 1000);
    }

    function levelWin() {
        if (currentLevel < 3) {
            showScreen('screen-level-win');
            document.getElementById('win-score').innerText = `${score} Poin`;
            document.getElementById('btn-next-lvl').innerText = `Lanjut ke Level ${currentLevel + 1} ➡️`;
        } else {
            gameOver("SELAMAT! Kamu berhasil menamatkan seluruh Tantangan Pancasila!", true);
        }
    }

    function nextLevel() {
        currentLevel++;
        showScreen('screen-game');
        initLevel();
    }

    function gameOver(msg, isVictory = false) {
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
components.html(game_html, height=660, scrolling=False)

# Panduan Petualangan
with st.expander("🎮 Cara Bermain & Aturan Baru"):
    st.write("""
    - **Sistem Nyawa (❤️):** Kamu memiliki 3 Nyawa. Jika salah menjawab kuis atau waktu habis, **Nyawa akan berkurang 1**.
    - **Langkah Berkurang Saat Swap Gagal:** Setiap kali menukar permata, **1 Langkah langsung berkurang** meskipun penukaran tersebut *tidak menghasilkan match*.
    - **Bonus Langkah (+2 Moves):** Menjawab soal kuis dengan **Benar** memberikan bonus **+2 Langkah** tambahan dan **+150 Skor**!
    - **Game Over:** Terjadi jika **Nyawa Habis (0 ❤️)** atau **Langkah Habis (0 Moves)**.
    """)
