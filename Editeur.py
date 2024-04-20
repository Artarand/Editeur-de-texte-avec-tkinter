import tkinter as tk

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

fen = tk.Tk()
fen.title("Editeur de texte")
fen.geometry("800x500")

e = tk.Entry(fen)
e.grid(row=0, column=0, padx=88, pady=10, sticky="w")

bouton_sauvegarde = tk.Button(fen, text="Sauvegarder", command=sauvegarder_contenu, bg="gray")
bouton_sauvegarde.grid(row=0, column=0, padx=10, pady=10, sticky="w")

s = tk.Entry(fen)
s.grid(row=0, column=1, padx=70, pady=10, sticky="e")

bouton_ouvrir = tk.Button(fen, text="Ouvrir", command=ouvrir_contenu, bg="gray")
bouton_ouvrir.grid(row=0, column=1, padx=10, pady=10, sticky="e")

zone_texte = tk.Text(fen)
zone_texte.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

fen.mainloop()
