def zbroj():
    return 3
import tkinter as tk

aplikacija = tk.Tk()
aplikacija.title("Calculomatrix")
aplikacija.geometry("1920x1080")



label = tk.Label(aplikacija,text="Matrica")
label.pack()

button = tk.Button(aplikacija, text="Izračunaj",width=20, height=2)
button.place(x=100, y=100)

aplikacija.mainloop()

print(zbroj())