from tkinter import *

aplikacija = Tk()
aplikacija.title("Racunanje matrica")
aplikacija.geometry("1920x1080")
aplikacija.config(bg="#aa90bb")
aplikacija.state('zoomed')

matrica_frame = Frame(aplikacija, bg="#aa90bb")
matrica_frame.pack(anchor="n", pady=10)

def formatiraj_broj(b, dec=6):  # dec = broj decimalnih mjesta za zaokruživanje
    b = round(b, dec)  # prvo zaokruži
    if b == int(b):
        return str(int(b))
    else:
        return str(b)





x = []
x2 = []
m1 = None
LABEL = None
potvrdi = None
selektor=0

def napravi_matricu():
    global r, c, x, potvrdi, LABEL
    try:
        r = int(br_redovi.get())
        c = int(br_stupci.get())
        if r <= 0 or c <= 0 or r > 5 or c>5:
            raise ValueError
    # Prikaz errora ako korisnik ne unese broj ili unese <=0 ili >10
    except:
        error = Label(aplikacija,text="REDOVI I STUPCI MORAJU BITI [1-5]!!!",
                      bg="#aa90bb", fg="#E40F0F", font=("Arial", 20, "bold underline"))
        error.pack(pady=200)
        aplikacija.after(2000, error.destroy)
        return
    
    for widget in aplikacija.winfo_children():
        if widget != matrica_frame:
            widget.destroy()

    x.clear()

    LABEL = Label(matrica_frame, text="UNESI MATRICU:", bg="#aa90bb", font=("Arial", 20, "bold"))
    LABEL.grid(row=0, column=0, columnspan=c, pady=10)

    for i in range(r):
        n = []
        for j in range(c):
            polje = Entry(matrica_frame, width=5)
            polje.grid(row=i+1, column=j, padx=5, pady=5)
            polje.config(bd=4, justify="center", font=("Arial", 20), bg="#b9a6c5")
            n.append(polje)
        x.append(n)

    potvrdi = Button(matrica_frame, text="POTVRDI", font=("Arial", 20, "bold"),
                     bg="#946aaf", cursor="hand2", relief="groove",
                     command=potvrdi_1_matricu, bd=6)
    potvrdi.grid(row=r+2, column=0, columnspan=c, pady=20)

def potvrdi_1_matricu():
    global m1, LABEL, potvrdi, odabir
    try:
        # Omogućava decimalne brojeve
        m1 = [[float(x[i][j].get()) for j in range(c)] for i in range(r)]
    except:
        # Prikaz errora ako korisnik unese neispravnu vrijednost u matricu
        error = Label(aplikacija,text="UNESITE ISPRAVNE BROJEVE U MATRICU!",
                      bg="#aa90bb", fg="#E40F0F", font=("Arial", 20, "bold underline"))
        error.pack(pady=200)
        aplikacija.after(2000, error.destroy)
        return

    if LABEL: LABEL.destroy()
    if potvrdi: potvrdi.destroy()

    # Očisti stare odabir frame-ove, ali ne dira matrica_frame ni labele

    odabir = Frame(aplikacija, bg="#aa90bb")
    odabir.pack(pady=20)

    Button(odabir, text="ZBRAJANJE", font=("Arial", 14, "bold"),
           bg="#946aaf", cursor="hand2", relief="groove", bd=6,
           command=zbrajanje_m).pack(side=LEFT, padx=10)

    Button(odabir, text="ODUZIMANJE", font=("Arial", 14, "bold"),
           bg="#946aaf", cursor="hand2", relief="groove", bd=6,
           command=oduzimanje_m).pack(side=LEFT, padx=10)

    Button(odabir, text="MNOZENJE", font=("Arial", 14, "bold"),
           bg="#946aaf", cursor="hand2", relief="groove", bd=6,
           command=mnozenje_m).pack(side=LEFT, padx=10)

    Button(odabir, text="TRANSLACIJA", font=("Arial", 14, "bold"),
           bg="#946aaf", cursor="hand2", relief="groove", bd=6,
           command=transponirana).pack(side=LEFT, padx=10)

