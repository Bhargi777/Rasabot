import customtkinter as ctk

def apply_style():
    # Set initial appearance mode (you can default to dark or light)
    ctk.set_appearance_mode("dark")  # Default mode can be set here (dark/light/system)
    
    # Set primary colors (Can adjust colors per theme)
    ctk.set_default_color_theme("blue")  # "blue", "dark-blue", "green", etc.

    # Apply global font styles
    ctk.CTkFont(family="Helvetica", size=14)
    
    # Configure buttons, entries, etc.
    ctk.CTkButton.configure(
        font=("Helvetica", 16), 
        corner_radius=10, 
        height=40
    )
    ctk.CTkEntry.configure(
        font=("Helvetica", 14),
        border_width=2,
        corner_radius=8
    )

# Function to change the theme
def toggle_theme(current_mode):
    new_mode = "light" if current_mode == "dark" else "dark"
    ctk.set_appearance_mode(new_mode)  # Switch theme
    return new_mode