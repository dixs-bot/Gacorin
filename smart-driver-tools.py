#!/usr/bin/env python3
# ==================================================
# SMART DRIVER TOOL v1.1 — ANDROID 9 NON-ROOT
# Crafted by D Z Y Q I
# Upgraded for real drivers, real work
# ==================================================

import subprocess, time, sys, json, os, re

# ================= WARNA =================
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RED    = "\033[91m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

# ================= PROTECTED APPS =================
PROTECTED_APPS = (
    "com.gojek.app",
    "com.grabtaxi.passenger",
    "com.whatsapp",
    "com.google",
)

# ================= UTIL =================
def run(cmd):
    return subprocess.getoutput(cmd)

def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ================= ANIMASI =================
def loading_text(text, duration=2):
    frames = ["", ".", "..", "..."]
    start = time.time()
    i = 0
    while time.time() - start < duration:
        sys.stdout.write(f"\r{text}{frames[i % 4]}")
        sys.stdout.flush()
        time.sleep(0.4)
        i += 1
    sys.stdout.write("\r" + " " * 80 + "\r")

def progress_bar(label, width=22):
    for i in range(width + 1):
        bar = "█" * i + "░" * (width - i)
        sys.stdout.write(f"\r{CYAN}[ {label:<22} {bar} ]{RESET}")
        sys.stdout.flush()
        time.sleep(0.04)
    print()

# ================= INTRO =================
def intro_banner():
    print(CYAN + """
██████╗ ███████╗██╗   ██╗ ██████╗ ██╗
██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔═══██╗██║
██║  ██║  ███╔╝  ╚████╔╝ ██║   ██║██║
██║  ██║ ███╔╝    ╚██╔╝  ██║▄▄ ██║██║
██████╔╝███████╗   ██║   ╚██████╔╝██║
╚═════╝ ╚══════╝   ╚═╝    ╚══▀▀═╝ ╚═╝
""" + RESET)
    print(GREEN + "SMART DRIVER TOOL v1.1" + RESET)
    print(YELLOW + "ANDROID 9 • NON-ROOT EDITION\n" + RESET)

    progress_bar("Initializing system")
    progress_bar("Loading GPS module")
    progress_bar("Loading Network module")
    progress_bar("Finalizing setup")

    print(GREEN + "\n✔ System Ready\n" + RESET)

# ================= GPS =================
def get_gps_accuracy():
    try:
        out = run("termux-location -p gps -r once")
        if "error" in out.lower():
            return None
        data = json.loads(out)
        return data.get("accuracy")
    except:
        return None

# ================= SIZE =================
def get_folder_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except:
                pass
    return total

# ================= MODE 1 =================
def aggressive_junk_cleaner():
    header("💣 SAFE AGGRESSIVE JUNK CLEANER++")

    total = 0
    cleaned = []

    thumb = "/storage/emulated/0/DCIM/.thumbnails"
    if os.path.exists(thumb):
        size = get_folder_size(thumb)
        loading_text("🖼️ Menghapus thumbnail cache", 2)
        run(f"rm -rf '{thumb}'")
        total += size
        cleaned.append("DCIM/.thumbnails")

    bases = [
        "/storage/emulated/0/Android/data",
        "/storage/emulated/0/Android/media"
    ]

    for base in bases:
        if not os.path.exists(base):
            continue

        for app in os.listdir(base):
            if app.startswith(PROTECTED_APPS):
                continue

            app_path = os.path.join(base, app)

            cache_path = os.path.join(app_path, "cache")
            if os.path.exists(cache_path):
                size = get_folder_size(cache_path)
                if size > 0:
                    loading_text(f"🗑️ Cache {app}", 0.7)
                    run(f"rm -rf '{cache_path}'")
                    total += size
                    cleaned.append(app)

            for root, dirs, files in os.walk(app_path):
                for f in files:
                    if f.endswith((".tmp", ".log", ".bak", ".cache")):
                        try:
                            fp = os.path.join(root, f)
                            size = os.path.getsize(fp)
                            os.remove(fp)
                            total += size
                        except:
                            pass

    print(GREEN + "\n✅ CLEAN SELESAI" + RESET)
    print(GREEN + f"💾 Dibersihkan: {total/1024/1024:.1f} MB" + RESET)

