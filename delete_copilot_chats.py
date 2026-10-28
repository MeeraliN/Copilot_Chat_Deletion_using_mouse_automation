import pyautogui
import time
import sys

pyautogui.FAILSAFE = True
MOVE_SPEED = 0.7

# --- PASTE YOUR 4 COORDINATES HERE ---

COORD_CHAT_HOVER  = (219, 398)   # Update with your recorded values
COORD_THREE_DOTS  = (219, 398)
COORD_MENU_DELETE = (270, 500)
COORD_CONFIRM_DEL = (950, 500)

# ------------------------------------

def execute_deletion_cycle():
    # 1. Hover to reveal '...'
    pyautogui.moveTo(*COORD_CHAT_HOVER, duration=MOVE_SPEED)
    time.sleep(0.4)

    # 2. Click three dots
    pyautogui.moveTo(*COORD_THREE_DOTS, duration=MOVE_SPEED)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1.0)

    # 3. First Delete (dropdown)
    pyautogui.moveTo(*COORD_MENU_DELETE, duration=MOVE_SPEED)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1.2)

    # 4. Second Delete (confirmation modal)
    pyautogui.moveTo(*COORD_CONFIRM_DEL, duration=MOVE_SPEED)
    time.sleep(0.2)
    pyautogui.click()

    # 5. Wait 6 seconds before restarting
    print("\nSecond delete completed. Waiting 6 seconds before restarting...")
    for remaining in range(6, 0, -1):
        print(f"Next chat deletion in {remaining}s...", end="\r", flush=True)
        time.sleep(1.0)
    print("\nRestarting cycle now...")

def main():
    print("Starting in 5 seconds. Focus your Microsoft Copilot browser window...")
    time.sleep(5)

    iteration = 1
    while True:
        print(f"\n--- Processing Chat #{iteration} ---")
        try:
            execute_deletion_cycle()
            iteration += 1
        except KeyboardInterrupt:
            print("\nStopped by user.")
            sys.exit()

if __name__ == "__main__":
    main()
