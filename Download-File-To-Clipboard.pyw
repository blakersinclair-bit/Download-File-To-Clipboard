import os
import glob
import subprocess
import keyboard
import threading

def copy_latest_download():
    download_path = r"C:\Users\Blake\Downloads\*"
    list_of_files = glob.glob(download_path)
    
    if not list_of_files:
        print("Downloads folder is empty.")
        return
        
    latest_file = max(list_of_files, key=os.path.getctime)
    command = f'Set-Clipboard -Path "{latest_file}"'
    
    def run_powershell():
        subprocess.run(["powershell", "-command", command], shell=True)
        
    threading.Thread(target=run_powershell).start()
    
    print(f"Ready to paste: {latest_file}")

keyboard.add_hotkey('ctrl+shift+v', copy_latest_download)
keyboard.wait()