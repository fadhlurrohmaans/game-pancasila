import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Nusantara Gem Crush: Sejarah Pancasila Quest",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling CSS Streamlit untuk Tampilan Layar Penuh
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

# Single Bundle Engine HTML5 + CSS + JavaScript
game_html = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">

<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-database-compat.js"></script>

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
    
    .input-field {
        width: 100%;
        padding: 10px 14px;
        border-radius: 8px;
        border: 1.5px solid rgba(255, 215, 0, 0.6);
        background: rgba(0, 0, 0, 0.6);
        color: #fff;
        font-size: 14px;
        outline: none;
        margin-top: 4px;
        margin-bottom: 12px;
    }
    .input-field:focus {
        border-color: #ffd700;
        box-shadow: 0 0 8px rgba(255, 215, 0, 0.5);
    }

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

    .tile:active { transform: scale(0.92); }

    .tile.selected {
        border: 2px solid #ffffff !important;
        transform: scale(1.12);
        box-shadow: 0 0 18px #ffd700, inset 0 0 8px #ffffff !important;
        z-index: 10;
        animation: pulse-gem 0.8s infinite alternate;
    }

    .tile.matched-pop {
        transform: scale(0) rotate(180deg) !important;
        opacity: 0 !important;
        filter: brightness(2) !important;
    }

    @keyframes pulse-gem {
        0% { filter: brightness(1); transform: scale(1.08); }
        100% { filter: brightness(1.35); transform: scale(1.15); }
    }

    .gem-topaz { background: linear-gradient(135deg, #ffe066, #d4af37, #8a7300); }
    .gem-sapphire { background: linear-gradient(135deg, #4dabf7, #1971c2, #0c365e); }
    .gem-emerald { background: linear-gradient(135deg, #51cf66, #2b8a3e, #123b1a); }
    .gem-ruby { background: linear-gradient(135deg, #ff6b6b, #c92a2a, #5c0b0b); }
    .gem-amber { background: linear-gradient(135deg, #ffc078, #d9480f, #7a2200); }
    .gem-amethyst { background: linear-gradient(135deg, #cc5de8, #862e9c, #3b0d48); }

    .modal-overlay {
        position: fixed;
        top: 0; left: 0;
        right: 0; bottom: 0;
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

    .opt-btn {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white; padding: 12px; border-radius: 10px;
        text-align: left; font-size: 13px; cursor: pointer;
        margin-bottom: 8px;
        width: 100%; transition: all 0.2s;
    }
    .opt-btn:active { background: rgba(255, 215, 0, 0.3); border-color: #ffd700; }
    .opt-btn.correct { background: #2e7d32 !important; }
    .opt-btn.wrong { background: #c62828 !important; }

    .hidden { display: none !important; }

    /* STYLING TABEL LEADERBOARD GLOBAL */
    .leaderboard-box {
        margin-top: 14px;
        background: rgba(0, 0, 0, 0.5);
        padding: 10px;
        border-radius: 12px;
        border: 1px solid rgba(255, 215, 0, 0.35);
    }
    .leaderboard-title {
        font-size: 13px;
        color: #ffd700;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .leaderboard-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 11px;
    }
    .leaderboard-table th {
        background: rgba(255, 215, 0, 0.25);
        color: #ffd700;
        padding: 6px 4px;
        text-align: left;
    }
    .leaderboard-table td {
        padding: 5px 4px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        text-align: left;
    }
    .leaderboard-table tr:nth-child(1) td { color: #ffd700; font-weight: bold; }
    .leaderboard-table tr:nth-child(2) td { color: #e0e0e0; font-weight: bold; }
    .leaderboard-table tr:nth-child(3) td { color: #cd7f32; font-weight: bold; }
</style>
</head>
<body>

<div class="card" id="screen-start">
    <h2>🦅 Nusantara Gem Crush</h2>
    <p style="font-size: 12px; color: #ffe066; margin-bottom: 14px;">Petualangan Kuis Kelahiran Pancasila</p>
    
    <div style="text-align: left; margin-bottom: 8px;">
        <label style="font-size: 12px; color: #ffd700; font-weight: bold;">Nama Lengkap Siswa:</label>
        <input type="text" id="input-nama" class="input-field" placeholder="Ketik nama kamu di sini...">

        <label style="font-size: 12px; color: #ffd700; font-weight: bold;">Kelas:</label>
        <input type="text" id="input-kelas" class="input-field" placeholder="Contoh: VII A / VIII B...">
    </div>

    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 10px; font-size: 11px; margin-bottom: 14px; text-align: left; border: 1px solid rgba(255, 215, 0, 0.2);">
        📜 <b>Materi & Aturan Main:</b><br>
        • Materi: <b>BPUPK (Lvl 1), Panitia 9 (Lvl 2), PPKI (Lvl 3)</b>.<br>
        • Tersedia <b>50 varian soal</b> pada tiap level.<br>
        • Modal: <b>25 Moves</b> & <b>3 Nyawa (❤️)</b> per Level.<br>
        • Jawaban Salah / Waktu Habis = <b>Nyawa (❤️) Berkurang 1</b>.
    </div>

    <button class="btn" style="font-size: 16px;" onclick="startGame()">Mulai Petualangan 🚀</button>

    <div class="leaderboard-box">
        <div class="leaderboard-title">🏆 TOP 10 SKOR GLOBAL</div>
        <div id="leaderboard-start-list">
            <p style="font-size:11px; color:#aaa; margin:4px 0;">Memuat skor global...</p>
        </div>
    </div>
</div>

<div id="screen-game" class="hidden" style="display:flex; flex-direction:column; align-items:center; width: 100%;">
    <div style="font-size: 11px; color: #ffe066; margin-bottom: 6px; font-weight: bold;" id="player-banner">
        Siswa: - | Kelas: -
    </div>

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
            <div class="stat-value" id="val-score" style="color:#51cf66;">0</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Moves</div>
            <div class="stat-value" id="val-moves" style="color:#4dabf7;">25</div>
        </div>
        <div class="stat-item">
            <div class="stat-title">Target</div>
            <div class="stat-value" id="val-target" style="color:#ffd700;">0/5</div>
        </div>
    </div>

    <div id="grid"></div>
</div>

<div class="modal-overlay hidden" id="quiz-modal">
    <div style="width: 100%; max-width: 440px; text-align: center;">
        <div style="font-size: 11px; color: #ffd700; font-weight: bold;" id="modal-tag">KUIS KELAHIRAN PANCASILA</div>
        <div class="timer-bar-container"><div class="timer-bar" id="timer-bar"></div></div>
        <h3 id="quiz-question" style="font-size: 14px; margin: 10px 0 15px 0; min-height: 40px; line-height: 1.4;">Pertanyaan...</h3>
        <div id="quiz-options"></div>
    </div>
</div>

<div class="card hidden" id="screen-level-win">
    <h2>🎉 Level Selesai!</h2>
    <p id="win-desc" style="font-size: 13px;">Selamat! Kamu berhasil menjawab target soal kuis tepat waktu.</p>
    <div style="font-size: 26px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="win-score">0 Poin</div>
    <button class="btn" id="btn-next-lvl" onclick="nextLevel()">Lanjut Level Berikutnya ➡️</button>
</div>

<div class="card hidden" id="screen-end">
    <h2 id="end-title">💥 GAME OVER</h2>
    <div style="font-size: 13px; color: #ffe066; font-weight: bold; margin-bottom: 6px;" id="final-player-info"></div>
    <p id="end-desc" style="font-size: 12px; color: #ff6b6b; font-weight: bold;">Gagal menyelesaikan tantangan!</p>
    <div style="font-size: 30px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="final-score">0 Poin</div>
    <div style="font-weight: bold; color: #4caf50; font-size: 14px; margin-bottom: 15px;" id="final-rank"></div>

    <div class="leaderboard-box">
        <div class="leaderboard-title">🏆 TOP 10 SKOR GLOBAL</div>
        <div id="leaderboard-end-list">
            <p style="font-size:11px; color:#aaa; margin:4px 0;">Memuat skor global...</p>
        </div>
    </div>

    <button class="btn" style="margin-top:15px;" onclick="resetGame()">Main Lagi 🔄</button>
</div>

<script>
    // ================================================================
    // ⚙️ KONFIGURASI FIREBASE REALTIME DATABASE (TOP SKOR GLOBAL)
    // Silakan ganti kredensial di bawah ini dengan milik Firebase Anda!
    // ================================================================
    const firebaseConfig = {
       apiKey: "AIzaSyAp3nx1FKqL9FxwKDqMUBk-OXgePUXyn0w",
    authDomain: "gamepancasila.firebaseapp.com",
    databaseURL: "https://gamepancasila-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "gamepancasila",
    storageBucket: "gamepancasila.firebasestorage.app",
    messagingSenderId: "780384650353",
    appId: "1:780384650353:web:d72fd5c121c01089bdc7d0",
    measurementId: "G-B4GPSRKP6B"
    };

    let db = null;
    try {
        if (!firebase.apps.length) {
            firebase.initializeApp(firebaseConfig);
        }
        db = firebase.database();
    } catch(e) {
        console.warn("Firebase belum diatur / bermasalah:", e);
    }

    // Fungsi Mengirim Skor ke Database Global
    function submitGlobalScore(nama, kelas, totalSkor) {
        if (!db || totalSkor <= 0) return;
        try {
            db.ref('leaderboard').push({
                nama: nama,
                kelas: kelas,
                score: totalSkor,
                timestamp: Date.now()
            });
        } catch(e) {
            console.error("Gagal menyimpan skor global:", e);
        }
    }

    // Fungsi Mengambil & Menampilkan Top Skor Global
    function fetchGlobalLeaderboard() {
        const startList = document.getElementById('leaderboard-start-list');
        const endList = document.getElementById('leaderboard-end-list');

        if (!db) {
            const warningMsg = "<p style='font-size:11px; color:#ffe066;'>Isi firebaseConfig untuk mengaktifkan leaderboard global online.</p>";
            if(startList) startList.innerHTML = warningMsg;
            if(endList) endList.innerHTML = warningMsg;
            return;
        }

        try {
            db.ref('leaderboard').orderByChild('score').limitToLast(10).on('value', (snapshot) => {
                let data = [];
                snapshot.forEach((child) => {
                    data.push(child.val());
                });
                data.reverse(); // Urutkan dari tertinggi ke terendah

                if (data.length === 0) {
                    const emptyMsg = "<p style='font-size:11px; color:#aaa;'>Belum ada skor tercatat. Jadilah yang pertama!</p>";
                    if(startList) startList.innerHTML = emptyMsg;
                    if(endList) endList.innerHTML = emptyMsg;
                    return;
                }

                let html = `<table class="leaderboard-table">
                    <thead>
                        <tr>
                            <th style="width:12%;">#</th>
                            <th style="width:48%;">Nama</th>
                            <th style="width:20%;">Kelas</th>
                            <th style="width:20%; text-align:right;">Skor</th>
                        </tr>
                    </thead>
                    <tbody>`;

                data.forEach((item, idx) => {
                    let medal = idx === 0 ? '🥇' : idx === 1 ? '🥈' : idx === 2 ? '🥉' : `${idx + 1}.`;
                    html += `<tr>
                        <td>${medal}</td>
                        <td>${item.nama || 'Anonim'}</td>
                        <td>${item.kelas || '-'}</td>
                        <td style="text-align:right; font-weight:bold; color:#ffd700;">${item.score}</td>
                    </tr>`;
                });

                html += `</tbody></table>`;

                if(startList) startList.innerHTML = html;
                if(endList) endList.innerHTML = html;
            });
        } catch(e) {
            console.error("Gagal memuat leaderboard:", e);
        }
    }

    // ================================================================
    // LOGIKA GAME SCRIPT
    // ================================================================
    const width = 6;
    const gems = ['🌟', '⛓️', '🌳', '🐂', '🌾', '🦅'];
    const gemClasses = ['gem-topaz', 'gem-sapphire', 'gem-emerald', 'gem-ruby', 'gem-amber', 'gem-amethyst'];

    const levelTimeLimits = { 1: 300, 2: 240, 3: 180 };
    const questionTimeLimits = { 1: 45, 2: 30, 3: 20 };

    // Bank Soal Kuis (BPUPK, Panitia 9, PPKI)
    const questionsDB = {
        1: [
            { q: "BPUPK secara resmi dibentuk oleh pemerintah pendudukan Jepang pada tanggal...", opt: ["1 Maret 1945", "29 April 1945", "1 Juni 1945", "17 Agustus 1945"], ans: 0 },
            { q: "Pelantikan pengurus BPUPK secara resmi dilaksanakan pada tanggal...", opt: ["28 Mei 1945", "1 Maret 1945", "22 Juni 1945", "18 Agustus 1945"], ans: 0 },
            { q: "Siapakah Ketua (Kaichou) utama dari BPUPK?", opt: ["Dr. K.R.T. Radjiman Wedyodiningrat", "Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Soepomo"], ans: 0 },
            { q: "Nama BPUPK dalam bahasa Jepang dinamakan...", opt: ["Dokuritsu Junbi Cosakai", "Dokuritsu Junbi Inkai", "Heiho", "Rikugun"], ans: 0 },
            { q: "Tokoh Jepang yang ditunjuk menjadi Wakil Ketua (Fuku Kaichou) BPUPK adalah...", opt: ["Ichibangase Yosio", "Maeda Tadashi", "Terauchi Hisaichi", "Kumakichi Harada"], ans: 0 },
            { q: "Tokoh Indonesia yang menjabat sebagai Wakil Ketua BPUPK mendampingi perwakilan Jepang adalah...", opt: ["R.P. Soeroso", "Mr. Mohammad Yamin", "K.H. A. Wahid Hasjim", "Achmad Soebardjo"], ans: 0 },
            { q: "Sidang Pertama BPUPK berlangsung dari tanggal...", opt: ["29 Mei - 1 Juni 1945", "10 - 17 Juli 1945", "22 - 25 Juni 1945", "17 - 18 Agustus 1945"], ans: 0 },
            { q: "Sidang Pertama BPUPK diselenggarakan di gedung Chuo Sangi In, yang saat ini dikenal sebagai...", opt: ["Gedung Pancasila", "Gedung Merdeka", "Gedung Agung", "Istana Negara"], ans: 0 },
            { q: "Agenda utama pembahasan dalam Sidang Pertama BPUPK adalah perumusan...", opt: ["Dasar Negara", "Teks Proklamasi", "Rancangan Undang-Undang Dasar", "Lambang Negara"], ans: 0 },
            { q: "Tokoh pertama yang menyampaikan usulan dasar negara secara lisan pada tanggal 29 Mei 1945 adalah...", opt: ["Mr. Mohammad Yamin", "Mr. Soepomo", "Ir. Soekarno", "Drs. Mohammad Hatta"], ans: 0 }
        ],
        2: [
            { q: "Panitia Sembilan dibentuk pada masa reses BPUPK, yaitu pada tanggal...", opt: ["22 Juni 1945", "1 Juni 1945", "10 Juli 1945", "17 Agustus 1945"], ans: 0 },
            { q: "Tugas utama dari Panitia Sembilan adalah...", opt: ["Menyelaraskan usulan dasar negara dan menyusun rancangan Pembukaan UUD", "Menyiapkan naskah proklamasi", "Memilih Presiden dan Wakil Presiden", "Membentuk komite nasional daerah"], ans: 0 },
            { q: "Siapakah yang bertindak sebagai Ketua Panitia Sembilan?", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Muhammad Yamin", "K.H. A. Wahid Hasjim"], ans: 0 }
        ],
        3: [
            { q: "PPKI secara resmi dibentuk oleh pihak Jepang pada tanggal...", opt: ["7 Agustus 1945", "18 Agustus 1945", "1 Maret 1945", "17 Agustus 1945"], ans: 0 },
            { q: "Sidang pertama PPKI pasca proklamasi kemerdekaan dilaksanakan pada tanggal...", opt: ["18 Agustus 1945", "17 Agustus 1945", "19 Agustus 1945", "22 Agustus 1945"], ans: 0 },
            { q: "Salah satu keputusan paling krusial dalam Sidang PPKI 18 Agustus 1945 adalah...", opt: ["Mengesahkan UUD 1945 dan penetapan Pancasila sebagai Dasar Negara", "Membentuk Tentara Nasional Indonesia", "Menetapkan lagu Indonesia Raya", "Memilih para menteri kabinet"], ans: 0 }
        ]
    };

    let playerNama = "";
    let playerKelas = "";
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

    function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

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
        let namaInput = document.getElementById('input-nama').value.trim();
        let kelasInput = document.getElementById('input-kelas').value.trim();

        if (!namaInput || !kelasInput) {
            alert('Silakan isi Nama dan Kelas terlebih dahulu sebelum memulai permainan!');
            return;
        }

        playerNama = namaInput;
        playerKelas = kelasInput;
        document.getElementById('player-banner').innerText = `👤 Siswa: ${playerNama} | 🏫 Kelas: ${playerKelas}`;

        currentLevel = 1;
        score = 0;
        lives = 3;
        showScreen('screen-game');
        initLevel();
    }

    function initLevel() {
        moves = 25;
        questionsAnswered = 0;
        levelTimeLeft = levelTimeLimits[currentLevel] || 300;
        
        updateUI();
        createBoard();
        startLevelTimer();
    }

    function updateUI() {
        document.getElementById('val-lives').innerText = '❤️'.repeat(lives) || '💀';
        document.getElementById('val-level').innerText = currentLevel;
        document.getElementById('val-level-time').innerText = formatTime(levelTimeLeft);
        document.getElementById('val-score').innerText = score;
        document.getElementById('val-moves').innerText = moves;
        document.getElementById('val-target').innerText = `${questionsAnswered}/${targetQuestions}`;
    }

    function startLevelTimer() {
        clearInterval(levelTimerInterval);
        levelTimerInterval = setInterval(() => {
            levelTimeLeft--;
            document.getElementById('val-level-time').innerText = formatTime(levelTimeLeft);
            if (levelTimeLeft <= 0) {
                clearInterval(levelTimerInterval);
                gameOver("⏳ Waktu Level Habis!");
            }
        }, 1000);
    }

    function createBoard() {
        board.innerHTML = '';
        grid = [];
        for (let i = 0; i < width * width; i++) {
            let tile = document.createElement('div');
            tile.classList.add('tile');
            tile.id = i;
            tile.innerText = gems[Math.floor(Math.random() * gems.length)];
            applyGemStyle(tile);
            tile.addEventListener('click', selectTile);
            board.appendChild(tile);
            grid.push(tile);
        }
        checkMatchesSilently();
    }

    function checkMatchesSilently() {
        for (let i = 0; i < width * width; i++) {
            if (i % width < width - 2) {
                if (grid[i].innerText === grid[i+1].innerText && grid[i].innerText === grid[i+2].innerText) {
                    grid[i].innerText = gems[Math.floor(Math.random() * gems.length)];
                    applyGemStyle(grid[i]);
                }
            }
        }
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

            let validMoves = [ firstId - 1, firstId + 1, firstId - width, firstId + width ];
            if (firstId % width === 0 && secondId === firstId - 1) validMoves = validMoves.filter(x => x !== secondId);
            if ((firstId + 1) % width === 0 && secondId === firstId + 1) validMoves = validMoves.filter(x => x !== secondId);

            if (validMoves.includes(secondId)) {
                isProcessing = true;
                swapGems(firstTile, secondTile);
                moves--;
                updateUI();

                let matchInfo = findAndMarkMatches();
                if (matchInfo.matchedIndices.length === 0) {
                    await sleep(200);
                    swapGems(firstTile, secondTile);
                    if (moves <= 0) {
                        gameOver("💥 Langkah (Moves) Kamu Habis!");
                    } else {
                        isProcessing = false;
                    }
                } else {
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

    function findAndMarkMatches() {
        let matchedIndices = new Set();
        let matchedSymbol = "";

        // Baris
        for (let r = 0; r < width; r++) {
            for (let c = 0; c < width - 2; c++) {
                let idx = r * width + c;
                let symbol = grid[idx].innerText;
                if (symbol && symbol === grid[idx+1].innerText && symbol === grid[idx+2].innerText) {
                    matchedIndices.add(idx); matchedIndices.add(idx+1); matchedIndices.add(idx+2);
                    matchedSymbol = symbol;
                }
            }
        }

        // Kolom
        for (let c = 0; c < width; c++) {
            for (let r = 0; r < width - 2; r++) {
                let idx = r * width + c;
                let symbol = grid[idx].innerText;
                if (symbol && symbol === grid[idx-width] ? false : (symbol && symbol === grid[idx+width].innerText && symbol === grid[idx+width*2].innerText)) {
                    matchedIndices.add(idx); matchedIndices.add(idx+width); matchedIndices.add(idx+width*2);
                    matchedSymbol = symbol;
                }
            }
        }

        return { matchedIndices: Array.from(matchedIndices), matchedSymbol: matchedSymbol };
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

        while (currentMatch.matchedIndices.length > 0) {
            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].classList.add('matched-pop');
            });

            let points = currentMatch.matchedIndices.length * 30 * combo;
            score += points;
            updateUI();

            await sleep(300);

            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].innerText = '';
                grid[idx].classList.remove('matched-pop');
                applyGemStyle(grid[idx]);
            });

            await sleep(150);
            dropGems();
            await sleep(250);

            currentMatch = findAndMarkMatches();
            combo++;
        }

        triggerQuiz();
    }

    function triggerQuiz() {
        let questions = questionsDB[currentLevel] || questionsDB[1];
        let qObj = questions[Math.floor(Math.random() * questions.length)];

        document.getElementById('modal-tag').innerText = `KUIS LEVEL ${currentLevel} - SEJARAH PANCASILA`;
        document.getElementById('quiz-question').innerText = qObj.q;

        let optionsContainer = document.getElementById('quiz-options');
        optionsContainer.innerHTML = '';

        let indices = [0, 1, 2, 3];
        indices.sort(() => Math.random() - 0.5);

        indices.forEach(idx => {
            let btn = document.createElement('button');
            btn.classList.add('opt-btn');
            btn.innerText = qObj.opt[idx];
            btn.onclick = () => handleAnswer(idx === qObj.ans, btn);
            optionsContainer.appendChild(btn);
        });

        document.getElementById('quiz-modal').classList.remove('hidden');

        let timeMax = questionTimeLimits[currentLevel] || 30;
        let timeRemaining = timeMax;
        let timerBar = document.getElementById('timer-bar');
        timerBar.style.width = '100%';

        clearInterval(quizTimerInterval);
        quizTimerInterval = setInterval(() => {
            timeRemaining -= 0.1;
            let percent = (timeRemaining / timeMax) * 100;
            timerBar.style.width = `${percent}%`;

            if (timeRemaining <= 0) {
                clearInterval(quizTimerInterval);
                handleAnswer(false, null);
            }
        }, 100);
    }

    function handleAnswer(isCorrect, clickedBtn) {
        clearInterval(quizTimerInterval);

        if (clickedBtn) {
            if (isCorrect) clickedBtn.classList.add('correct');
            else clickedBtn.classList.add('wrong');
        }

        setTimeout(() => {
            document.getElementById('quiz-modal').classList.add('hidden');
            if (isCorrect) {
                questionsAnswered++;
                score += 150;
                updateUI();
            } else {
                lives--;
                updateUI();
                if (lives <= 0) {
                    gameOver("💀 Nyawa Kamu Habis!");
                    return;
                }
            }

            isProcessing = false;

            if (questionsAnswered >= targetQuestions) {
                levelWin();
            } else if (moves <= 0) {
                gameOver("💥 Langkah (Moves) Kamu Habis!");
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
            gameOver("🏆 Selamat! Kamu telah menyelesaikan seluruh Petualangan Pancasila!", true);
        }
    }

    function nextLevel() {
        currentLevel++;
        showScreen('screen-game');
        initLevel();
    }

    // FUNGSI GAME OVER & SIMPAN SKOR GLOBAL
    function gameOver(msg, isVictory = false) {
        clearInterval(levelTimerInterval);
        clearInterval(quizTimerInterval);

        showScreen('screen-end');
        document.getElementById('end-title').innerText = isVictory ? "🏆 Champion Sejarah Pancasila!" : "💥 GAME OVER";
        document.getElementById('final-player-info').innerText = `Siswa: ${playerNama} | Kelas: ${playerKelas}`;
        document.getElementById('end-desc').innerText = msg;
        document.getElementById('final-score').innerText = `${score} Poin`;

        let rank = "";
        if (score > 2500) rank = "🥇 Gelar: Ahli Sejarah Pancasila";
        else if (score > 1500) rank = "🥈 Gelar: Pejuang Patriot Muda";
        else rank = "🥉 Gelar: Pelajar Pancasila";

        document.getElementById('final-rank').innerText = rank;

        // KIRIM SKOR KE LEADERBOARD GLOBAL IF SKOR > 0
        if (score > 0 && playerNama) {
            submitGlobalScore(playerNama, playerKelas, score);
        }
        
        // REFRESH TABEL LEADERBOARD
        fetchGlobalLeaderboard();
    }

    function resetGame() {
        clearInterval(levelTimerInterval);
        clearInterval(quizTimerInterval);
        showScreen('screen-start');
        fetchGlobalLeaderboard();
    }

    function showScreen(screenId) {
        ['screen-start', 'screen-game', 'screen-level-win', 'screen-end'].forEach(id => {
            let el = document.getElementById(id);
            if(id === screenId) el.classList.remove('hidden');
            else el.classList.add('hidden');
        });
    }

    // Muat leaderboard saat pertama kali aplikasi dibuka
    window.onload = fetchGlobalLeaderboard;
</script>
</body>
</html>
"""

# Tampilkan Aplikasi Game di Streamlit
components.html(game_html, height=880, scrolling=True)
