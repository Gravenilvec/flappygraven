from cx_Freeze import setup, Executable

base = None
executables = [Executable("main.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages
    }
}

setup(
    name = "Flappy Graven Game",
    options = options,
    version = "1.0",
    description = "mon super jeu",
    executables = executables
)