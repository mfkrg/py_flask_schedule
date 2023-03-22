import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from conf import CACHE_FOLDER
from selenium.webdriver.common.by import By
from Screenshot import Screenshot

def schedule_png_gen(html_file, group):
    print('Not in cache')
    file_name = f'{group}.html'
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get('file://' + str(Path(html_file).resolve()))
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    # driver.implicitly_wait(10)
    # Path(CACHE_FOLDER).mkdir(parents=True, exist_ok=True)
    filename_without_extension = os.path.splitext(file_name)[0]
    # el = driver.find_element(By.TAG_NAME, 'body')
    # el.screenshot(f'cache/{filename_without_extension}.png')
    driver.save_screenshot(f'cache/{filename_without_extension}' + '.png')
    driver.quit()
    return 0