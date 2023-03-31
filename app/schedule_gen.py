import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

def schedule_png_gen(html_file, group):
    logging.debug(f'Schedule not in cache. Generating. Requested - {group}')
    file_name = f'{group}.html'

    #Headless mode for selenium web driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    chromedriver_path = '/path/to/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    driver.get('file://' + str(Path(html_file).resolve()))

    #Scrolling reads the required height and width for the screenshot
    required_width = driver.execute_script('return document.body.scrollWidth')
    required_height = driver.execute_script('return document.body.scrollHeight')
    print(required_width)
    print(required_height)
    driver.set_window_size(required_width, required_height)

    #cut off the .html extension and save in cache folder
    filename_without_extension = os.path.splitext(file_name)[0]
    driver.save_screenshot(f'cache/{filename_without_extension}' + '.png')
    driver.quit()
    logging.debug(f'Schedule generated successfully. Requeted - {group}')
    return 0