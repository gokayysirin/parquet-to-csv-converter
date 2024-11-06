# libraries 
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a Parquet File", filetypes=[("Parquet files", "*.parquet")]
    )
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def convert_to_csv():
    parquet_file = entry_path.get()
    if not os.path.isfile(parquet_file) or not parquet_file.endswith(".parquet"):
        messagebox.showerror("Error", "Please select a valid Parquet file.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".csv", filetypes=[("CSV files", "*.csv")]
    )
    if not save_path:
        return

    try:
        df = pd.read_parquet(parquet_file)
        df.to_csv(save_path, index=False)
        messagebox.showinfo("Success", f"File successfully saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

app = tk.Tk()
app.title("Parquet to CSV Converter")
app.geometry("500x250")
app.configure(bg='#f0f0f0')

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Helvetica", 10), padding=10)
style.configure("TEntry", font=("Helvetica", 10))

frame = tk.Frame(app, bg='#f0f0f0')
frame.pack(pady=30)

entry_path = ttk.Entry(frame, width=45)
entry_path.grid(row=0, column=0, padx=10, pady=5)

btn_browse = ttk.Button(frame, text="Browse", command=select_file)
btn_browse.grid(row=0, column=1, padx=5)

btn_convert = ttk.Button(app, text="Convert to CSV", command=convert_to_csv)
btn_convert.pack(pady=20)

app.mainloop()
