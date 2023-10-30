import tkinter as tk
from math import pi

root= tk.Tk()
root.geometry("500x400")
root.title("Homescreen")


def home_page():
    home_frame=tk.Frame(main_frame)
    
    lb=tk.Label(home_frame, text="homepage", font=("bold",30))
    lb.pack()
    home_frame.pack(pady=20)
    
def w1_page():
    def bereken_btw():
        bedrag = float(entry_bedrag.get())
        btw_tarief = float(entry_btw_tarief.get())
        
        btw = (btw_tarief / 100) * bedrag
        totaal_bedrag = bedrag + btw

        label_resultaat.config(text=f'BTW: {btw:.2f} EUR\nTotaal bedrag: {totaal_bedrag:.2f} EUR')
        
    w1_frame=tk.Frame(main_frame)
    
    label_bedrag = tk.Label(w1_frame, text="Bedrag in euro's:")
    label_bedrag.pack()
    entry_bedrag = tk.Entry(w1_frame)
    entry_bedrag.pack()

    label_btw_tarief = tk.Label(w1_frame, text="BTW percentage (9% of 21%):")
    label_btw_tarief.pack()
    entry_btw_tarief = tk.Entry(w1_frame)
    entry_btw_tarief.pack()

    # Voeg een knop toe om de BTW te berekenen
    bereken_knop = tk.Button(w1_frame, text="Bereken BTW", command=bereken_btw)
    bereken_knop.pack()

    # Voeg een label toe om het resultaat weer te geven
    label_resultaat = tk.Label(w1_frame, text="")
    label_resultaat.pack()

    w1_frame.pack(pady=20)
        
def w2_page():
    def bereken_reistijd():
        try:
            afstand = float(entry_afstand.get())
            snelheid = float(entry_snelheid.get())
            tijd = afstand / snelheid
            label_resultaat.config(text=f'Reistijd: {int(tijd)} uur en {int((tijd % 1) * 60)} minuten')
        except ValueError:
            label_resultaat.config(text="Voer geldige waarden in voor afstand en snelheid.")

    w2_frame=tk.Frame(main_frame)
        
    tk.Label(w2_frame, text="Afstand (km):").pack()
    entry_afstand = tk.Entry(w2_frame)
    entry_afstand.pack()

    tk.Label(w2_frame, text="Snelheid (km/u):").pack()
    entry_snelheid = tk.Entry(w2_frame)
    entry_snelheid.pack()

    # Voeg een knop toe om de reistijd te berekenen
    tk.Button(w2_frame, text="Bereken Reistijd", command=bereken_reistijd).pack()

    # Voeg een label toe om het resultaat weer te geven
    label_resultaat = tk.Label(w2_frame, text="")
    label_resultaat.pack()
        
    w2_frame.pack(pady=20)


def w3_page():
    
    def bereken_omtrek():
        try:
            lengte_invoer = float(lengte.get())
            breedte_invoer = float(breedte.get())
            omtrek = 2 * (lengte_invoer + breedte_invoer)
            result_label.config(text=f"De omtrek is {omtrek} cm.")
        except ValueError:
            result_label.config(text="Voer een geldig getal in.")


    def bereken_oppervlakte():
        try:
            lengte_invoer = float(lengte.get())
            breedte_invoer = float(breedte.get())
            oppervlakte = lengte_invoer * breedte_invoer
            result_label.config(text=f"De oppervlakte is {oppervlakte} cm^2.")
        except ValueError:
            result_label.config(text="Voer een geldig jaartal in.")
            
    def clear_input():
        lengte.delete(0, 'end')
        breedte.delete(0, 'end')
        result_label.config(text="")

    w3_frame = tk.Frame(main_frame)
    w3_frame.grid(row=0, column=0)

    lengte_label = tk.Label(w3_frame, text="Voer de lengte (cm) in:")
    lengte_label.grid(row=0, column=0)

    lengte = tk.Entry(w3_frame)
    lengte.grid(row=0, column=1)

    breedte_label = tk.Label(w3_frame, text="Voer de breedte (cm) in:")
    breedte_label.grid(row=1, column=0)

    breedte = tk.Entry(w3_frame)
    breedte.grid(row=1, column=1)

    submit_button2 = tk.Button(w3_frame, text="Bereken omtrek", command=bereken_omtrek)
    submit_button2.grid(row=2, column=0)

    submit_button1 = tk.Button(w3_frame, text="Bereken oppervlakte", command=bereken_oppervlakte)
    submit_button1.grid(row=2, column=1)

    clear_button = tk.Button(w3_frame, text="Clear", command=clear_input)
    clear_button.grid(row=4, column=0)

    result_label = tk.Label(w3_frame, text="")
    result_label.grid(row=6, columnspan=2)

    
    w3_frame.pack(pady=20)

