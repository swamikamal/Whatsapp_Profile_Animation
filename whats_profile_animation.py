from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *
bot=webdriver.Firefox()
bot.get('https://web.whatsapp.com/')
time.sleep(6)
pyautogui.moveTo(73, 150, 2)
pyautogui.click()
def whatsup():
        mint=int(input("ENTER THE Minutes : "))
        mint=mint*2
        pyautogui.moveTo(520, 850)
        pyautogui.click()
        pyautogui.moveTo(300, 450,2)
        pyautogui.click()
        pyautogui.moveTo(350, 600)
        pyautogui.click()
        pyautogui.moveTo(500, 200,2)
        pyautogui.click(clicks=2)
        for i in range(mint):
                l=["0.png","1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png","12.png","13.png","14.png","15.png","16.png","17.png","18.png","19.png","20.png","21.png","22.png","23.png","24.png","25.png","26.png","27.png","28.png","29.png"]
                for i in l:
                        pyautogui.moveTo(300, 450)
                        pyautogui.click()
                        pyautogui.moveTo(350, 600)
                        pyautogui.click()
                        pyautogui.moveTo(350, 560)
                        pyautogui.typewrite((i))
                        pyautogui.press('enter')
                        pyautogui.moveTo(1050, 750)
                        pyautogui.click()

while True:
        y=input("WANT TO CONTINUE Then Press Y : ")
        if y=="y":
                whatsup()
        else :print("SEE YOU Later")
        if y=="n":
                break;










