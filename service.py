import cv2
from datetime import datetime
import time
import keyboard
import pyautogui
import mouse
import os
import numpy as np
from tkinter import simpledialog
from configparser import ConfigParser
import configparser
import threading
import winsound
from tkinter import messagebox
from multiprocessing import Process

global Save_list
Save_list = []

def camHook():
    global webcam
    global index
    webcam = cv2.VideoCapture(index)
    webcam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    frq=500
    for i in range (0,3):
        winsound.Beep(frq, 100)
        frq+=500


def screenshot():  
    global webcam
    global Path
    global index
    global TRFPath
    height= 1080
    width = 1440           
    dim = (width, height)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, img1 = webcam.read()
        now = datetime.now()
        global monthstamp, datestamp
        monthstamp = now.strftime("%b (%Y)")
        datestamp = now.strftime("%m.%d")
        if not os.path.exists(rf'{Path}\{monthstamp}\{datestamp}'):
                    os.makedirs(rf'{Path}\{monthstamp}\{datestamp}')
        if keyboard.is_pressed('enter'):
            try:
                # # now = datetime.now()
                # # monthstamp = now.strftime("%b (%Y)")
                # # datestamp = now.strftime("%m.%d")
                # timestamp = now.strftime("%I.%M.%S %p")
                # Screenshot = pyautogui.screenshot()
                # img2 = cv2.cvtColor(np.array(Screenshot), cv2.COLOR_RGB2BGR)
                # ret, img1 = webcam.read()
                # img1r = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                # h_img = cv2.hconcat([img1r, img2])
                # # if not os.path.exists(rf'{Path}\{monthstamp}\{datestamp}'):
                # #     os.makedirs(rf'{Path}\{monthstamp}\{datestamp}')
                # cv2.imwrite(rf'{Path}\{monthstamp}\{datestamp}\{timestamp}.jpg', h_img, [cv2.IMWRITE_JPEG_QUALITY, 50])
                global timestamp, textstamp
                timestamp = now.strftime("%I.%M.%S %p")
                textstamp = now.strftime("%m/%d/%Y  %H:%M:%S")
                capture_click(ret,img1)
                screenshot()
            except:
                screenshot()
        elif mouse.is_pressed(button='left'):
            try:
                # # now = datetime.now()
                # # monthstamp = now.strftime("%b (%Y)")
                # # datestamp = now.strftime("%m.%d")
                # timestamp = now.strftime("%I.%M.%S %p")
                # ret, img1 = webcam.read()
                # if ret:
                #     Screenshot = pyautogui.screenshot()
                #     img2 = cv2.cvtColor(np.array(Screenshot), cv2.COLOR_RGB2BGR)
                #     img1 = cv2.putText(img1, now.strftime("%m/%d/%Y  %H:%M:%S"),(5, 470), font, 1, (0,255,0), 2, cv2.LINE_8)
                #     img1r = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                #     h_img = cv2.hconcat([img1r, img2])
                #     # if not os.path.exists(rf'{Path}\{monthstamp}\{datestamp}'):
                #     #     os.makedirs(rf'{Path}\{monthstamp}\{datestamp}')
                #     cv2.imwrite(rf'{Path}\{monthstamp}\{datestamp}\{timestamp}.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 50])
                timestamp = now.strftime("%I.%M.%S %p")
                textstamp = now.strftime("%m/%d/%Y  %H:%M:%S")
                capture_click(ret,img1)
                time.sleep(0.1)
                screenshot()
            except:
                screenshot()
        elif keyboard.is_pressed('F2+F12'):
            webcam.release()
            parser = ConfigParser()
            parser.read(r'info\config.ini')
            parser.set('Path', 'Path', Path)
            parser.set('TRFPath', 'TRFPath', TRFPath)
            parser.set('index', 'index', str(index))
            with open(r'info\config.ini', 'w') as configfile:
                parser.write(configfile) 
            frq=1500
            for i in range (0,3):
                winsound.Beep(frq, 100)
                frq-=500
            os._exit(0)
            
        elif keyboard.is_pressed('F9'):
            Path = simpledialog.askstring("Input Folder Path", r'Folder Path (do not include trailing "\"):', initialvalue=f'{Path}')
            if not os.path.exists(rf'{Path}'):
                os.makedirs(rf'{Path}')
            screenshot()
        elif keyboard.is_pressed('F10'):
            TRFPath = simpledialog.askstring("Input Folder Path", r'Folder Path (do not include trailing "\"):', initialvalue=f'{TRFPath}')
            if not os.path.exists(rf'{TRFPath}'):
                messagebox.showwarning('Path does not exist', 'Press the F10 key and type in a valid directory path')
            screenshot()
        elif keyboard.is_pressed('F8'):
            index = simpledialog.askinteger( "Webcam index Value", 'Input index value (0 or 1, defualt value = 0):', initialvalue=f'{index}')
            if index >1 or index <0:
                index = 0
            webcam.release()
            camHook()
            screenshot()
        elif keyboard.is_pressed('F7'):
            print("Saving")
            for i,t in enumerate(Save_list):
                    monthstamp, datestamp, timestamp, h_img=t
                    cv2.imwrite(rf'{Path}\{monthstamp}\{datestamp}\{timestamp}.jpg', h_img, [cv2.IMWRITE_JPEG_QUALITY, 50])
            
            # frq=500
            # for i in range (0,3):
            #     winsound.Beep(frq, 100)
            #     frq+=500
            # time.sleep(1)
            screenshot()
        
        

