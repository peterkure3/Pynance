import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import datetime
import os


def on_submit():
    # Get the values from the form
    item = item_entry.get()
    price = price_entry.get()
    charges = charges_entry.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Validate the inputs
    if not item or not price or not charges:
        messagebox.showerror("Error", "Please fill all the fields")
        return
    
    # Write the data to the CSV file
    with open("finance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, item, price, charges])
    
    # Clear the form
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    charges_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", "Data saved successfully")

# No need for on_export function as data is saved automatically

# Create the main window
root = tk.Tk()
root.geometry("400x200")
root.config(bg="#333")
root.title("Finance Management")

# Heading
heading_label = ttk.Label(root, text="Finance Management Program", font=("Helvetica", 18), foreground="white", background="#333")
heading_label.pack(pady=20)

# Create the form
frame = ttk.Frame(root)
frame.pack(pady=20)

# Create the form fields
item_label = ttk.Label(frame, text="Item", font=("Helvetica", 14), foreground="white", background="#333")
item_label.grid(row=0, column=0, padx=10, pady=10)
item_entry = ttk.Entry(frame, font=("Helvetica", 14))
item_entry.grid(row=0, column=1, padx=10, pady=10)

price_label = ttk.Label(frame, text="Price", font=("Helvetica", 14), foreground="white", background="#333")
price_label.grid(row=1, column=0, padx=10, pady=10)
price_entry = ttk.Entry(frame, font=("Helvetica", 14))
price_entry.grid(row=1, column=1, padx=10, pady=10)

charges_label = ttk.Label(frame, text="Additional Charges", font=("Helvetica", 14), foreground="white", background="#333")
charges_label.grid(row=2, column=0, padx=10, pady=10)
charges_entry = ttk.Entry(frame, font=("Helvetica", 14))
charges_entry.grid(row=2, column=1, padx=10, pady=10)

# Create the submit button
submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=3, column=0, padx=10, pady=10)

def on_edit():
    data = []
    with open("finance.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    
    selected = messagebox.askquestion("Edit", "Do you want to edit the data?")
    if selected == "yes":
        for index, row in enumerate(data):
            item = row[1]
            price = row[2]
            charges = row[3]
            
            edit = messagebox.askquestion("Edit", f"Do you want to edit the data for {item}?")
            if edit == "yes":
                item_entry.delete(0, tk.END)
                item_entry.insert(0, item)
                price_entry.delete(0, tk.END)
                price_entry.insert(0, price)
                charges_entry.delete(0, tk.END)
                charges_entry.insert(0, charges)
                
                def on_update():
                    data[index][1] = item_entry.get()
                    data[index][2] = price_entry.get()
                    data[index][3] = charges_entry.get()
                    
                    with open("finance.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(data)
                        
                    messagebox.showinfo("Success", "Data updated successfully")
                    root.destroy()
                
                update_button = ttk.Button(frame, text="Update", command=on_update)
                update_button.grid(row=4, column=0, columnspan=2, pady=10)
                
                root.mainloop()

edit_button = ttk.Button(frame, text="Edit", command=on_edit)
edit_button.grid(row=4, column=0, padx=10, pady=10)

def on_export():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")
    if file_path:
        with open("finance.csv", "r") as read_file, open(file_path, "w", newline="") as write_file:
            reader = csv.reader(read_file)
            writer = csv.writer(write_file)
            for row in reader:
                writer.writerow(row)
    
    messagebox.showinfo("Success", "Data exported successfully")

# Create the export button
export_button = ttk.Button(frame, text="Export", command=on_export)
export_button.grid(row=3, column=2, padx=10, pady=10)

# Create the exit button
exit_button = ttk.Button(frame, text="Exit", command=root.quit)
exit_button.grid(row=4, column=0, padx=10, pady=10)

# Create the radio button for saving to a different directory
save_directory = tk.StringVar()
save_directory.set("default")

default_rb = ttk.Radiobutton(frame, text="Default Directory", variable=save_directory, value="default")
default_rb.grid(row=4, column=0, padx=10, pady=10, sticky="w")

saves_rb = ttk.Radiobutton(frame, text="Saves Directory", variable=save_directory, value="saves")
saves_rb.grid(row=4, column=1, padx=10, pady=10, sticky="w")

def on_submit():
    # Get the values from the form
    item = item_entry.get()
    price = price_entry.get()
    charges = charges_entry.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Validate the inputs
    if not item or not price or not charges:
        messagebox.showerror("Error", "Please fill all the fields")
        return
    
    # Write the data to the CSV file
    if save_directory.get() == "default":
        file_path = "finance.csv"
    else:
        if not os.path.exists("Saves"):
            os.makedirs("Saves")
        file_path = "Saves/finance.csv"
        
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, item, price, charges])
    
    # Clear the form
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    charges_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", "Data saved successfully")


# Run the main loop
root.mainloop()