def zbrajanje_m():
    global gore_ljevo, frame_za_matricu, frame_za_2_matricu, x2, znak_plus, potvrdi2,selektor
    
    matrica_frame.pack_forget()

    odabir.destroy()

    #stvara frame u kojem ce biti prva matrica neki znak druga matrica i rjesenje (stavlja ga gore desno)
    gore_ljevo = Frame(aplikacija, bg="#aa90bb")
    gore_ljevo.pack(anchor="nw", pady=40)

    #radimo frame za prvu matricu u frame (gore_ljevo)
    frame_za_matricu = Frame(gore_ljevo, bg="#aa90bb")
    frame_za_matricu.pack(side=LEFT, padx=20)

    #ispisujemo prvu matricu u frame u obliku labela koji se ne moze mijenjat
    for i in range(r):
        for j in range(c):
            Label(frame_za_matricu, text=formatiraj_broj(m1[i][j]), width=5, font=("Arial", 20),
                  bg="#b9a6c5", bd=4).grid(row=i, column=j, padx=5, pady=5)

    #stvaramo znak plus
    znak_plus = Label(gore_ljevo, text="+", font=("Arial", 40, "bold"), bg="#aa90bb")
    znak_plus.pack(side=LEFT, padx=20)

    #stvaramo frame za 2 matricu u farme (gore_ljevo)
    frame_za_2_matricu = Frame(gore_ljevo, bg="#aa90bb")
    frame_za_2_matricu.pack(side=LEFT, padx=20)

    #ovdje upisujemo 2 matricu
    x2.clear()
    for i in range(r):
        red = []
        for j in range(c):
            e = Entry(frame_za_2_matricu, width=5)
            e.grid(row=i, column=j, padx=5, pady=5)
            e.config(bd=4, justify="center", font=("Arial", 20), bg="#b9a6c5")
            red.append(e)
        x2.append(red)
    selektor=1

    potvrdi2 = Button(gore_ljevo, text="POTVRDI", font=("Arial", 20, "bold"),
                      
                      bg="#946aaf", cursor="hand2", relief="groove", bd=6,
                      command=potvrdi_2_matricu)
    potvrdi2.pack(side=LEFT, padx=20)

def oduzimanje_m():
    global gore_ljevo, frame_za_matricu, frame_za_2_matricu, x2, znak_plus, potvrdi2,selektor
    
    matrica_frame.pack_forget()

    odabir.destroy()

    #stvara frame u kojem ce biti prva matrica neki znak druga matrica i rjesenje (stavlja ga gore desno)
    gore_ljevo = Frame(aplikacija, bg="#aa90bb")
    gore_ljevo.pack(anchor="nw", pady=40)

    #radimo frame za prvu matricu u frame (gore_ljevo)
    frame_za_matricu = Frame(gore_ljevo, bg="#aa90bb")
    frame_za_matricu.pack(side=LEFT, padx=20)

    #ispisujemo prvu matricu u frame u obliku labela koji se ne moze mijenjat
    for i in range(r):
        for j in range(c):
            Label(frame_za_matricu, text=formatiraj_broj(m1[i][j]), width=5, font=("Arial", 20),
                  bg="#b9a6c5", bd=4).grid(row=i, column=j, padx=5, pady=5)

    #stvaramo znak plus
    znak_plus = Label(gore_ljevo, text="-", font=("Arial", 40, "bold"), bg="#aa90bb")
    znak_plus.pack(side=LEFT, padx=20)

    #stvaramo frame za 2 matricu u farme (gore_ljevo)
    frame_za_2_matricu = Frame(gore_ljevo, bg="#aa90bb")
    frame_za_2_matricu.pack(side=LEFT, padx=20)

    #ovdje upisujemo 2 matricu
    x2.clear()
    for i in range(r):
        red = []
        for j in range(c):
            e = Entry(frame_za_2_matricu, width=5)
            e.grid(row=i, column=j, padx=5, pady=5)
            e.config(bd=4, justify="center", font=("Arial", 20), bg="#b9a6c5")
            red.append(e)
        x2.append(red)
    selektor=2

    potvrdi2 = Button(gore_ljevo, text="POTVRDI", font=("Arial", 20, "bold"),
                      bg="#946aaf", cursor="hand2", relief="groove", bd=6,
                      command=potvrdi_2_matricu)
    potvrdi2.pack(side=LEFT, padx=20)

