import streamlit as st
import streamlit.components.v1 as components
import urllib.request
import json
import pandas as pd

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Nusantara Gem Crush: Sejarah Pancasila Quest",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling CSS Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100% !important;
    }
    .main {
        background: #100002;
    }
    iframe {
        border-radius: 16px;
        width: 100% !important;
    }
    /* Style Tab Streamlit */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: #1a080c;
        border-radius: 8px 8px 0px 0px;
        color: #ffd700;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #d32f2f !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Default Bank Soal jika Firebase belum memiliki data soal
DEFAULT_QUESTIONS = {
    "1": [
        {"q": "BPUPK secara resmi dibentuk oleh pemerintah pendudukan Jepang pada tanggal...", "opt": ["1 Maret 1945", "29 April 1945", "1 Juni 1945", "17 Agustus 1945"], "ans": 0},
        {"q": "Pelantikan pengurus BPUPK secara resmi dilaksanakan pada tanggal...", "opt": ["1 Maret 1945", "28 Mei 1945", "22 Juni 1945", "18 Agustus 1945"], "ans": 1},
        {"q": "Siapakah Ketua (Kaichou) utama dari BPUPK?", "opt": ["Ir. Soekarno", "Drs. Mohammad Hatta", "Dr. K.R.T. Radjiman Wedyodiningrat", "Mr. Soepomo"], "ans": 2},
        {"q": "Nama BPUPK dalam bahasa Jepang dinamakan...", "opt": ["Dokuritsu Junbi Inkai", "Heiho", "Chuo Sangi In", "Dokuritsu Junbi Cosakai"], "ans": 3},
        {"q": "Tokoh Jepang yang ditunjuk menjadi Wakil Ketua (Fuku Kaichou) BPUPK adalah...", "opt": ["Ichibangase Yosio", "Maeda Tadashi", "Terauchi Hisaichi", "Kumakichi Harada"], "ans": 0},
        {"q": "Sidang Pertama BPUPK berlangsung dari tanggal...", "opt": ["10 - 17 Juli 1945", "22 - 25 Juni 1945", "29 Mei - 1 Juni 1945", "17 - 18 Agustus 1945"], "ans": 2},
        {"q": "Agenda utama pembahasan dalam Sidang Pertama BPUPK adalah perumusan...", "opt": ["Dasar Negara", "Teks Proklamasi", "Rancangan Undang-Undang Dasar", "Lambang Negara"], "ans": 0}
    ],
    "2": [
        {"q": "Panitia Sembilan dibentuk pada masa reses BPUPK, yaitu pada tanggal...", "opt": ["22 Juni 1945", "1 Juni 1945", "10 Juli 1945", "17 Agustus 1945"], "ans": 0},
        {"q": "Tugas utama dari Panitia Sembilan adalah...", "opt": ["Menyelaraskan usulan dasar negara dan menyusun rancangan Pembukaan UUD", "Menyiapkan naskah proklamasi", "Memilih Presiden dan Wakil Presiden", "Membentuk komite nasional daerah"], "ans": 0},
        {"q": "Siapakah yang bertindak sebagai Ketua Panitia Sembilan?", "opt": ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Muhammad Yamin", "K.H. A. Wahid Hasjim"], "ans": 0}
    ],
    "3": [
        {"q": "PPKI secara resmi dibentuk oleh pihak Jepang pada tanggal...", "opt": ["7 Agustus 1945", "18 Agustus 1945", "1 Maret 1945", "17 Agustus 1945"], "ans": 0},
        {"q": "Sidang pertama PPKI dilaksanakan pada tanggal...", "opt": ["18 Agustus 1945", "17 Agustus 1945", "19 Agustus 1945", "22 Agustus 1945"], "ans": 0},
        {"q": "Keputusan penting Sidang PPKI 18 Agustus 1945 adalah...", "opt": ["Mengesahkan UUD 1945 dan penetapan Pancasila sebagai Dasar Negara", "Membentuk Tentara Nasional Indonesia", "Menetapkan lagu Indonesia Raya", "Memilih para menteri kabinet"], "ans": 0}
    ]
}

# Function Fetch Data Leaderboard dari Firebase
def fetch_firebase_data():
    url = "https://gamepancasila-default-rtdb.asia-southeast1.firebasedatabase.app/leaderboard.json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data:
                records = list(data.values())
                df = pd.DataFrame(records)
                return df
    except Exception as e:
        st.error(f"Gagal terhubung ke database leaderboard: {e}")
    return pd.DataFrame()

# Function Fetch Questions dari Firebase
def fetch_questions():
    url = "https://gamepancasila-default-rtdb.asia-southeast1.firebasedatabase.app/questions.json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data:
                return data
    except Exception:
        pass
    return DEFAULT_QUESTIONS

# Function Save Questions ke Firebase
def save_questions(questions_data):
    url = "https://gamepancasila-default-rtdb.asia-southeast1.firebasedatabase.app/questions.json"
    try:
        payload = json.dumps(questions_data).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'}, method='PUT')
        with urllib.request.urlopen(req, timeout=5) as response:
            return True
    except Exception as e:
        st.error(f"Gagal menyimpan ke database: {e}")
        return False

# Master Template Engine HTML5 + CSS + JavaScript (Siswa)
game_html_template = """
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
        background: linear-gradient(135deg, #3a0000 0%, #120002 50%, #20000e 100%);
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
    }

    .card {
        background: rgba(26, 8, 12, 0.92);
        border: 2px solid rgba(255, 215, 0, 0.5);
        border-radius: 16px;
        padding: 16px;
        width: 100%;
        max-width: 480px;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.6);
        will-change: transform, opacity;
        transform: translateZ(0);
        animation: popIn 0.35s ease-out;
    }

    h2 { 
        color: #ffd700;
        margin-top: 0; 
        font-size: clamp(20px, 5vw, 26px);
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    
    .input-field {
        width: 100%;
        padding: 10px 14px;
        border-radius: 8px;
        border: 1.5px solid rgba(255, 215, 0, 0.6);
        background: rgba(0, 0, 0, 0.7);
        color: #fff;
        font-size: 14px;
        outline: none;
        margin-top: 4px;
        margin-bottom: 10px;
        transition: border-color 0.2s ease;
    }
    .input-field:focus {
        border-color: #ffd700;
    }

    .stats-bar {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 4px;
        width: 100%;
        max-width: 480px;
        background: rgba(10, 2, 4, 0.85);
        padding: 8px 4px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid rgba(255, 215, 0, 0.4);
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
        background: rgba(15, 5, 5, 0.95);
        padding: 8px;
        border-radius: 16px;
        border: 2px solid #ffd700;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
        position: relative;
        will-change: transform;
        transform: translateZ(0);
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
        transition: transform 0.15s ease-out, opacity 0.15s ease-out;
        border: 1.5px solid rgba(255, 255, 255, 0.4);
        box-shadow: inset 0 -3px 4px rgba(0,0,0,0.5), inset 0 2px 4px rgba(255,255,255,0.5);
        position: relative;
        overflow: hidden;
        will-change: transform, opacity;
        transform: translateZ(0);
    }

    .tile::before {
        content: '';
        position: absolute;
        top: 2px;
        left: 3px;
        right: 3px;
        height: 38%;
        background: linear-gradient(to bottom, rgba(255,255,255,0.5), rgba(255,255,255,0.02));
        border-radius: 6px 6px 100% 100%;
        pointer-events: none;
    }

    .tile:active { transform: scale(0.92); }

    .tile.selected {
        border: 2.5px solid #ffffff !important;
        transform: scale(1.12);
        box-shadow: 0 0 15px #ffd700 !important;
        z-index: 10;
        animation: pulse-gem 0.6s infinite alternate ease-in-out;
    }

    .tile.matched-pop {
        transform: scale(1.3) rotate(90deg) !important;
        opacity: 0 !important;
        transition: transform 0.25s ease-out, opacity 0.25s ease-out;
    }

    @keyframes pulse-gem {
        0% { transform: scale(1.08); }
        100% { transform: scale(1.16); }
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
        background: rgba(0, 0, 0, 0.9);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 16px;
        z-index: 100;
    }

    .timer-bar-container {
        width: 100%;
        height: 8px;
        background: rgba(255,255,255,0.2);
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 12px;
    }
    .timer-bar { 
        height: 100%; 
        background: #ffd700; 
        width: 100%; 
    }
    
    .btn {
        background: linear-gradient(45deg, #d32f2f, #b71c1c);
        color: white; border: 1.5px solid #ffd700;
        padding: 12px 20px; font-size: 15px; font-weight: bold;
        border-radius: 25px; cursor: pointer; 
        transition: transform 0.15s ease;
        margin: 6px;
        width: 100%;
        max-width: 300px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }
    .btn:active { transform: scale(0.95); }

    .opt-btn {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: white; padding: 12px; border-radius: 10px;
        text-align: left; font-size: 13px; cursor: pointer;
        margin-bottom: 8px;
        width: 100%; transition: background-color 0.15s ease;
    }
    .opt-btn:active { background: rgba(255, 215, 0, 0.3); border-color: #ffd700; }
    .opt-btn.correct { background: #2e7d32 !important; }
    .opt-btn.wrong { background: #c62828 !important; }

    .hidden { display: none !important; }

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

    @keyframes popIn {
        from { opacity: 0; transform: scale(0.92); }
        to { opacity: 1; transform: scale(1); }
    }

    .shake {
        animation: shakeAnim 0.3s ease-in-out;
    }
    @keyframes shakeAnim {
        0%, 100% { transform: translate(0, 0); }
        25% { transform: translate(-6px, 0); }
        75% { transform: translate(6px, 0); }
    }

    .floating-text {
        position: absolute;
        font-weight: 900;
        font-size: 20px;
        color: #ffd700;
        text-shadow: 0 2px 4px #000;
        pointer-events: none;
        animation: floatUp 0.75s ease-out forwards;
        z-index: 999;
        will-change: transform, opacity;
    }
    @keyframes floatUp {
        0% { opacity: 1; transform: translateY(0) scale(0.9); }
        50% { opacity: 1; transform: translateY(-20px) scale(1.1); }
        100% { opacity: 0; transform: translateY(-40px) scale(1); }
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

        <div style="display: flex; gap: 8px;">
            <div style="flex: 2;">
                <label style="font-size: 12px; color: #ffd700; font-weight: bold;">Kelas:</label>
                <input type="text" id="input-kelas" class="input-field" placeholder="Contoh: VII A / VIII B">
            </div>
            <div style="flex: 1;">
                <label style="font-size: 12px; color: #ffd700; font-weight: bold;">No. Absen:</label>
                <input type="number" id="input-absen" class="input-field" placeholder="No. Absen">
            </div>
        </div>
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
        Siswa: - | Kelas: - | Absen: -
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
        console.warn("Firebase bermasalah:", e);
    }

    function submitGlobalScore(nama, kelas, absen, totalSkor, isVictory) {
        if (!db || totalSkor <= 0) return;
        try {
            const now = new Date();
            const timeStr = now.toLocaleDateString('id-ID') + ' ' + now.toLocaleTimeString('id-ID', {hour: '2-digit', minute:'2-digit'});
            db.ref('leaderboard').push({
                nama: nama,
                kelas: kelas,
                absen: absen,
                score: totalSkor,
                status: isVictory ? "BERHASIL TAMAT 🎉" : "Gagal / Terhenti ❌",
                isVictory: isVictory,
                waktu: timeStr,
                timestamp: Date.now()
            });
        } catch(e) {
            console.error("Gagal menyimpan data:", e);
        }
    }

    function fetchGlobalLeaderboard() {
        const startList = document.getElementById('leaderboard-start-list');
        const endList = document.getElementById('leaderboard-end-list');

        if (!db) return;

        try {
            db.ref('leaderboard').orderByChild('score').limitToLast(10).once('value', (snapshot) => {
                let data = [];
                snapshot.forEach((child) => {
                    data.push(child.val());
                });
                data.reverse();

                if (data.length === 0) {
                    const emptyMsg = "<p style='font-size:11px; color:#aaa;'>Belum ada skor tercatat.</p>";
                    if(startList) startList.innerHTML = emptyMsg;
                    if(endList) endList.innerHTML = emptyMsg;
                    return;
                }

                let html = `<table class="leaderboard-table">
                    <thead>
                        <tr>
                            <th style="width:10%;">#</th>
                            <th style="width:40%;">Nama</th>
                            <th style="width:15%;">Absen</th>
                            <th style="width:15%;">Kelas</th>
                            <th style="width:20%; text-align:right;">Skor</th>
                        </tr>
                    </thead>
                    <tbody>`;

                data.forEach((item, idx) => {
                    let medal = idx === 0 ? '🥇' : idx === 1 ? '🥈' : idx === 2 ? '🥉' : `${idx + 1}.`;
                    html += `<tr>
                        <td>${medal}</td>
                        <td>${item.nama || 'Anonim'}</td>
                        <td>${item.absen || '-'}</td>
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

    // Bank Soal Dihubungkan secara Dinamis dari Python Backend
    const questionsDB = __QUESTIONS_JSON__;

    let playerNama = "";
    let playerKelas = "";
    let playerAbsen = "";
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
        void element.offsetWidth;
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

        setTimeout(() => floatEl.remove(), 750);
    }

    function formatTime(seconds) {
        let mins = Math.floor(seconds / 60);
        let secs = seconds % 60;
        return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }

    function applyGemStyle(tile) {
        const symbol = tile.innerText;
        const index = gems.indexOf(symbol);
        tile.className = 'tile';
        if (index !== -1) {
            tile.classList.add(gemClasses[index]);
        }
    }

    function startGame() {
        let namaInput = document.getElementById('input-nama').value.trim();
        let kelasInput = document.getElementById('input-kelas').value.trim();
        let absenInput = document.getElementById('input-absen').value.trim();

        if (!namaInput || !kelasInput || !absenInput) {
            alert('Silakan lengkapi Nama, Kelas, dan No. Absen terlebih dahulu!');
            return;
        }

        playerNama = namaInput;
        playerKelas = kelasInput;
        playerAbsen = absenInput;
        document.getElementById('player-banner').innerText = `👤 ${playerNama} (Absen: ${playerAbsen}) | 🏫 Kelas: ${playerKelas}`;

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
        
        let rawQuestions = questionsDB[currentLevel] || questionsDB[String(currentLevel)] || [];
        if(!rawQuestions || rawQuestions.length === 0) {
            rawQuestions = questionsDB[1] || questionsDB["1"] || [];
        }
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
        let fragment = document.createDocumentFragment();
        
        for (let i = 0; i < width * width; i++) {
            let tile = document.createElement('div');
            tile.id = i;
            tile.innerText = gems[Math.floor(Math.random() * gems.length)];
            applyGemStyle(tile);
            tile.addEventListener('click', selectTile);
            fragment.appendChild(tile);
            grid.push(tile);
        }
        board.appendChild(fragment);
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
                    await sleep(180);
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

            currentMatch.matchedIndices.forEach(idx => grid[idx].classList.add('matched-pop'));

            score += points;
            updateUI();
            await sleep(250);

            currentMatch.matchedIndices.forEach(idx => {
                grid[idx].innerText = '';
                grid[idx].classList.remove('matched-pop');
                applyGemStyle(grid[idx]);
            });

            await sleep(100);
            dropGems();
            await sleep(200);

            currentMatch = findAndMarkMatches();
            combo++;
        }

        triggerQuiz();
    }

    function triggerQuiz() {
        if (currentQuestionPool.length === 0) {
            let rawQuestions = questionsDB[currentLevel] || questionsDB[String(currentLevel)] || [];
            if(!rawQuestions || rawQuestions.length === 0) {
                rawQuestions = questionsDB[1] || questionsDB["1"] || [];
            }
            currentQuestionPool = shuffleArray(rawQuestions);
        }

        let qObj = currentQuestionPool.pop();

        document.getElementById('modal-tag').innerText = `KUIS LEVEL ${currentLevel} - SEJARAH PANCASILA`;
        document.getElementById('quiz-question').innerText = qObj ? qObj.q : "Pertanyaan tidak tersedia.";

        let optionsContainer = document.getElementById('quiz-options');
        optionsContainer.innerHTML = '';

        if(qObj && qObj.opt) {
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
        }

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
                    gameOver("💀 Nyawa Kamu Habis!", false);
                    return;
                }
            }

            isProcessing = false;

            if (questionsAnswered >= targetQuestions) {
                levelWin();
            } else if (moves <= 0) {
                gameOver("💥 Langkah (Moves) Kamu Habis!", false);
            }
        }, 800);
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
        document.getElementById('final-player-info').innerText = `Siswa: ${playerNama} (Absen: ${playerAbsen}) | Kelas: ${playerKelas}`;
        document.getElementById('end-desc').innerText = msg;
        document.getElementById('final-score').innerText = `${score} Poin`;

        let rank = "";
        if (score > 2500) rank = "🥇 Gelar: Ahli Sejarah Pancasila";
        else if (score > 1500) rank = "🥈 Gelar: Pejuang Patriot Muda";
        else rank = "🥉 Gelar: Pelajar Pancasila";

        document.getElementById('final-rank').innerText = rank;

        if (score > 0 && playerNama) {
            submitGlobalScore(playerNama, playerKelas, playerAbsen, score, isVictory);
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

# Inisialisasi Session State untuk Login Guru
if "teacher_logged_in" not in st.session_state:
    st.session_state["teacher_logged_in"] = False

# Layout Utama Menggunakan Tab Streamlit
tab_siswa, tab_guru = st.tabs(["🎮 Zone Main Siswa", "👨‍🏫 Dashboard Guru"])

with tab_siswa:
    # Ambil soal terbaru dari database untuk komponen game
    current_questions = fetch_questions()
    rendered_game_html = game_html_template.replace("__QUESTIONS_JSON__", json.dumps(current_questions))
    components.html(rendered_game_html, height=880, scrolling=True)

with tab_guru:
    st.title("👨‍🏫 Dashboard Pengelolaan & Pemantauan Guru")

    # Cek Status Login Guru
    if not st.session_state["teacher_logged_in"]:
        st.subheader("🔒 Autentikasi Guru")
        st.info("Silakan masukan kredensial login Anda untuk mengakses Rekap Nilai Siswa dan Mengedit Bank Soal.")
        
        col_login, _ = st.columns([2, 3])
        with col_login:
            with st.form("form_login_guru"):
                username = st.text_input("Username Guru:")
                password = st.text_input("Password:", type="password")
                btn_login = st.form_submit_button("🔑 Login Guru")

                if btn_login:
                    # Kredensial Default Guru (Dapat disesuaikan)
                    if username == "guru" and password == "pancasila123":
                        st.session_state["teacher_logged_in"] = True
                        st.success("Login berhasil!")
                        st.rerun()
                    else:
                        st.error("Username atau Password salah!")
    else:
        # Header Guru Logged In
        col_header_1, col_header_2 = st.columns([4, 1])
        with col_header_1:
            st.success("🟢 Terhubung sebagai: **Guru / Administrator**")
        with col_header_2:
            if st.button("🚪 Logout"):
                st.session_state["teacher_logged_in"] = False
                st.rerun()

        st.markdown("---")

        # Tab Sub-Menu Guru
        sub_tab_nilai, sub_tab_soal = st.tabs(["📊 Rekap Nilai Siswa", "📝 Kelola Bank Soal"])

        # SUB-TAB 1: REKAP NILAI SISWA
        with sub_tab_nilai:
            st.subheader("📋 Hasil Permainan Siswa Realtime")

            col_btn, _ = st.columns([1, 4])
            with col_btn:
                if st.button("🔄 Refresh Data Realtime"):
                    st.rerun()

            df = fetch_firebase_data()

            if df.empty:
                st.info("Belum ada data siswa yang tercatat atau bermain saat ini.")
            else:
                expected_cols = ['nama', 'kelas', 'absen', 'score', 'status', 'waktu', 'isVictory']
                for col in expected_cols:
                    if col not in df.columns:
                        df[col] = "-"

                df['absen'] = pd.to_numeric(df['absen'], errors='coerce').fillna(0).astype(int)
                df['score'] = pd.to_numeric(df['score'], errors='coerce').fillna(0).astype(int)

                # Metrik Ringkasan
                total_siswa = len(df)
                total_lulus = len(df[df['isVictory'] == True])
                rata_skor = int(df['score'].mean()) if total_siswa > 0 else 0

                m1, m2, m3 = st.columns(3)
                m1.metric("Total Percobaan Siswa", f"{total_siswa} Kali")
                m2.metric("Siswa Tamat 🎉", f"{total_lulus} Siswa")
                m3.metric("Rata-rata Skor", f"{rata_skor} Poin")

                st.markdown("---")

                col_f1, col_f2 = st.columns(2)
                with col_f1:
                    daftar_kelas = ["Semua Kelas"] + sorted(list(df['kelas'].astype(str).unique()))
                    selected_kelas = st.selectbox("Filter Berdasarkan Kelas:", daftar_kelas)
                
                with col_f2:
                    filter_status = st.radio("Tampilkan Status:", ["Semua Siswa", "Hanya yang BERHASIL TAMAT 🎉"], horizontal=True)

                filtered_df = df.copy()
                if selected_kelas != "Semua Kelas":
                    filtered_df = filtered_df[filtered_df['kelas'].astype(str) == selected_kelas]
                
                if filter_status == "Hanya yang BERHASIL TAMAT 🎉":
                    filtered_df = filtered_df[filtered_df['isVictory'] == True]

                filtered_df = filtered_df.sort_values(by=['kelas', 'absen', 'score'], ascending=[True, True, False])

                display_df = filtered_df[['nama', 'kelas', 'absen', 'score', 'status', 'waktu']].rename(columns={
                    'nama': 'Nama Siswa',
                    'kelas': 'Kelas',
                    'absen': 'No. Absen',
                    'score': 'Skor Akhir',
                    'status': 'Status Penyelesaian',
                    'waktu': 'Waktu Bermain'
                })

                st.dataframe(display_df, use_container_width=True, hide_index=True)

                csv_data = display_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Rekap Data Siswa (CSV)",
                    data=csv_data,
                    file_name="Rekap_Game_Pancasila.csv",
                    mime="text/csv"
                )

        # SUB-TAB 2: KELOLA BANK SOAL
        with sub_tab_soal:
            st.subheader("✏️ Editor Bank Soal Kuis")
            st.caption("Perubahan pada soal akan langsung diterapkan dalam permainan siswa saat halaman dimuat ulang.")

            # Load Data Soal dari Firebase ke Session State jika belum ada
            if "questions_editor" not in st.session_state:
                st.session_state["questions_editor"] = fetch_questions()

            # Pilihan Level yang ingin diedit
            level_options = {
                "1": "Level 1: BPUPK (Kelahiran Pancasila)",
                "2": "Level 2: Panitia Sembilan (Piagam Jakarta)",
                "3": "Level 3: PPKI (Pengesahan UUD 1945)"
            }
            selected_lvl_key = st.selectbox(
                "Pilih Level yang Ingin Diedit:",
                options=list(level_options.keys()),
                format_func=lambda x: level_options[x]
            )

            current_lvl_questions = st.session_state["questions_editor"].get(selected_lvl_key, [])

            st.write(f"**Daftar Soal {level_options[selected_lvl_key]} ({len(current_lvl_questions)} Soal):**")

            # Form Pengeditan Soal-soal
            questions_to_delete = []
            for idx, item in enumerate(current_lvl_questions):
                with st.expander(f"📌 Soal #{idx + 1}: {item['q'][:60]}..."):
                    # Edit Pertanyaan
                    new_q = st.text_area(f"Pertanyaan Soal #{idx+1}:", value=item['q'], key=f"q_{selected_lvl_key}_{idx}")
                    
                    # Edit Opsi
                    c1, c2 = st.columns(2)
                    opts = item['opt']
                    with c1:
                        opt_a = st.text_input(f"Opsi A:", value=opts[0] if len(opts)>0 else "", key=f"opt_a_{selected_lvl_key}_{idx}")
                        opt_b = st.text_input(f"Opsi B:", value=opts[1] if len(opts)>1 else "", key=f"opt_b_{selected_lvl_key}_{idx}")
                    with c2:
                        opt_c = st.text_input(f"Opsi C:", value=opts[2] if len(opts)>2 else "", key=f"opt_c_{selected_lvl_key}_{idx}")
                        opt_d = st.text_input(f"Opsi D:", value=opts[3] if len(opts)>3 else "", key=f"opt_d_{selected_lvl_key}_{idx}")

                    # Edit Kunci Jawaban
                    ans_map = {"A (Opsi 1)": 0, "B (Opsi 2)": 1, "C (Opsi 3)": 2, "D (Opsi 4)": 3}
                    current_ans_index = item.get('ans', 0)
                    selected_ans_str = st.selectbox(
                        f"Kunci Jawaban Benar:",
                        options=list(ans_map.keys()),
                        index=current_ans_index if current_ans_index in [0, 1, 2, 3] else 0,
                        key=f"ans_{selected_lvl_key}_{idx}"
                    )

                    # Update ke Session State
                    st.session_state["questions_editor"][selected_lvl_key][idx] = {
                        "q": new_q,
                        "opt": [opt_a, opt_b, opt_c, opt_d],
                        "ans": ans_map[selected_ans_str]
                    }

                    # Hapus Soal
                    if st.button(f"🗑️ Hapus Soal #{idx+1}", key=f"del_{selected_lvl_key}_{idx}"):
                        questions_to_delete.append(idx)

            # Proses Penghapusan Soal
            if questions_to_delete:
                for del_idx in reversed(questions_to_delete):
                    st.session_state["questions_editor"][selected_lvl_key].pop(del_idx)
                st.rerun()

            st.markdown("---")
            
            col_add, col_save = st.columns(2)
            with col_add:
                if st.button("➕ Tambah Soal Baru"):
                    new_default_question = {
                        "q": "Tulis pertanyaan baru di sini...",
                        "opt": ["Pilihan A", "Pilihan B", "Pilihan C", "Pilihan D"],
                        "ans": 0
                    }
                    if selected_lvl_key not in st.session_state["questions_editor"]:
                        st.session_state["questions_editor"][selected_lvl_key] = []
                    st.session_state["questions_editor"][selected_lvl_key].append(new_default_question)
                    st.rerun()

            with col_save:
                if st.button("💾 Simpan Perubahan Bank Soal ke Database", type="primary"):
                    success = save_questions(st.session_state["questions_editor"])
                    if success:
                        st.success("✅ Bank Soal berhasil diperbarui di database Firebase!")
                    else:
                        st.error("❌ Gagal menyimpan Bank Soal!")
