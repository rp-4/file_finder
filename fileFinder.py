import pyautogui
import time
import os

st = time.time()
#############################################

def main():
    fileName = str(input("Enter any file name: ").strip())
    rootDir = searchFile(fileName)
    try:
        os.startfile(rootDir)  #--open directory which has the file with asked name
    except TypeError:
        print("Dir not found")

def searchFile(file):
    path =r'path of main directory'  #<===== change this 
    for root, dirs, files in os.walk(path):
        for name in files:  #--look for asked name in files
            if name.find(file) >= 0:
                print(root)
                return root
        for directory in dirs:   #--look for asked name in directory name
            if directory.find(file) >= 0:
                print(root)
                return root

main()

#############################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
