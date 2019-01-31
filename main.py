import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib import request
class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome('/Users/marco/Desktop/EdgardLeNotre/chromedriver')
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        # print('CAAAAAAA', self.browser.find_elements_by_css_selector('input'))
        emailInput = self.browser.find_elements_by_css_selector('input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def search(self):
        #searchInput = self.browser.find_elements_by_class_name('XTCLo x3qfX')
        searchInput = self.browser.find_elements_by_css_selector('input')[3]
        searchInput.send_keys('Alinity')
        # searchInput.send_keys(Keys.ENTER)
    
    def deprecatedSaveImages(self, hashTag,nb_img):
        link = self.browser.get('https://www.instagram.com/explore/tags/' + hashTag + '/')
        #postLink = self.browser.find_element_by_css_selector("article a")
        #postLink.click()
        for i in range(nb_img):
            time.sleep(1)
            img_src = self.browser.find_elements_by_css_selector("article img")[i].get_attribute("src")
            print(img_src)
            time.sleep(1)
            request.urlretrieve(img_src, 'img/' + str(i) + '.png')
            time.sleep(2)
            
    def saveImages(self, hashTag, nb_img):
        link = self.browser.get('https://www.instagram.com/explore/tags/' + hashTag + '/')
        elm = self.browser.find_element_by_tag_name("html")
        img_src = []
        i=0
        while (len(img_src) <= nb_img):
            img = self.browser.find_elements_by_css_selector("article img")
            for u in img:
                img_src.append(u.get_attribute('src'))
            elm.send_keys(Keys.END)
            time.sleep(0.5)
            img_src = list(set(img_src))
            print(len(img_src))
        for url in img_src:
            request.urlretrieve(url, 'img/' + str(i) + '.png')
            time.sleep(1)
            i = i + 1



    def followUser(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Abonné(e)'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")
    
    def followFollowers(self):
        followerLink = self.browser.find_element_by_css_selector("a[href*='followers']")
        followerLink.click()
        time.sleep(3)
        for i in range(1000):
            followButton = self.browser.find_elements_by_css_selector("button[type=button]")[i]
            if (followButton.text != 'Abonné(e)' and followButton.text != 'Demandé'):
                followButton.click()
                time.sleep(30)
            else:
                print("You are already following this user")
                
    def hashTagFollow(self, hashTag):
        linkF4F = self.browser.get('https://www.instagram.com/explore/tags/' + hashTag + '/')
        time.sleep(1)
        postLink = self.browser.find_element_by_css_selector("article a")
        postLink.click()
        time.sleep(1)
        while True:
            try:
                heartLink = self.browser.find_element_by_css_selector("span[aria-label*='aime']")
                heartLink.click()
                followLink = self.browser.find_elements_by_css_selector("button[type=button]")[1]
                if (followLink.text != 'Abonné(e)' and followLink.text != 'Demandé'):
                    followLink.click()
                    time.sleep(1)
                else:
                    print("You are already following this user")
                time.sleep(30)
            except NoSuchElementException:
                print("Pas de panique")
            nextLink = self.browser.find_element_by_xpath("//*[contains(text(), 'Suivant')]")
            nextLink.click()


bot = InstagramBot('billabong33@gmail.com', 'nico06')
bot.signIn()
time.sleep(0.5)
bot.saveImages('vegansandwich', 100)


