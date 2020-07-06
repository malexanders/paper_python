import time
import os
import re

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

def format_markdown_checkboxes(input_dir, output_dir):
    file_list = list(os.listdir(input_dir))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for file in file_list:

        if not file.endswith('.md') or os.path.isdir(input_dir + '/' + file):
            continue

        with open(input_dir + '/' + file, 'r') as reader:
            # Note: readlines doesn't trim the line endings
            markdown_lines = reader.readlines()

        with open(output_dir + '/' + file, 'w') as writer:
            for line in markdown_lines:
                # If line starts with [], [ ] or [x] with 0 or more spaces add md line break
                if re.match(r'^\s*\[]|^\s*\[ ]|^\s*\[x]', line):
                    new_line = line + '\x20' + '\x20' + '\n'
                    writer.write(new_line)
                else:
                    writer.write(line)