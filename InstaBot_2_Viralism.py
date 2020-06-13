from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import datetime

class instabot():
    #login_id="travelling.lad"
    #password="Japan@786"
    #hash_tag="travelblogger"
    #hash_tag="foodblogger"
    
    #login_id="mayankshivhare"
    #password="Shivhare@786"
    #hash_tag="beard"
    
    #login_id="Viralism1"
    #password="Viral@786"
    #hash_tag="meme"
    
    def __init__(self):
        self.driver=webdriver.Firefox()
        
    def login(self):
        try:
            print("Loading Instagram")
            self.driver.get("https://instagram.com")
            sleep(10)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys("Viralism1")
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys("Viral@786")
            sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click() #Login Button
            sleep(10)

            try:
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click() #Save Login info Not Now
                sleep(3)
            except:
                 print("EXCEPTION : in Save Login info")

            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click() #not now notification
            sleep(3)
        except:
            print("EXCEPTION : in logging")
                

    def like_feeds(self):
        print("------------ENTERING like_feeds Loop------------")
        try:
            print("Refresh Page")
            self.driver.get("https://instagram.com")
            sleep(5)
            i=1
            scrolltoy=500
            #self.driver.execute_script("window.scrollTo(0, 500)")
            while(i<=30):
                try:
                    scrolltoy=scrolltoy+1000
                    sleep(random.randint(1,7))
                    print("Scroll")
                    self.driver.execute_script("window.scrollTo(0,{})".format(scrolltoy))
                    sleep(random.randint(1,7))
                    print("Click on like")
                    self.driver.find_element_by_class_name("_8-yf5 ").click()
                    print("Image Liked")
                    sleep(random.randint(1,7))
                    i=i+1
                except:
                    print("EXCEPTION : in liking image")
                    i=i+1
        except:
                    print("EXCEPTION : in like_feeds")

    def watch_stories(self):
        print("------------watch_stories Loop------------")
        try:
            print("Refresh Page")
            self.driver.get("https://instagram.com")
            sleep(5)
            #watch story of 5th person
            try:
                print("Click on 5th story")
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[7]/div/button").click()
                sleep(5)
            except:
                print("Could not Click on stories from top")
                try:
                    print("Clicking stories from left")
                    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/button").click()
                    sleep(5)
                except:
                    print("Could not Click on stories from right section too")

            #Click next on stories
            random_no_stories=random.randint(50,100)
            for x in range(random_no_stories):
                try:
                    print("Click on next Story")
                    self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div/section/div[2]/button[2]").send_keys(Keys.RIGHT)
                    sleep(random.randint(2,5))
                except:
                    print("EXCEPTION : in Clicking right in stories")
        except:
            print("EXCEPTION : in watch_stories")
            

    def intraction_from_feed(self):
        like_counter=0
        print("------------intraction_from_feed Loop------------")
        try:
            print("Refresh Page")
            self.driver.get("https://instagram.com")
            sleep(5)
            #select 1st user from feed
            print("Selection 1st story from the feed")
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[1]/header/div[2]/div[1]/div/a").click()
            sleep(3)
            #select 1st feed
            print("Selecting user 1 feed")
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]").click()
            sleep(2)
            random_no_feeds=random.randint(10,15)
            for x in range(random_no_feeds):
                try:
                    #Click on  like
                    print("Clicking on image")
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                    print("Image Liked")
                    sleep(random.randint(1,3))
                    #Click Next
                    #self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
                    print("Click right")
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").send_keys(Keys.RIGHT)
                    sleep(random.randint(1,3))
                    return like

                except:
                    print("EXCEPTION : in Clicking right in intraction_from_feed")
        except:
            print("EXCEPTION : in intraction_from_feed")
        sleep(random.randint(12,16))


    def like_popular_feeds(self):
        print("------------like_popular_feeds Loop------------")
        try:
            #search tag
            print("Load hashtag page")
            #print(hash_tag)
            self.driver.get("https://www.instagram.com/explore/tags/meme")
            sleep(5)
            #scroll down to most recent
            print("Scroll")
            self.driver.execute_script("window.scrollTo(0, 1000)")
            sleep(3)
            #open 1st feed
            print("Click on the feed")
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]").click()
            sleep(3)
            random_no_feeds=random.randint(15,20)
            for x in range(random_no_feeds):
                try:
                    #like
                    print("Click on Like Button")
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                    print("Image Liked")
                    sleep(random.randint(1,3))
                    #next
                    print("Click on right button")
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").send_keys(Keys.RIGHT)
                    sleep(random.randint(1,3))
                except:
                    print("EXCEPTION : in Clicking right in like_popular_feeds")
        except:
            print("EXCEPTION : in like_popular_feeds")

    def interaction_with_popular_feeds(self):
        print("------------interaction_with_popular_feeds Loop------------")
        try:
            #search tag
            print("Loading hashtag page")
            #print(hash_tag)
            self.driver.get("https://www.instagram.com/explore/tags/meme")
            sleep(5)
            #scroll down to most recent
            print("Scroll ")
            self.driver.execute_script("window.scrollTo(0, 1000)")
            sleep(3)
            #open 1st recent feed
            print("Click on 1st recent feed")
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]").click()
            sleep(3)
            #open user from popup feed
            print("Clicking on username")
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a").click()
            sleep(3)
            #open 1st feed(reused)
            print("Clicking on user feed")
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]").click()
            sleep(3)
            random_no_feeds=random.randint(10,15)
            for x in range(random_no_feeds):
                try:
                    #like
                    print("Clicking on like button")
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                    print("Image Liked")
                    sleep(random.randint(1,3))
                    #next(reuse-popup)
                    print("Clicking on right button")
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").send_keys(Keys.RIGHT)
                    sleep(random.randint(1,3))
                except:
                    print("EXCEPTION : in Clicking right in like_popular_feeds")
        except:
            print("EXCEPTION : in interaction_with_popular_feeds")

        sleep(random.randint(12,16))

    def comment_feeds(self):
        print("------------ENTERING comment_feeds Loop------------")
        try:
            print("Refresh Page")
            self.driver.get("https://instagram.com")
            sleep(5)
            i=1
            scrolltoy=500
            try:
                sleep(random.randint(1,7))
                print("Scroll")
                self.driver.execute_script("window.scrollTo(0,{})".format(scrolltoy))
                sleep(2)
                print("Click on comment button")
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[1]/div[2]/section[1]/span[2]/button").click()
                sleep(5)
                self.driver.execute_script("window.scrollTo(0,{})".format(scrolltoy))
                print("Click on comment line")
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea").click()
                sleep(1)
                print("Writing Comment")
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea").send_keys("WOW 😍")
                sleep(1)
                print("Hitting Post Button")
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/button").click()
            except:
                 print("EXCEPTION : in comment_feeds")                 
        except:
            print("EXCEPTION : in comment_feeds")

    def comment_popular_feeds(self):
        print("------------ENTERING comment_popular_feeds Loop------------")
        try:
            #search tag
            print("Loading hashtag page")
            #print(hash_tag)
            self.driver.get("https://www.instagram.com/explore/tags/meme")
            sleep(5)
            #scroll down to most recent
            print("Scroll ")
            self.driver.execute_script("window.scrollTo(0, 1000)")
            sleep(3)
            #open 1st recent feed
            print("Click on 1st recent feed")
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]").click()
            sleep(3)
            try:
                print("Click on comment line")
                self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea").click()
                sleep(1)
                print("Writing Comment")
                self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea").send_keys("WOW 😍")
                sleep(1)
                print("Hitting Post Button")
                self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button").click()
            except:
                 print("EXCEPTION : in comment_popular_feeds")
        except:
            print("EXCEPTION : in comment_popular_feeds")    

        sleep(random.randint(12,16))
                
        

current_time = datetime.datetime.now()
print(current_time)
                     
'''
bot=instabot()
bot.login()
sleep(5)


for _ in range(5):

    for _ in range(4):
    	int(live_counter)=bot.intraction_from_feed() #10 Likes * 3 = 30
    	print(type(live_counter))
    	final_counter=final_counter+live_counter
    print("Total Likes %i" % final_counter)
    sleep(300)
    bot.watch_stories() #watch few stories 200-400
    sleep(300)


    for _ in range(4):
        bot.interaction_with_popular_feeds() #10 Likes * 3 =30
    sleep(300)
    bot.watch_stories() #watch few stories 200-400
    sleep(300)


    bot.like_feeds() #20 Likes
    sleep(300)
    bot.watch_stories() #watch few stories 200-400
    sleep(300)


    bot.like_popular_feeds() #20 Likes
    sleep(300)
    bot.watch_stories() #watch few stories 200-400
    sleep(300)

    current_time = datetime.datetime.now()
    print(current_time)
    
# one loop = 100 likes

'''
