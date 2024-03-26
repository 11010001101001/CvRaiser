# Headhunter.ru FREE cv_raiser 🐱‍🏍
Multi-threaded OCR text recognition clicker for free cv raising on hh.ru 

## 💅 Quick launch:

0) install python and pip

1) install tesseract: 
- On Linux: sudo apt-get update; sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
- On Mac: brew install tesseract. Also for /rus/ u need to download rus trained data https://github.com/tesseract-ocr/tessdata/blob/main/rus.traineddata and add it to TESSDATA dir  
- On Windows: download binary from https://github.com/UB-Mannheim/tesseract/wiki. Then add path to tesseract.exe to config.py to TESSERACT_PATH
- Then you should install python package using pip: pip install pytesseract

2) enter your CV_LINK, RAISE_WORD and MSG_DELAY in config.py:
- CV_LINK - your cv link
- RAISE_WORD - word with raise cv href link to tap
- MSG_DELAY - message delay in seconds, for example 3600 = 1 hour

3) double click launcher.exe for Windows (as administrator), others - run sh launcher.sh in terminal
   
4) program will try to raise your cv every 4 hours with default settings, you will hear 'execution sounds', just have some seconds rest please while executing. To stop program close cmd.

## ☕️
- **TON**: UQCQclFDQnQkHI4bJETisvn4QAZevjMWx5mjC3AErZaXvhlU
- **USDT**: TSiRAGH2apuygsgYP7Q9mS48WN4gDS6D5o
- **BTC**: 1HCZ7KsmVoiDrvPpnZ5jLQPp7mi7xWR7fi
