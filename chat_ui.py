import tkinter as tk
import customtkinter as ctk

class ChatUI:
    def __init__(self, parent, send_callback, voice_callback, emotion_callback, features_callback):
        self.parent = parent
        self.send_callback = send_callback
        self.voice_callback = voice_callback
        self.emotion_callback = emotion_callback
        self.features_callback = features_callback
        
        # Create main layout
        self.create_layout()
        
    def create_layout(self):
        # Chat history area
        self.chat_frame = ctk.CTkFrame(self.parent)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.chat_history = ctk.CTkTextbox(self.chat_frame, height=400, width=600)
        self.chat_history.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.chat_history.configure(state=tk.DISABLED)
        
        # Input area
        self.input_frame = ctk.CTkFrame(self.parent)
        self.input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.user_input = ctk.CTkEntry(self.input_frame, placeholder_text="Type your message...")
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", lambda event: self.send_callback())
        
        self.send_button = ctk.CTkButton(
            self.input_frame, 
            text="Send", 
            command=self.send_callback,
            width=80
        )
        self.send_button.pack(side=tk.RIGHT, padx=5)
        
        # Toolbar
        self.toolbar_frame = ctk.CTkFrame(self.parent)
        self.toolbar_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Voice input button
        self.voice_button = ctk.CTkButton(
            self.toolbar_frame,
            text="Voice Input",
            command=self.voice_callback,
            width=100
        )
        self.voice_button.pack(side=tk.LEFT, padx=5)
        
        # Emotion detection button
        self.emotion_button = ctk.CTkButton(
            self.toolbar_frame,
            text="Detect Emotion",
            command=self.emotion_callback,
            width=120
        )
        self.emotion_button.pack(side=tk.LEFT, padx=5)
        
        # More features button
        self.features_button = ctk.CTkButton(
            self.toolbar_frame,
            text="More Features",
            command=self.features_callback,
            width=120
        )
        self.features_button.pack(side=tk.LEFT, padx=5)
        
        # Settings frame
        self.settings_frame = ctk.CTkFrame(self.toolbar_frame)
        self.settings_frame.pack(side=tk.RIGHT, padx=5)
        
        # TTS checkbox
        self.tts_enabled = tk.BooleanVar(value=False)
        self.tts_checkbox = ctk.CTkCheckBox(
            self.settings_frame,
            text="TTS",
            variable=self.tts_enabled
        )
        self.tts_checkbox.pack(side=tk.RIGHT, padx=5)
        
        # Display welcome message
        self.update_chat_history("Bot: Hello! How can I help you today?")
    
    def get_user_input(self):
        """Get the current user input text"""
        return self.user_input.get().strip()
        
    def set_user_input(self, text):
        """Set the user input text"""
        self.user_input.delete(0, tk.END)
        self.user_input.insert(0, text)
        
    def update_chat_history(self, message):
        """Add a message to the chat history"""
        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message + "\n\n")
        self.chat_history.configure(state=tk.DISABLED)
        self.chat_history.see(tk.END)  # Auto-scroll to bottom