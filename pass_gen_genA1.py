import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("400x450")
        self.root.configure(bg="#1e1e1e") # Dark background
        self.root.resizable(False, False)

        # --- VARIABLES ---
        self.length_var = tk.IntVar(value=12)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        # --- UI COMPONENTS ---
        
        # 1. Header
        title_label = tk.Label(root, text="PASSWORD GENERATOR", font=("Consolas", 18, "bold"), 
                               bg="#1e1e1e", fg="#00ff00") # Green text (Hacker vibes)
        title_label.pack(pady=20)

        # 2. Options Frame
        options_frame = tk.Frame(root, bg="#1e1e1e")
        options_frame.pack(pady=10)

        # Length Input
        tk.Label(options_frame, text="Panjang Karakter:", font=("Arial", 10), 
                 bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="w", padx=10)
        
        # Spinbox untuk memilih panjang password (min 6, max 32)
        self.spin_length = tk.Spinbox(options_frame, from_=6, to=32, textvariable=self.length_var, 
                                      width=5, font=("Arial", 10))
        self.spin_length.grid(row=0, column=1, pady=5)

        # Checkboxes
        tk.Checkbutton(options_frame, text="Huruf Besar (A-Z)", variable=self.use_upper, 
                       bg="#1e1e1e", fg="white", selectcolor="#333", activebackground="#1e1e1e", activeforeground="white").grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
        
        tk.Checkbutton(options_frame, text="Angka (0-9)", variable=self.use_numbers, 
                       bg="#1e1e1e", fg="white", selectcolor="#333", activebackground="#1e1e1e", activeforeground="white").grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
        
        tk.Checkbutton(options_frame, text="Simbol (!@#$)", variable=self.use_symbols, 
                       bg="#1e1e1e", fg="white", selectcolor="#333", activebackground="#1e1e1e", activeforeground="white").grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

        # 3. Generate Button
        generate_btn = tk.Button(root, text="GENERATE PASSWORD", font=("Arial", 11, "bold"), 
                                 bg="#007acc", fg="white", activebackground="#005f9e", 
                                 command=self.generate_password)
        generate_btn.pack(pady=20, ipadx=10)

        # 4. Result Entry (Output)
        self.result_entry = tk.Entry(root, font=("Consolas", 14), justify="center", bd=0, bg="#2d2d2d", fg="#00ff00")
        self.result_entry.pack(pady=10, ipady=5, ipadx=5, padx=20, fill="x")

        # 5. Copy Button
        copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 9), 
                             bg="#444", fg="white", command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)

    def generate_password(self):
        # 1. Build Character Set
        chars = string.ascii_lowercase # Selalu include huruf kecil
        
        if self.use_upper.get():
            chars += string.ascii_uppercase
        if self.use_numbers.get():
            chars += string.digits
        if self.use_symbols.get():
            chars += string.punctuation

        # 2. Validasi (Jika user uncheck semua kecuali lowercase yg default)
        # (Dalam kode ini lowercase sudah default, jadi chars tidak mungkin kosong)
        
        length = self.length_var.get()
        
        # 3. Random Sample & Insert
        # Menggunakan random.choice di dalam loop agar karakter bisa berulang (repetition allowed)
        password = "".join(random.choice(chars) for _ in range(length))

        # Update GUI
        self.result_entry.delete(0, tk.END) # Hapus isi lama
        self.result_entry.insert(0, password) # Masukkan password baru

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update() # Menjaga clipboard tetap tersimpan setelah aplikasi ditutup (opsional)
            messagebox.showinfo("Success", "Password berhasil disalin!")
        else:
            messagebox.showwarning("Warning", "Belum ada password yang dibuat.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()