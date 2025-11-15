import tkinter as tk

def napravi_matricu():
    # procitaj brojeve
    try:
        r = int(b_redovi.get())
        c = int(b_stupci.get())
    except:
        return

    # obrisi sve iz prozora
    for widget in aplikacija.winfo_children():
        widget.destroy()

    # napravi matricu
    for i in range(r):
        for j in range(c):
            polje = tk.Entry(aplikacija, width=5)
            polje.grid(row=i, column=j, padx=5, pady=5)

aplikacija = tk.Tk()
aplikacija.title("MATRICE zadatak")
aplikacija.geometry("1000x500")
aplikacija.config(bg="#aa90bb")

label = tk.Label(aplikacija, text="MATRICE",bg="#aa90bb" ,font=("Minecraftia", 50))
label.pack(pady=20)

label_redovi = tk.Label(aplikacija, text="Broj redova:",bg="#aa90bb" ,font=("Arial",20))
label_redovi.pack()
b_redovi = tk.Entry(aplikacija,bg="#aa90bb" ,font=("Arial", 18), width=4)
b_redovi.pack()

label_stupci = tk.Label(aplikacija,bg="#aa90bb" ,text="Broj stupaca:", font=("Arial", 20))
label_stupci.pack()
b_stupci = tk.Entry(aplikacija,bg="#aa90bb" ,font=("Arial", 18), width=4)
b_stupci.pack()

gumb = tk.Button(aplikacija, text="Potvrdi", font=("Arial", 20), command=napravi_matricu)
gumb.pack(pady=80)

aplikacija.mainloop()
