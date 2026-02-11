# 🚀 SMART DRIVER TOOL
**All-in-One Optimizer for Android Driver (OJOL Friendly)**  
🧠 GPS Stabilizer • 🧹 Aggressive Junk Cleaner • 🎯 Focus Mode  
✨ Crafted with ❤️ by **D Z Y Q I**

---

## 📌 Tentang Project
**Smart Driver Tool** adalah script Python berbasis **Termux** yang dirancang khusus untuk:
- Driver **Gojek / Grab**
- HP **RAM kecil (2–4 GB)**
- Android **tanpa root**
- Aman, ringan, dan realistis

Tool ini **bukan cheat & bukan fake GPS**.  
Fokus ke **optimasi sistem yang benar-benar bisa dilakukan** di Android non-root.

---

## ✨ Fitur Utama

### 🧹 1. Aggressive Safe Junk Cleaner
- Auto-detect cache aplikasi (tanpa hardcode)
- Hapus:
  - DCIM/.thumbnails
  - Android/data/*/cache
  - Android/media/*/cache
  - File `.tmp`, `.log`, `.bak`
- Menampilkan **nama aplikasi yang dibersihkan**
- Menghitung **total MB yang dibersihkan**
- Aman untuk akun & data

---

### 📍 2. GPS Stabilizer PRO
- Mengambil data GPS asli via **Termux:API**
- Menunggu GPS hingga **akurasi < 10 meter**
- Deteksi kondisi:
  - GPS belum fix
  - Area tertutup / cuaca buruk
- Rekomendasi geser lokasi agar GPS cepat lock

---

### 🎯 3. Focus Mode (GOJEK & GRAB)
- Ping server stabil (AWS SEA)
- 20x ping dengan animasi
- Hitung skor **SIAP NARIK**
- Status jaringan & GPS
- Animasi “mencari orderan terdekat…”

---

### 🔥 4. Aggressive Performance Mode
- Force-stop aplikasi berat (FB, IG, TikTok, dll)
- Membantu RAM lebih lega
- Cocok HP RAM 3 GB
- Aman & non-root

---

### 🤲 5. Doa Keselamatan
Doa lengkap:
- Bahasa Arab
- Latin (bold)
- Arti bahasa Indonesia  
Untuk keselamatan & kelancaran narik.

---

## ⚠️ Catatan Keamanan
- ❌ Tidak mengubah sistem
- ❌ Tidak fake GPS
- ❌ Tidak inject aplikasi
- ✅ 100% non-root
- ✅ Aman untuk akun ojol

---

## 🛠️ Cara Install (Lengkap dari Nol)

### 1️⃣ Install Termux & Termux:API
> **WAJIB dari F-Droid, bukan Play Store**

- https://f-droid.org
- Install:
  - **Termux**
  - **Termux:API**

---

### 2️⃣ Setting Permission (PENTING)
**Termux**
- Storage → Izinkan
- Baterai → Jangan dioptimalkan

**Termux:API**
- Lokasi → Izinkan
- Lokasi Presisi → Aktif

---

### 3️⃣ Update & Install Dependency
Buka Termux, lalu jalankan:
```bash
pkg update && pkg upgrade -y
pkg install python git termux-api -y
termux-setup-storage
