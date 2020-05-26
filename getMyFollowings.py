from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from urllib.parse import urlparse

class Instagram:
    def __init__(self,username,password):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

    def getMyFollowings(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(4)
        myFollowingsLink = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(4)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        myFollowingsCount = len(dialog.find_elements_by_css_selector("li"))

        action = webdriver.ActionChains(self.browser)

        dialog.click()

        while True:
            action.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(1)
            action.key_down(Keys.HOME).key_up(Keys.HOME).perform()
            time.sleep(1)
            action.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(1)
            action.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(1)
            action.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(1)
            action.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(5)
            newCount = len(dialog.find_elements_by_css_selector("li"))

            if myFollowingsCount == newCount:
                break
            else:
                myFollowingsCount = newCount
                time.sleep(1)
                dialog.click()
                time.sleep(1)
        myFollowings = dialog.find_elements_by_css_selector("li")

        with open("myFollowings.txt","w",encoding="UTF-8") as file:
            for user in myFollowings:
                link = urlparse(user.find_element_by_css_selector("a").get_attribute("href"))
                parsedLink = link[2]
                cutSlashes = parsedLink[1:-1]
                file.write(cutSlashes + "\n")

        print(f"Takip Ettiğiniz: {myFollowingsCount}")