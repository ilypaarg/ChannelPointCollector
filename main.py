# import what we need for the screen capture
import pyautogui # use this to move the mouse location
#X = 1656 Y = 1002
from PIL import ImageGrab
import time
import os
import colorama
from colorama import Fore, Style, init

init()

#X, Y = 1656, 1002
checkX, checkY = 1658, 1007
clickX, clickY = 1658, 1007

selectedColor = (0, 219, 132)
Tolerance = 0

pyautogui.FAILSAFE = False

def is_match(color, selectedcolor, tolerance):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color, selectedcolor))

def main():
    try:
        #start_script = time.time()
        while True:

            #elapsed_time = time.time() - start_script
            #if elapsed_time > 10:
                #os.system('cls')
                #start_script = time.time()

            screenshot = ImageGrab.grab()

            pixel_color = screenshot.getpixel((checkX, checkY))
            #print(f"COLOR FOUND AT ({checkX}, {checkY}): {pixel_color}")

            if is_match(pixel_color, selectedColor, Tolerance):
                #print(f"SELECTED COLOR FOUND. CLICKING AT: ({clickX}, {clickY})")
                #pyautogui.moveTo(1656, 1002)
                pyautogui.click(clickX, clickY)
                #879, 567
                #92 255 190
            else:
                # print("SELECTED COLOR NOT FOUND")

                time.sleep(0.1)

    except KeyboardInterrupt:
        print(Fore.RED + "SCRIPT TERMINATED. ;)")


if __name__ == "__main__":
    def set_window_title(title):
        os.system(f"title {title}")

    os.system('cls')

    set_window_title("Emshot's Channel Point Collector")
    time.sleep(0.3)
    print(Fore.LIGHTMAGENTA_EX + """
\ \ \______ \ \______  /
 \ \ \  / /\ \ \  / / /
  \ \ \/ / /\ \ \/ / /
   \ \/ / /__\_\/ / /
    \  / /______\/ /
     \/___________/     EMSHOT PRODUCTIONS.
     """)
    print("\n")
    time.sleep(0.5)
    print(Fore.RED + "Press CTRL + C to terminate the script.\n")
    time.sleep(1)
    print(Fore.GREEN + "RUNNING... YOU MAY MINIMIZE THIS WINDOW.")
    main()
