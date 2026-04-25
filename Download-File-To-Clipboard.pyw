import os
import glob
import subprocess
import keyboard

def copy_latest_download():
    download_path = r"C:\Users\Blake\Downloads\*"
    
    list_of_files = glob.glob(download_path)
    
    latest_file = max(list_of_files, key=os.path.getctime)
    
    command = f'Set-Clipboard -Path "{latest_file}"'
    
    subprocess.run(["powershell", "-command", command], shell=True)
    
    print(f"Ready to paste: {latest_file}")

keyboard.add_hotkey('ctrl+shift+v', copy_latest_download)

keyboard.wait()