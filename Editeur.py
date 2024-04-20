import tkinter as tk
from tkinter import font, filedialog
 
def sauvegarder_contenu():
    content = zone_texte.get("1.0", tk.END)
    filename = e.get()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def ouvrir_contenu():
    try:
        filename = s.get()
        with open(filename, "r", encoding="utf-8") as f:
            message = f.read()
            zone_texte.delete("1.0", tk.END)
            zone_texte.insert(tk.END, message)
    except FileNotFoundError:
        print("Le fichier n'existe pas.")

def changer_police(event=None):
    selected_font = selected_font_var.get()
    zone_texte.config(font=(selected_font, current_font_size))

fen = tk.Tk()
fen.title("Editeur de texte")
fen.geometry("750x550")

e = tk.Entry(fen)
e.grid(row=0, column=0, padx=88, pady=10, sticky="w")

bouton_sauvegarde = tk.Button(fen, text="Sauvegarder", command=sauvegarder_contenu, bg="gray")
bouton_sauvegarde.grid(row=0, column=0, padx=10, pady=10, sticky="w")

s = tk.Entry(fen)
s.grid(row=0, column=1, padx=70, pady=10, sticky="e")

bouton_ouvrir = tk.Button(fen, text="Ouvrir", command=ouvrir_contenu, bg="gray")
bouton_ouvrir.grid(row=0, column=1, padx=10, pady=10, sticky="e")

zone_texte = tk.Text(fen, font = ("Arial") )
zone_texte.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

fonts = list(font.families())
current_font_size = 12
selected_font_var = tk.StringVar(fen, fonts[0])
fonts_combobox = tk.OptionMenu(fen, selected_font_var, *fonts, command=changer_police)
fonts_combobox.grid(row=2, column=0, padx=10, pady=10, sticky="w")

fen.mainloop()
