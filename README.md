# Microsoft 365 Copilot Chat Deletion using Mouse Automation

A beginner-friendly Python script that automatically deletes your chats on [Microsoft 365 Copilot Chat](https://m365.cloud.microsoft/chat) one by one using human-like mouse movements and clicks.

---

## What This Script Does

Microsoft 365 Copilot ([https://m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)) does not always provide a one-click "Delete All Chats" button. Deleting dozens or hundreds of chats manually can be repetitive and time-consuming.

When you run `delete_copilot_chats.py`, the script acts just like a human user and repeats the following cycle continuously:

1. **Hover over a chat** in the sidebar list to reveal the `...` (more options) button.
2. **Click the `...` (three dots) icon** on that chat item.
3. **Click `Delete`** from the dropdown menu.
4. **Click `Delete`** on the confirmation popup modal.
5. **Wait 6 seconds** (with a live countdown in the terminal) for the chat list to update before moving on to the next chat.

---

## Required Python Imports (Beginner Guide)

The script uses three Python modules at the top of the file:

```python
import pyautogui
import time
import sys
```

| Import | Type | Needs `pip install`? | Purpose in This Script |
| :--- | :--- | :--- | :--- |
| **`pyautogui`** | Third-party package | **Yes** (`pip install pyautogui`) | Moves the mouse cursor smoothly across the screen (`moveTo`) and performs mouse clicks (`click`). |
| **`time`** | Built-in Python library | **No** (comes with Python) | Pauses execution (`time.sleep`) between clicks so the browser UI has time to open menus and confirmation dialogs. |
| **`sys`** | Built-in Python library | **No** (comes with Python) | Cleanly exits the program (`sys.exit()`) when you stop the script with `Ctrl + C`. |

---

## Prerequisites & Installation

### 1. Install Python
Make sure you have **Python 3.7 or newer** installed on your computer.
- Download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
- **Important (Windows users):** Check the box **"Add Python to PATH"** during installation.

Verify Python is installed by running this in your terminal (Command Prompt / PowerShell / Terminal):
```bash
python --version
```

### 2. Install `pyautogui`
Install the required external package using `pip`:

```bash
pip install pyautogui
```

*(Alternatively, you can run `pip install -r requirements.txt` from this repository folder.)*

---

## How to Configure Screen Coordinates

Because screen resolutions, window sizes, and browser zoom levels vary from computer to computer, you may need to update the 4 `(X, Y)` screen coordinates in `delete_copilot_chats.py`:

```python
# --- PASTE YOUR 4 COORDINATES HERE ---

COORD_CHAT_HOVER  = (219, 398)   # 1. Where the top chat item sits in the sidebar
COORD_THREE_DOTS  = (219, 398)   # 2. The '...' button that appears on hover
COORD_MENU_DELETE = (270, 500)   # 3. The 'Delete' option in the dropdown menu
COORD_CONFIRM_DEL = (950, 500)   # 4. The 'Delete' button in the confirmation modal
```

### How to Find Your Coordinates Easily
Open a terminal, run the following command, and move your mouse to the target button within 4 seconds:

```bash
python -c "import pyautogui, time; print('Move mouse to target...'); time.sleep(4); print(pyautogui.position())"
```

Repeat this for each of the 4 positions and update the `(X, Y)` numbers in `delete_copilot_chats.py`.

---

## How to Execute the Script

1. Open your browser and go to **[https://m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)**.
2. Sign in and make sure the **Chat History / Recent Chats sidebar** is open and visible on your screen.
3. Open a terminal (Command Prompt, PowerShell, or VS Code Terminal) in this repository folder.
4. Run the script:
   ```bash
   python delete_copilot_chats.py
   ```
5. You will see:
   ```text
   Starting in 5 seconds. Focus your Microsoft Copilot browser window...
   ```
6. **Quickly click/focus your browser window** showing Microsoft 365 Copilot Chat before the 5 seconds are up, then let go of your mouse.
7. The script will now automatically delete your chats one by one!

---

## How to Stop the Script

You can stop the automation at any time using either method:

- **Emergency Fail-Safe (Fastest):** Quickly slam/move your mouse cursor to **any of the 4 corners of your screen** (e.g., top-left `(0, 0)`). Since `pyautogui.FAILSAFE = True` is enabled, PyAutoGUI will immediately abort the script.
- **Keyboard Interrupt:** Switch to the terminal window and press **`Ctrl + C`**.
