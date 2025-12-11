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

    Label(frame_q, text="Unesi broj stupaca druge matrice:", bg="#aa90bb", font=("Arial", 14)).pack(pady=5)

    q_entry = Entry(frame_q, width=5, font=("Arial", 14), justify="center", bd=4, bg="#b9a6c5")
    q_entry.pack(pady=5)

    def kreiraj_drugu_matricu():
        global x2, frame_za_2_matricu, selektor, q,potvrdi2
        try:
            q = int(q_entry.get())
            if q < 1 or q > 6:
                raise ValueError
        except:
            error = Label(aplikacija, text="BROJ STUPACA DRUGE MATRICE MORA BITI [1-5]!",
                      bg="#aa90bb", fg="#E40F0F", font=("Arial", 20, "bold underline"))
            error.pack(pady=400)
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
    Button(frame_q, 
       text="Potvrdi", 
       font=("Arial", 20, "bold"), 
       bg="#946aaf", 
       cursor="hand2", 
       relief="groove", 
       bd=6,
       command=kreiraj_drugu_matricu
      ).pack(pady=10)


def transponirana():
    global m1,selektor,trans
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
    selektor=4
    svojstva_matrice()

def potvrdi_2_matricu():
    global m1, x2, selektor, r, c, q,rez,m2

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
        error.pack(pady=400)
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
    global m1,x2,rez,matrice_mnozenje,svojstva_dolje
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
    
    if selektor !=4:
        matrice = [(m1, svojstva_m1_frame), (m2, svojstva_m2_frame), (rez, svojstva_rjesenje_frame)]

    else:
        matrice = [(trans,svojstva_m1_frame)]
        svojstva_m2_frame.destroy()
        svojstva_rjesenje_frame.destroy()
        

    for matrica, frame in matrice:
        tekst = "SIMETRIČNA: ✅" if simetricna(matrica) else "SIMETRIČNA: ❌"
        Label(frame, text=tekst, bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)

    for matrica, frame in matrice:
        tekst = "ANTISIMETRIČNA: ✅" if antisimetricna(matrica) else "ANTISIMETRIČNA: ❌"
        Label(frame, text=tekst, bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)

    for matrica, frame in matrice:
        tekst = "ORTOGONALNA: ✅" if ortogonalna(matrica) else "ORTOGONALNA: ❌"
        Label(frame, text=tekst, bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)

    if selektor==3:
    
        matrice_mnozenje = [(rez, svojstva_rjesenje_frame)]    

        for matrica, frame in matrice_mnozenje:
            tekst = "KOMUTATIVNO MNOZENJE: ✅" if komutativnost(m1,m2) else "KOMUTATIVNO MNOZENJE: ❌"
            Label(frame, text=tekst, bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)
    
    for matrica, frame in matrice:
        tekst = "GORNJE TROKUTASTA: ✅" if gornje_trokutasta(matrica) else "GORNJE TROKUTASTA: ❌"
        Label(frame, text=tekst, bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)
    
    for matrica, frame in matrice:
        tekst = "DONJE TROKUTASTA: ✅" if donje_trokutasta(matrica) else "DONJE TROKUTASTA: ❌"
        Label(frame, text=tekst, bg="#d7c5e8", font=("Arial", 16, "bold")).pack(pady=10)

def simetricna(m):
    # provjera jel matrica kvvadratna
    if len(m) != len(m[0]):
        return False


    # provjeri simetričnost
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != m[j][i]:
                return False

    return True

def antisimetricna(m):
    if len(m) != len(m[0]):
        return False

    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != -m[j][i]:
                return False

    return True

def ortogonalna(m):
    # Mora biti kvadratna
    if len(m) != len(m[0]):
        return False
    
    # Izračun transponirane
    T = [[m[j][i] for j in range(len(m))] for i in range(len(m))]
    
    # A * A^T
    n = len(m)
    rezultat = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rezultat[i][j] += m[i][k] * T[k][j]

    # Provjeri je li A * A^T == jedinicna
    for i in range(n):
        for j in range(n):
            if i == j:
                if formatiraj_broj(rezultat[i][j]) != "1":
                    return False
            else:
                if formatiraj_broj(rezultat[i][j]) != "0":
                    return False

    return True

def komutativnost(m1, m2):
    def mnozenje_matrica(A, B):
        if len(A[0]) != len(B):
            return None
        rezultat = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    rezultat[i][j] += A[i][k] * B[k][j]
        return rezultat

    AB = mnozenje_matrica(m1, m2)
    BA = mnozenje_matrica(m2, m1)

    if AB is None or BA is None:

        return False

    if AB == BA:
        return True
    else:
        return False

def gornje_trokutasta(m):
    if len(m) != len(m[0]):
        return False
    
    n = len(m)
    for i in range(1, n):          
        for j in range(i):        
            if m[i][j] != 0:
                return False
    return True

def donje_trokutasta(m):

    if len(m) != len(m[0]):
        return False
    
    n = len(m)

    for i in range(n):
        for j in range(i+1, n):  
            if m[i][j] != 0:
                return False
    return True





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