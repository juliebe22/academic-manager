import tkinter as tk
from tkinter import messagebox

try:

    from database import client
    from interface import AcademicManager

    root = tk.Tk()

    app = AcademicManager(root)

    root.mainloop()

    client.close()

except Exception as erro:

    messagebox.showerror(
        "Erro ao iniciar",
        f"Não foi possível iniciar o sistema:\n{erro}"
    )