def capture_click(ret,img1):
    start = time.time()
    height= 1080
    width = 1440           
    dim = (width, height)
    # now = datetime.now()
    # monthstamp = now.strftime("%b (%Y)")
    # datestamp = now.strftime("%m.%d")
    # timestamp = now.strftime("%I.%M.%S %p")
    # ret, img1 = webcam.read()
    if ret:
        Screenshot = pyautogui.screenshot()
        img2 = cv2.cvtColor(np.array(Screenshot), cv2.COLOR_RGB2BGR)
        img1 = cv2.putText(img1, textstamp,(5, 470), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_8)
        img1r = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
        h_img = cv2.hconcat([img1r, img2])
    # Save_list.append((monthstamp, datestamp, timestamp,img1))
        cv2.imwrite(rf'{Path}\{monthstamp}\{datestamp}\{timestamp}.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 50])
    end = time.time()
    print(end - start)
        # cv2.imwrite(rf'{Path}\{monthstamp}\{datestamp}\{timestamp}.jpg', h_img, [cv2.IMWRITE_JPEG_QUALITY, 50])



def save():
    try:
        for i,t in enumerate(Save_list):
            monthstamp, datestamp, timestamp, h_img=t
            cv2.imwrite(rf'{Path}\{monthstamp}\{datestamp}\{timestamp}.jpg', h_img, [cv2.IMWRITE_JPEG_QUALITY, 50])
        save()
    except:
        save()



def config():
    try:
        global Path
        global index
        global TRFPath
        parser = ConfigParser()
        parser.read(r'info\config.ini')
        Path = parser.get('Path', 'Path')
        index = int(parser.get('index', 'index'))
        TRFPath = parser.get('TRFPath', 'TRFPath')
        return Path, index, TRFPath
    except:
        if not os.path.exists('info'):
            os.makedirs('info')
            os.makedirs(r'info\data')

            config_file = configparser.ConfigParser()
            config_file["Path"]={"Path": r"info\data"}
            config_file["index"]={"index":"0",}
            config_file["TRFPath"]={"TRFPath": r"info\data"}
           
            with open(r"info\config.ini","w") as file_object:
                config_file.write(file_object)
            config()
        else:
            if not os.path.exists(r'info\data'):
                os.makedirs(r'info\data')
                config_file = configparser.ConfigParser()
        
                config_file = configparser.ConfigParser()
                config_file["Path"]={"Path": r"info\data"}
                config_file["index"]={"index":"0",}
                config_file["TRFPath"]={"TRFPath": r"info\data"}
                
                with open(r"info\config.ini","w") as file_object:
                    config_file.write(file_object)
                config()



def start_thread_Main():
    start_thread=threading.Thread(target=screenshot)
    start_thread.start()


# def start_thread_capture():
#     now = datetime.now()
#     monthstamp = now.strftime("%b (%Y)")
#     datestamp = now.strftime("%m.%d")
#     timestamp = now.strftime("%I.%M.%S %p")
#     textstamp = now.strftime("%m/%d/%Y  %H:%M:%S")
#     start_thread=threading.Thread(target=capture_click, args=(monthstamp, datestamp, timestamp, textstamp))
#     start_thread.start()


def start_thread_save():
    start_thread=threading.Thread(target=save)
    start_thread.start()

def start_thread_camhook():
    start_thread=threading.Thread(target=camHook())
    start_thread.start()   

config()
start_thread_camhook()        
          
# start_thread_Main()
screenshot()
# start_thread_save()