def mnozenje_m():
    global gore_ljevo, frame_za_matricu, frame_za_2_matricu, x2, znak_plus, potvrdi2,selektor,q,q_entry
    
    matrica_frame.pack_forget()

    odabir.destroy()

    #stvara frame u kojem ce biti prva matrica neki znak druga matrica i rjesenje (stavlja ga gore desno)
    gore_ljevo = Frame(aplikacija, bg="#aa90bb")
    gore_ljevo.pack(anchor="nw", pady=40)

    #radimo frame za prvu matricu u frame (gore_ljevo)
    frame_za_matricu = Frame(gore_ljevo, bg="#aa90bb")
    frame_za_matricu.pack(side=LEFT, padx=20)

    #ispisujemo prvu matricu u frame u obliku labela koji se ne moze mijenjat
    for i in range(r):
        for j in range(c):
            Label(frame_za_matricu, text=formatiraj_broj(m1[i][j]), width=5, font=("Arial", 20),
                  bg="#b9a6c5", bd=4).grid(row=i, column=j, padx=5, pady=5)

    #stvaramo znak plus
    znak_puta = Label(gore_ljevo, text="X", font=("Arial", 40, "bold"), bg="#aa90bb")
    znak_puta.pack(side=LEFT, padx=20)

    frame_q = Frame(gore_ljevo, bg="#aa90bb")
    frame_q.pack(side=LEFT, padx=20)

    Label(frame_q, text="Unesi broj stupaca druge matrice (q):", bg="#aa90bb", font=("Arial", 14)).pack(pady=5)

    q_entry = Entry(frame_q, width=5, font=("Arial", 14), justify="center", bd=4, bg="#b9a6c5")
    q_entry.pack(pady=5)

    def kreiraj_drugu_matricu():
        global x2, frame_za_2_matricu, selektor, q,potvrdi2
        try:
            q = int(q_entry.get())
            if q < 1 or q > 6:
                raise ValueError
        except:
            error = Label(aplikacija, text="BROJ STUPACA DRUGE MATRICE MORA BITI [1-6]!",
                      bg="#aa90bb", fg="#E40F0F", font=("Arial", 20, "bold underline"))
            error.pack(pady=200)
            aplikacija.after(2000, error.destroy)
            return
        
        frame_q.destroy()
        q_entry.destroy()
        #stvaramo frame za 2 matricu u farme (gore_ljevo)
        frame_za_2_matricu = Frame(gore_ljevo, bg="#aa90bb")
        frame_za_2_matricu.pack(side=LEFT, padx=20)

        #ovdje upisujemo 2 matricu
        x2.clear()
        for i in range(c):
            red = []
            for j in range(q):
                e = Entry(frame_za_2_matricu, width=5)
                e.grid(row=i, column=j, padx=5, pady=5)
                e.config(bd=4, justify="center", font=("Arial", 20), bg="#b9a6c5")
                red.append(e)
            x2.append(red)
        selektor=3

        potvrdi2 = Button(gore_ljevo, text="POTVRDI", font=("Arial", 20, "bold"),
                        bg="#946aaf", cursor="hand2", relief="groove", bd=6,
                        command=potvrdi_2_matricu)
        potvrdi2.pack(side=LEFT, padx=20)
    Button(frame_q, text="Potvrdi q", command=kreiraj_drugu_matricu).pack(pady=10)

def transponirana():
    global m1,selektor
    redci=len(m1)
    stupci=len(m1[0])
    trans = [[m1[j][i] for j in range(redci)] for i in range(stupci)]
    matrica_frame.pack_forget()

    odabir.destroy()
    gore_ljevo = Frame(aplikacija, bg="#aa90bb")
    gore_ljevo.pack(anchor="nw", pady=40)
    
    #radimo frame za prvu matricu u frame (gore_ljevo)
    frame_za_matricu = Frame(gore_ljevo, bg="#aa90bb")
    frame_za_matricu.pack(side=LEFT, padx=20)

    for i in range(stupci):
        for j in range(redci):
            Label(frame_za_matricu, text=formatiraj_broj(trans[i][j]), width=5,
                  font=("Arial", 20), bg="#b9a6c5", bd=4).grid(row=i, column=j, padx=5, pady=5)

