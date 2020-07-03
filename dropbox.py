import time

def login(driver, sleep=False):
    driver.find_element_by_xpath('//*[@id="page-header"]/a[2]').click()
    driver.find_element_by_name('login_email').send_keys('<insertusername>')
    driver.find_element_by_name('login_password').send_keys('<insert password>')
    driver.find_element_by_xpath('//*[@id="regular-login-forms"]/div/form/div[3]/button/div[1]').click()
    if sleep == True:
        time.sleep(15)

def export_as_markdown(driver, sleep=False):
    if sleep == True:
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

    time.sleep(15)

# TODO:
# Dropbox paper markdown export does not format properly
# Checkboxes do not have the required double space at the end of each line
# def format_markdown_checkboxes(file):
#     # Read file lines
#     # Where a line starts with [x] || [] || [ ]
#         # Does it end with 2 spaces?
#             # If No, add two spaces
#             # Else, do nothing