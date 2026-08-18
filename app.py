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
        background: linear-gradient(-45deg, #4a0000, #1a0000, #310015, #0a0002);
        background-size: 400% 400%;
        animation: gradientBg 12s ease infinite;
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
    }

    @keyframes gradientBg {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .card {
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(255, 215, 0, 0.5);
        border-radius: 16px;
        padding: 16px;
        width: 100%;
        max-width: 480px;
        text-align: center;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(255, 215, 0, 0.15), 0 8px 25px rgba(0,0,0,0.8);
        animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    h2 { 
        color: #ffd700;
        margin-top: 0; 
        font-size: clamp(20px, 5vw, 26px);
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.6), 0 2px 6px rgba(0,0,0,0.8);
        animation: glowHeader 2.5s ease-in-out infinite alternate;
    }

    @keyframes glowHeader {
        0% { text-shadow: 0 0 5px #ffd700, 0 0 10px #ffd700; }
        100% { text-shadow: 0 0 15px #ffd700, 0 0 25px #ff4500, 0 0 35px #ff4500; }
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
        transition: all 0.3s ease;
    }
    .input-field:focus {
        border-color: #ffd700;
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.8);
    }

    .stats-bar {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 4px;
        width: 100%;
        max-width: 480px;
        background: rgba(0,0,0,0.75);
        padding: 8px 4px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid rgba(255, 215, 0, 0.4);
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5), 0 0 15px rgba(255, 215, 0, 0.1);
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
        background: rgba(15, 5, 5, 0.9);
        padding: 8px;
        border-radius: 16px;
        border: 2px solid #ffd700;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.35), inset 0 0 15px rgba(0,0,0,0.9);
        position: relative;
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
        transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.2s ease, filter 0.15s;
        border: 1.5px solid rgba(255, 255, 255, 0.4);
        box-shadow: inset -2px -3px 5px rgba(0,0,0,0.6), inset 2px 2px 4px rgba(255,255,255,0.6), 0 4px 8px rgba(0,0,0,0.5);
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
        background: linear-gradient(to bottom, rgba(255,255,255,0.6), rgba(255,255,255,0.05));
        border-radius: 6px 6px 100% 100%;
        pointer-events: none;
    }

    .tile:active { transform: scale(0.9); }

    .tile.selected {
        border: 2.5px solid #ffffff !important;
        transform: scale(1.15);
        box-shadow: 0 0 22px #ffd700, 0 0 10px #ffffff, inset 0 0 10px #ffffff !important;
        z-index: 10;
        animation: pulse-gem 0.6s infinite alternate ease-in-out;
    }

    .tile.matched-pop {
        transform: scale(1.4) rotate(180deg) !important;
        opacity: 0 !important;
        filter: brightness(2.5) drop-shadow(0 0 15px #ffd700) !important;
        transition: all 0.3s ease-out;
    }

    @keyframes pulse-gem {
        0% { filter: brightness(1); transform: scale(1.08); }
        100% { filter: brightness(1.4); transform: scale(1.18); }
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
        background: rgba(0, 0, 0, 0.92);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 16px;
        z-index: 100;
        backdrop-filter: blur(8px);
    }
    .modal-overlay > div {
        animation: popIn 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .timer-bar-container {
        width: 100%;
        height: 8px;
        background: rgba(255,255,255,0.2);
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 12px;
        box-shadow: inset 0 0 4px rgba(0,0,0,0.5);
    }
    .timer-bar { 
        height: 100%; 
        background: linear-gradient(90deg, #ff4500, #ffd700); 
        width: 100%; 
        box-shadow: 0 0 10px #ffd700;
    }
    
    .btn {
        background: linear-gradient(45deg, #d32f2f, #b71c1c);
        color: white; border: 1.5px solid #ffd700;
        padding: 12px 20px; font-size: 15px; font-weight: bold;
        border-radius: 25px; cursor: pointer; 
        transition: all 0.25s ease;
        margin: 6px;
        width: 100%;
        max-width: 300px;
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.4), 0 0 10px rgba(255, 215, 0, 0.2);
    }
    .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(211, 47, 47, 0.6), 0 0 15px rgba(255, 215, 0, 0.5);
    }
    .btn:active { transform: scale(0.96); }

    .opt-btn {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: white; padding: 12px; border-radius: 10px;
        text-align: left; font-size: 13px; cursor: pointer;
        margin-bottom: 8px;
        width: 100%; transition: all 0.2s;
    }
    .opt-btn:hover {
        background: rgba(255, 215, 0, 0.25);
        border-color: #ffd700;
    }
    .opt-btn:active { background: rgba(255, 215, 0, 0.4); border-color: #ffd700; }
    .opt-btn.correct { background: #2e7d32 !important; box-shadow: 0 0 15px #4caf50; }
    .opt-btn.wrong { background: #c62828 !important; box-shadow: 0 0 15px #f44336; }

    .hidden { display: none !important; }

    /* TABEL LEADERBOARD GLOBAL */
    .leaderboard-box {
        margin-top: 14px;
        background: rgba(0, 0, 0, 0.55);
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

    /* ANIMASI DYNAMIC LENGKAP */
    @keyframes popIn {
        from { opacity: 0; transform: scale(0.85); }
        to { opacity: 1; transform: scale(1); }
    }

    .shake {
        animation: shakeAnim 0.35s ease-in-out;
    }
    @keyframes shakeAnim {
        0%, 100% { transform: translate(0, 0); }
        20% { transform: translate(-8px, 4px); }
        40% { transform: translate(8px, -4px); }
        60% { transform: translate(-5px, 2px); }
        80% { transform: translate(5px, -2px); }
    }

    .floating-text {
        position: absolute;
        font-weight: 900;
        font-size: 22px;
        color: #ffd700;
        text-shadow: 0 0 10px #ff9f43, 0 0 20px #ff4500, 0 2px 4px #000;
        pointer-events: none;
        animation: floatUp 0.85s ease-out forwards;
        z-index: 999;
    }
    @keyframes floatUp {
        0% { opacity: 1; transform: translateY(0) scale(0.8); }
        50% { opacity: 1; transform: translateY(-25px) scale(1.3); }
        100% { opacity: 0; transform: translateY(-50px) scale(1); }
    }
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
    <div style="width: 100%; max-width: 440px; text-align: center;" class="card">
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
                data.reverse();

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

    const width = 6;
    const gems = ['🌟', '⛓️', '🌳', '🐂', '🌾', '🦅'];
    const gemClasses = ['gem-topaz', 'gem-sapphire', 'gem-emerald', 'gem-ruby', 'gem-amber', 'gem-amethyst'];

    const levelTimeLimits = { 1: 300, 2: 240, 3: 180 };
    const questionTimeLimits = { 1: 45, 2: 30, 3: 20 };

    // BANK SOAL DENGAN Rincian KEDALAMAN HISTORIS TINGGI
    const questionsDB = {
        1: [
{ q: "BPUPK secara resmi dibentuk oleh pemerintah pendudukan Jepang pada tanggal...", opt: ["1 Maret 1945", "29 April 1945", "1 Juni 1945", "17 Agustus 1945"], ans: 0 },
{ q: "Pelantikan pengurus BPUPK secara resmi dilaksanakan pada tanggal...", opt: ["1 Maret 1945", "28 Mei 1945", "22 Juni 1945", "18 Agustus 1945"], ans: 1 },
{ q: "Siapakah Ketua (Kaichou) utama dari BPUPK?", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Dr. K.R.T. Radjiman Wedyodiningrat", "Mr. Soepomo"], ans: 2 },
{ q: "Nama BPUPK dalam bahasa Jepang dinamakan...", opt: ["Dokuritsu Junbi Inkai", "Heiho", "Chuo Sangi In", "Dokuritsu Junbi Cosakai"], ans: 3 },
{ q: "Tokoh Jepang yang ditunjuk menjadi Wakil Ketua (Fuku Kaichou) BPUPK adalah...", opt: ["Ichibangase Yosio", "Maeda Tadashi", "Terauchi Hisaichi", "Kumakichi Harada"], ans: 0 },
{ q: "Tokoh Indonesia yang menjabat sebagai Wakil Ketua BPUPK mendampingi perwakilan Jepang adalah...", opt: ["Mr. Mohammad Yamin", "R.P. Soeroso", "K.H. A. Wahid Hasjim", "Achmad Soebardjo"], ans: 1 },
{ q: "Sidang Pertama BPUPK berlangsung dari tanggal...", opt: ["10 - 17 Juli 1945", "22 - 25 Juni 1945", "29 Mei - 1 Juni 1945", "17 - 18 Agustus 1945"], ans: 2 },
{ q: "Sidang Pertama BPUPK diselenggarakan di gedung Chuo Sangi In, yang saat ini dikenal sebagai...", opt: ["Gedung Merdeka", "Gedung Agung", "Istana Negara", "Gedung Pancasila"], ans: 3 },
{ q: "Agenda utama pembahasan dalam Sidang Pertama BPUPK adalah perumusan...", opt: ["Dasar Negara", "Teks Proklamasi", "Rancangan Undang-Undang Dasar", "Lambang Negara"], ans: 0 },
{ q: "Tokoh pertama yang menyampaikan usulan dasar negara secara lisan pada tanggal 29 Mei 1945 adalah...", opt: ["Mr. Soepomo", "Mr. Mohammad Yamin", "Ir. Soekarno", "Drs. Mohammad Hatta"], ans: 1 },
{ q: "Jumlah seluruh anggota awal BPUPK saat dilantik pada 28 Mei 1945 (termasuk 60 anggota aktif Indonesia dan 7 perwakilan Jepang) adalah...", opt: ["60 Orang", "62 Orang", "67 Orang", "74 Orang"], ans: 2 },
{ q: "Tokoh yang menyampaikan gagasan dasar negara dengan paham 'negara integralistik' pada tanggal 31 Mei 1945 adalah...", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Mohammad Yamin", "Mr. Soepomo"], ans: 3 },
{ q: "Pidato Ir. Soekarno pada tanggal 1 Juni 1945 yang mengusulkan lima dasar negara kini diperingati sebagai...", opt: ["Hari Lahir Pancasila", "Hari Kesaktian Pancasila", "Hari Kebangkitan Nasional", "Hari Sumpah Pemuda"], ans: 0 },
{ q: "Istilah 'Pancasila' yang diusulkan oleh Ir. Soekarno pada 1 Juni 1945 diperoleh atas saran dari seorang ahli...", opt: ["Sejarah", "Bahasa", "Hukum", "Agama"], ans: 1 },
{ q: "Untuk menindaklanjuti usulan dasar negara dari para anggota BPUPK pada masa reses, dibentuk panitia kecil yang dikenal sebagai...", opt: ["Panitia Lima", "PPKI", "Panitia Sembilan", "Chuo Sangi In"], ans: 2 },
{ q: "Siapakah tokoh yang menjabat sebagai Ketua Panitia Sembilan?", opt: ["Drs. Mohammad Hatta", "Mr. A.A. Maramis", "K.H. A. Wahid Hasjim", "Ir. Soekarno"], ans: 3 },
{ q: "Hasil rumusan Panitia Sembilan yang disepakati pada tanggal 22 Juni 1945 dikenal dengan sebutan...", opt: ["Piagam Jakarta (Jakarta Charter)", "Teks Proklamasi", "Trisila", "Dekrit Presiden"], ans: 0 },
{ q: "Rumusan Sila Pertama Pancasila dalam Piagam Jakarta sebelum disempurnakan pada 18 Agustus 1945 berbunyi...", opt: ["Ketuhanan Yang Maha Esa", "Ketuhanan dengan kewajiban menjalankan syariat Islam bagi pemeluk-pemeluknya", "Kemanusiaan yang adil dan beradab", "Persatuan Indonesia"], ans: 1 },
{ q: "Sidang Kedua BPUPK dilaksanakan pada tanggal...", opt: ["29 Mei - 1 Juni 1945", "1 - 7 Agustus 1945", "10 - 17 Juli 1945", "17 - 18 Agustus 1945"], ans: 2 },
{ q: "Fokus utama pembahasan dalam Sidang Kedua BPUPK adalah...", opt: ["Dasar Negara", "Pemilihan Presiden dan Wakil Presiden", "Pembentukan TNI", "Rancangan Undang-Undang Dasar"], ans: 3 },
{ q: "Dalam Sidang Kedua, BPUPK membentuk Panitia Perancang UUD yang diketuai oleh...", opt: ["Ir. Soekarno", "Mr. Soepomo", "Drs. Mohammad Hatta", "Mr. A.A. Maramis"], ans: 0 },
{ q: "Panitia Kecil Perancang Undang-Undang Dasar yang bertugas menyusun isi UUD diketuai oleh...", opt: ["Ir. Soekarno", "Mr. Soepomo", "Mr. Mohammad Yamin", "K.H. A. Wahid Hasjim"], ans: 1 },
{ q: "Selain Panitia Perancang UUD, BPUPK juga membentuk Panitia Keuangan dan Perekonomian yang diketuai oleh...", opt: ["Abikoesno Tjokrosoejoso", "Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. A.A. Maramis"], ans: 2 },
{ q: "BPUPK secara resmi dibubarkan oleh pemerintah pendudukan Jepang pada tanggal 7 Agustus 1945 karena...", opt: ["Gagal merumuskan UUD", "Melakukan pemberontakan", "Tidak patuh pada perintah Jepang", "Dianggap telah selesai menjalankan tugasnya"], ans: 3 },
{ q: "Setelah BPUPK dibubarkan pada 7 Agustus 1945, badan baru yang dibentuk sebagai penggantinya adalah...", opt: ["PPKI (Dokuritsu Junbi Inkai)", "PETA", "Heiho", "KNIP"], ans: 0 }
],
        2: [
            { q: "Panitia Sembilan dibentuk pada masa reses BPUPK, yaitu pada tanggal...", opt: ["22 Juni 1945", "1 Juni 1945", "10 Juli 1945", "17 Agustus 1945"], ans: 0 },
            { q: "Tugas utama dari Panitia Sembilan adalah...", opt: ["Menyelaraskan usulan dasar negara dan menyusun rancangan Pembukaan UUD", "Menyiapkan naskah proklamasi", "Memilih Presiden dan Wakil Presiden", "Membentuk komite nasional daerah"], ans: 0 },
            { q: "Siapakah yang bertindak sebagai Ketua Panitia Sembilan?", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Muhammad Yamin", "K.H. A. Wahid Hasjim"], ans: 0 },
            { q: "Tokoh yang mewakili unsur Islam dari organisasi Nahdlatul Ulama (NU) dalam Panitia Sembilan adalah...", opt: ["K.H. Abdul Wahid Hasjim", "K.H. Kahar Moezakir", "H. Agus Salim", "Abikoesno Tjokrosoejoso"], ans: 0 },
            { q: "Penamaan 'Jakarta Charter' untuk hasil rumusan Panitia Sembilan 22 Juni 1945 pertama kali diusulkan oleh...", opt: ["Mr. Muhammad Yamin", "Ir. Soekarno", "H. Agus Salim", "Mr. Kasman Singodimedjo"], ans: 0 },
            { q: "Tokoh golongan kebangsaan di Panitia Sembilan yang berasal dari wilayah Indonesia Timur (Minahasa) adalah...", opt: ["Mr. Alexander Andries Maramis", "Mr. Johannes Latuharhary", "Sam Ratulangi", "I Gusti Ketut Pudja"], ans: 0 },
            { q: "Lokasi penandatanganan naskah Piagam Jakarta oleh Panitia Sembilan pada 22 Juni 1945 berlangsung di...", opt: ["Kediaman Ir. Soekarno (Jl. Pegangsaan Timur No. 56)", "Gedung Chuo Sangi In", "Rumah Laksamana Maeda", "Gedung Pejambon 2"], ans: 0 }
        ],
        3: [
            { q: "PPKI secara resmi dibentuk oleh pihak Jepang pada tanggal...", opt: ["7 Agustus 1945", "18 Agustus 1945", "1 Maret 1945", "17 Agustus 1945"], ans: 0 },
            { q: "Sidang pertama PPKI pasca proklamasi kemerdekaan dilaksanakan pada tanggal...", opt: ["18 Agustus 1945", "17 Agustus 1945", "19 Agustus 1945", "22 Agustus 1945"], ans: 0 },
            { q: "Salah satu keputusan paling krusial dalam Sidang PPKI 18 Agustus 1945 adalah...", opt: ["Mengesahkan UUD 1945 dan penetapan Pancasila sebagai Dasar Negara", "Membentuk Tentara Nasional Indonesia", "Menetapkan lagu Indonesia Raya", "Memilih para menteri kabinet"], ans: 0 },
            { q: "Jumlah awal anggota PPKI adalah 21 orang. Ir. Soekarno kemudian menambah anggota baru tanpa sepengetahuan Jepang sebanyak...", opt: ["6 Orang", "5 Orang", "7 Orang", "9 Orang"], ans: 0 },
            { q: "Perubahan 7 kata pada Sila Pertama Piagam Jakarta diputuskan sebelum sidang PPKI 18 Agustus 1945. Tokoh yang TIDAK ikut dalam diskusi cepat tersebut adalah...", opt: ["H. Agus Salim", "Ki Bagoes Hadikoesoemo", "Mr. Kasman Singodimedjo", "Teuku Mohammad Hasan"], ans: 0 },
            { q: "Hasil sidang PPKI kedua pada tanggal 19 Agustus 1945 menyepakati pembagian wilayah Indonesia menjadi...", opt: ["8 Provinsi", "12 Provinsi", "10 Provinsi", "5 Provinsi"], ans: 0 },
            { q: "Badan yang dibentuk pada sidang PPKI tanggal 22 Agustus 1945 untuk berfungsi sebagai partai tunggal sebelum akhirnya dibatalkan adalah...", opt: ["PNI (Partai Nasional Indonesia)", "BKR (Badan Keamanan Rakyat)", "KNIP (Komite Nasional Indonesia Pusat)", "Masyumi"], ans: 0 }
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

    // POOL SOAL ANTI-DUPLIKASI SESSION
    let currentQuestionPool = [];

    function shuffleArray(array) {
        let arr = [...array];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }

    function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

    function triggerShake(element = board) {
        element.classList.remove('shake');
        void element.offsetWidth; // Force reflow
        element.classList.add('shake');
    }

    function spawnFloatingText(targetTile, text, color = '#ffd700') {
        const rect = targetTile.getBoundingClientRect();
        const floatEl = document.createElement('div');
        floatEl.className = 'floating-text';
        floatEl.innerText = text;
        floatEl.style.color = color;
        floatEl.style.left = `${rect.left + rect.width / 2 - 20}px`;
        floatEl.style.top = `${rect.top + rect.height / 2 - 10}px`;
        document.body.appendChild(floatEl);

        setTimeout(() => floatEl.remove(), 850);
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
        
        // Inisialisasi pool soal acak anti-duplikasi
        let rawQuestions = questionsDB[currentLevel] || questionsDB[1];
        currentQuestionPool = shuffleArray(rawQuestions);

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
            triggerShake();
            
            const firstIdx = currentMatch.matchedIndices[0];
            const points = currentMatch.matchedIndices.length * 30 * combo;
            spawnFloatingText(grid[firstIdx], combo > 1 ? `COMBO x${combo}! +${points}` : `+${points}`);

            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].classList.add('matched-pop');
            });

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
        // Isi ulang jika bank soal dalam pool habis
        if (currentQuestionPool.length === 0) {
            let rawQuestions = questionsDB[currentLevel] || questionsDB[1];
            currentQuestionPool = shuffleArray(rawQuestions);
        }

        // Ambil soal paling atas tanpa duplikasi
        let qObj = currentQuestionPool.pop();

        document.getElementById('modal-tag').innerText = `KUIS LEVEL ${currentLevel} - SEJARAH PANCASILA`;
        document.getElementById('quiz-question').innerText = qObj.q;

        let optionsContainer = document.getElementById('quiz-options');
        optionsContainer.innerHTML = '';

        // Mengacak posisi jawaban pilihan ganda
        let optionsList = qObj.opt.map((optText, index) => ({
            text: optText,
            isCorrect: index === qObj.ans
        }));
        optionsList = shuffleArray(optionsList);

        optionsList.forEach(optItem => {
            let btn = document.createElement('button');
            btn.classList.add('opt-btn');
            btn.innerText = optItem.text;
            btn.onclick = () => handleAnswer(optItem.isCorrect, btn);
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
                triggerShake(document.body);
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

        if (score > 0 && playerNama) {
            submitGlobalScore(playerNama, playerKelas, score);
        }
        
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

    window.onload = fetchGlobalLeaderboard;
</script>
</body>
</html>
"""

# Tampilkan Aplikasi Game di Streamlit
components.html(game_html, height=880, scrolling=True)
