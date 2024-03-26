#!/bin/sh
echo "\nChecking files...\n"
pip3 install keyboard
pip3 install pytesseract
pip3 install pyautogui
pip3 install playsound==1.2.2
echo "\nDone! Now running...\n"
python3 raiser.py
