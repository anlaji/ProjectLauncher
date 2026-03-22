# ui/app.py
import customtkinter as ctk
import subprocess
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

IDE_COLORS = {
    "pycharm": "#1f538d",
    "idea":    "#534AB7",
    "vscode":  "#3B6D11",
}

class LauncherApp(ctk.CTk):
    def __init__(self, projects: list, ides: dict):
        super().__init__()
        self.projects   = projects
        self.ides       = ides
        self.filtered   = projects[:]

        self.title("Project Launcher")
        self.geometry("620x500")
        self._build_ui()

    def _build_ui(self):
        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=16, pady=(16, 0))
        ctk.CTkLabel(header, text="Project Launcher", font=("Arial", 18, "bold")).pack(side="left")
        self.count_label = ctk.CTkLabel(header, text=f"{len(self.projects)} proyectos",
                                        font=("Arial", 12), text_color="gray")
        self.count_label.pack(side="right")

        # Buscador
        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self._on_search)
        search = ctk.CTkEntry(self, placeholder_text="Buscar proyecto...",
                              textvariable=self.search_var, height=36)
        search.pack(fill="x", padx=16, pady=10)

        # Lista scrollable
        self.scroll = ctk.CTkScrollableFrame(self)
        self.scroll.pack(fill="both", expand=True, padx=16)

        # Footer
        ctk.CTkButton(self, text="Reescanear", height=32,
                      command=self._rescan).pack(pady=10)

        self._render_list()

    def _render_list(self):
        for w in self.scroll.winfo_children():
            w.destroy()

        for proj in self.filtered:
            row = ctk.CTkFrame(self.scroll, fg_color="transparent")
            row.pack(fill="x", pady=2)

            info = ctk.CTkFrame(row, fg_color="transparent")
            info.pack(side="left", fill="x", expand=True)
            ctk.CTkLabel(info, text=proj["name"],
                         font=("Arial", 13, "bold")).pack(anchor="w")
            ctk.CTkLabel(info, text=proj["path"], font=("Arial", 11),
                         text_color="gray").pack(anchor="w")

            color = IDE_COLORS.get(proj["ide"], "#444")
            ctk.CTkButton(row, text=proj["ide"], width=80, height=28,
                          fg_color=color,
                          command=lambda p=proj: self._open(p)).pack(side="right", padx=4)

    def _on_search(self, *_):
        q = self.search_var.get().lower()
        self.filtered = [p for p in self.projects if q in p["name"].lower()]
        self.count_label.configure(text=f"{len(self.filtered)} proyectos")
        self._render_list()

    def _open(self, proj: dict):
        ide_path = self.ides.get(proj["ide"])
        if ide_path and os.path.exists(ide_path):
            subprocess.Popen([ide_path, proj["path"]])
        else:
            print(f"IDE no encontrado: {ide_path}")

    def _rescan(self):
        # Reimporta la lógica de escaneo
        from launcher.scanner import scan_projects  # ajusta el import
        self.projects = scan_projects()
        self.filtered = self.projects[:]
        self.count_label.configure(text=f"{len(self.projects)} proyectos")
        self._render_list()