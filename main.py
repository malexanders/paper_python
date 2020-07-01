# os for file management
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set download directory Chrome
options = webdriver.ChromeOptions()
options.add_argument("download.default_directory=/Users/Matt.Smith/Downloads/dropbox_paper")
prefs = {"download.default_directory" : "/Users/Matt.Smith/Downloads/dropbox_paper"}
options.add_experimental_option("prefs", prefs)

# Get list of dropbox paper.url files
paper_dir = '/Users/Matt.Smith/Downloads/dropbox_paper/Universe/'
file_list = list(os.listdir(paper_dir))

# Intialize webdriver
chrome_path = 'open -a Google\ Chrome'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(30)

for i, file in enumerate(file_list):
    f = open(paper_dir + file, "r")

    for line in f.readlines():
        if "URL" in line:
            url = line.split("URL=")[1].replace('\n','')
            driver.get(url)

            # Login in on first iteration only
            if i == 0:
                driver.find_element_by_xpath('//*[@id="page-header"]/a[2]').click()
                driver.find_element_by_name('login_email').send_keys('<insertusername>')
                driver.find_element_by_name('login_password').send_keys('<insert password>')
                driver.find_element_by_xpath('//*[@id="regular-login-forms"]/div/form/div[3]/button/div[1]').click()

            # Wait a few seconds for page to load
            time.sleep(15)

            driver.switch_to.frame(0)
            # Click tri-dot dropdown
            driver.find_element_by_xpath('//header[@id="main-header"]/div[4]/div[2]/div/button/span/span/span').click()
            # Click Export button
            driver.find_element_by_xpath('//header[@id="main-header"]/div[4]/div[2]/div[2]/div/ul/li[14]/button/span/span').click()
            # Select 'Markdown' as output format
            driver.find_element_by_xpath('//label[contains(.,"Markdown (.md)")]').click()
            # Click Export Button
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/button[2]/span').click()

            # Wait a few seconds for file to download
            time.sleep(15)
