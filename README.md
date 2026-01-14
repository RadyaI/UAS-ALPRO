# UAS Algoritma Pemrograman - Kelas F

## 👥 Anggota Kelompok

| Nama Lengkap | NIM |
| :--- | :--- |
| **Nur Aini** | 202410370110381 |
| **Muhammad Radya Iftikhar** | 202410370110370 |

> Live Preview -> https://uas-alpro.streamlit.app/

> Jika halaman menunjukkan "This app has gone to sleep due to inactivity. Would you like to wake it back up?"
> Tekan tombol "Yes, get this app back up!"

## 📚 Deskripsi Proyek

Aplikasi ini dirancang untuk memvisualisasikan dua studi kasus algoritma secara interaktif, sehingga memudahkan pengguna dalam memahami konsep struktur data. Algoritma yang diimplementasikan adalah:

### 1. Huffman Coding (Kompresi Data)
Implementasi algoritma *greedy* untuk kompresi data *lossless*. Fitur mencakup:
* Pohon Huffman berdasarkan frekuensi karakter input.
* Visualisasi pohon biner Huffman.
* Perhitungan efisiensi kompresi (perbandingan bit asli vs. bit hasil kompresi).
* Tabel kode biner untuk setiap karakter.

### 2. Binary Search Tree (BST) & Traversal
Implementasi struktur data pohon biner pencarian. Fitur mencakup:
* Pembentukan BST secara dinamis berdasarkan input angka dari pengguna.
* Visualisasi struktur pohon menggunakan *Graphviz*.
* Simulasi penelusuran pohon (*Tree Traversal*) dengan metode:
    * **PreOrder** (Root -> Left -> Right)
    * **InOrder** (Left -> Root -> Right)
    * **PostOrder** (Left -> Right -> Root)

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.x
* **Framework Web:** Streamlit
* **Visualisasi Graf:** Graphviz
* **Struktur Data:** Heap Queue (untuk Huffman), Node Class (untuk Tree)