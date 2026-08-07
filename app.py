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

# Single Bundle Engine HTML5 + CSS + JavaScript (Pure Match-3 Fast Cascade)
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
        grid-template-columns: repeat(5, 1fr);
        gap: 4px;
        width: 100%;
        max-width: 480px;
        background: rgba(0,0,0,0.65);
        padding: 10px 6px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    .stat-item { text-align: center; }
    .stat-title { font-size: 10px; color: #ffd700; font-weight: bold; text-transform: uppercase; }
    .stat-value { font-size: 13px; font-weight: bold; white-space: nowrap; }

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

    .hidden { display: none !important; }
</style>
</head>
<body>

<!-- SCREEN 1: START & DIFFICULTY -->
<div class="card" id="screen-start">
    <h2>🦅 Nusantara Gem Crush</h2>
    <p style="font-size: 12px; color: #ffe066; margin-bottom: 12px;">Petualangan Permata Pancasila</p>
    
    <div style="margin: 10px 0;">
        <button class="btn btn-diff selected" onclick="setDiff('mudah', this)">🟢 Mode Normal (25 Langkah)</button><br>
        <button class="btn btn-diff" onclick="setDiff('tinggi', this)">🔴 Mode Tantangan (15 Langkah)</button>
    </div>

    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 10px; font-size: 11px; margin-bottom: 14px; text-align: left; border: 1px solid rgba(255, 215, 0, 0.2);">
        🎯 <b>Target Level & Waktu:</b><br>
        • Level 1: <b>500 Poin</b> (Waktu: 5 Menit)<br>
        • Level 2: <b>1.200 Poin</b> (Waktu: 4 Menit)<br>
        • Level 3: <b>2.500 Poin</b> (Waktu: 3 Menit)<br>
        ⚠️ Waktu Habis / Langkah Habis = <b>GAME OVER</b>!
    </div>

    <button class="btn" style="font-size: 16px;" onclick="startGame()">Mulai Petualangan 🚀</button>
</div>

<!-- SCREEN 2: GAME BOARD -->
<div id="screen-game" class="hidden" style="display:flex; flex-direction:column; align-items:center; width: 100%;">
    <div class="stats-bar">
        <div class="stat-item">
            <div class="stat-title">Lvl</div>
            <div class="stat-value" id="val-level" style="color:#ffd700;">1</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Waktu</div>
            <div class="stat-value" id="val-level-time" style="color:#ff9f43;">05:00</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Moves</div>
            <div class="stat-value" id="val-moves" style="color:#4dabf7;">25</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Skor</div>
            <div class="stat-value" id="val-score" style="color:#51cf66;">0</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Target</div>
            <div class="stat-value" id="val-target" style="color:#ffd700;">500</div>
        </div>
    </div>

    <div id="grid"></div>
</div>

<!-- SCREEN 3: LEVEL COMPLETE -->
<div class="card hidden" id="screen-level-win">
    <h2>🎉 Level Selesai!</h2>
    <p id="win-desc" style="font-size: 13px;">Selamat! Kamu berhasil mencapai target skor tepat waktu.</p>
    <div style="font-size: 30px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="win-score">0 Poin</div>
    <button class="btn" id="btn-next-lvl" onclick="nextLevel()">Lanjut Level Berikutnya ➡️</button>
</div>

<!-- SCREEN 4: GAME OVER / TAMAT -->
<div class="card hidden" id="screen-end">
    <h2 id="end-title">💥 GAME OVER</h2>
    <p id="end-desc" style="font-size: 13px; color: #ff6b6b; font-weight: bold;">Gagal mencapai target skor!</p>
    <div style="font-size: 32px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="final-score">0 Poin</div>
    <div style="font-weight: bold; color: #4caf50; font-size: 15px; margin-bottom: 15px;" id="final-rank"></div>
    <button class="btn" onclick="resetGame()">Main Lagi 🔄</button>
</div>

<script>
    const width = 6;
    
    // Simbol Permata Pancasila
    const gems = ['🌟', '⛓️', '🌳', '🐂', '🌾', '🦅'];
    const gemClasses = ['gem-topaz', 'gem-sapphire', 'gem-emerald', 'gem-ruby', 'gem-amber', 'gem-amethyst'];

    // Target Skor per Level
    const targetScores = { 1: 500, 2: 1200, 3: 2500 };

    // Waktu Level dalam detik (Lvl 1: 5m/300s, Lvl 2: 4m/240s, Lvl 3: 3m/180s)
    const levelTimeLimits = { 1: 300, 2: 240, 3: 180 };

    // Game Variables
    let selectedDiff = 'mudah';
    let initialMoves = 25;
    
    let currentLevel = 1;
    let score = 0;
    let moves = 25;
    let targetScore = 500;
    
    let levelTimeLeft = 300;
    let levelTimerInterval = null;

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

        if (diff === 'mudah') { initialMoves = 25; }
        else if (diff === 'tinggi') { initialMoves = 15; }
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
        showScreen('screen-game');
        initLevel();
    }

    function initLevel() {
        moves = initialMoves;
        targetScore = targetScores[currentLevel];
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
                gameOver("⏳ Waktu Level Habis! Kamu tidak berhasil mencapai target tepat waktu.");
            }
        }, 1000);
    }

    function updateUI() {
        document.getElementById('val-level').innerText = currentLevel;
        document.getElementById('val-score').innerText = score;
        document.getElementById('val-moves').innerText = moves;
        document.getElementById('val-target').innerText = targetScore;
        document.getElementById('val-level-time').innerText = formatTime(levelTimeLeft);
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
        if (isProcessing || moves <= 0 || levelTimeLeft <= 0) return;

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
                
                // Tukar Posisi Permata
                swapGems(firstTile, secondTile);

                // PENGURANGAN MOVES OTOMATIS: 1 Move Terpotong Setiap Melangkah
                moves--;
                updateUI();

                let matchInfo = findAndMarkMatches();

                if (matchInfo.matchedIndices.length === 0) {
                    // Jika TIDAK MATCH: Kembalikan permata ke posisi awal
                    await sleep(200);
                    swapGems(firstTile, secondTile);
                    
                    if (moves <= 0 && score < targetScore) {
                        gameOver("💥 Langkah Kamu Habis!");
                    } else {
                        isProcessing = false;
                    }
                } else {
                    // Jika MATCH: Jalankan cascade otomatis
                    await handleCascade(matchInfo);
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
                }
            }
        }

        return { matchedIndices: Array.from(matchedIndices) };
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

    async function handleCascade(initialMatchInfo) {
        let currentMatch = initialMatchInfo;
        let combo = 1;

        while (currentMatch.matchedIndices.length > 0) {
            // 1. Animasi Menghilang & Tambah Skor
            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].classList.add('matched-pop');
            });

            // Tambah skor otomatis (+30 poin per permata x Combo)
            let points = currentMatch.matchedIndices.length * 30 * combo;
            score += points;
            updateUI();

            await sleep(300); // Tunggu animasi pecah

            // Kosongkan Teks Permata yang Cocok
            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].innerText = '';
                grid[idx].classList.remove('matched-pop');
                applyGemStyle(grid[idx]);
            });

            await sleep(150);

            // 2. Permata Jatuh Mengisi Kotak Kosong
            dropGems();
            await sleep(250);

            // 3. Cek combo lanjutan
            currentMatch = findAndMarkMatches();
            if (currentMatch.matchedIndices.length > 0) {
                combo++;
            }
        }

        isProcessing = false;

        // CEK KONDISI MENANG / KALAH
        if (score >= targetScore) {
            levelWin();
        } else if (moves <= 0) {
            gameOver("💥 Langkah Kamu Habis!");
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

        showScreen('screen-end');
        document.getElementById('end-title').innerText = isVictory ? "🏆 Champion Pancasila!" : "💥 GAME OVER";
        document.getElementById('end-desc').innerText = msg;
        document.getElementById('final-score').innerText = `${score} Poin`;

        let rank = "";
        if (score >= 3000) rank = "🥇 Gelar: Duta Utama Garuda Pancasila";
        else if (score >= 1500) rank = "🥈 Gelar: Pejuang Patriot Muda";
        else rank = "🥉 Gelar: Pertiwi Muda";

        document.getElementById('final-rank').innerText = rank;
    }

    function resetGame() {
        clearInterval(levelTimerInterval);
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
