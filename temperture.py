import tkinter as tk

def celsius_to_fahrenheit():
    celsius_temp = float(celsius_entry.get())
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    fahrenheit_result_label.config(text=f"{fahrenheit_temp:} °F")

def fahrenheit_to_celsius():
    
    fahrenheit_temp = float(fahrenheit_entry.get())
    celsius_temp = (fahrenheit_temp * 9/5) + 32
    celsius_result_label.config(text=f"{celsius_temp:} °c")
root = tk.Tk()
root.title("Temperature Converter")


celsius_label = tk.Label(root, bg="lightblue", text="Celsius:")
celsius_label.pack()

celsius_entry = tk.Entry(root)
celsius_entry.pack()

celsius_to_fahrenheit_button = tk.Button(root, text="Convert to Fahrenheit", bg="lightblue", command=celsius_to_fahrenheit)
celsius_to_fahrenheit_button.pack()

fahrenheit_result_label = tk.Label(root, text="")
fahrenheit_result_label.pack()


fahrenheit_label = tk.Label(root, bg="lightblue", text="Fahrenheit:")
fahrenheit_label.pack()

fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.pack()

fahrenheit_to_celsius_button = tk.Button(root, text="Convert to Celsius", bg="lightblue", command=fahrenheit_to_celsius)
fahrenheit_to_celsius_button.pack()

celsius_result_label = tk.Label(root, text="")
celsius_result_label.pack()

root.configure(bg="darkslategray")

root.geometry("400x400")
root.mainloop()
