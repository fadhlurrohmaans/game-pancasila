import streamlit as st
import streamlit.components.v1 as components
import urllib.request
import json
import pandas as pd
import io

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

# Initial Bank Soal Default
DEFAULT_QUESTIONS = {
    "1": [
        { "q": "BPUPK secara resmi dibentuk oleh pemerintah pendudukan Jepang pada tanggal...", "opt": ["1 Maret 1945", "29 April 1945", "1 Juni 1945", "17 Agustus 1945"], "ans": 0 },
        { "q": "Pelantikan pengurus BPUPK secara resmi dilaksanakan pada tanggal...", "opt": ["1 Maret 1945", "28 Mei 1945", "22 Juni 1945", "18 Agustus 1945"], "ans": 1 },
        { "q": "Siapakah Ketua (Kaichou) utama dari BPUPK?", "opt": ["Ir. Soekarno", "Drs. Mohammad Hatta", "Dr. K.R.T. Radjiman Wedyodiningrat", "Mr. Soepomo"], "ans": 2 },
        { "q": "Nama BPUPK dalam bahasa Jepang dinamakan...", "opt": ["Dokuritsu Junbi Inkai", "Heiho", "Chuo Sangi In", "Dokuritsu Junbi Cosakai"], "ans": 3 },
        { "q": "Tokoh Jepang yang ditunjuk menjadi Wakil Ketua (Fuku Kaichou) BPUPK adalah...", "opt": ["Ichibangase Yosio", "Maeda Tadashi", "Terauchi Hisaichi", "Kumakichi Harada"], "ans": 0 },
        { "q": "Sidang Pertama BPUPK berlangsung dari tanggal...", "opt": ["10 - 17 Juli 1945", "22 - 25 Juni 1945", "29 Mei - 1 Juni 1945", "17 - 18 Agustus 1945"], "ans": 2 },
        { "q": "Agenda utama pembahasan dalam Sidang Pertama BPUPK adalah perumusan...", "opt": ["Dasar Negara", "Teks Proklamasi", "Rancangan Undang-Undang Dasar", "Lambang Negara"], "ans": 0 }
    ],
    "2": [
        { "q": "Panitia Sembilan dibentuk pada masa reses BPUPK, yaitu pada tanggal...", "opt": ["22 Juni 1945", "1 Juni 1945", "10 Juli 1945", "17 Agustus 1945"], "ans": 0 },
        { "q": "Tugas utama dari Panitia Sembilan adalah...", "opt": ["Menyelaraskan usulan dasar negara dan menyusun rancangan Pembukaan UUD", "Menyiapkan naskah proklamasi", "Memilih Presiden dan Wakil Presiden", "Membentuk komite nasional daerah"], "ans": 0 },
        { "q": "Siapakah yang bertindak sebagai Ketua Panitia Sembilan?", "opt": ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Muhammad Yamin", "K.H. A. Wahid Hasjim"], "ans": 0 }
    ],
    "3": [
        { "q": "PPKI secara resmi dibentuk oleh pihak Jepang pada tanggal...", "opt": ["7 Agustus 1945", "18 Agustus 1945", "1 Maret 1945", "17 Agustus 1945"], "ans": 0 },
        { "q": "Sidang pertama PPKI dilaksanakan pada tanggal...", "opt": ["18 Agustus 1945", "17 Agustus 1945", "19 Agustus 1945", "22 Agustus 1945"], "ans": 0 },
        { "q": "Keputusan penting Sidang PPKI 18 Agustus 1945 adalah...", "opt": ["Mengesahkan UUD 1945 dan penetapan Pancasila sebagai Dasar Negara", "Membentuk Tentara Nasional Indonesia", "Menetapkan lagu Indonesia Raya", "Memilih para menteri kabinet"], "ans": 0 }
    ]
}

# Inisialisasi Session State
if 'questions_db' not in st.session_state:
    st.session_state.questions_db = DEFAULT_QUESTIONS

if 'logged_in_guru' not in st.session_state:
    st.session_state.logged_in_guru = False

# Function Fetch Data Firebase untuk Dashboard Guru
def fetch_firebase_data():
    url = "https://gamepancasila-default-rtdb.asia-southeast1.firebasedatabase.app/leaderboard.json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data:
                records = list(data.values())
                return pd.DataFrame(records)
    except Exception as e:
        st.error(f"Gagal terhubung ke database: {e}")
    return pd.DataFrame()

# Function Hapus Semua Data Siswa dari Firebase
def delete_firebase_data():
    url = "https://gamepancasila-default-rtdb.asia-southeast1.firebasedatabase.app/leaderboard.json"
    try:
        req = urllib.request.Request(url, method='DELETE')
        with urllib.request.urlopen(req, timeout=5) as response:
            return True
    except Exception as e:
        st.error(f"Gagal menghapus data dari database: {e}")
        return False

# Function untuk membuat file template Excel
def generate_excel_template():
    data = [
        {"level": 1, "pertanyaan": "Siapakah Ketua BPUPK?", "pilihan_a": "Soekarno", "pilihan_b": "Hatta", "pilihan_c": "Dr. Radjiman", "pilihan_d": "Soepomo", "jawaban_benar": "C"},
        {"level": 2, "pertanyaan": "Kapan Panitia Sembilan dibentuk?", "pilihan_a": "22 Juni 1945", "pilihan_b": "1 Juni 1945", "pilihan_c": "10 Juli 1945", "pilihan_d": "17 Agustus 1945", "jawaban_benar": "A"},
        {"level": 3, "pertanyaan": "Kapan sidang pertama PPKI?", "pilihan_a": "18 Agustus 1945", "pilihan_b": "17 Agustus 1945", "pilihan_c": "19 Agustus 1945", "pilihan_d": "22 Agustus 1945", "jawaban_benar": "A"}
    ]
    df_template = pd.DataFrame(data)
    buffer = io.BytesIO()
    try:
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df_template.to_excel(writer, index=False, sheet_name='BankSoal')
    except ModuleNotFoundError:
        st.error("Pustaka 'openpyxl' belum terpasang di server. Mohon tambahkan 'openpyxl' ke file requirements.txt.")
        return b""
    return buffer.getvalue()

# Function parsing file Excel menjadi format JSON Bank Soal
def process_uploaded_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip().str.lower()
    
    required_cols = ['level', 'pertanyaan', 'pilihan_a', 'pilihan_b', 'pilihan_c', 'pilihan_d', 'jawaban_benar']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Kolom wajib '{col}' tidak ditemukan di file Excel.")
    
    new_db = {"1": [], "2": [], "3": []}
    ans_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, '0': 0, '1': 1, '2': 2, '3': 3}

    for _, row in df.iterrows():
        lvl = str(int(row['level'])).strip()
        if lvl not in new_db:
            continue
        
        raw_ans = str(row['jawaban_benar']).strip().upper()
        ans_idx = ans_map.get(raw_ans, 0)

        new_db[lvl].append({
            "q": str(row['pertanyaan']).strip(),
            "opt": [
                str(row['pilihan_a']).strip(),
                str(row['pilihan_b']).strip(),
                str(row['pilihan_c']).strip(),
                str(row['pilihan_d']).strip()
            ],
            "ans": ans_idx
        })
    return new_db

