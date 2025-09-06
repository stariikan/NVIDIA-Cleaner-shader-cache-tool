import os
import shutil
import subprocess
from win10toast import ToastNotifier

# Path to target folder
user_home = os.path.expanduser("~")
target = os.path.join(user_home, r"AppData\Local\NVIDIA")

toaster = ToastNotifier()

def notify(msg, title="NVIDIA Cleaner"):
    toaster.show_toast(title, msg, duration=4, threaded=True)

# Define NVIDIA processes and their restart paths
processes = {
    "nvcontainer.exe": r"C:\Program Files\NVIDIA Corporation\Display.NvContainer\NVDisplay.Container.exe",
    "nvsphelper64.exe": None,  # helper, not required to restart manually
    "nvcplui.exe": r"C:\Program Files\NVIDIA Corporation\Control Panel Client\nvcplui.exe"
}

def stop_nvidia_processes():
    for proc in processes.keys():
        try:
            subprocess.run(["taskkill", "/F", "/IM", proc], capture_output=True)
        except Exception as e:
            notify(f"Error stopping {proc}: {e}", "ERROR")

def clear_folder():
    if not os.path.exists(target):
        notify("NVIDIA folder not found.")
        return

    deleted_count = 0
    for root, dirs, files in os.walk(target, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)
                deleted_count += 1
            except Exception:
                pass  # ignore locked files
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                shutil.rmtree(dir_path)
                deleted_count += 1
            except Exception:
                pass

    notify(f"Cleanup finished. Deleted {deleted_count} items")

def restart_nvidia_processes():
    for proc, path in processes.items():
        if path and os.path.exists(path):
            try:
                subprocess.Popen([path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                notify(f"Restarted {proc}")
            except Exception as e:
                notify(f"Failed to restart {proc}: {e}", "ERROR")

if __name__ == "__main__":
    stop_nvidia_processes()
    clear_folder()
    restart_nvidia_processes()
    notify("All tasks completed")
