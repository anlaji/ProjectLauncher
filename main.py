# main.py
from config import load_env
load_env()
from scanner import scan_projects
from config import IDES
from ui.app import LauncherApp


if __name__ == "__main__":
    projects = scan_projects()
    app = LauncherApp(projects=projects, ides=IDES)
    app.mainloop()