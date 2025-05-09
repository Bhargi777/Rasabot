import tkinter as tk
import customtkinter as ctk
from chatbot_app import AwesomeChatbotApp
import rasa.core.agent as agent
import asyncio
import os

def main():
    # Set appearance mode and theme
    ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
    ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"
    
    # Create the root window
    root = ctk.CTk()
    
    # Find the most recent model
    models_dir = "models"
    if os.path.exists(models_dir) and os.path.isdir(models_dir):
        model_files = [os.path.join(models_dir, f) for f in os.listdir(models_dir) 
                      if f.endswith('.tar.gz')]
        if model_files:
            latest_model = max(model_files, key=os.path.getctime)
        else:
            latest_model = None
    else:
        latest_model = None
    
    if not latest_model:
        show_error("Model not found", "No trained Rasa model found in 'models' directory.")
        return
    
    # Load Rasa agent
    rasa_agent = agent.Agent.load(latest_model)
    
    # Create the chatbot app
    app = AwesomeChatbotApp(root, rasa_agent)
    
    # Start the main loop
    root.mainloop()

def show_error(title, message):
    """Show error dialog"""
    error_window = ctk.CTk()
    error_window.title(title)
    error_window.geometry("400x200")
    ctk.CTkLabel(
        error_window, 
        text=message,
        font=("Helvetica", 14)
    ).pack(expand=True, padx=20, pady=20)
    ctk.CTkButton(
        error_window,
        text="OK",
        command=error_window.destroy
    ).pack(pady=20)
    error_window.mainloop()

if __name__ == "__main__":
    main()