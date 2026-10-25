import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

ventana = tk.Tk()
ventana.title("Cámara")
ventana.geometry("420x300")
ventana.resizable(False, False)

foto_actual = None

titulo = tk.Label(
    ventana,
    text="📷 Cámara",
    font=("Arial", 22, "bold")
)
titulo.pack(pady=20)

estado = tk.Label(
    ventana,
    text="Todavía no abriste ninguna foto",
    wraplength=360
)
estado.pack(pady=10)


def abrir_foto():
    global foto_actual

    archivo = filedialog.askopenfilename(
        title="Elegir una fotografía",
        filetypes=[
            ("Imágenes", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("Todos los archivos", "*.*")
        ]
    )

    if archivo:
        foto_actual = Path(archivo)
        estado.config(text=f"Foto seleccionada:\n{foto_actual.name}")


def configurar():
    messagebox.showinfo(
        "Configuración",
        "La configuración estará disponible en una próxima versión."
    )


tk.Button(
    ventana, text="Abrir fotografía",
    command=abrir_foto, width=22
).pack(pady=8)

tk.Button(
    ventana, text="Configurar",
    command=configurar, width=22
).pack(pady=8)

ventana.mainloop()
