
import tkinter as tk

aplikacija = tk.Tk()
aplikacija.title("MATRICE zadatak")
aplikacija.geometry("1000x600")
aplikacija.configure(bg="#aa90bb")

label = tk.Label(aplikacija, text="MATRICE",bg="#aa90bb", font=("Arial", 34))
label.pack(pady=40)

aplikacija.mainloop()