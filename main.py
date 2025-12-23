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


        self.styles = {
            "Standart": "",
            "Gerçekçi Fotoğraf": ", photorealistic, 8k resolution, highly detailed, sharp focus, cinematic lighting, masterpiece",
            "Sinematik Sahne": ", cinematic movie scene, dramatic lighting, atmospheric, highly detailed, 8k, movie still",
            "3D Render (Oyun)": ", 3d render, unreal engine 5, intricate details, smooth textures, global illumination, 8k",
            "Anime / Çizim": ", anime style, studio Ghibli inspired, vibrant colors, high quality illustration",
            "Cyberpunk": ", cyberpunk style, neon lights, futuristic, highly detailed, digital painting"
        }

        self.sizes = {
            "Kare (1024x1024)": "1024x1024",
            "Geniş/Yatay (1792x1024)": "1792x1024",
            "Dikey/Telefon (1024x1792)": "1024x1792"
        }

        self.random_prompts = [
            "Dev bir ağacın üzerine kurulmuş fütüristik bir şehir, sinematik aydınlatma",
            "İstanbul'da cypherpunk bir sokak yemeği satıcısı, neon ışıklar, gece",
            "Yüzen bir ada üzerindeki ortaçağ kalesi",
            "Bir serada bitkileri sulayan sevimli bir robot, pixar tarzı",
            "Seradaki bitkileri sulayan sevimli bir robot,pixar tarzı",
            "Bir ormanda gizlenmiş antik bir tapınak, mistik atmosfer   "
        ]
