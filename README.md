# NVIDIA Shader Cache Cleaner
Kills NVIDIA background tasks → Cleans the NVIDIA cache folder → Restarts the tasks → Notifies you of progress.


How it works:
1. Stops NVIDIA processes

2. Kills certain NVIDIA background processes (nvcontainer.exe, nvcplui.exe, etc.) that may lock files in
C:\Users\<CurrentUser>\AppData\Local\NVIDIA.

3. Clean the NVIDIA cache folder

4. Deletes all files and subfolders inside C:\Users\<CurrentUser>\AppData\Local\NVIDIA.

5. If a file is still locked, it skips it without crashing.

6. Shows a Windows notification when cleanup is complete.

7. Restarts NVIDIA processes

8. After cleanup, it automatically launches back key NVIDIA processes (like nvcontainer.exe and the Control Panel client).
This ensures NVIDIA continues working normally without requiring a PC reboot.

9. Sends notifications

You’ll see toast notifications for:

- Processes stopped

- Cleanup finished

- Processes restarted

Requirements:

- Python installed (or convert to .exe for standalone use).
- Python libraries: win10toast.
