# os for file management
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import dropbox

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
                dropbox.login(driver, True)

            dropbox.export_as_markdown(driver, True if i != 0 else False )
