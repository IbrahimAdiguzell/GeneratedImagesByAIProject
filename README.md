🎨 AI Art Studio (AI Image Generator)

This project is a desktop application developed as part of the Object-Oriented Programming (OOP) course. It converts text prompts into images using Artificial Intelligence.

Built with Python and the modern GUI library CustomTkinter.

🚀 Features

Modern GUI: User-friendly interface designed with CustomTkinter, supporting Dark Mode.

Multi-Model Support: Integrated with Hugging Face (Stable Diffusion) and OpenAI (DALL-E).

Threaded Operations: Prevents UI freezing during image generation by running tasks in background threads.

Extensible Architecture: Designed to easily add new AI models in the future.

🏗️ Applied OOP Principles

This project adheres to SOLID principles and core OOP concepts:

Abstraction: The ImageGeneratorStrategy abstract base class defines a common template for all image generators.

Inheritance: The AIArtApp class inherits from ctk.CTk, and specific model classes inherit from ImageGeneratorStrategy.

Polymorphism: The application can switch between models dynamically and call the generate() method without knowing the specific implementation details.

Encapsulation: UI components and internal logic are hidden within protected methods like _setup_ui.

🛠️ Installation

Follow these steps to run the project on your local machine.

1. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git](https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git)
cd YOUR_PROJECT_NAME


2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

Windows:

python -m venv venv
.\venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate


3. Install Requirements

pip install customtkinter requests pillow python-dotenv openai


4. Setup API Keys

Create a .env file in the root directory and add your API keys:

HUGGINGFACE_API_KEY=hf_your_key_here
OPENAI_API_KEY=sk_your_key_here


(Note: If no keys are provided, the app will run in simulation mode for testing purposes.)

5. Run the Application

python main.py


📂 Project Structure

AI-Art-Studio/
├── generators.py    # Image generation logic (Backend & Strategy Pattern)
├── main.py          # Main application and GUI code
├── .env             # API Keys (Keep secret)
└── README.md        # Project documentation


📸 Screenshots

🤝 Contributing

Fork this repository.

Create a new feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📝 License

Distributed under the MIT License.
