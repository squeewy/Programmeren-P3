import tkinter as tk



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

w2 = tk.Tk()
w2.title = ("omtrek en oppervlakte van een vierkant berekenen")

frame = tk.Frame(w2)
frame.grid(row=0, column=0)

lengte_label = tk.Label(frame, text="Voer de lengte (cm) in:")
lengte_label.grid(row=0, column=0)

lengte = tk.Entry(frame)
lengte.grid(row=0, column=1)

breedte_label = tk.Label(frame, text="Voer de breedte (cm) in:")
breedte_label.grid(row=1, column=0)

breedte = tk.Entry(frame)
breedte.grid(row=1, column=1)

submit_button2 = tk.Button(frame, text="Bereken omtrek", command=bereken_omtrek)
submit_button2.grid(row=2, column=0)

submit_button1 = tk.Button(frame, text="Bereken oppervlakte", command=bereken_oppervlakte)
submit_button1.grid(row=2, column=1)

clear_button = tk.Button(frame, text="Clear", command=clear_input)
clear_button.grid(row=4, column=0)

result_label = tk.Label(frame, text="")
result_label.grid(row=6, columnspan=2)

w2.mainloop()