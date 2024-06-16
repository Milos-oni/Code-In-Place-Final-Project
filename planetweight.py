import customtkinter as ctk

MARS_CONVERSION = 0.378
VENUS_CONVERSION = 0.889
MERCURY_CONVERSION = 0.376
JUPITER_CONVERSION = 2.36
SATURN_CONVERSION = 1.081
URANUS_CONVERSION = 0.815
NEPTUNE_CONVERSION = 1.14

def calculate_weight():
    earth_weight = float(weight_entry.get())
    planet = planet_var.get()
    conversion_factor = conversion_factors[planet]
    planet_weight = earth_weight * conversion_factor
    result_label.configure(text=f"Weight on {planet}: {planet_weight:.2f} kg")


conversion_factors = {
    "Mars": MARS_CONVERSION,
    "Venus": VENUS_CONVERSION,
    "Mercury": MERCURY_CONVERSION,
    "Jupiter": JUPITER_CONVERSION,
    "Saturn": SATURN_CONVERSION,
    "Uranus": URANUS_CONVERSION,
    "Neptune": NEPTUNE_CONVERSION,
}

root = ctk.CTk()
root.title("Weight on Different Planets")
root.geometry("400x300")
root.resizable(False, False)
root.iconbitmap('planet.ico')


weight_label = ctk.CTkLabel(root, text="Enter your weight on Earth (kg):")
weight_label.pack(pady=5)
weight_entry = ctk.CTkEntry(root)
weight_entry.pack(pady=5)

# Selection menu for planets
planet_var = ctk.StringVar(root)
planet_var.set("Mars")  

planet_menu = ctk.CTkComboBox(root, variable=planet_var, values=list(conversion_factors.keys()))
planet_menu.pack(pady=5)

# Calculate Button
calculate_button = ctk.CTkButton(root, text="Calculate", command=calculate_weight)
calculate_button.pack(pady=5)

# Result
result_label = ctk.CTkLabel(root, text="Weight on selected planet: ")
result_label.pack(pady=20)

root.mainloop()
