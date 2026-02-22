import tkinter as tk
from PIL import Image, ImageTk
import googletrans
import tkinter.messagebox as messagebox

# Default translation engine
translator = googletrans.Translator()

def load_image(path, size):
    """Load an image from path and resize it to the specified size"""
    try:
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Warning: Image file not found: {path}")
        # Create a placeholder image
        img = Image.new('RGB', size, color='#cccccc')
        return ImageTk.PhotoImage(img)

def confirm_exit():
    """Confirm before exiting the application"""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # Clean up any resources here
        tk._default_root.destroy()

def translate_text(text, target_lang='en'):
    """Translate text to the target language"""
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return f"Translation error: {e}"

def perform_sentiment_analysis(text):
    """
    Perform basic sentiment analysis on text
    Returns: (sentiment, confidence)
    """
    # This is a very simple sentiment analysis - in real app, use NLTK or other NLP library
    positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'nice', 'wonderful', 'best', 'awesome']
    negative_words = ['bad', 'terrible', 'awful', 'sad', 'hate', 'poor', 'worst', 'horrible', 'annoying']
    
    text = text.lower()
    
    pos_count = sum(text.count(word) for word in positive_words)
    neg_count = sum(text.count(word) for word in negative_words)
    
    if pos_count > neg_count:
        return ("POSITIVE", pos_count / (pos_count + neg_count + 0.1))
    elif neg_count > pos_count:
        return ("NEGATIVE", neg_count / (pos_count + neg_count + 0.1))
    else:
        return ("NEUTRAL", 1.0)