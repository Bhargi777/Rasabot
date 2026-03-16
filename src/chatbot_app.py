import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import calendar
from datetime import datetime
import webbrowser
import random
import wikipedia
import asyncio
import os
from src.chat_ui import ChatUI
from src.voice_input import VoiceInput
from src.emotion_detection import EmotionDetection
from src.utils import load_image, confirm_exit, translate_text, perform_sentiment_analysis

class AwesomeChatbotApp:
    def __init__(self, root, agent):
        self.root = root
        self.agent = agent
        self.root.title("Awesome Rasa Chatbot")
        self.root.geometry("1200x800")

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create assets directory if it doesn't exist
        os.makedirs("assets", exist_ok=True)
        
        self.load_assets()
        self.voice_input = VoiceInput()
        self.emotion_detection = EmotionDetection()
        self.conversation_memory = []

        self.create_welcome_screen()
        self.root.protocol("WM_DELETE_WINDOW", confirm_exit)

    def load_assets(self):
        # Create placeholder images if files don't exist
        try:
            self.chat_icon = load_image("assets/chat_icon.png", (100, 100))
        except:
            # Create a blank image as fallback
            img = Image.new('RGB', (100, 100), color='#4CAF50')
            self.chat_icon = ImageTk.PhotoImage(img)
            
        try:
            self.mic_icon = load_image("assets/mic_icon.png", (30, 30))
        except:
            img = Image.new('RGB', (30, 30), color='#2196F3')
            self.mic_icon = ImageTk.PhotoImage(img)
            
        try:
            self.camera_icon = load_image("assets/camera_icon.png", (30, 30))
        except:
            img = Image.new('RGB', (30, 30), color='#FF9800')
            self.camera_icon = ImageTk.PhotoImage(img)

    def create_welcome_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        welcome_frame = ctk.CTkFrame(self.frame, corner_radius=10)
        welcome_frame.pack(expand=True, padx=20, pady=20)
        ctk.CTkLabel(
            welcome_frame,
            text="Welcome to Awesome Rasa Chatbot",
            font=("Helvetica", 24, "bold")
        ).pack(pady=20)
        ctk.CTkLabel(welcome_frame, image=self.chat_icon, text="").pack(pady=20)
        ctk.CTkLabel(
            welcome_frame,
            text="Your AI-powered assistant",
            font=("Helvetica", 18)
        ).pack(pady=10)
        ctk.CTkButton(
            welcome_frame,
            text="Start Chatting",
            command=self.create_chat_screen,
            font=("Helvetica", 16),
            fg_color="#4CAF50",
            hover_color="#45a049"
        ).pack(pady=20)

    def create_chat_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.chat_ui = ChatUI(
            self.frame,
            self.send_message,
            self.start_voice_input,
            self.start_emotion_detection,
            self.show_additional_features
        )
        self.chat_ui.user_input.focus_set()

    def send_message(self):
        user_message = self.chat_ui.get_user_input()
        if not user_message:
            return
        self.chat_ui.set_user_input("")
        self.chat_ui.update_chat_history(f"You: {user_message}")
        self.conversation_memory.append({"role": "user", "content": user_message})

        # Fetch Rasa response synchronously
        try:
            responses = asyncio.run(self.agent.handle_text(user_message))
            reply = responses[0].get(
                "text", "Sorry, I didn't understand that."
            ) if responses else "Sorry, I didn't understand that."
        except Exception as e:
            reply = f"Error fetching response: {e}"

        self.chat_ui.update_chat_history(f"Bot: {reply}")
        self.conversation_memory.append({"role": "assistant", "content": reply})
        
        # Only attempt text-to-speech if it's enabled
        if hasattr(self.chat_ui, 'tts_enabled') and self.chat_ui.tts_enabled.get():
            try:
                self.voice_input.text_to_speech(reply)
            except Exception as e:
                print(f"TTS Error: {e}")

    def start_voice_input(self):
        self.chat_ui.update_chat_history("Bot: Listening... (Please speak now)")
        text = self.voice_input.listen()
        if text:
            self.chat_ui.set_user_input(text)
            self.send_message()

    def start_emotion_detection(self):
        emotion = self.emotion_detection.detect_emotion()
        if emotion:
            self.chat_ui.update_chat_history(
                f"Bot: I detect that you're feeling {emotion}. How can I help you with that?"
            )
        else:
            self.chat_ui.update_chat_history(
                "Bot: I couldn't detect any emotions. Is everything okay?"
            )

    def show_additional_features(self):
        features_window = tk.Toplevel(self.root)
        features_window.title("Additional Features")
        features_window.geometry("400x400")
        features_window.transient(self.root)
        features_window.lift()
        features_window.grab_set()
        tk.Label(features_window, text="✨ Available Features", font=("Arial", 16)).pack(pady=10)
        
        features = [
            ("🔍 Sentiment Analysis", self.create_data_visualization),
            ("📈 Word Cloud", self.generate_word_cloud),
            ("🗓️ Calendar", self.show_calendar),
            ("🌐 Web Search", self.web_search),
            ("❓ Fun Facts", self.show_fun_fact),
            ("🌍 Translation", self.show_translation_dialog),
            ("📝 To-Do List", self.create_todo_list),
            ("🎮 Mini Game", self.create_mini_game),
            ("🌤️ Weather", self.show_weather)
        ]
        
        # Create a frame for the buttons
        buttons_frame = tk.Frame(features_window)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create style for buttons
        for i, (text, command) in enumerate(features):
            btn = tk.Button(
                buttons_frame, 
                text=text, 
                font=("Arial", 12),
                command=command,
                relief=tk.GROOVE,
                bg="#f0f0f0",
                activebackground="#e0e0e0",
                borderwidth=2,
                padx=10,
                pady=5
            )
            btn.pack(fill=tk.X, pady=5)

    def generate_word_cloud(self):
        text = " ".join([msg["content"] for msg in self.conversation_memory])
        
        # Check if there's any meaningful text to generate word cloud
        if not text or len(text.strip()) < 5:
            self.chat_ui.update_chat_history(
                "Bot: Not enough conversation data to generate a word cloud. Please chat more!"
            )
            return
            
        try:
            wc = WordCloud(width=800, height=400, background_color='white', min_word_length=2)
            wordcloud = wc.generate(text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('Conversation Word Cloud')
            plt.show()
        except Exception as e:
            self.chat_ui.update_chat_history(f"Bot: Error generating word cloud: {e}")

    def show_calendar(self):
        now = datetime.now()
        cal = calendar.month(now.year, now.month)
        window = ctk.CTkToplevel(self.root)
        window.title("Calendar")
        window.geometry("300x250")
        ctk.CTkLabel(window, text=cal, font=("Courier", 12)).pack(padx=10, pady=10)

    def web_search(self):
        query = ctk.CTkInputDialog(text="Enter your search query:", title="Web Search").get_input()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")

    def show_fun_fact(self):
        try:
            fact = wikipedia.random(1)
            summary = wikipedia.summary(fact, sentences=2)
            self.chat_ui.update_chat_history(
                f"Bot: Here's a fun fact: {summary}"
            )
        except Exception:
            self.chat_ui.update_chat_history(
                "Bot: Sorry, could not fetch a fun fact."
            )

    def show_translation_dialog(self):
        text = ctk.CTkInputDialog(text="Enter text to translate:", title="Translate").get_input()
        if text:
            lang = ctk.CTkInputDialog(
                text="Enter target language code (e.g., 'fr'):",
                title="Translate"
            ).get_input()
            if lang:
                translated = translate_text(text, lang)
                self.chat_ui.update_chat_history(
                    f"Bot: Translation to {lang}: {translated}"
                )

    def create_todo_list(self):
        window = ctk.CTkToplevel(self.root)
        window.title("To-Do List")
        window.geometry("300x400")
        self.todo_items = []
        self.todo_listbox = tk.Listbox(window)
        self.todo_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        entry = ctk.CTkEntry(window)
        entry.pack(pady=5, padx=10, fill=tk.X)
        ctk.CTkButton(window, text="Add Item", command=lambda: self.add_todo_item(entry.get())).pack(pady=5)
        ctk.CTkButton(window, text="Remove Selected", command=self.remove_todo_item).pack(pady=5)

    def add_todo_item(self, item):
        if item:
            self.todo_items.append(item)
            self.todo_listbox.insert(tk.END, item)
            self.chat_ui.update_chat_history(
                f"Bot: Added '{item}' to your to-do list."
            )

    def remove_todo_item(self):
        try:
            idx = self.todo_listbox.curselection()[0]
            itm = self.todo_items.pop(idx)
            self.todo_listbox.delete(idx)
            self.chat_ui.update_chat_history(
                f"Bot: Removed '{itm}' from your to-do list."
            )
        except Exception:
            self.chat_ui.update_chat_history(
                "Bot: Please select an item to remove."
            )

    def create_mini_game(self):
        window = ctk.CTkToplevel(self.root)
        window.title("Guess the Number")
        window.geometry("300x200")
        self.secret = random.randint(1, 100)
        self.tries = 0
        ctk.CTkLabel(window, text="Guess a number between 1 and 100:").pack(pady=10)
        ent = ctk.CTkEntry(window)
        ent.pack(pady=5)
        res_lbl = ctk.CTkLabel(window, text="")
        res_lbl.pack(pady=10)
        def guess():
            try:
                g = int(ent.get())
                self.tries += 1
                if g < self.secret:
                    res_lbl.configure(text="Too low!")
                elif g > self.secret:
                    res_lbl.configure(text="Too high!")
                else:
                    res_lbl.configure(text=f"Correct in {self.tries} tries!")
                    self.chat_ui.update_chat_history(
                        f"Bot: You won in {self.tries} tries!"
                    )
            except:
                res_lbl.configure(text="Invalid input.")
        ctk.CTkButton(window, text="Submit", command=guess).pack(pady=5)

    def show_weather(self):
        conditions = ["sunny","cloudy","rainy","snowy"]
        temp = random.randint(0,40)
        cond = random.choice(conditions)
        self.chat_ui.update_chat_history(
            f"Bot: The weather is {cond} at {temp}°C."  
        )

    def create_data_visualization(self):
        if not self.conversation_memory:
            self.chat_ui.update_chat_history(
                "Bot: Not enough conversation data to analyze sentiment. Please chat more!"
            )
            return
            
        try:
            sentiments = [perform_sentiment_analysis(m["content"])[0] for m in self.conversation_memory]
            counts = {s:sentiments.count(s) for s in ['POSITIVE','NEGATIVE','NEUTRAL']}
            plt.figure(figsize=(8,6))
            plt.bar(counts.keys(), counts.values())
            plt.title('Sentiment Analysis')
            plt.xlabel('Sentiment')
            plt.ylabel('Count')
            plt.show()
        except Exception as e:
            self.chat_ui.update_chat_history(f"Bot: Error analyzing sentiment: {e}")