# Template HTML/JS Game
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
    .input-field:focus { border-color: #ffd700; }
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
        top: 2px; left: 3px; right: 3px; height: 38%;
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
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.9);
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
        padding: 16px; z-index: 100;
    }
    .timer-bar-container {
        width: 100%; height: 8px;
        background: rgba(255,255,255,0.2);
        border-radius: 4px; overflow: hidden; margin-bottom: 12px;
    }
    .timer-bar { height: 100%; background: #ffd700; width: 100%; }
    .btn {
        background: linear-gradient(45deg, #d32f2f, #b71c1c);
        color: white; border: 1.5px solid #ffd700;
        padding: 12px 20px; font-size: 15px; font-weight: bold;
        border-radius: 25px; cursor: pointer; transition: transform 0.15s ease;
        margin: 6px; width: 100%; max-width: 300px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }
    .btn:active { transform: scale(0.95); }
    .opt-btn {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: white; padding: 12px; border-radius: 10px;
        text-align: left; font-size: 13px; cursor: pointer;
        margin-bottom: 8px; width: 100%; transition: background-color 0.15s ease;
    }
    .opt-btn:active { background: rgba(255, 215, 0, 0.3); border-color: #ffd700; }
    .opt-btn.correct { background: #2e7d32 !important; }
    .opt-btn.wrong { background: #c62828 !important; }
    .hidden { display: none !important; }
    .leaderboard-box {
        margin-top: 14px; background: rgba(0, 0, 0, 0.55);
        padding: 10px; border-radius: 12px; border: 1px solid rgba(255, 215, 0, 0.35);
    }
    .leaderboard-title { font-size: 13px; color: #ffd700; font-weight: bold; margin-bottom: 8px; }
    .leaderboard-table { width: 100%; border-collapse: collapse; font-size: 11px; }
    .leaderboard-table th { background: rgba(255, 215, 0, 0.25); color: #ffd700; padding: 6px 4px; text-align: left; }
    .leaderboard-table td { padding: 5px 4px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); text-align: left; }
    @keyframes popIn { from { opacity: 0; transform: scale(0.92); } to { opacity: 1; transform: scale(1); } }
    .shake { animation: shakeAnim 0.3s ease-in-out; }
    @keyframes shakeAnim {
        0%, 100% { transform: translate(0, 0); }
        25% { transform: translate(-6px, 0); }
        75% { transform: translate(6px, 0); }
    }
    .floating-text {
        position: absolute; font-weight: 900; font-size: 20px; color: #ffd700;
        text-shadow: 0 2px 4px #000; pointer-events: none;
        animation: floatUp 0.75s ease-out forwards; z-index: 999;
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
        • Level Permainan: <b>Level 1, Level 2, Level 3</b>.<br>
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
        <div style="font-size: 11px; color: #ffd700; font-weight: bold;" id="modal-tag">KUIS SEJARAH PANCASILA</div>
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

    const questionsDB = %%QUESTIONS_DB%%;

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
        
        let rawQuestions = questionsDB[currentLevel] || questionsDB[1] || [];
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
            let rawQuestions = questionsDB[currentLevel] || questionsDB[1] || [];
            currentQuestionPool = shuffleArray(rawQuestions);
        }

        let qObj = currentQuestionPool.pop();

        document.getElementById('modal-tag').innerText = `KUIS LEVEL ${currentLevel} - SEJARAH PANCASILA`;
        document.getElementById('quiz-question').innerText = qObj.q;

        let optionsContainer = document.getElementById('quiz-options');
        optionsContainer.innerHTML = '';

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

# Render HTML dengan Injeksi JSON Bank Soal terbaru
game_html = game_html_template.replace("%%QUESTIONS_DB%%", json.dumps(st.session_state.questions_db))

# Layout Utama Menggunakan Tab Streamlit
tab_siswa, tab_guru = st.tabs(["🎮 Zone Main Siswa", "👨‍🏫 Dashboard Guru"])

with tab_siswa:
    components.html(game_html, height=880, scrolling=True)

with tab_guru:
    st.title("👨‍🏫 Portal Pengelolaan Guru")

    # Sistem Login Guru
    if not st.session_state.logged_in_guru:
        st.subheader("🔒 Silakan Login Terlebih Dahulu")
        with st.form("form_login"):
            username_input = st.text_input("Username")
            password_input = st.text_input("Password", type="password")
            btn_login = st.form_submit_button("🔑 Login Guru")

            if btn_login:
                if username_input == "guru" and password_input == "guru":
                    st.session_state.logged_in_guru = True
                    st.success("Login Berhasil! Mengalihkan...")
                    st.rerun()
                else:
                    st.error("Username atau Password salah! (Default: guru / guru)")
    else:
        # Tombol Logout
        col_title, col_logout = st.columns([4, 1])
        with col_logout:
            if st.button("🚪 Logout"):
                st.session_state.logged_in_guru = False
                st.rerun()

        # Tab Menu Internal Guru
        tab_nilai, tab_soal = st.tabs(["📊 Rekap Nilai Siswa", "✏️ Kelola Bank Soal (Excel)"])

        # TAB REKAP NILAI SISWA
        with tab_nilai:
            st.caption("Pantau progres dan hasil akhir siswa secara realtime.")

            col_btn, col_del = st.columns([1, 1])
            with col_btn:
                if st.button("🔄 Refresh Data Realtime"):
                    st.rerun()
            with col_del:
                with st.popover("🗑️ Hapus Semua Data Siswa"):
                    st.warning("⚠️ Apakah Anda yakin ingin menghapus SELURUH data permainan siswa dari database?")
                    if st.button("Ya, Hapus Semua Data Sekarang", type="primary"):
                        if delete_firebase_data():
                            st.success("✅ Seluruh data siswa berhasil dihapus!")
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

                # Filter Siswa
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

                st.subheader("📋 Rekap Hasil Permainan Siswa")
                st.dataframe(display_df, use_container_width=True, hide_index=True)

                csv_data = display_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Rekap Data Siswa (CSV)",
                    data=csv_data,
                    file_name="Rekap_Game_Pancasila.csv",
                    mime="text/csv"
                )

        # TAB KELOLA BANK SOAL VIA EXCEL
        with tab_soal:
            st.subheader("📂 Update Bank Soal via File Excel")
            st.markdown("""
            Anda dapat memperbarui seluruh bank soal kuis yang muncul di dalam game dengan mengunggah file Excel (`.xlsx`).
            
            **Format Kolom Excel Wajib:**
            - **level** : `1` (Level 1), `2` (Level 2), atau `3` (Level 3)
            - **pertanyaan** : Teks pertanyaan kuis
            - **pilihan_a** : Teks opsi pilihan A
            - **pilihan_b** : Teks opsi pilihan B
            - **pilihan_c** : Teks opsi pilihan C
            - **pilihan_d** : Teks opsi pilihan D
            - **jawaban_benar** : Jawaban benar (`A`, `B`, `C`, atau `D`)
            """)

            # Download Template
            template_excel = generate_excel_template()
            if template_excel:
                st.download_button(
                    label="📥 Unduh Templat Excel Bank Soal",
                    data=template_excel,
                    file_name="Template_Bank_Soal_Pancasila.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            st.markdown("---")

            # Form Upload
            uploaded_file = st.file_uploader("Unggah File Excel Soal Baru (.xlsx)", type=["xlsx"])
            if uploaded_file is not None:
                if st.button("🚀 Terapkan & Update Bank Soal Game"):
                    try:
                        parsed_db = process_uploaded_excel(uploaded_file)
                        st.session_state.questions_db = parsed_db
                        st.success("✅ Bank Soal berhasil diperbarui! Game siswa kini menggunakan soal terbaru.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Gagal memproses file Excel: {e}")

            # Preview Soal Saat Ini
            st.markdown("---")
            st.subheader("👀 Preview Soal yang Aktif Saat Ini")
            
            lvl_select = st.selectbox("Pilih Level untuk Dilihat:", ["Level 1", "Level 2", "Level 3"])
            lvl_key = "1" if "1" in lvl_select else "2" if "2" in lvl_select else "3"
            
            soal_list = st.session_state.questions_db.get(lvl_key, [])
            if soal_list:
                for idx, s in enumerate(soal_list, 1):
                    with st.expander(f"Soal #{idx}: {s['q']}"):
                        ans_text = s['opt'][s['ans']] if s['ans'] < len(s['opt']) else "-"
                        st.write(f"- **Pilihan**: {', '.join(s['opt'])}")
                        st.write(f"- **Jawaban Benar**: {ans_text}")
            else:
                st.warning("Belum ada soal pada level ini.")
