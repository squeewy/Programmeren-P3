import tkinter as tk
from math import pi
    
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
        
window =tk.Tk()

window.title = ("omtrek en oppervlakte van een cirkel berekenen")

frame = tk.Frame(window)
frame.grid(row=0, column=0)

diameter_label = tk.Label(frame, text="Voer de diameter (cm) in: ")
diameter_label.grid(row=0, column=0)


diameter = tk.Entry(frame)
diameter.grid(row=0, column=1)


submit_button1 = tk.Button(frame, text="Bereken oppervlakte en omtrek", command=bereken_opervlakte_en_omtrek)
submit_button1.grid(row=3, column=1)

clear_button = tk.Button(frame, text="Clear", command=clear_input)
clear_button.grid(row=3, column=0)

result_label = tk.Label(frame, text="")
result_label.grid(row=6, columnspan=2)

result2_label = tk.Label(frame, text="")
result2_label.grid(row=7, columnspan=2)

window.mainloop()