def w4_page():
    def bereken_opervlakte_en_omtrek():
        try: 
            diameter2 = float(diameter.get())
            straal = diameter2 / 2
            oppervlakte = pi * (straal ** 2)
            omtrek = 2 * pi * straal
            result_label.config(text=f"De oppervlakte van de cirkel is {oppervlakte} cm^2.")
            result2_label.config(text=f"De omtrek van de cirkel is {omtrek} cm.")
        except ValueError:
            result_label.config(text="Voer een geldig getal in.")
            
    def clear_input():
        diameter.delete(0, 'end')
        result_label.config(text="")
            

    w4_frame=tk.Frame(main_frame)
    w4_frame.grid(row=0, column=0)

    diameter_label = tk.Label(w4_frame, text="Voer de diameter (cm) in: ")
    diameter_label.grid(row=0, column=0)

    diameter = tk.Entry(w4_frame)
    diameter.grid(row=0, column=1)


    submit_button1 = tk.Button(w4_frame, text="Bereken oppervlakte en omtrek", command=bereken_opervlakte_en_omtrek)
    submit_button1.grid(row=3, column=1)

    clear_button = tk.Button(w4_frame, text="Clear", command=clear_input)
    clear_button.grid(row=3, column=0)

    result_label = tk.Label(w4_frame, text="")
    result_label.grid(row=6, columnspan=2)

    result2_label = tk.Label(w4_frame, text="")
    result2_label.grid(row=7, columnspan=2)
        
    
    w4_frame.pack(pady=20)
    

def hide_indicators():
    home_indicate.config(bg="#8db6f7")
    w1_indicate.config(bg="#8db6f7")
    w2_indicate.config(bg="#8db6f7")
    w3_indicate.config(bg="#8db6f7")
    w4_indicate.config(bg="#8db6f7")
        
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg="#345d9e")
    delete_pages()
    page()

options_frame = tk.Frame(root, bg="#8db6f7")

home_btn = tk.Button(options_frame,text="Home", font=("bold",15), fg="#345d9e", bd=0,bg="#8db6f7",command=lambda:indicate(home_indicate, home_page))
home_btn.place(x=10,y=50)
home_indicate= tk.Label(options_frame, text="",bg="#8db6f7")
home_indicate.place(x=3,y=50,width=5,height=40)

w1_btn = tk.Button(options_frame,text="BTW ", font=("bold",15), fg="#345d9e", bd=0,bg="#8db6f7",command=lambda:indicate(w1_indicate, w1_page))
w1_btn.place(x=10,y=100)
w1_indicate= tk.Label(options_frame, text="",bg="#8db6f7")
w1_indicate.place(x=3,y=100,width=5,height=40)

w2_btn = tk.Button(options_frame,text="Reistijd ", font=("bold",15), fg="#345d9e", bd=0,bg="#8db6f7",command=lambda:indicate(w2_indicate,w2_page))
w2_btn.place(x=10,y=150)
w2_indicate= tk.Label(options_frame, text="",bg="#8db6f7")
w2_indicate.place(x=3,y=150,width=5,height=40)

w3_btn = tk.Button(options_frame,text="vierkant", font=("bold",15), fg="#345d9e", bd=0,bg="#8db6f7",command=lambda:indicate(w3_indicate,w3_page))
w3_btn.place(x=10,y=200)
w3_indicate= tk.Label(options_frame, text="",bg="#8db6f7")
w3_indicate.place(x=3,y=200,width=5,height=40)

w4_btn = tk.Button(options_frame,text="cirkel", font=("bold",15), fg="#345d9e", bd=0,bg="#8db6f7",command=lambda:indicate(w4_indicate,w4_page))
w4_btn.place(x=10,y=250)
w4_indicate= tk.Label(options_frame, text="",bg="#8db6f7")
w4_indicate.place(x=3,y=250,width=5,height=40)



options_frame.pack(side = tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)

main_frame = tk.Frame(root, highlightbackground="#345d9e",highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=400, height=500)

root.mainloop()