def potvrdi_2_matricu():
    global m1, x2, selektor, r, c, q,rez

    # Dohvati vrijednosti iz druge matrice
    try:
        if selektor == 3:
            # Množenje: dimenzije c x q
            m2 = [[float(x2[i][j].get()) for j in range(q)] for i in range(c)]
        else:
            # Zbrajanje/oduzimanje: dimenzije r x c
            m2 = [[float(x2[i][j].get()) for j in range(c)] for i in range(r)]
    except:
        error = Label(aplikacija, text="UNESITE ISPRAVNE BROJEVE!",
                      bg="#aa90bb", fg="#E40F0F", font=("Arial", 20, "bold underline"))
        error.pack(pady=200)
        aplikacija.after(2000, error.destroy)
        return

    # Uništi Entry widgete u frame_za_2_matricu
    for widget in frame_za_2_matricu.winfo_children():
        widget.destroy()

    # Pretvori drugu matricu u Label
    if selektor == 3:
        for i in range(c):
            for j in range(q):
                Label(frame_za_2_matricu, text=formatiraj_broj(m2[i][j]), width=5, font=("Arial", 20),
                      bg="#b9a6c5", bd=4).grid(row=i, column=j, padx=5, pady=5)
    else:
        for i in range(r):
            for j in range(c):
                Label(frame_za_2_matricu, text=formatiraj_broj(m2[i][j]), width=5, font=("Arial", 20),
                      bg="#b9a6c5", bd=4).grid(row=i, column=j, padx=5, pady=5)

    potvrdi2.destroy()

    # Dodaj znak "=" i frame za rezultat
    znak_jednako = Label(gore_ljevo, text="=", font=("Arial", 40, "bold"), bg="#aa90bb")
    znak_jednako.pack(side=LEFT, padx=20)

    rez_frame = Frame(gore_ljevo, bg="#aa90bb")
    rez_frame.pack(side=LEFT, padx=20)

    # Izračunaj rezultat
    if selektor == 1:  # Zbrajanje
        rez = [[m1[i][j] + m2[i][j] for j in range(c)] for i in range(r)]
    elif selektor == 2:  # Oduzimanje
        rez = [[m1[i][j] - m2[i][j] for j in range(c)] for i in range(r)]
    elif selektor == 3:  # Množenje
        rez = [[0 for j in range(q)] for i in range(r)]
        for i in range(r):
            for j in range(q):
                for k in range(c):
                    rez[i][j] += m1[i][k] * m2[k][j]

    # Ispiši rezultat u Label
    for i in range(len(rez)):
        for j in range(len(rez[0])):
            Label(rez_frame, text=formatiraj_broj(rez[i][j]), width=5, font=("Arial", 20),
                  bg="#b9a6c5", bd=4).grid(row=i, column=j, padx=5, pady=5)
    svojstva_matrice()

def svojstva_matrice():
    global m1,x2,rez
    svojstva_dolje = Frame(aplikacija, bg="#aa90bb")
    svojstva_dolje.pack(side=TOP, fill="x", pady=20)

    svojstva_m1_frame = Frame(svojstva_dolje, bg="#d7c5e8", bd=4, relief="groove")
    svojstva_m1_frame.pack(side=LEFT, expand=True, fill="both", padx=10)

    svojstva_m2_frame = Frame(svojstva_dolje, bg="#d7c5e8", bd=4, relief="groove")
    svojstva_m2_frame.pack(side=LEFT, expand=True, fill="both", padx=10)

    svojstva_rjesenje_frame = Frame(svojstva_dolje, bg="#d7c5e8", bd=4, relief="groove")
    svojstva_rjesenje_frame.pack(side=LEFT, expand=True, fill="both", padx=10)

    Label(svojstva_m1_frame, text="Svojstva 1. matrice:", 
      bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)
    
    Label(svojstva_m2_frame, text="Svojstva 2. matrice:", 
      bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)
    
    Label(svojstva_rjesenje_frame, text="Svojstva rješenja:", 
      bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)





# Glavne labele i inputi
label = Label(aplikacija, text="MATRICE", bg="#aa90bb", font=("Arial", 50, "bold"))
label.pack()

label_redovi = Label(aplikacija, text="Broj redova:", bg="#aa90bb", font=("Arial", 20, "bold"))
label_redovi.pack(pady=10)
br_redovi = Entry(aplikacija, bg="#b9a6c5", font=("Arial", 18), width=4, justify='center', bd=4)
br_redovi.pack(pady=10)

label_stupci = Label(aplikacija, text="Broj stupaca:", bg="#aa90bb", font=("Arial", 20, "bold"))
label_stupci.pack(pady=10)
br_stupci = Entry(aplikacija, bg="#b9a6c5", font=("Arial", 18), width=4, justify='center', bd=4)
br_stupci.pack(pady=10)

napravi = Button(aplikacija, text="NAPRAVI", font=("Arial", 20, "bold"),
                 bg="#946aaf", command=napravi_matricu, cursor="hand2", relief="groove", bd=6)
napravi.pack(pady=70)

aplikacija.mainloop()