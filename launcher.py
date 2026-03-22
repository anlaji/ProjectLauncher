import json
import subprocess
import os
from dotenv import load_dotenv

# Cargar .env
load_dotenv()
USER_FOLDER = os.getenv("USER_FOLDER")

# IDEs
JETBRAINS_BASE = os.getenv("JETBRAINS_BASE", r"C:\Program Files\JetBrains")
VSCODE_BASE    = os.getenv("VSCODE_BASE",    fr"C:\Users\{USER_FOLDER}\AppData\Local\Programs\Microsoft VS Code")

IDES = {
    "pycharm": os.getenv("IDE_PYCHARM", fr"{JETBRAINS_BASE}\PyCharm Community Edition 2023.3.2\bin\pycharm64.exe"),
    "idea":    os.getenv("IDE_IDEA",    fr"{JETBRAINS_BASE}\IntelliJ IDEA 2025.3.1.1\bin\idea64.exe"),
    "vscode":  os.getenv("IDE_VSCODE",  fr"{VSCODE_BASE}\Code.exe"),
}

# Cargar parent projects
with open("projects.json", "r") as f:
    parent_projects = json.load(f)

# Crear lista de subproyectos con .git
projects = []
for parent in parent_projects:
    parent_path = parent["path"].replace("${USER_FOLDER}", USER_FOLDER)

    for root, dirs, files in os.walk(parent_path):
        if root == parent_path:
            continue
        if os.path.isdir(os.path.join(root, ".git")):
            projects.append({
                "name": os.path.basename(root),
                "path": root,
                "ide": parent["ide"]
            })

# Loop interactivo
while True:
    print("\nSubproyectos con .git encontrados:")
    for i, proj in enumerate(projects):
        print(f"{i+1}. {proj['name']} ({proj['ide']})")
    print("0. Salir")

    try:
        choice = int(input("Selecciona un proyecto por número: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        continue

    if choice == 0:
        print("Saliendo...")
        break
    elif 1 <= choice <= len(projects):
        proj = projects[choice - 1]
        ide_path = IDES[proj['ide']]
        subprocess.Popen([ide_path, proj['path']])
        print("Abriendo..")
    else:
        print("Número fuera de rango, intenta de nuevo.")