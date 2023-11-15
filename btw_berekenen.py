import tkinter as tk

#dit is een test

# Functie om de BTW te berekenen
def bereken_btw():
    bedrag = float(entry_bedrag.get())
    btw_tarief = float(entry_btw_tarief.get())
    
    btw = (btw_tarief / 100) * bedrag
    totaal_bedrag = bedrag + btw

    label_resultaat.config(text=f'BTW: {btw:.2f} EUR\nTotaal bedrag: {totaal_bedrag:.2f} EUR')

# Maak het hoofdvenster
root = tk.Tk()
root.title("BTW Calculator")
root.geometry('250x175')

# Voeg invoervelden toe
label_bedrag = tk.Label(root, text="Bedrag in euro's:")
label_bedrag.pack()
entry_bedrag = tk.Entry(root)
entry_bedrag.pack()

label_btw_tarief = tk.Label(root, text="BTW percentage (9% of 21%):")
label_btw_tarief.pack()
entry_btw_tarief = tk.Entry(root)
entry_btw_tarief.pack()

# Voeg een knop toe om de BTW te berekenen
bereken_knop = tk.Button(root, text="Bereken BTW", command=bereken_btw)
bereken_knop.pack()

# Voeg een label toe om het resultaat weer te geven
label_resultaat = tk.Label(root, text="")
label_resultaat.pack()

# Start de GUI-loop
root.mainloop()