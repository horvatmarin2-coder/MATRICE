#napravio sam button koji spremi vrijednosti matrcie. Sprema je u m1. Moramo kasnije komentare za sve ukratko da znamo se snalazit i sve.



def ispis(polje_matrice): #ispis matrice onako fino lijepo po domaci kak treba
    for i in range(len(polje_matrice)):           
        for j in range(len(polje_matrice[i])):      
            print(polje_matrice[i][j], end=" ")
        print()  




import tkinter as tk

x = []
m1 = None

def napravi_matricu():
    global r, c, x, potvrdi, LABEL
    try:
        r = int(br_redovi.get())
        c = int(br_stupci.get())
    except:
        return print("Unesite ispravne brojeve za redove i stupce.")
    
    for widget in aplikacija.winfo_children():
        if widget != matrica_frame:
            widget.destroy()

    LABEL = tk.Label(matrica_frame, text="UNESI MATRICU:", bg="#aa90bb", font=("Arial", 20, "bold"))
    LABEL.grid(row=0, column=0, columnspan=c, pady=10)

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
        m1 = [[int(x[i][j].get()) for j in range(c)] for i in range(r)] #znam da glupo izgleda ali radi :)
    except:
        return print("Unesite ispravne cijele brojeve u matricu.")
    ispis(m1) # ovo samo stavio da se vidi da radi spremanje matrice, mozes obrisat to

    LABEL.destroy()
    potvrdi.destroy()

    odabir = tk.Frame(aplikacija, bg="#aa90bb")
    odabir.pack(pady=20)

    zbrajanje = tk.Button(odabir, text="ZBRAJANJE", font=("Arial", 12, "bold"), bg="#946aaf", cursor="hand2", relief="groove", bd=6)
    zbrajanje.pack(side=tk.LEFT, padx=10)

    oduzimanje = tk.Button(odabir, text="ODUZIMANJE", font=("Arial", 12, "bold"), bg="#946aaf", cursor="hand2", relief="groove", bd=6)
    oduzimanje.pack(side=tk.LEFT, padx=10)
    

aplikacija = tk.Tk()
aplikacija.title("MATRICE zadatak")
aplikacija.geometry("1500x700")
aplikacija.config(bg="#aa90bb")

matrica_frame = tk.Frame(aplikacija, bg="#aa90bb")
matrica_frame.pack(anchor="n", pady=10)

label = tk.Label(aplikacija, text="MATRICE", bg="#aa90bb", font=("Arial", 50, "bold"))
label.pack()

label_redovi = tk.Label(aplikacija, text="Broj redova:", bg="#aa90bb", font=("Arial", 20, "bold"))
label_redovi.pack(pady=10)
br_redovi = tk.Entry(aplikacija, bg="#b9a6c5", font=("Arial", 18), width=4, justify='center', bd=4)
br_redovi.pack(pady=10)

label_stupci = tk.Label(aplikacija, text="Broj stupaca:", bg="#aa90bb", font=("Arial", 20, "bold"))
label_stupci.pack(pady=10)
br_stupci = tk.Entry(aplikacija, bg="#b9a6c5", font=("Arial", 18), width=4, justify='center', bd=4)
br_stupci.pack(pady=10)

napravi = tk.Button(aplikacija, text="NAPRAVI", font=("Arial", 20, "bold"), bg="#946aaf", command=napravi_matricu, cursor="hand2", relief="groove", bd=6)
napravi.pack(pady=70)

aplikacija.mainloop()
