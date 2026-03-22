# launcher/scanner.py
from dotenv import load_dotenv
import os, json

from config import get_base_path


def scan_projects() -> list:
    user_folder = os.getenv("USER_FOLDER", "alagu")
    base = get_base_path()

    with open(os.path.join(base, "projects.json"), "r") as f:
        parent_projects = json.load(f)

    projects = []
    for parent in parent_projects:
        parent_path = parent["path"].replace("${USER_FOLDER}", user_folder)
        for root, dirs, files in os.walk(parent_path):
            if root == parent_path:
                continue
            if os.path.isdir(os.path.join(root, ".git")):
                projects.append({
                    "name": os.path.basename(root),
                    "path": root,
                    "ide":  parent["ide"]
                })

    return projects