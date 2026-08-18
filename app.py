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
            { q: "Tokoh pertama yang menyampaikan usulan dasar negara secara lisan pada tanggal 29 Mei 1945 adalah...", opt: ["Mr. Mohammad Yamin", "Mr. Soepomo", "Ir. Soekarno", "Drs. Mohammad Hatta"], ans: 0 },
            { q: "Salah satu lima asas dasar negara yang diusulkan oleh Mr. Mohammad Yamin secara lisan adalah...", opt: ["Peri Kebangsaan", "Sosio-nasionalisme", "Ketuhanan yang Berkebudayaan", "Internasionalisme"], ans: 0 },
            { q: "Pada tanggal 31 Mei 1945, pembicara yang menyampaikan konsep negara integralistik adalah...", opt: ["Mr. Soepomo", "Ir. Soekarno", "Mr. Mohammad Yamin", "K.H. Agus Salim"], ans: 0 },
            { q: "Teori paham negara yang diusulkan Mr. Soepomo menekankan persatuan antara pemerintah dan rakyat, disebut paham...", opt: ["Integralistik", "Individualistik", "Kelas/Golongan", "Liberalisme"], ans: 0 },
            { q: "Ir. Soekarno menyampaikan pidato rumusan Dasar Negara pada sidang BPUPK pada tanggal...", opt: ["1 Juni 1945", "29 Mei 1945", "31 Mei 1945", "22 Juni 1945"], ans: 0 },
            { q: "Nama 'Pancasila' yang diusulkan oleh Ir. Soekarno diperoleh atas petunjuk dari seorang ahli...", opt: ["Bahasa", "Sejarah", "Hukum", "Agama"], ans: 0 },
            { q: "Arti kata 'Panca' dalam istilah Pancasila adalah...", opt: ["Lima", "Satu", "Tiga", "Dasar"], ans: 0 },
            { q: "Arti kata 'Sila' dalam istilah Pancasila adalah...", opt: ["Asas atau Dasar", "Aturan", "Hukum", "Tujuan"], ans: 0 },
            { q: "Di bawah ini yang BUKAN merupakan lima asas yang diusulkan Ir. Soekarno pada 1 Juni 1945 adalah...", opt: ["Peri Kemanusiaan", "Kebangsaan Indonesia", "Internasionalisme atau Perikemanusiaan", "Kesejahteraan Sosial"], ans: 0 },
            { q: "Sila kelima yang diusulkan oleh Ir. Soekarno pada 1 Juni 1945 berbunyi...", opt: ["Ketuhanan yang berkebudayaan", "Ketuhanan Yang Maha Esa", "Keadilan Sosial", "Sosio-Demokrasi"], ans: 0 },
            { q: "Konsep peras gagasan Pancasila oleh Ir. Soekarno menjadi tiga sila disebut...", opt: ["Trisila", "Ekasila", "Duisila", "Pancasila"], ans: 0 },
            { q: "Unsur-unsur dari Trisila yang diusulkan oleh Ir. Soekarno adalah...", opt: ["Sosio-nasionalisme, Sosio-demokrasi, Ketuhanan", "Kebangsaan, Kemanusiaan, Keadilan", "Ketuhanan, Kerakyatan, Persatuan", "Persatuan, Mufakat, Kesejahteraan"], ans: 0 },
            { q: "Jika Trisila diperas lagi menjadi satu sila (Ekasila), maka inti dari Ekasila adalah...", opt: ["Gotong Royong", "Musyawarah", "Keadilan", "Ketuhanan"], ans: 0 },
            { q: "Jumlah anggota BPUPK dari bangsa Indonesia (luar anggota Jepang) pada awal pembentukannya adalah...", opt: ["60 orang", "21 orang", "9 orang", "100 orang"], ans: 0 },
            { q: "Jumlah anggota Jepang yang menjadi pengamat/anggota pasif dalam BPUPK adalah...", opt: ["7 orang", "10 orang", "5 orang", "15 orang"], ans: 0 },
            { q: "Pengumuman pembentukan BPUPK disampaikan oleh Panglima Tentara ke-16 Jepang, yaitu...", opt: ["General Kumakichi Harada", "General Terauchi", "Laksamana Maeda", "Tadashi Maeda"], ans: 0 },
            { q: "Penyebab utama pemerintah Jepang membentuk BPUPK adalah...", opt: ["Posisi Jepang terdesak dalam Perang Pasifik", "Keinginan tulus memberi kemerdekaan", "Desakan dari Perserikatan Bangsa-Bangsa", "Pemberontakan serentak seluruh Indonesia"], "ans": 0 },
            { q: "Dalam pidato 29 Mei 1945, Mr. Mohammad Yamin mengusulkan asas kedua yaitu...", opt: ["Peri Kemanusiaan", "Peri Kebangsaan", "Peri Ketuhanan", "Peri Kerakyatan"], "ans": 0 },
            { q: "Usulan tertulis Mr. Mohammad Yamin dalam rancangan UUD memuat sila pertama berbunyi...", opt: ["Ketuhanan Yang Maha Esa", "Ketuhanan dengan kewajiban menjalankan syariat", "Peri Ketuhanan", "Ketuhanan yang berkebudayaan"], "ans": 0 },
            { q: "Prinsip Internasionalisme dalam usulan Ir. Soekarno bertujuan agar Indonesia...", opt: ["Memiliki rasa persaudaraan antar-bangsa di dunia", "Menguasai negara lain", "Menutup diri dari pergaulan dunia", "Tunduk pada kekuasaan asing"], "ans": 0 },
            { q: "Mr. Soepomo menolak paham individualisme karena paham tersebut dianggap...", opt: ["Mementingkan kepentingan diri sendiri di atas masyarakat", "Sesuai dengan adat ketimuran", "Memperkuat persatuan nasional", "Mendukung gotong royong"], "ans": 0 },
            { q: "Dalam pidato 31 Mei 1945, Mr. Soepomo juga menolak paham negara kelas/golongan yang diajarkan oleh...", opt: ["Marx dan Lenin", "John Locke", "Adam Smith", "Montesquieu"], "ans": 0 },
            { q: "Lima prinsip yang diusulkan Mr. Soepomo mencakup: Persatuan, Kekeluargaan, Keseimbangan lahir dan batin, Musyawarah, dan...", opt: ["Keadilan rakyat", "Ketuhanan", "Kebangsaan", "Internasionalisme"], "ans": 0 },
            { q: "Hari Lahir Pancasila yang diperingati setiap tanggal 1 Juni didasarkan pada...", opt: ["Pidato Ir. Soekarno tentang Pancasila tahun 1945", "Pengesahan UUD 1945", "Pembentukan Panitia Sembilan", "Penandatanganan Piagam Jakarta"], "ans": 0 },
            { q: "Keputusan Presiden yang menetapkan tanggal 1 Juni sebagai Hari Lahir Pancasila dan Libur Nasional adalah...", opt: ["Keppres No. 24 Tahun 2016", "Keppres No. 10 Tahun 2000", "Keppres No. 17 Tahun 1945", "Keppres No. 45 Tahun 1965"], "ans": 0 },
            { q: "Siapakah kepala kantor tata usaha / sekretariat BPUPK yang membantu kelancaran sidang?", opt: ["R.P. Soeroso", "Abdoel Gafar Pringgodigdo", "Ichibangase Yosio", "Sanusi"], "ans": 0 },
            { q: "Di antara tokoh berikut, siapakah yang turut menyampaikan pandangan pada sidang pertama BPUPK?", opt: ["Drs. Mohammad Hatta", "Jendral Terauchi", "K.H. Mas Mansyur", "W.R. Soepratman"], "ans": 0 },
            { q: "Perbedaan utama antara gagasan dasar negara Soekarno dan Soepomo terletak pada...", opt: ["Prinsip Internasionalisme & Kesejahteraan Sosial", "Penolakan terhadap gotong royong", "Penggunaan istilah bahasa Jepang", "Penerimaan paham liberalisme"], "ans": 0 },
            { q: "BPUPK dibubarkan pada tanggal 7 Agustus 1945 karena...", opt: ["Dianggap telah menyelesaikan tugas perumusan dasar negara & UUD", "Terjadi perselisihan antar anggota", "Jepang melarang kegiatan politik", "Indonesia sudah secara resmi merdeka"], "ans": 0 },
            { q: "Sebelum BPUPK dibubarkan, hasil kerja sidang diserahkan kepada lembaga penerusnya yaitu...", opt: ["PPKI", "KNIP", "Panitia Sembilan", "DPR"], "ans": 0 },
            { q: "Sila 'Mufakat atau Demokrasi' dalam pidato Soekarno 1 Juni 1945 menekankan pentingnya...", opt: ["Musyawarah dalam mengambil keputusan negara", "Pemilihan umum secara barat", "Keputusan mutlak pemimpin", "Sistem pemerintahan kerajaan"], "ans": 0 },
            { q: "Apa arti penting pidato Ir. Soekarno pada 1 Juni 1945 bagi bangsa Indonesia?", opt: ["Meletakkan kerangka konseptual pertama nama dan isi Dasar Negara", "Menyatakan kemerdekaan Indonesia secara sepihak", "Membentuk pasukan tentara nasional", "Membubarkan kekuasaan Jepang"], "ans": 0 },
            { q: "Dalam pandangan Mr. Soepomo, negara yang ideal bagi Indonesia adalah negara yang...", opt: ["Menyatukan diri dengan seluruh lapisan masyarakat (Integralistik)", "Mengutamakan golongan terbesar", "Melindungi hak pemilik modal saja", "Memisahkan total agama dan negara secara sekuler keras"], "ans": 0 },
            { q: "Ruang sidang Gedung Chuo Sangi In saat ini berlokasi di dalam kompleks...", opt: ["Kementerian Luar Negeri RI", "Kementerian Pendidikan RI", "Istana Merdeka", "Kementerian Pertahanan RI"], "ans": 0 },
            { q: "Tugas utama dari BPUPK ketika pertama kali dibentuk adalah...", opt: ["Mempelajari dan menyelidiki hal penting terkait pembentukan negara Indonesia merdeka", "Menyiapkan teks deklarasi perang", "Mengumpulkan dana perjuangan", "Melantik presiden dan wakil presiden"], "ans": 0 },
            { q: "Sidang BPUPK dilaksanakan secara maraton. Berapa hari lamanya Sidang Pertama BPUPK berlangsung?", opt: ["4 hari", "7 hari", "2 hari", "10 hari"], "ans": 0 },
            { q: "Siapakah di antara tokoh berikut yang mengusulkan prinsip Peri Ketuhanan pada 29 Mei 1945?", opt: ["Mr. Mohammad Yamin", "Ir. Soekarno", "Mr. Soepomo", "Ki Bagus Hadikusumo"], "ans": 0 },
            { q: "Mengapa usulan Ir. Soekarno pada 1 Juni 1945 diterima secara aklamasi oleh para anggota BPUPK?", opt: ["Karena merumuskan nilai-nilai yang menggali jiwa bangsa Indonesia", "Karena diperintahkan oleh pihak Jepang", "Karena hanya Soekarno yang berpidato saat itu", "Karena usulan lain ditolak panitia"], "ans": 0 },
            { q: "Setelah Sidang Pertama BPUPK berakhir pada 1 Juni 1945, BPUPK memasuki masa...", opt: ["Reses (istirahat sidang)", "Pembubaran organisasi", "Perang gerilya", "Pendudukan sekutu"], "ans": 0 },
            { q: "Selama masa reses setelah 1 Juni 1945, dibentuk panitia kecil untuk menampung usulan yang masuk, dinamakan...", opt: ["Panitia Delapan", "PPKI", "KNIP", "Panitia Tiga"], "ans": 0 },
            { q: "Tokoh keagamaan dari Muhammadiyah yang juga menjadi anggota BPUPK adalah...", opt: ["Ki Bagus Hadikusumo", "K.H. Hasyim Asy'ari", "Buya Hamka", "Mohammad Natsir"], "ans": 0 }
        ],
        2: [
            { q: "Panitia Sembilan dibentuk pada masa reses BPUPK, yaitu pada tanggal...", opt: ["22 Juni 1945", "1 Juni 1945", "10 Juli 1945", "17 Agustus 1945"], "ans": 0 },
            { q: "Tugas utama dari Panitia Sembilan adalah...", opt: ["Menyelaraskan usulan dasar negara dan menyusun rancangan Pembukaan UUD", "Menyiapkan naskah proklamasi", "Memilih Presiden dan Wakil Presiden", "Membentuk komite nasional daerah"], "ans": 0 },
            { q: "Siapakah yang bertindak sebagai Ketua Panitia Sembilan?", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Mr. Muhammad Yamin", "K.H. A. Wahid Hasjim"], "ans": 0 },
            { q: "Siapakah yang menjabat sebagai Wakil Ketua Panitia Sembilan?", opt: ["Drs. Mohammad Hatta", "Ir. Soekarno", "Achmad Soebardjo", "Mr. A.A. Maramis"], "ans": 0 },
            { q: "Hasil karya monumental dari Panitia Sembilan yang disepakati pada 22 Juni 1945 dinamakan...", opt: ["Piagam Jakarta (Jakarta Charter)", "Teks Proklamasi", "Dekrit Presiden", "Sumpah Pemuda"], "ans": 0 },
            { q: "Siapakah tokoh yang memberikan nama 'Piagam Jakarta' pada naskah rancangan Pembukaan UUD tersebut?", opt: ["Mr. Muhammad Yamin", "Ir. Soekarno", "Drs. Mohammad Hatta", "H. Agus Salim"], "ans": 0 },
            { q: "Ir. Soekarno menyebut naskah hasil Panitia Sembilan (Piagam Jakarta) dengan istilah...", opt: ["Mukaddimah", "Gentlemen's Agreement", "Konstitusi Negara", "Deklarasi Kemerdekaan"], "ans": 0 },
            { q: "Sukiman Wirjosandjojo menyebut Piagam Jakarta sebagai...", opt: ["Gentlemen's Agreement", "Mukaddimah UUD", "Naskah Kemerdekaan", "Batang Tubuh UUD"], "ans": 0 },
            { q: "Rumusan Sila Pertama Pancasila dalam Piagam Jakarta berbunyi...", opt: ["Ketuhanan dengan kewajiban menjalankan syariat Islam bagi pemeluk-pemeluknya", "Ketuhanan Yang Maha Esa", "Ketuhanan yang berkebudayaan", "Peri Ketuhanan"], "ans": 0 },
            { q: "Berapa jumlah kata yang terkenal diubah pada Sila Pertama Piagam Jakarta saat pengesahan 18 Agustus 1945?", opt: ["7 kata", "5 kata", "9 kata", "3 kata"], "ans": 0 },
            { q: "Anggota Panitia Sembilan yang mewakili unsur Kristen/Golongan Nasionalis Kristen adalah...", opt: ["Mr. A.A. Maramis", "H. Agus Salim", "K.H. Kahar Muzakir", "Abikoesno Tjokrosoejoso"], "ans": 0 },
            { q: "Tokoh Panitia Sembilan dari unsur organisasi Nahdlatul Ulama (NU) adalah...", opt: ["K.H. A. Wahid Hasjim", "K.H. Kahar Muzakir", "H. Agus Salim", "Abikoesno Tjokrosoejoso"], "ans": 0 },
            { q: "Tokoh diplomasi ulung yang menjadi anggota Panitia Sembilan dan terkenal cerdas berdebat adalah...", opt: ["H. Agus Salim", "Mr. A.A. Maramis", "Achmad Soebardjo", "Mr. Muhammad Yamin"], "ans": 0 },
            { q: "Di manakah lokasi dilaksanakannya rapat penetapan Piagam Jakarta oleh Panitia Sembilan?", opt: ["Kediaman Ir. Soekarno, Jl. Pegangsaan Timur No. 56", "Gedung Chuo Sangi In", "Rumah Laksamana Maeda", "Gedung Pejambon"], "ans": 0 },
            { q: "Anggota Panitia Sembilan dari Sarekat Islam (PSII) adalah...", opt: ["Abikoesno Tjokrosoejoso", "K.H. Kahar Muzakir", "Mr. A.A. Maramis", "Achmad Soebardjo"], "ans": 0 },
            { q: "Tokoh Panitia Sembilan dari Muhammadiyah / Perguruan Islam yang mewakili golongan Islam adalah...", opt: ["K.H. Kahar Muzakir", "K.H. A. Wahid Hasjim", "Mr. Muhammad Yamin", "Drs. Mohammad Hatta"], "ans": 0 },
            { q: "Tokoh diplomat yang nantinya menjabat Menteri Luar Negeri RI Pertama dan menjadi anggota Panitia Sembilan adalah...", opt: ["Achmad Soebardjo", "H. Agus Salim", "Mr. A.A. Maramis", "Drs. Mohammad Hatta"], "ans": 0 },
            { q: "Panitia Sembilan dibentuk karena adanya perbedaan pandangan mendasar antara dua kelompok utama, yaitu...", opt: ["Golongan Kebangsaan (Nasionalis) dan Golongan Agama (Islam)", "Golongan Tua dan Golongan Muda", "Golongan Militer dan Golongan Sipil", "Golongan Jawa dan Luar Jawa"], "ans": 0 },
            { q: "Sidang Kedua BPUPK dilaksanakan pada tanggal...", opt: ["10 - 17 Juli 1945", "29 Mei - 1 Juni 1945", "22 Juni 1945", "18 Agustus 1945"], "ans": 0 },
            { q: "Pada Sidang Kedua BPUPK, naskah Piagam Jakarta disepakati untuk dijadikan sebagai...", opt: ["Rancangan Pembukaan UUD", "Teks Proklamasi", "Batang Tubuh Konstitusi", "Dekrit Presiden"], "ans": 0 },
            { q: "Dalam Sidang Kedua BPUPK dibentuk Panitia Perancang UUD yang diketuai oleh...", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Abikoesno Tjokrosoejoso", "Mr. Soepomo"], "ans": 0 },
            { q: "Panitia Kecil Keuangan dan Perekonomian dalam Sidang Kedua BPUPK diketuai oleh...", opt: ["Drs. Mohammad Hatta", "Ir. Soekarno", "Mr. A.A. Maramis", "Abikoesno Tjokrosoejoso"], "ans": 0 },
            { q: "Panitia Kecil Pembelaan Tanah Air dalam BPUPK diketuai oleh...", opt: ["Abikoesno Tjokrosoejoso", "Drs. Mohammad Hatta", "Ir. Soekarno", "Mr. Soepomo"], "ans": 0 },
            { q: "Siapakah ketua Panitia Kecil Perancang Tata Bahasa / UUD yang dibentuk oleh Ir. Soekarno?", opt: ["Mr. Soepomo", "Mr. Muhammad Yamin", "Achmad Soebardjo", "H. Agus Salim"], "ans": 0 },
            { q: "Berapa jumlah keseluruhan anggota Panitia Sembilan?", opt: ["9 orang", "8 orang", "12 orang", "21 orang"], "ans": 0 },
            { q: "Di bawah ini yang BUKAN anggota Panitia Sembilan adalah...", opt: ["Dr. K.R.T. Radjiman Wedyodiningrat", "Mr. A.A. Maramis", "H. Agus Salim", "K.H. A. Wahid Hasjim"], "ans": 0 },
            { q: "Apa nama Panitia Kecil yang dibentuk sebelum Panitia Sembilan pada akhir sidang pertama BPUPK?", opt: ["Panitia Delapan", "Panitia Tujuh", "Panitia Lima", "Panitia Sebelas"], "ans": 0 },
            { q: "Sila kedua dalam naskah Piagam Jakarta berbunyi...", opt: ["Kemanusiaan yang adil dan beradab", "Persatuan Indonesia", "Peri Kemanusiaan", "Keadilan sosial bagi seluruh rakyat Indonesia"], "ans": 0 },
            { q: "Sila ketiga dalam naskah Piagam Jakarta berbunyi...", opt: ["Persatuan Indonesia", "Kemanusiaan yang adil dan beradab", "Kebangsaan Indonesia", "Kerakyatan yang dipimpin oleh hikmat kebijaksanaan"], "ans": 0 },
            { q: "Sila keempat dalam naskah Piagam Jakarta berbunyi...", opt: ["Kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan", "Persatuan Indonesia", "Keadilan sosial", "Mufakat atau demokrasi"], "ans": 0 },
            { q: "Sila kelima dalam naskah Piagam Jakarta berbunyi...", opt: ["Keadilan sosial bagi seluruh rakyat Indonesia", "Kesejahteraan sosial", "Ketuhanan Yang Maha Esa", "Persatuan Indonesia"], "ans": 0 },
            { q: "Fungsi utama kesepakatan Piagam Jakarta pada 22 Juni 1945 adalah sebagai kompromi politik antara...", opt: ["Nasionalis sekuler dan Nasionalis Islami", "Pemerintah Jepang dan Pejuang Indonesia", "Golongan Pemuda dan Golongan Tua", "Pemerintah Sekutu dan Indonesia"], "ans": 0 },
            { q: "Tokoh Nasionalis dalam Panitia Sembilan terdiri dari Ir. Soekarno, Moh. Hatta, Muh. Yamin, Achmad Soebardjo, dan...", opt: ["Mr. A.A. Maramis", "K.H. Wahid Hasjim", "H. Agus Salim", "Abikoesno Tjokrosoejoso"], "ans": 0 },
            { q: "Empat tokoh perwakilan Golongan Islam dalam Panitia Sembilan adalah Wahid Hasjim, Agus Salim, Kahar Muzakir, dan...", opt: ["Abikoesno Tjokrosoejoso", "Achmad Soebardjo", "Mr. A.A. Maramis", "Moh. Hatta"], "ans": 0 },
            { q: "Pada sidang BPUPK tanggal 14 Juli 1945, Ir. Soekarno melaporkan tiga hasil kerja Panitia Perancang UUD, yaitu...", opt: ["Pernyataan Kemerdekaan, Pembukaan UUD, dan Batang Tubuh UUD", "Teks Proklamasi, Pancasila, dan Lagu Indonesia Raya", "Pancasila, Bendera Merah Putih, dan struktur kementerian", "Lagu Kebangsaan, Wilayah Negara, dan Presiden"], "ans": 0 },
            { q: "Sikap yang ditunjukkan para tokoh pendiri bangsa saat menyusun Piagam Jakarta adalah...", opt: ["Toleransi, saling menghargai, dan mengutamakan persatuan", "Mementingkan kelompok sendiri secara mutlak", "Menolak musyawarah", "Mengikuti seluruh arahan penjajah"], "ans": 0 },
            { q: "Istilah 'Charter' dalam kata Jakarta Charter berarti...", opt: ["Piagam / Naskah Perjanjian Resmi", "Surat Keputusan", "Undang-Undang", "Hukum Adat"], "ans": 0 },
            { q: "Mengapa Piagam Jakarta menjadi naskah yang sangat krusial dalam sejarah Pancasila?", opt: ["Karena memuat sistematika 5 sila Pancasila yang lengkap secara tertulis", "Karena diumumkan langsung oleh Kaisar Jepang", "Karena menghapus semua hukum kolonial", "Karena ditandatangani oleh seluruh rakyat Indonesia"], "ans": 0 },
            { q: "Siapakah anggota Panitia Sembilan yang berasal dari wilayah Minahasa, Sulawesi Utara?", opt: ["Mr. A.A. Maramis", "H. Agus Salim", "K.H. Kahar Muzakir", "Achmad Soebardjo"], "ans": 0 },
            { q: "Siapakah anggota Panitia Sembilan yang lahir di Minangkabau dan terkenal dengan julukan 'The Grand Old Man'?", opt: ["H. Agus Salim", "Mr. Muhammad Yamin", "Drs. Mohammad Hatta", "Achmad Soebardjo"], "ans": 0 },
            { q: "Siapakah anggota Panitia Sembilan yang memimpin perumusan awal naskah proklamasi bersama Soekarno-Hatta?", opt: ["Achmad Soebardjo", "Abikoesno Tjokrosoejoso", "K.H. Kahar Muzakir", "Mr. A.A. Maramis"], "ans": 0 },
            { q: "Pada Sidang BPUPK 16 Juli 1945, BPUPK secara resmi menyetujui...", opt: ["Rancangan Undang-Undang Dasar", "Pembubaran organisasi", "Perang melawan tentara Sekutu", "Penunjukan Soekarno sebagai Raja"], "ans": 0 },
            { q: "Rancangan Pembukaan UUD yang diambil dari Piagam Jakarta disahkan BPUPK pada tanggal...", opt: ["14 Juli 1945", "22 Juni 1945", "18 Agustus 1945", "17 Agustus 1945"], "ans": 0 },
            { q: "Nilai utama yang dapat diteladani dari keputusan Panitia Sembilan adalah...", opt: ["Musyawarah mufakat demi persatuan nasional", "Mempertahankan ego pribadi", "Mementingkan suara terbanyak tanpa kompromi", "Menyerahkan keputusan pada pihak luar"], "ans": 0 },
            { q: "Tujuan Panitia Sembilan mengumpulkan usulan-usulan anggota BPUPK adalah...", opt: ["Menyusun dasar negara yang disepakati seluruh golongan", "Memilih menteri-menteri kabinet", "Mengumpulkan naskah sejarah antik", "Menyusun strategi militer"], "ans": 0 },
            { q: "Siapakah tokoh dalam Panitia Sembilan yang juga adik dari HOS Tjokroaminoto?", opt: ["Abikoesno Tjokrosoejoso", "K.H. A. Wahid Hasjim", "Achmad Soebardjo", "Mr. A.A. Maramis"], "ans": 0 },
            { q: "Panitia Sembilan bekerja pada kurun waktu antara...", opt: ["Akhir Sidang I dan Pembukaan Sidang II BPUPK", "Setelah Proklamasi Kemerdekaan", "Saat pendudukan Belanda di Yogyakarta", "Sebelum pembentukan BPUPK"], "ans": 0 },
            { q: "Mengapa Piagam Jakarta dinamakan 'Gentlemen's Agreement' oleh Ir. Soekarno?", opt: ["Karena merupakan kesepakatan kehormatan antartokoh berbudi luhur", "Karena dibuat oleh tentara Inggris", "Karena hanya berlaku bagi laki-laki", "Karena sifatnya tidak resmi"], "ans": 0 },
            { q: "Apa pengaruh kesepakatan Piagam Jakarta terhadap kelancaran sidang BPUPK kedua?", opt: ["Mempermudah jalannya pembatasan perumusan pasal-pasal UUD", "Menyebabkan sidang dibatalkan", "Membuat Jepang membubarkan BPUPK lebih cepat", "Memicu konflik berkepanjangan"], "ans": 0 },
            { q: "Apa landasan utama Panitia Sembilan dalam merumuskan isi Piagam Jakarta?", opt: ["Nilai luhur dan cita-cita kemerdekaan bangsa Indonesia", "Konstitusi negara Jepang", "Konstitusi Amerika Serikat", "Peraturan hukum kolonial Belanda"], "ans": 0 }
        ],
        3: [
            { q: "PPKI secara resmi dibentuk oleh pihak Jepang pada tanggal...", opt: ["7 Agustus 1945", "18 Agustus 1945", "1 Maret 1945", "17 Agustus 1945"], "ans": 0 },
            { q: "Nama PPKI dalam bahasa Jepang dinamakan...", opt: ["Dokuritsu Junbi Inkai", "Dokuritsu Junbi Cosakai", "Heiho", "Chuo Sangi In"], "ans": 0 },
            { q: "Siapakah Ketua dari Panitia Persiapan Kemerdekaan Indonesia (PPKI)?", opt: ["Ir. Soekarno", "Drs. Mohammad Hatta", "Dr. Radjiman Wedyodiningrat", "Mr. Soepomo"], "ans": 0 },
            { q: "Siapakah Wakil Ketua dari PPKI?", opt: ["Drs. Mohammad Hatta", "Ir. Soekarno", "Mr. A.A. Maramis", "Achmad Soebardjo"], "ans": 0 },
            { q: "Pada awal pembentukannya, berapa jumlah anggota PPKI yang ditunjuk oleh Jepang?", opt: ["21 orang", "60 orang", "9 orang", "27 orang"], "ans": 0 },
            { q: "Berapa jumlah anggota tambahan yang dimasukkan oleh tokoh Indonesia tanpa sepengetahuan Jepang ke dalam PPKI?", opt: ["6 orang", "7 orang", "5 orang", "10 orang"], "ans": 0 },
            { q: "Sehingga total keseluruhan anggota PPKI saat sidang tanggal 18 Agustus 1945 berjumlah...", opt: ["27 orang", "21 orang", "67 orang", "30 orang"], "ans": 0 },
            { q: "Penambahan 6 anggota PPKI tanpa izin Jepang bertujuan untuk menegaskan bahwa...", opt: ["PPKI adalah badan murni perjuangan bangsa Indonesia, bukan bentukan Jepang", "Jepang telah menyerah tanpa syarat", "Anggota tersebut adalah kerabat penguasa", "Untuk memenuhi syarat voting"], "ans": 0 },
            { q: "Sidang pertama PPKI pasca proklamasi kemerdekaan dilaksanakan pada tanggal...", opt: ["18 Agustus 1945", "17 Agustus 1945", "19 Agustus 1945", "22 Agustus 1945"], "ans": 0 },
            { q: "Di manakah sidang PPKI pada tanggal 18 Agustus 1945 diselenggarakan?", opt: ["Gedung Pejambon (Gedung Kesenian Jakarta)", "Kediaman Ir. Soekarno", "Rumah Laksamana Maeda", "Gedung Merdeka Bandung"], "ans": 0 },
            { q: "Salah satu keputusan paling krusial dalam Sidang PPKI 18 Agustus 1945 adalah...", opt: ["Mengesahkan UUD 1945 dan penetapan Pancasila sebagai Dasar Negara", "Membentuk Tentara Nasional Indonesia", "Menetapkan lagu Indonesia Raya", "Memilih para menteri kabinet"], "ans": 0 },
            { q: "Sidang PPKI 18 Agustus 1945 secara resmi memilih Ir. Soekarno dan Drs. Mohammad Hatta masing-masing sebagai...", opt: ["Presiden dan Wakil Presiden RI Pertama", "Ketua BPUPK dan Wakil BPUPK", "Perdana Menteri dan Menteri Luar Negeri", "Gubernur Jenderal dan Wakil"], "ans": 0 },
            { q: "Keputusan ketiga dari Sidang PPKI 18 Agustus 1945 sebelum terbentuknya DPR/MPR adalah membentuk...", opt: ["Komite Nasional Indonesia Pusat (KNIP)", "Dewan Pertimbangan Agung", "Mahkamah Agung", "Badan Keamanan Rakyat"], "ans": 0 },
            { q: "Perubahan 7 kata sila pertama Piagam Jakarta menjadi 'Ketuhanan Yang Maha Esa' diprakarsai oleh...", opt: ["Drs. Mohammad Hatta", "Ir. Soekarno", "Mr. Soepomo", "Sutan Sjahrir"], "ans": 0 },
            { q: "Sebelum sidang 18 Agustus 1945 dimulai, Moh. Hatta mengumpulkan tokoh-tokoh Islam untuk mendiskusikan...", opt: ["Keberatan utusan Indonesia Timur terhadap rumusan 7 kata Sila Pertama", "Penetapan ibu kota negara", "Pemilihan menteri kabinet", "Rancangan bendera negara"], "ans": 0 },
            { q: "Utusan dari Indonesia Bagian Timur yang menyampaikan aspirasi keberatan terhadap 7 kata dalam Piagam Jakarta menemui Hatta melalui seorang perwira Jepang bernama...", opt: ["Laksamana Tadashi Maeda / Nishijima", "General Terauchi", "Kumakichi Harada", "Ichibangase Yosio"], "ans": 0 },
            { q: "Siapakah di antara tokoh Islam berikut yang ikut diajak berdiskusi oleh Hatta pada 18 Agustus pagi mengenai perubahan Sila I?", opt: ["Ki Bagus Hadikusumo, Wahid Hasjim, Kasman Singodimedjo, Teuku M. Hasan", "K.H. Agus Salim, Abikoesno, Kahar Muzakir", "Natsir, Hamka, Sukiman, Syahrir", "Soepomo, Yamin, Maramis"], "ans": 0 },
            { q: "Alasan utama tokoh-tokoh Islam bersedia mengubah 7 kata sila pertama Piagam Jakarta adalah...", opt: ["Demi menjaga persatuan, kesatuan, dan keutuhan NKRI", "Karena dipaksa oleh Jepang", "Karena mendapat kompensasi jabatan", "Karena ketakutan akan ancaman sekutu"], "ans": 0 },
            { q: "Pengubahan rumusan Sila Pertama Pancasila membuktikan bahwa para pendiri bangsa memiliki jiwa...", opt: ["Toleransi tinggi, negarawan, dan mengutamakan kepentingan nasional", "Egois dan kaku", "Pasrah pada keadaan", "Mementingkan wilayah tertentu saja"], "ans": 0 },
            { q: "Kata 'Mukaddimah' dalam rancangan UUD pada sidang PPKI 18 Agustus 1945 diubah menjadi kata...", opt: ["Pembukaan", "Pendahuluan", "Preambule", "Pengantar"], "ans": 0 },
            { q: "Kata 'Hukum Dasar' dalam naskah UUD diubah oleh PPKI menjadi...", opt: ["Undang-Undang Dasar", "Konstitusi Negara", "Peraturan Pemerintah", "Hukum Nasional"], "ans": 0 },
            { q: "Persyaratan Presiden pada Pasal 6 UUD 1945 awal berbunyi 'orang Indonesia asli yang beragama Islam' diubah menjadi...", opt: ["orang Indonesia asli", "warga negara Indonesia saja", "orang yang lahir di Jawa", "orang yang berusia 40 tahun"], "ans": 0 },
            { q: "Sistematika UUD 1945 yang disahkan PPKI pada 18 Agustus 1945 terdiri dari...", opt: ["Pembukaan, Batang Tubuh (Pasal-pasal), dan Penjelasan", "Pembukaan saja", "Batang Tubuh dan Lampiran", "Piagam Jakarta dan Konstitusi"], "ans": 0 },
            { q: "Siapakah tokoh Islam yang ditunjuk Hatta untuk meyakinkan Ki Bagus Hadikusumo agar menerima rumusan 'Ketuhanan Yang Maha Esa'?", opt: ["Kasman Singodimedjo", "K.H. Agus Salim", "Achmad Soebardjo", "Mr. A.A. Maramis"], "ans": 0 },
            { q: "Tiga tokoh Indonesia yang dipanggil oleh Jenderal Terauchi ke Dalat, Vietnam pada 9 Agustus 1945 adalah...", opt: ["Ir. Soekarno, Drs. Moh. Hatta, Dr. Radjiman Wedyodiningrat", "Ir. Soekarno, Moh. Yamin, Soepomo", "Moh. Hatta, Sjahrir, Tan Malaka", "Radjiman, Agus Salim, Wahid Hasyim"], "ans": 0 },
            { q: "Tujuan Jenderal Terauchi memanggil tiga tokoh Indonesia ke Dalat adalah untuk...", opt: ["Menyampaikan janji kemerdekaan Indonesia oleh pemerintah Jepang", "Melarang kegiatan PPKI", "Menangkap para pejuang", "Meminta bantuan pasukan tentara"], "ans": 0 },
            { q: "Pada tanggal 19 Agustus 1945, PPKI mengadakan sidang kedua yang memutuskan...", opt: ["Pembagian wilayah Indonesia menjadi 8 Provinsi & pembentukan 12 Kementerian", "Pengesahan Teks Proklamasi", "Pembentukan TNI", "Pengangkatan anggota DPR"], "ans": 0 },
            { q: "Berapa jumlah provinsi pertama yang dibentuk oleh PPKI pada sidang tanggal 19 Agustus 1945?", opt: ["8 Provinsi", "12 Provinsi", "5 Provinsi", "34 Provinsi"], "ans": 0 },
            { q: "Pada sidang tanggal 22 Agustus 1945, PPKI memutuskan pembentukan tiga badan utama, yaitu...", opt: ["KNIP, PNI (Partai Nasional Indonesia), dan BKR (Badan Keamanan Rakyat)", "TNI, POLRI, dan DPR", "BPUPK, PPKI, dan MPR", "Kabinet, Kejaksaan, dan Mahkamah Agung"], "ans": 0 },
            { q: "Kapan PPKI secara de facto menyelesaikan seluruh tugas perumusan awal kelengkapan negara?", opt: ["22 Agustus 1945", "18 Agustus 1945", "17 Agustus 1945", "1 Oktober 1945"], "ans": 0 },
            { q: "Secara yuridis-formal, Pancasila disahkan sebagai Dasar Negara Indonesia pada tanggal...", opt: ["18 Agustus 1945", "1 Juni 1945", "22 Juni 1945", "17 Agustus 1945"], "ans": 0 },
            { q: "Tata urutan Pancasila yang sah dan berlaku hingga saat ini tercantum dalam...", opt: ["Pembukaan UUD 1945 Alinea IV", "Piagam Jakarta", "Batang Tubuh UUD 1945", "Teks Proklamasi"], "ans": 0 },
            { q: "Di bawah ini yang BUKAN merupakan keputusan Sidang PPKI 18 Agustus 1945 adalah...", opt: ["Menetapkan 8 Provinsi Indonesia", "Mengesahkan Pembukaan dan Batang Tubuh UUD 1945", "Memilih Presiden Ir. Soekarno", "Memilih Wakil Presiden Drs. Mohammad Hatta"], "ans": 0 },
            { q: "Siapakah tokoh asal Aceh yang ikut berdiskusi pada pagi 18 Agustus 1945 dan menyetujui perubahan Sila I?", opt: ["Teuku Muhammad Hasan", "Mr. Kasman Singodimedjo", "Ki Bagus Hadikusumo", "K.H. A. Wahid Hasjim"], "ans": 0 },
            { q: "Rumusan sila kedua Pancasila yang terdapat dalam Pembukaan UUD 1945 alinea IV berbunyi...", opt: ["Kemanusiaan yang adil dan beradab", "Persatuan Indonesia", "Keadilan sosial", "Kerakyatan yang dipimpin oleh hikmat"], "ans": 0 },
            { q: "Rumusan sila ketiga Pancasila yang terdapat dalam Pembukaan UUD 1945 alinea IV berbunyi...", opt: ["Persatuan Indonesia", "Kemanusiaan yang adil dan beradab", "Ketuhanan Yang Maha Esa", "Kebangsaan Indonesia"], "ans": 0 },
            { q: "Rumusan sila kelima Pancasila yang disahkan oleh PPKI berbunyi...", opt: ["Keadilan sosial bagi seluruh rakyat Indonesia", "Kesejahteraan sosial", "Perikemanusiaan dan keadilan", "Keadilan rakyat Indonesia"], "ans": 0 },
            { q: "Sifat keanggotaan PPKI pasca penambahan 6 tokoh tanpa izin Jepang berubah menjadi...", opt: ["Perwakilan murni seluruh rakyat Indonesia", "Badan boneka Jepang", "Organisasi militer", "Badan pengawas sekutu"], "ans": 0 },
            { q: "Siapakah anggota tambahan PPKI yang dimasukkan tanpa sepengetahuan Jepang?", opt: ["Achmad Soebardjo, Sayuti Melik, Ki Hadjar Dewantara, Kasman Singodimedjo, Iwa Koesoemasoemantri, R.A.A. Wiranatakoesoema", "Moh. Yamin, Soepomo, Radjiman", "Agus Salim, Maramis, Wahid Hasyim", "Sjahrir, Tan Malaka, Hatta"], "ans": 0 },
            { q: "Peristiwa Rengasdengklok terjadi menjelang pelaksanaan sidang PPKI karena dorongan dari...", opt: ["Golongan Pemuda yang menginginkan proklamasi tanpa campur tangan Jepang/PPKI", "Pemerintah Jepang", "Tentara Sekutu", "Anggota BPUPK"], "ans": 0 },
            { q: "Mengapa Soekarno-Hatta menolak desakan pemuda untuk memproklamasikan kemerdekaan di luar PPKI pada 16 Agustus?", opt: ["Karena ingin menghindari pertumpahan darah dan mengonfirmasi situasi via PPKI", "Karena takut kepada tentara Jepang", "Karena belum membuat naskah proklamasi", "Karena menanti kabar dari Sekutu"], "ans": 0 },
            { q: "Usulan agar pemilihan Presiden dan Wakil Presiden dilakukan secara aklamasi dalam sidang PPKI diajukan oleh...", opt: ["Otto Iskandardinata", "Mr. Soepomo", "Moh. Yamin", "Achmad Soebardjo"], "ans": 0 },
            { q: "Aklamasi dalam pemilihan Ir. Soekarno dan Moh. Hatta berarti pemilihan dilakukan secara...", opt: ["Persetujuan bulat secara lisan tanpa pemungutan suara tertulis", "Voting rahasia", "Undian terbuka", "Penunjukan langsung oleh Sekutu"], "ans": 0 },
            { q: "Kedudukan Pancasila yang disahkan pada 18 Agustus 1945 berfungsi sebagai...", opt: ["Dasar Negara dan Pandangan Hidup Bangsa Indonesia", "Hukum pidana sementara", "Piagam perjanjian dengan Sekutu", "Aturan keanggotaan komite"], "ans": 0 },
            { q: "Gedung tempat berlangsungnya Sidang PPKI 18 Agustus 1945 kini digunakan sebagai Gedung...", opt: ["Kementerian Luar Negeri (Gedung Pancasila)", "Kementerian Keuangan", "Museum Nasional", "DPR RI"], "ans": 0 },
            { q: "Siapakah tokoh yang mengetik teks Proklamasi sebelum disahkan dan dibacakan?", opt: ["Sayuti Melik", "BM Diah", "Sukarni", "Chaerul Saleh"], "ans": 0 },
            { q: "Salah satu Gubernur pertama yang diangkat oleh PPKI pada sidang 19 Agustus 1945 untuk Jawa Tengah adalah...", opt: ["R. Panji Soeroso", "Teuku Muhammad Hasan", "R.A. Suryo", "Sam Ratulangi"], "ans": 0 },
            { q: "Penetapan 18 Agustus sebagai Hari Konstitusi Republik Indonesia didasarkan pada Keppres Nomor...", opt: ["Keppres No. 18 Tahun 2008", "Keppres No. 24 Tahun 2016", "Keppres No. 10 Tahun 1999", "Keppres No. 5 Tahun 1945"], "ans": 0 },
            { q: "Makna utama pengesahan Pancasila pada 18 Agustus 1945 bagi keberlangsungan NKRI adalah...", opt: ["Landasan kokoh pemersatu keanekaragaman suku, agama, dan budaya Indonesia", "Syarat pemberian pinjaman modal luar negeri", "Formalitas pengakuan sekutu", "Dasar pembentukan koalisi politik"], "ans": 0 },
            { q: "Hubungan antara Proklamasi 17 Agustus 1945 dan Sidang PPKI 18 Agustus 1945 adalah...", opt: ["Proklamasi menyatakan kemerdekaan, sedangkan Sidang PPKI menegakkan tata kelola dan dasar negara yang sah", "Proklamasi membatalkan hasil sidang PPKI", "Sidang PPKI membubarkan kemerdekaan", "Dua peristiwa yang tidak saling berkaitan"], "ans": 0 }
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
