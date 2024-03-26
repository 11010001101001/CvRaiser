#include <stdlib.h>
#include <stdio.h>

FILE *python_version;

int main(void)
{
    python_version = popen("python -V", "r");

    if (python_version == NULL)
        printf("Please install python first");
    else
    {
        printf("\nChecking files...\n");
        system("pip install keyboard");
        system("pip install pytesseract");
        system("pip install pyautogui");
        system("pip install playsound==1.2.2");
        printf("\nDone! Now running...\n");
        system("python raiser.py");
    }

    pclose(python_version);

    return 0;
}