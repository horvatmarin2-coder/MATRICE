#napravio sam button koji spremi vrijednosti matrcie. Sprema je u m1. Moramo kasnije komentare za sve ukratko da znamo se snalazit i sve.

import tkinter as tk

x = []
m1 = None

def napravi_matricu():
    global r, c, x
    try:
        r = int(b_redovi.get())
        c = int(b_stupci.get())
    except:
        return print("Unesite ispravne brojeve za redove i stupce.")
    
    for widget in aplikacija.winfo_children():
        if widget != matrica_frame:
            widget.destroy()

    label = tk.Label(matrica_frame, text="UNESI MATRICU:", bg="#aa90bb", font=("Arial", 20, "bold"))
    label.grid(row=0, column=0, columnspan=c, pady=10)

    for i in range(r):
        n = []
        for j in range(c):
            polje = tk.Entry(matrica_frame, width=3)
            polje.grid(row=i + 1, column=j, padx=5, pady=5)
            polje.config(bd=4, justify="center", font=("Arial", 20), bg="#b9a6c5")
            n.append(polje)
        x.append(n)

    potvrdi = tk.Button(matrica_frame, text="POTVRDI", font=("Arial", 20, "bold"), bg="#946aaf", cursor="hand2", relief="groove",command=potvrdi_matricu, bd=6)
    potvrdi.grid(row=r + 2, column=0, columnspan=c, pady=20)

def potvrdi_matricu():
    global m1
    try:
        m1 = [[int(x[i][j].get()) for j in range(c)] for i in range(r)]
    except:
        return print("Unesite ispravne cijele brojeve u matricu.")
    print(m1)
    

aplikacija = tk.Tk()
aplikacija.title("MATRICE zadatak")
aplikacija.geometry("1500x700")
aplikacija.config(bg="#aa90bb")

matrica_frame = tk.Frame(aplikacija, bg="#aa90bb")
matrica_frame.pack(anchor="n", pady=10)

label = tk.Label(aplikacija, text="MATRICE", bg="#aa90bb", font=("Arial", 50, "bold"))
label.pack(pady=40)

label_redovi = tk.Label(aplikacija, text="Broj redova:", bg="#aa90bb", font=("Arial", 20, "bold"))
label_redovi.pack()
b_redovi = tk.Entry(aplikacija, bg="#b9a6c5", font=("Arial", 18), width=4, justify='center', bd=4)
b_redovi.pack(pady=10)

label_stupci = tk.Label(aplikacija, text="Broj stupaca:", bg="#aa90bb", font=("Arial", 20, "bold"))
label_stupci.pack()
b_stupci = tk.Entry(aplikacija, bg="#b9a6c5", font=("Arial", 18), width=4, justify='center', bd=4)
b_stupci.pack(pady=10)

napravi = tk.Button(aplikacija, text="NAPRAVI", font=("Arial", 20, "bold"), bg="#946aaf", command=napravi_matricu, cursor="hand2", relief="groove", bd=6)
napravi.pack(pady=110)

aplikacija.mainloop()
