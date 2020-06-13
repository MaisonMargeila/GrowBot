from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random


def login():
    while True:
        try:
            driver.get("https://instagram.com")
            sleep(5)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").click()
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys("travelling.lad")
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").click()
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys("Japan@786")
            sleep(3)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click() #Login Button
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//button[text()="Not Now"]').click() #not now notification
            sleep(3)
        except:
            print("Exception in logging")
            continue
        break
        

def follow_Suggested():
    try :
        driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button").click()
        sleep(random.randint(0,3))
        driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button").click()
        sleep(random.randint(0,3))
        driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button").click()
        sleep(random.randint(0,3))
        driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[4]/div[3]/button").click()
        sleep(random.randint(0,3))
        driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[5]/div[3]/button]").click()
        sleep(random.randint(0,3))
    except:
        print("Error Was occured")

def like_feeds():
    i=0
    scrollto=500
    driver.execute_script("window.scrollTo(0, 500)")
    while(i<=20):
        try:
            scrollto=scrollto+1000
            driver.execute_script("window.scrollTo(0,{})".format(scrollto))
            sleep(1)
            feed1=driver.find_element_by_class_name("_8-yf5 ")
            feed1.click()
            print("Image Liked")
            sleep(random.randint(0,5))
            i=i+1
        except:
            print("Exception")
            i=i+1

def View_Stories():
    driver.execute_script("window.scrollTo(0, 0)")
    i=0
    while(i<=5):
        try:
            driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[4]/div/button").click()
            sleep(180)
            i=i+1
        except:
            print("Exception in Stories")
            driver.get("https://instagram.com")
            sleep(3)
            i=i+1
   
        

#def feed_intraction():
   # try:
        

if __name__=="__main__":
    driver=webdriver.Firefox()
    driver.implicitly_wait(2)
    login()
    for x in range(15):
        driver.get("https://instagram.com")
        sleep(5)
        like_feeds() ### 10-20 likes
        print("Sleeping For 20-30 mins & Loop is {}".format(x))
        sleep(random.randint(1200,1800))
        

