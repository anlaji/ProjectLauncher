# ProjectLauncher

ProjectLauncher es un launcher interactivo para abrir múltiples subproyectos que sean repositorios Git (`.git`) desde carpetas parent definidas en `projects.json`. Cada subproyecto se abre en la IDE configurada para su parent (PyCharm, IntelliJ IDEA, VS Code).

---

## Requisitos

- Python 3.10+  
- IDEs instaladas (PyCharm, IntelliJ, VS Code)  
- Dependencias Python:

## APPDATA
```
mkdir "%APPDATA%\ProjectLauncher"
copy projects.json "%APPDATA%\ProjectLauncher\"
copy .env "%APPDATA%\ProjectLauncher\"
```
C:\Users\...\AppData\Roaming\ProjectLauncher\
  projects.json
  .env

