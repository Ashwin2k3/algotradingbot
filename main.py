

from nsepy import get_history
from datetime import date, datetime
import os
from tradingview_ta import TA_Handler, Interval, Exchange
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pynput.keyboard import Key,Controller
import pyautogui

keyboard= Controller()

os.system("figlet -c Python Trading Bot ")
Today = date.today()
y = Today.strftime("%Y")
m = Today.strftime("%m")
d = Today.strftime("%d")
# d = "30"

import datetime
starting_time = datetime.datetime.now()
print("current time :", starting_time)
NAME = str(input("enter the name of stock/crypto/forex: "))
SCREENER = str(input("enter the screener: "))
EXCHANGE = str(input("enter the exchange in capital: "))
CLOSETIME= str(input("at what time do want to END the trade (in - hh:mm:ss format: "))
# NAME = "ETHUSDT"
# SCREENER = "crypto"
# EXCHANGE = "BINANCE"

#last order
last_order="sell"
sold_before = False
bought_before = False
current_price = 0
take_profit = 0.0
take_loss = 0.0


#load chrome driver 
driver = webdriver.Chrome(executable_path="/Users/mrm/Downloads/chromedriver")
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.tradingview.com/")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div[3]/button[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[6]/div/span/div[1]/div/div/div/button[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span").click()
time.sleep(2)
# driver.find_element(By.ID,"email-signin__user-name-input__8fa247e6-a406-4609-ac7a-ce8cc339d4d8")
# username = driver.find_element(By.ID,"email-signin__user-name-input__8fa247e6-a406-4609-ac7a-ce8cc339d4d8")
# username.send_keys("ashwin.2k3@gmail.com")
driver.find_element(By.NAME,"username").send_keys("enter email")
driver.find_element(By.NAME,"password").send_keys("enter password")

time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div/div/div/form/div[5]/div[2]/button/span[2]").click()
time.sleep(15)



keyboard.press(Key.cmd)
time.sleep(0.5)
keyboard.press("k")
keyboard.release(Key.cmd)
keyboard.release("k")

time.sleep(1)
driver.find_element(By.NAME,"query").send_keys(f"{NAME}")
time.sleep(1)
driver.find_element(By.CLASS_NAME,"title-iQpFFgN_").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"input-nVh4c_cg").send_keys(f"{EXCHANGE}")
time.sleep(1)

# driver.find_element(By.CLASS_NAME,"textBlock-jKCUPVoO").click()
# time.sleep(2)
# driver.find_element(By.CLASS_NAME,"symbolTitle-DPHbT8fH").click()
# #driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/span/em").click()
# time.sleep(6)
# #driver.find_element(By.CLASS_NAME,"counter-ocTuaBGx").click()
time.sleep(20)

QUANITY = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[5]/div[1]/div/span/span/span[1]/input").get_attribute("value")

#initiating tradingview handler to get the recomendation for sonata software for 15 min interval
ssw = TA_Handler(
    symbol=NAME,
    screener=SCREENER,
    exchange=EXCHANGE,
    interval=Interval.INTERVAL_5_MINUTES
)
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if(current_time >= "09:30:00" and current_time < CLOSETIME):

        rec = ssw.get_analysis()
        RSI = rec.indicators["RSI"]
        MACD = rec.indicators["MACD.macd"]
        EMA = rec.moving_averages["COMPUTE"]["EMA10"]
        print("RSI:", RSI, "EMA:", EMA ,"MACD:",MACD)


        if ( RSI >= 30 and RSI <= 70 and EMA == "BUY" ):
            if (last_order=="sell"):
                print(f"Buying {QUANITY} stock of {NAME} ")
                last_order="buy"
                print(last_order)
                print(sold_before)
                #buy 1 stock of NAME 
                driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[6]/button/div/span[2]").click()
                
                current_price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[5]/span/span[1]/span[2]/span[1]/input").get_attribute("value")
                
                print(current_price)
                take_profit = float(current_price) + 8
                take_loss = float(current_price) - 5
                while True:
                    print("Time left till next call - ")
                    countdown(int(5))
                    rec = ssw.get_analysis()
                    RSI = rec.indicators["RSI"]
                    # MACD = rec.indicators["MACD.macd"]
                    EMA = rec.moving_averages["COMPUTE"]["EMA10"]
                    print("RSI:", RSI, "EMA:", EMA ,"MACD:",MACD)
                    current_price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[5]/span/span[1]/span[2]/span[1]/input").get_attribute("value")
                    if((RSI >= 30 and EMA == "SELL") or (float(current_price) >= take_profit) or (float(current_price) <= take_loss)):
                        #sell the stock
                        print(f"Selling {QUANITY} stock of {NAME} ")
                        last_order="sell"
                        print(last_order)
                        #sell 1 stock of NAME
                        
                        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[1]/div[2]/div").click()
                        time.sleep(2)
                        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[6]/button/div/span[2]").click()
                        break
                    else:
                        print("no adjustment required")
            else:
                print("last order not sold")
        elif( RSI >= 50 and EMA == "SELL" ):
            if ( last_order == "sell"):
                print(F"selling {QUANITY} stock of {NAME} ")
                driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[1]/div[2]/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[6]/button/div/span[2]").click()
                current_price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[5]/span/span[1]/span[2]/span[1]/input").get_attribute("value")
                print(current_price)
                take_profit = float(current_price) - 8
                take_loss = float(current_price) + 5
                while True:
                    print("Time left till next call - ")
                    countdown(int(5))
                    rec = ssw.get_analysis()
                    RSI = rec.indicators["RSI"]
                    # MACD = rec.indicators["MACD.macd"]
                    EMA = rec.moving_averages["COMPUTE"]["EMA10"]
                    print("RSI:", RSI, "EMA:", EMA ,"MACD:",MACD)
                    current_price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[5]/span/span[1]/span[2]/span[1]/input").get_attribute("value")
                    if((RSI <= 30 and EMA == "BUY") or ( float(current_price) <= take_profit) or (float(current_price) >= take_loss)):
                        #buy the stock
                        print(f"Buying {QUANITY} the stock {NAME}")
                        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div").click()
                        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[6]/button/div/span[2]").click()
                        break
                    else:
                        print("no adjustment required")

        else:
            print("condition not favourable..waiting")
          
    elif(current_time >= CLOSETIME):
        print("Time to close for the day")
        # #fetch open profit
        open_profit = driver.find_element(By.XPATH,"//div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]").text
        # print(open_profit)
        # P = "1000"
        print("Calculating profit :",open_profit)
        break
    else:
        if(current_time >= "09:15:00" and current_time < CLOSETIME):
            print("Analysing market","\n\n")
        elif(current_time < "9:15:00"):
            print("Waiting for market to open")
        else:
            print("No action required")
        
    
    


