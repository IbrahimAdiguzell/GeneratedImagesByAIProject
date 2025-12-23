import customtkinter as ctk
from tkinter import messagebox, filedialog
import threading
from PIL import Image, ImageTk
import os
import datetime
import random
from dotenv import load_dotenv

try:
    from generators import HuggingFaceGenerator, OpenAIGenerator, ImageGeneratorStrategy
except ImportError as e:
    print(f"KRİTİK HATA: generators.py dosyası bulunamadı! {e}")
    exit()

load_dotenv()

class AIArtApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Görsel İstasyonu v2.0")
        self.geometry("1200x850")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.auto_save_path = r"C:\GeneratedImagesByAIProject\SavedPictures"
        if not os.path.exists(self.auto_save_path):
            try:
                os.makedirs(self.auto_save_path)
                print(f"Klasör oluşturuldu: {self.auto_save_path}")
            except Exception as e:
                print(f"Klasör oluşturma hatası: {e}")

        self.current_generator = None
        self.generated_image = None
        self.history_images = [] 