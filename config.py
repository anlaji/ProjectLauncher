import sys, os
from dotenv import load_dotenv

load_dotenv()
USER_FOLDER = os.getenv("USER_FOLDER")

# launcher/config.py
def get_base_path() -> str:
    if hasattr(sys, "_MEIPASS"):
        # carpeta fija en AppData, independiente de donde esté el .exe
        app_dir = os.path.join(os.environ["APPDATA"], "ProjectLauncher")
        os.makedirs(app_dir, exist_ok=True)
        return app_dir
    return os.path.abspath(".")

def load_env():
    load_dotenv(os.path.join(get_base_path(), ".env"))
# IDEs
JETBRAINS_BASE = os.getenv("JETBRAINS_BASE", r"C:\Program Files\JetBrains")
VSCODE_BASE    = os.getenv("VSCODE_BASE",    fr"C:\Users\{USER_FOLDER}\AppData\Local\Programs\Microsoft VS Code")

IDES = {
    "pycharm": os.getenv("IDE_PYCHARM", fr"{JETBRAINS_BASE}\PyCharm Community Edition 2023.3.2\bin\pycharm64.exe"),
    "idea":    os.getenv("IDE_IDEA",    fr"{JETBRAINS_BASE}\IntelliJ IDEA 2025.3.1.1\bin\idea64.exe"),
    "vscode":  os.getenv("IDE_VSCODE",  fr"{VSCODE_BASE}\Code.exe"),
}