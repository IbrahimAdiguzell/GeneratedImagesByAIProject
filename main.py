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