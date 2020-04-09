# export PATH=$PATH:/snap/bin/chromium.chromedriver/
# importing os module 
import os 
from selenium import webdriver 
import shutil
import requests
import time 
import urllib.request

WEB_URL =  "";

directory = "images"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium" 
driver = webdriver.Chrome( executable_path='/snap/bin/chromium.chromedriver')

driver.get(WEB_URL)
time.sleep(3) 

def is_url_image(image_url):  
   return image_url.endswith('.jpg')
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

def saveImage ( path, url ):
    try:
        if is_url_image( url ):
            print("valid image" + url)
            with open( path, 'wb') as handle:
                response = requests.get(url, stream=True)

                if not response.ok:
                    print (response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

    except Exception as e:
        print(  e)

if os.path.exists(directory) and os.path.isdir(directory):
    shutil.rmtree(directory)
os.mkdir(directory) 

count = 100

for a in driver.find_elements_by_xpath('.//a'):
    imageUrl = a.get_attribute('href')
    saveImage( directory+"/"+str(count)+".jpg" , imageUrl)
    count = count + 1


time.sleep(3) 
driver.close()