# ================= MODE 2 =================
def gps_stabilizer_pro():
    header("📍 GPS STABILIZER PRO")

    loading_text("🛰️ Mengunci GPS", 2)
    start = time.time()

    while True:
        acc = get_gps_accuracy()
        if acc:
            if acc <= 10:
                print(GREEN + f"✅ GPS FIX ±{acc:.1f} m" + RESET)
                print("📍 Lokasi stabil & siap narik")
                return
            else:
                print(YELLOW + f"⏳ Akurasi ±{acc:.1f} m" + RESET)
        else:
            print(RED + "❌ GPS belum terbaca" + RESET)

        if time.time() - start > 45:
            print(RED + "\n⚠️ GPS belum optimal" + RESET)
            print("👉 Geser ke area terbuka")
            return

        time.sleep(2)

# ================= MODE 3 & 4 =================
def focus_mode(label):
    header(f"🎯 FOCUS MODE {label}")

    host = "ec2.ap-southeast-1.amazonaws.com"
    pings = []

    for _ in range(10):
        out = run(f"ping -c 1 -W 1 {host}")
        m = re.search(r'time=([\d.]+)', out)
        if m:
            ms = float(m.group(1))
            pings.append(ms)
            print(GREEN + f"🛰️ {ms:.1f} ms" + RESET)
        else:
            print(RED + "🛰️ UNREACHABLE" + RESET)

    avg = sum(pings)/len(pings) if pings else None
    acc = get_gps_accuracy()

    print("\n📊 STATUS")
    print(f"• GPS     : ±{acc:.1f} m" if acc else "• GPS     : UNKNOWN")
    print(f"• Network : {avg:.1f} ms" if avg else "• Network : UNKNOWN")

# ================= MODE 5 =================
def aggressive_performance_mode():
    header("🔥 AGGRESSIVE PERFORMANCE MODE v2")

    heavy = [
        "com.facebook.katana",
        "com.instagram.android",
        "com.tiktok.android",
        "com.android.chrome",
        "com.spotify.music"
    ]

    for pkg in heavy:
        loading_text(f"⛔ Force stop {pkg}", 0.6)
        run(f"am force-stop {pkg}")
        time.sleep(0.4)
        run(f"am kill {pkg}")

    print(GREEN + "\n✅ MODE AGRESIF v2 AKTIF\n" + RESET)

# ================= MODE 7 =================
def smart_auto_mode():
    header("🤖 SMART AUTO MODE")

    loading_text("📍 Lock GPS", 2)
    acc = get_gps_accuracy()

    if not acc or acc > 25:
        print(RED + "❌ GPS belum ideal" + RESET)
        return

    print(GREEN + f"✅ GPS OK ±{acc:.1f} m" + RESET)

    loading_text("📡 Test network", 2)
    out = run("ping -c 3 -W 1 ec2.ap-southeast-1.amazonaws.com")
    if "time=" not in out:
        print(RED + "❌ Network lemah" + RESET)
        return

    print(GREEN + "✅ Network stabil" + RESET)
    aggressive_performance_mode()
    print(GREEN + "\n🎯 SIAP NARIK — AUTO MODE AKTIF\n" + RESET)

# ================= DOA =================
def doa_keselamatan():
    header("🤲 DOA KESELAMATAN")
    print(GREEN + "Ya Allah, lindungi kami di perjalanan dan lancarkan rezeki." + RESET)

# ================= MENU =================
def menu():
    print("""
[1] Aggressive Junk Cleaner++
[2] GPS Stabilizer PRO
[3] Focus Mode GOJEK
[4] Focus Mode GRAB
[5] Aggressive Performance Mode v2
[6] Doa Keselamatan
[7] Smart Auto Mode
""")
    return input("Pilih nomor: ").strip()

# ================= MAIN =================
if __name__ == "__main__":
    intro_banner()
    try:
        while True:
            c = menu()
            if c == "1": aggressive_junk_cleaner()
            elif c == "2": gps_stabilizer_pro()
            elif c == "3": focus_mode("GOJEK")
            elif c == "4": focus_mode("GRAB")
            elif c == "5": aggressive_performance_mode()
            elif c == "6": doa_keselamatan()
            elif c == "7": smart_auto_mode()
            else:
                print("❌ Pilihan tidak valid")

            print(YELLOW + "\n↩️ Kembali ke menu...\n" + RESET)
            time.sleep(1)

    except KeyboardInterrupt:
        print(GREEN + "\n👋 Keluar dari Smart Driver Tool" + RESET)
        print(GREEN + "Semoga orderan lancar & gacor 🤲\n" + RESET)