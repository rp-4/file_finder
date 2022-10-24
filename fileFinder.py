import pyautogui
import time
import os

st = time.time()
#############################################

def main():
    path =  str(input("Enter path: ").strip())
    fileName = str(input("Enter any file name: ").strip())
    rootDir = searchFile(fileName, path)
    try:
        os.startfile(rootDir)
    except TypeError:
        print("Dir not found")

def searchFile(file, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.find(file) >= 0:
                print(root)
                return root
        for directory in dirs:
            if directory.find(file) >= 0:
                print(root)
                return root

main()

#############################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
