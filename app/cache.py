import os
from conf import CACHE_FOLDER, HTML_FOLDER


#check cache folder for the file
def get_cached_schedule(group):
    cache_path = os.path.join(CACHE_FOLDER, f'{group}.png')
    if os.path.exists(cache_path):
        with open(cache_path, 'rb') as f:
            return f.read()
    else:
        return None


#adding png in cache
def cache_schedule(group, png_image):
    os.makedirs(CACHE_FOLDER, exist_ok=True)
    cache_path = os.path.join(CACHE_FOLDER, f'{group}.png')
    with open(cache_path, 'wb') as f:
        f.write(png_image)