import tkinter as tk
from tkinter import messagebox

# Sample product data
products = [
    {"name": "Laptop", "price": 85000},
    {"name": "Smartphone", "price": 30000},
    {"name": "Headphones", "price": 1500},
    {"name": "Shoes", "price": 2200},
    {"name": "Watch", "price": 4500},
]

cart = []

# Main App Window
root = tk.Tk()
root.title("E-Commerce Shop")
root.geometry("600x500")
root.config(bg="#f2f2f2")

# Header
header = tk.Label(root, text="Welcome to Mini E-Shop", font=("Helvetica", 20, "bold"), bg="#f2f2f2", fg="#333")
header.pack(pady=10)

# Frame for products
product_frame = tk.LabelFrame(root, text="Available Products", font=("Helvetica", 12, "bold"), padx=10, pady=10)
product_frame.pack(pady=10, padx=10, fill="x")

# Cart Frame
cart_frame = tk.LabelFrame(root, text="Your Cart", font=("Helvetica", 12, "bold"), padx=10, pady=10)
cart_frame.pack(pady=10, padx=10, fill="x")

cart_listbox = tk.Listbox(cart_frame, width=60, height=5)
cart_listbox.pack(pady=5)

total_label = tk.Label(cart_frame, text="Total: ৳0", font=("Helvetica", 12, "bold"))
total_label.pack()

def update_cart():
    cart_listbox.delete(0, tk.END)
    total = 0
    for item in cart:
        cart_listbox.insert(tk.END, f"{item['name']} - ৳{item['price']}")
        total += item['price']
    total_label.config(text=f"Total: ৳{total}")

def add_to_cart(product):
    cart.append(product)
    update_cart()

def checkout():
    if not cart:
        messagebox.showwarning("Cart Empty", "Please add products to the cart before checkout.")
    else:
        total = sum(item['price'] for item in cart)
        messagebox.showinfo("Checkout", f"Thank you for shopping!\nTotal bill: ৳{total}")
        cart.clear()
        update_cart()

# Add product buttons
for idx, product in enumerate(products):
    frame = tk.Frame(product_frame)
    frame.pack(fill="x", pady=2)

    name_label = tk.Label(frame, text=f"{product['name']} - ৳{product['price']}", font=("Helvetica", 11))
    name_label.pack(side="left", padx=10)

    add_button = tk.Button(frame, text="Add to Cart", bg="#4CAF50", fg="white", command=lambda p=product: add_to_cart(p))
    add_button.pack(side="right", padx=10)

# Checkout Button
checkout_button = tk.Button(root, text="Checkout", font=("Helvetica", 12, "bold"), bg="#007acc", fg="white", width=20, command=checkout)
checkout_button.pack(pady=20)

# Run App
root.mainloop()
