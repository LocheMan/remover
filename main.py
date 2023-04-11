import os
import json

try: import pystyle
except:
    try: os.system(f"pip uninstall pystyle")
    except: pass
    os.system(f"pip install pystyle")
    
try: import shutil
except:
    try: os.system(f"pip uninstall shutil")
    except: pass
    os.system(f"pip install shutil")

import watermark


def remover():
    data = json.load(open('config.json', 'r'))
    user = os.getenv("UserName")

    # Prefetch
    prefetches = data["cheats"]["prefetches"]
    try:
        for file in os.listdir("C:/Windows/prefetch"):
            for i in range(len(prefetches)):
                if prefetches[i] in file:
                    os.remove(f"C:/Windows/prefetch/{file}")
                    print(f"\nLe prefetch du programme \"{prefetches[i]}\" a été supprimé")
    except:
        print("\nErreur: Prefetches")

    # RoamingState Directory
    directories = data["cheats"]["directories"]
    try:
        for i in range(len(directories)):
            try:
                shutil.rmtree(f"C:/Users/{user}/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/RoamingState/{directories[i]}")
                print(f"Le répertoire \"{directories[i]}\" a été supprimé")
            except:
                pass
    except:
        print("Erreur: Directories")

    # Temp
    temp = data["cheats"]["temp"]
    try:
        for file in os.listdir(f"C:/Users/{user}/AppData/Local/Temp/"):
            for i in range(len(temp)):
                if temp[i] in file:
                    os.remove(f"C:/Users/{user}/AppData/Local/Temp/{file}")
                    print(f"Le fichier temporaire \"{temp[i]}\" a été supprimé")
    except:
        print("Erreur: Temp\n\n")

    # Local
    local = data["cheats"]["local"]
    try:
        for i in range(len(local)):
            try:
                shutil.rmtree(f"C:/Users/{user}/AppData/Local/{local[i]}")
                print(f"Le répertoire local \"{local[i]}\" a été supprimé")
            except:
                pass
    except:
        print("Erreur: Local")
    
    # UsageLogs
    usageLogs = data["cheats"]["usageLogs"]
    try:
        for file in os.listdir(f"C:/Users/{user}/AppData/Local/Microsoft/CLR_v4.0/UsageLogs"):
            for i in range(len(usageLogs)):
                if usageLogs[i] in file:
                    os.remove(f"C:/Users/{user}/AppData/Local/Microsoft/CLR_v4.0/UsageLogs/{file}")
                    print(f"Le log \"{usageLogs[i]}\" a été supprimé")
    except Exception as e:
        print("Erreur: usageLogs\n\n")
    
    # Logs
    logs = data["cheats"]["logs"]
    try:
        for file in os.listdir(f"C:/Users/{user}/AppData/Local/Microsoft/CLR_v4.0/UsageLogs"):
            for i in range(len(logs)):
                if logs[i] in file:
                    os.remove(f"C:/Users/{user}/AppData/Local/Microsoft/CLR_v4.0/UsageLogs/{file}")
                    print(f"Le log \"{logs[i]}\" a été supprimé")
    except Exception as e:
        print("Erreur: Logs\n\n")

    # Dossier remover
    try:
        shutil.rmtree(f"remover")
    except Exception as e:
        print("Erreur: Remover")
    
    
    os.makedirs('remover', exist_ok=True)
    try: open("remover/REMOVER", "x")
    except: pass


    # Stop
    print(f"\n {pystyle.Colors.cyan}Les traces de cheat sont maintenant supprimés{pystyle.Colors.red}")

remover()

os.system('timeout 5')
print(pystyle.Colors.reset)
