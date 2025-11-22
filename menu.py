from tkinter import *
import subprocess

aplikacija = Tk()
aplikacija.title("Kalkulator matrica")
aplikacija.state('zoomed')
aplikacija.config(bg="#65ba9e")


def pokreni_racunanje():
    subprocess.Popen(["python", "matrice.py"])
    aplikacija.destroy()



naslov = Label(aplikacija, text="Kalkulator Matrica", font=("Comic Sans MS",70), bg="#65ba9e")
naslov.place(x=580, y=300)
    

Button(aplikacija, text="Racunanje sa Matricama", bg="#65ba9e", bd=7, relief="groove",
       font=("Comic Sans MS",35), pady=20, padx=20, command=pokreni_racunanje).place(x=680, y=800)


aplikacija.mainloop()
