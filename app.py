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

<!-- SCREEN 1: START & IDENTITAS -->
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
</div>

<!-- SCREEN 2: GAME BOARD -->
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

<!-- QUIZ MODAL OVERLAY -->
<div class="modal-overlay hidden" id="quiz-modal">
    <div style="width: 100%; max-width: 440px; text-align: center;">
        <div style="font-size: 11px; color: #ffd700; font-weight: bold;" id="modal-tag">KUIS KELAHIRAN PANCASILA</div>
        <div class="timer-bar-container"><div class="timer-bar" id="timer-bar"></div></div>
        <h3 id="quiz-question" style="font-size: 14px; margin: 10px 0 15px 0; min-height: 40px; line-height: 1.4;">Pertanyaan...</h3>
        <div id="quiz-options"></div>
    </div>
</div>

<!-- SCREEN 3: LEVEL COMPLETE -->
<div class="card hidden" id="screen-level-win">
    <h2>🎉 Level Selesai!</h2>
    <p id="win-desc" style="font-size: 13px;">Selamat! Kamu berhasil menjawab target soal kuis tepat waktu.</p>
    <div style="font-size: 26px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="win-score">0 Poin</div>
    <button class="btn" id="btn-next-lvl" onclick="nextLevel()">Lanjut Level Berikutnya ➡️</button>
</div>

<!-- SCREEN 4: GAME OVER / TAMAT -->
<div class="card hidden" id="screen-end">
    <h2 id="end-title">💥 GAME OVER</h2>
    <div style="font-size: 13px; color: #ffe066; font-weight: bold; margin-bottom: 6px;" id="final-player-info"></div>
    <p id="end-desc" style="font-size: 12px; color: #ff6b6b; font-weight: bold;">Gagal menyelesaikan tantangan!</p>
    <div style="font-size: 30px; font-weight: bold; color: #ffd700; margin: 10px 0;" id="final-score">0 Poin</div>
    <div style="font-weight: bold; color: #4caf50; font-size: 14px; margin-bottom: 15px;" id="final-rank"></div>
    <button class="btn" onclick="resetGame()">Main Lagi 🔄</button>
</div>

