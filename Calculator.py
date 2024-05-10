import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to evaluate the expression and display the result
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Create the main window
parent = tk.Tk()
parent.title("Calculator")
parent.configure(bg='lightgray')

# Create a variable to store the current display value
display_var = tk.StringVar()
display_var.set("0")

# Create the display label
display_label = tk.Label(parent, textvariable=display_var, font=("Arial", 24), anchor="e", bg="lightgray", padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define the button layout
button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create and place the buttons
for (text, row, col) in button_layout:
    button = tk.Button(parent, text=text, padx=20, pady=20, font=("Arial", 18), bd=0,
                       command=lambda t=text: update_display(t) if t != "=" else calculate_result(), bg='lightpink')
    button.grid(row=row, column=col, sticky="nsew")

# Create a Clear button
clear_button = tk.Button(parent, text="C", padx=20, pady=20, font=("Arial", 18), bd=0, command=clear_display, bg='lightpink')
clear_button.grid(row=5, column=0, columnspan=3, sticky="nsew")

# Configure grid weights
for i in range(5):
    parent.grid_rowconfigure(i, weight=1)
for i in range(4):
    parent.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
parent.mainloop()
