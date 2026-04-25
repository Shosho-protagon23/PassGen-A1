# Secure Password Generator

> Aplikasi desktop GUI berbasis Python untuk membuat password acak yang kuat — dengan tampilan bergaya terminal simple.

---

## Fitur

- Generate password acak dengan panjang 6 hingga 32 karakter.
- Pilihan kombinasi karakter: huruf kecil (default), huruf besar, angka, dan simbol.
- Salin password ke clipboard dengan satu klik.
- Antarmuka gelap (dark mode) bergaya terminal.

---

## Persyaratan

- Python 3.x
- `tkinter` (bawaan Python, tidak perlu instalasi tambahan)

---

## Cara Menjalankan

```bash
python pass_gen_genA1.py
```

---

## Cara Penggunaan

1. **Atur panjang password** menggunakan Spinbox (min 6, maks 32)
2. **Centang opsi karakter** yang diinginkan:
   - Huruf Besar (A-Z)
   - Angka (0-9)
   - Simbol (!@#$)
3. Klik **GENERATE PASSWORD**
4. Klik **Copy to Clipboard** untuk menyalin hasilnya

> Huruf kecil (a-z) selalu disertakan secara default.

---

## Struktur Kode

```
pass_gen_genA1.py
│
└── class PasswordGeneratorApp
    ├── __init__()           # Inisialisasi UI dan variabel
    ├── generate_password()  # Logika generate password acak
    └── copy_to_clipboard()  # Salin password ke clipboard
```

---

*Built by Ech0_f0xtr0t · Shosho-protagon23*