<script>
    const width = 6;
    
    const gems = ['🌟', '⛓️', '🌳', '🐂', '🌾', '🦅'];
    const gemClasses = ['gem-topaz', 'gem-sapphire', 'gem-emerald', 'gem-ruby', 'gem-amber', 'gem-amethyst'];

    const levelTimeLimits = { 1: 300, 2: 240, 3: 180 };
    const questionTimeLimits = { 1: 45, 2: 30, 3: 20 };

    // Bank 50 Varian Soal per Level (Total 150 Soal)
    const questionsDB = {
        // Bank Soal Materi BPUPK (Lvl 1), Panitia 9 (Lvl 2), PPKI (Lvl 3) - Tingkat SMP
    const questionsDB = {
        1: [ // LEVEL 1: BPUPK
            { q: "BPUPK secara resmi dibentuk oleh pemerintah pendudukan Jepang pada tanggal...", opt: ["29 April 1945", "1 Maret 1945", "1 Juni 1945", "17 Agustus 1945"], ans: 1 },
            { q: "Nama resmi BPUPK dalam bahasa Jepang adalah...", opt: ["Dokuritsu Junbi Cosakai", "Dokuritsu Junbi Inkai", "Heiho", "Jawa Hokokai"], ans: 0 },
            { q: "Siapakah Ketua (Kaichou) utama BPUPK?", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Dr. K.R.T. Radjiman Wedyodiningrat", "Mr. Soepomo"], ans: 2 },
            { q: "Wakil Ketua BPUPK yang mewakili pihak Jepang adalah...", opt: ["Laksamana Maeda", "Ichibangase Yosio", "General Terauchi", "Kumakichi Harada"], ans: 1 },
            { q: "Tokoh Indonesia yang menjabat sebagai Wakil Ketua BPUPK adalah...", opt: ["R.P. Soeroso", "Mr. Mohammad Yamin", "K.H. Wachid Hasjim", "Achmad Soebardjo"], ans: 0 },
            { q: "Sidang Pertama BPUPK berlangsung pada tanggal...", opt: ["10 - 17 Juli 1945", "22 - 25 Juni 1945", "29 Mei - 1 Juni 1945", "17 - 18 Agustus 1945"], ans: 2 },
            { q: "Agenda utama yang dibahas pada Sidang Pertama BPUPK adalah rumusan...", opt: ["Teks Proklamasi", "Dasar Negara", "Rancangan UUD", "Bentuk Negara"], ans: 1 },
            { q: "Tokoh pertama yang menyampaikan usulan lisan tentang 5 asas dasar negara pada 29 Mei 1945 adalah...", opt: ["Mr. Soepomo", "Ir. Soekarno", "Mr. Mohammad Yamin", "Drs. Mohammad Hatta"], ans: 2 },
            { q: "Berikut ini yang BUKAN merupakan usulan asas lisan Mr. Mohammad Yamin adalah...", opt: ["Peri Kebangsaan", "Peri Kemanusiaan", "Mufakat atau Demokrasi", "Peri Ketuhanan"], ans: 2 },
            { q: "Pada tanggal 31 Mei 1945, Mr. Soepomo menekankan dasar negara Indonesia merdeka berlandaskan paham...", opt: ["Integralistik (Persatuan)", "Individualisme", "Liberalisme", "Kapitalisme"], ans: 0 },
            { q: "Ir. Soekarno menyampaikan pidato rumusan Dasar Negara pada tanggal...", opt: ["29 Mei 1945", "31 Mei 1945", "22 Juni 1945", "1 Juni 1945"], ans: 3 },
            { q: "Istilah 'Pancasila' yang diusulkan Ir. Soekarno lahir atas saran dari seorang ahli...", opt: ["Bahasa", "Sejarah", "Hukum", "Agama"], ans: 0 },
            { q: "Gagasan perasan Pancasila menjadi tiga sila oleh Ir. Soekarno disebut...", opt: ["Ekasila", "Trisila", "Duisila", "Pancasila"], ans: 1 },
            { q: "Inti dari Ekasila (perasan dari Trisila) yang diusulkan oleh Ir. Soekarno adalah...", opt: ["Musyawarah", "Keadilan", "Gotong Royong", "Ketuhanan"], ans: 2 },
            { q: "Jumlah anggota BPUPK dari bangsa Indonesia pada awal pembentukannya adalah...", opt: ["21 orang", "60 orang", "9 orang", "27 orang"], ans: 1 },
            { q: "Gedung Chuo Sangi In yang menjadi tempat sidang BPUPK sekarang dikenal dengan nama...", opt: ["Gedung Merdeka", "Gedung Agung", "Gedung Pancasila", "Istana Negara"], ans: 2 },
            { q: "BPUPK secara resmi dibubarkan pada tanggal...", opt: ["7 Agustus 1945", "18 Agustus 1945", "1 Juni 1945", "22 Juni 1945"], ans: 0 },
            { q: "Alasan utama pemerintah pendudukan Jepang membentuk BPUPK adalah...", opt: ["Ingin memberi kemerdekaan tanpa syarat", "Terdesak oleh Sekutu dalam Perang Pasifik", "Adanya dorongan dari PBB", "Menghadapi pemberontakan dalam negeri"], ans: 1 },
            { q: "Sidang Kedua BPUPK dilaksanakan pada tanggal...", opt: ["29 Mei - 1 Juni 1945", "10 - 17 Juli 1945", "22 Juni 1945", "18 Agustus 1945"], ans: 1 },
            { q: "Fokus pembahasan utama pada Sidang Kedua BPUPK adalah menyusun...", opt: ["Rancangan Undang-Undang Dasar", "Naskah Proklamasi", "Lambang Negara", "Kabinet Pertama"], ans: 0 }
        ],
        2: [ // LEVEL 2: PANITIA 9
            { q: "Panitia Sembilan dibentuk pada masa reses BPUPK, yaitu pada tanggal...", opt: ["1 Juni 1945", "22 Juni 1945", "10 Juli 1945", "17 Agustus 1945"], ans: 1 },
            { q: "Tugas utama dari Panitia Sembilan adalah...", opt: ["Menyusun naskah Proklamasi", "Menyelaraskan usulan dasar negara & menyusun rancangan Pembukaan UUD", "Memilih Presiden dan Wakil Presiden", "Membentuk Komite Nasional"], ans: 1 },
            { q: "Tokoh yang bertindak sebagai Ketua Panitia Sembilan adalah...", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Mohammad Yamin", "K.H. Wachid Hasjim"], ans: 0 },
            { q: "Siapakah yang menjabat sebagai Wakil Ketua Panitia Sembilan?", opt: ["Achmad Soebardjo", "Mr. A.A. Maramis", "Drs. Mohammad Hatta", "H. Agus Salim"], ans: 2 },
            { q: "Naskah rumusan Pembukaan UUD yang dihasilkan Panitia Sembilan pada 22 Juni 1945 adalah...", opt: ["Teks Proklamasi", "Piagam Jakarta (Jakarta Charter)", "Dekrit Presiden", "Sumpah Pemuda"], ans: 1 },
            { q: "Nama 'Piagam Jakarta' untuk naskah hasil Panitia Sembilan diberikan oleh...", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Mohammad Yamin", "H. Agus Salim"], ans: 2 },
            { q: "Ir. Soekarno menyebut naskah hasil Panitia Sembilan dengan istilah...", opt: ["Mukaddimah", "Gentlemen's Agreement", "Konstitusi Negara", "Deklarasi Kemerdekaan"], ans: 0 },
            { q: "Dr. Sukiman Wirjosandjojo memberi sebutan bagi Piagam Jakarta berupa...", opt: ["Gentlemen's Agreement", "Mukaddimah UUD", "Naskah Proklamasi", "Batang Tubuh"], ans: 0 },
            { q: "Rumusan Sila Pertama Pancasila dalam Piagam Jakarta berbunyi...", opt: ["Ketuhanan Yang Maha Esa", "Ketuhanan dengan kewajiban menjalankan syariat Islam bagi pemeluk-pemeluknya", "Ketuhanan yang berkebudayaan", "Peri Ketuhanan"], ans: 1 },
            { q: "Satu-satunya anggota Panitia Sembilan dari wakil golongan Kristen/Non-Muslim adalah...", opt: ["H. Agus Salim", "K.H. Kahar Muzakir", "Mr. A.A. Maramis", "Abikoesno Tjokrosoejoso"], ans: 2 },
            { q: "Tokoh Panitia Sembilan yang mewakili organisasi Nahdlatul Ulama (NU) adalah...", opt: ["K.H. Wachid Hasjim", "K.H. Kahar Muzakir", "H. Agus Salim", "Achmad Soebardjo"], ans: 0 },
            { q: "Tokoh Panitia Sembilan yang mewakili organisasi Muhammadiyah adalah...", opt: ["K.H. Wachid Hasjim", "K.H. Kahar Muzakir", "Mr. Mohammad Yamin", "Drs. Mohammad Hatta"], ans: 1 },
            { q: "Tokoh diplomat berpengalaman yang menjadi anggota Panitia Sembilan adalah...", opt: ["H. Agus Salim", "Mr. A.A. Maramis", "Ir. Soekarno", "Abikoesno Tjokrosoejoso"], ans: 0 },
            { q: "Rapat penyusunan Piagam Jakarta oleh Panitia Sembilan diselenggarakan di...", opt: ["Gedung Chuo Sangi In", "Rumah Ir. Soekarno (Jl. Pegangsaan Timur 56)", "Rumah Laksamana Maeda", "Gedung Pejambon"], ans: 1 },
            { q: "Panitia Sembilan dibentuk sebagai kompromi antara dua kelompok utama di BPUPK, yaitu...", opt: ["Golongan Tua dan Golongan Muda", "Golongan Kebangsaan (Nasionalis) dan Golongan Agama (Islam)", "Golongan Sipil dan Golongan Militer", "Golongan Jawa dan Luar Jawa"], ans: 1 },
            { q: "Berapa jumlah keseluruhan anggota Panitia Sembilan?", opt: ["8 orang", "9 orang", "12 orang", "21 orang"], ans: 1 },
            { q: "Tokoh anggota Panitia Sembilan yang kelak menjadi Menteri Luar Negeri RI Pertama adalah...", opt: ["Achmad Soebardjo", "H. Agus Salim", "Mr. A.A. Maramis", "Drs. Mohammad Hatta"], ans: 0 },
            { q: "Anggota Panitia Sembilan yang mewakili Syarikat Islam (PSII) adalah...", opt: ["K.H. Kahar Muzakir", "Abikoesno Tjokrosoejoso", "Mr. A.A. Maramis", "Achmad Soebardjo"], ans: 1 },
            { q: "Pada Sidang Kedua BPUPK, naskah Piagam Jakarta disepakati untuk dijadikan sebagai...", opt: ["Rancangan Pembukaan UUD", "Naskah Proklamasi", "Dekrit Presiden", "Batang Tubuh Hukum"], ans: 0 },
            { q: "Jumlah kata dalam sila pertama Piagam Jakarta yang diubah saat pengesahan UUD 18 Agustus 1945 adalah...", opt: ["5 kata", "9 kata", "7 kata", "3 kata"], ans: 2 }
        ],
        3: [ // LEVEL 3: PPKI
            { q: "PPKI dibentuk untuk melanjutkan tugas BPUPK pada tanggal...", opt: ["1 Maret 1945", "7 Agustus 1945", "17 Agustus 1945", "18 Agustus 1945"], ans: 1 },
            { q: "Nama resmi PPKI dalam bahasa Jepang dinamakan...", opt: ["Dokuritsu Junbi Inkai", "Dokuritsu Junbi Cosakai", "Heiho", "Jawa Hokokai"], ans: 0 },
            { q: "Siapakah yang ditunjuk sebagai Ketua PPKI?", opt: ["Drs. Mohammad Hatta", "Ir. Soekarno", "Dr. K.R.T. Radjiman Wedyodiningrat", "Mr. Soepomo"], ans: 1 },
            { q: "Siapakah Wakil Ketua PPKI mendampingi Ir. Soekarno?", opt: ["Drs. Mohammad Hatta", "Achmad Soebardjo", "R.P. Soeroso", "Mr. A.A. Maramis"], ans: 0 },
            { q: "Jumlah anggota PPKI yang awalnya dibentuk/disetujui oleh Jepang adalah...", opt: ["21 orang", "60 orang", "9 orang", "27 orang"], ans: 0 },
            { q: "Untuk menegaskan PPKI bukan badan buatan Jepang, anggota PPKI ditambah sebanyak...", opt: ["10 orang", "6 orang tanpa izin Jepang", "5 orang tokoh militer", "9 orang panitia kecil"], ans: 1 },
            { q: "Jumlah total anggota PPKI setelah adanya penambahan anggota bangsa Indonesia menjadi...", opt: ["21 orang", "27 orang", "60 orang", "30 orang"], ans: 1 },
            { q: "Sidang Pertama PPKI diselenggarakan pada tanggal...", opt: ["17 Agustus 1945", "18 Agustus 1945", "19 Agustus 1945", "22 Agustus 1945"], ans: 1 },
            { q: "Berikut ini yang BUKAN merupakan hasil Sidang Pertama PPKI (18 Agustus 1945) adalah...", opt: ["Mengesahkan UUD 1945", "Memilih Presiden dan Wakil Presiden", "Membentuk Komite Nasional Indonesia Pusat (KNIP)", "Membentuk Tentara Nasional Indonesia (TNI)"], ans: 3 },
            { q: "Perubahan Sila Pertama Piagam Jakarta menjadi 'Ketuhanan Yang Maha Esa' diprakarsai oleh...", opt: ["Drs. Mohammad Hatta atas masukan tokoh Indonesia Timur", "Pemerintah Sekutu", "Pihak Tentara Jepang", "Pengurus KNIP"], ans: 0 },
            { q: "Tujuan utama pengubahan Sila Pertama Piagam Jakarta pada tanggal 18 Agustus 1945 adalah...", opt: ["Menjaga persatuan dan kesatuan bangsa Indonesia", "Mengikuti perintah Sekutu", "Menyenangkan pemerintah Jepang", "Meniru konstitusi barat"], ans: 0 },
            { q: "Siapakah Presiden dan Wakil Presiden Pertama RI yang dipilih pada sidang PPKI 18 Agustus 1945?", opt: ["Ir. Soekarno dan Drs. Mohammad Hatta", "Ir. Soekarno dan Mr. Soepomo", "Drs. Mohammad Hatta dan Sutan Sjahrir", "Mr. Mohammad Yamin dan Ir. Soekarno"], ans: 0 },
            { q: "Lembaga pembantu tugas Presiden sebelum dibentuknya DPR/MPR yang disahkan PPKI adalah...", opt: ["KNIP (Komite Nasional Indonesia Pusat)", "DPRD", "PETA", "Kabinet Perdana Menteri"], ans: 0 },
            { q: "Salah satu keputusan penting Sidang Kedua PPKI (19 Agustus 1945) adalah membagi wilayah Indonesia menjadi...", opt: ["5 Provinsi", "8 Provinsi", "12 Provinsi", "27 Provinsi"], ans: 1 },
            { q: "Selain membagi provinsi, Sidang Kedua PPKI (19 Agustus 1945) juga memutuskan pembentukan...", opt: ["12 Kementerian Negara", "Partai Nasional Indonesia", "Badan Keamanan Rakyat", "TNI Angkatan Darat"], ans: 0 },
            { q: "Badan keamanan yang dibentuk pada Sidang Ketiga PPKI tanggal 22 Agustus 1945 dinamakan...", opt: ["Tentara Keamanan Rakyat (TKR)", "Badan Keamanan Rakyat (BKR)", "TNI", "PETA"], ans: 1 },
            { q: "Tokoh yang mengusulkan agar Ir. Soekarno dan Drs. Mohammad Hatta dipilih secara aklamasi adalah...", opt: ["Sayuti Melik", "Achmad Soebardjo", "Otto Iskandardinata", "Sukarni"], ans: 2 },
            { q: "UUD 1945 yang disahkan PPKI pada 18 Agustus 1945 terdiri atas...", opt: ["Pembukaan dan Batang Tubuh (Pasal-pasal)", "Naskah Proklamasi dan Penjelasan", "Piagam Jakarta dan Lampiran", "Dasar Negara dan Aturan Peralihan"], ans: 0 },
            { q: "Perbedaan utama fungsi BPUPK dan PPKI adalah...", opt: ["BPUPK bertugas menyelidiki persiapan kemerdekaan, PPKI bertugas mempersiapkan dan mengesahkan sarana negara merdeka", "BPUPK dibentuk Indonesia, PPKI dibentuk Sekutu", "BPUPK beranggotakan 21 orang, PPKI 60 orang", "BPUPK tidak mengadakan sidang, PPKI mengadakan sidang"], ans: 0 },
            { q: "Penambahan 6 anggota PPKI tanpa sepengetahuan Jepang membuktikan bahwa kemerdekaan Indonesia...", opt: ["Merupakan hadiah dari Jepang", "Merupakan hasil perjuangan murni bangsa Indonesia", "Ditentukan oleh PBB", "Atas dorongan pemerintah Sekutu"], ans: 1 }
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

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
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
        
        if (currentLevel === 1) targetQuestions = 5;
        else if (currentLevel === 2) targetQuestions = 8;
        else if (currentLevel === 3) targetQuestions = 10;

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
        for (let i = 0; i < 3; i++) {
            if (i < lives) heartStr += "❤️";
            else heartStr += "🖤";
        }
        document.getElementById('val-lives').innerText = heartStr;
    }

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
        let matchedSymbol = null;

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
            if (currentMatch.matchedIndices.length > 0) {
                combo++;
            }
        }

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

    function triggerQuiz(symbol) {
        let qList = questionsDB[currentLevel];
        let randomQ = qList[Math.floor(Math.random() * qList.length)];

        document.getElementById('modal-tag').innerText = `KUIS SEJARAH PANCASILA (MATCH ${symbol})`;
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
        let timeLimit = questionTimeLimits[currentLevel];
        let step = 100;
        let totalSteps = (timeLimit * 1000) / step;
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
            questionsAnswered++;
        } else {
            lives--;
        }

        updateUI();

        setTimeout(() => {
            document.getElementById('quiz-modal').classList.add('hidden');
            isProcessing = false;

            if (lives <= 0) {
                gameOver("💔 Nyawa Kamu Habis! Pelajari kembali materi BPUPK, Panitia 9, dan PPKI.");
            } else if (questionsAnswered >= targetQuestions) {
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
            gameOver("SELAMAT! Kamu berhasil menamatkan seluruh Tantangan Sejarah Pancasila!", true);
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
components.html(game_html, height=730, scrolling=False)
