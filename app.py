import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Nusantara Gem Crush",
    page_icon="💎",
    layout="centered"
)

# Custom Styling untuk Streamlit Container
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #0f0c20 100%);
    }
    .stAppHeader {
        background-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💎 Nusantara Gem Crush Saga")
st.caption("Cocokkan 3 atau lebih permata sejajar untuk mencetak skor tertinggi! Game khusus untuk Streamlit.")

# Kode Game HTML + CSS + JavaScript (Match-3 Engine)
game_html = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<style>
    * {
        box-sizing: border-box;
        user-select: none;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    body {
        margin: 0;
        padding: 10px;
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .score-board {
        display: flex;
        justify-content: space-around;
        width: 100%;
        max-width: 400px;
        margin-bottom: 15px;
        background: rgba(255, 255, 255, 0.1);
        padding: 10px 15px;
        border-radius: 12px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.1);
    }
    .score-box {
        text-align: center;
    }
    .score-title {
        font-size: 12px;
        text-transform: uppercase;
        color: #00d2d3;
        font-weight: bold;
    }
    .score-value {
        font-size: 24px;
        font-weight: bold;
        color: #fff;
    }
    #grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        grid-gap: 8px;
        background: rgba(0, 0, 0, 0.4);
        padding: 12px;
        border-radius: 16px;
        border: 2px solid #00d2d3;
        box-shadow: 0 0 20px rgba(0, 210, 211, 0.2);
    }
    .tile {
        width: 50px;
        height: 50px;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        cursor: pointer;
        transition: transform 0.2s, background 0.2s;
        border: 1px solid rgba(255,255,255,0.05);
    }
    .tile:hover {
        transform: scale(1.08);
        background: rgba(255, 255, 255, 0.2);
    }
    .tile.selected {
        border: 2px solid #ff9f43;
        transform: scale(1.1);
        box-shadow: 0 0 12px #ff9f43;
        animation: pulse 0.8s infinite alternate;
    }
    @keyframes pulse {
        0% { transform: scale(1.05); }
        100% { transform: scale(1.15); }
    }
    .btn {
        margin-top: 15px;
        padding: 10px 24px;
        background: linear-gradient(45deg, #ff6b6b, #ff8e53);
        border: none;
        color: white;
        font-weight: bold;
        font-size: 14px;
        border-radius: 25px;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
        transition: transform 0.2s;
    }
    .btn:hover {
        transform: translateY(-2px);
    }
    .game-over {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0,0,0,0.85);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 16px;
        z-index: 10;
    }
</style>
</head>
<body>

<div class="score-board">
    <div class="score-box">
        <div class="score-title">Skor</div>
        <div class="score-value" id="score">0</div>
    </div>
    <div class="score-box">
        <div class="score-title">Langkah</div>
        <div class="score-value" id="moves">20</div>
    </div>
</div>

<div id="grid"></div>

<button class="btn" onclick="resetGame()">🎮 Main Ulang</button>

<script>
    const width = 6;
    const gems = ['💎', '🌟', '🥑', '🔮', '🍎', '⚡'];
    let grid = [];
    let board = document.getElementById('grid');
    let scoreDisplay = document.getElementById('score');
    let movesDisplay = document.getElementById('moves');
    
    let score = 0;
    let moves = 20;
    let selectedTile = null;

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
        if (moves <= 0) return;

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

            // Cegah swap antar baris di pinggir
            if (firstId % width === 0 && secondId === firstId - 1) validMoves = validMoves.filter(x => x !== secondId);
            if ((firstId + 1) % width === 0 && secondId === firstId + 1) validMoves = validMoves.filter(x => x !== secondId);

            if (validMoves.includes(secondId)) {
                swapGems(selectedTile, this);
                moves--;
                movesDisplay.innerText = moves;
                
                setTimeout(() => {
                    let hasMatch = checkAndClearMatches();
                    if (!hasMatch) {
                        // Kembalikan jika tidak ada match
                        swapGems(selectedTile, this);
                        moves++;
                        movesDisplay.innerText = moves;
                    } else {
                        setTimeout(fillBoard, 300);
                    }
                    selectedTile.classList.remove('selected');
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
        let matched = false;

        // Cek Horisontal
        for (let i = 0; i < width * width; i++) {
            if (i % width < width - 2) {
                let row = [i, i+1, i+2];
                let decidedGem = grid[i].innerText;
                if (decidedGem !== '' && row.every(index => grid[index].innerText === decidedGem)) {
                    row.forEach(index => grid[index].innerText = '');
                    score += 30;
                    matched = true;
                }
            }
        }

        // Cek Vertikal
        for (let i = 0; i < width * (width - 2); i++) {
            let col = [i, i+width, i+width*2];
            let decidedGem = grid[i].innerText;
            if (decidedGem !== '' && col.every(index => grid[index].innerText === decidedGem)) {
                col.forEach(index => grid[index].innerText = '');
                score += 30;
                matched = true;
            }
        }

        scoreDisplay.innerText = score;
        return matched;
    }

    function fillBoard() {
        for (let i = 0; i < width * width; i++) {
            if (grid[i].innerText === '') {
                // Jatuhkan dari atas
                for (let k = i; k >= width; k -= width) {
                    grid[k].innerText = grid[k - width].innerText;
                }
                grid[i % width].innerText = gems[Math.floor(Math.random() * gems.length)];
            }
        }
        
        // Cek combo match beruntun
        setTimeout(() => {
            if (checkAndClearMatches()) {
                setTimeout(fillBoard, 300);
            } else if (moves <= 0) {
                alert("Game Selesai! Skor Akhir Anda: " + score);
            }
        }, 200);
    }

    function checkMatchesSilently() {
        while (checkAndClearMatches()) {
            for (let i = 0; i < width * width; i++) {
                if (grid[i].innerText === '') {
                    grid[i].innerText = gems[Math.floor(Math.random() * gems.length)];
                }
            }
        }
        score = 0;
        scoreDisplay.innerText = score;
    }

    function resetGame() {
        score = 0;
        moves = 20;
        scoreDisplay.innerText = score;
        movesDisplay.innerText = moves;
        selectedTile = null;
        createBoard();
    }

    createBoard();
</script>

</body>
</html>
"""

# Render Game HTML di Streamlit
components.html(game_html, height=520, scrolling=False)

# Informasi Tambahan
with st.expander("ℹ️ Cara Bermain"):
    st.write("""
    1. Klik salah satu **Permata (Gem)**.
    2. Klik permata di sebelahnya (atas, bawah, kiri, atau kanan) untuk menukar posisi.
    3. Jika terbentuk sejajar **3 permata atau lebih** yang sama, permata akan pecah dan menambah skor!
    4. Anda memiliki **20 Langkah** untuk meraih skor tertinggi.
    """)
