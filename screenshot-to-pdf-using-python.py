from selenium import webdriver
from PIL import Image
import time

driver = webdriver.Chrome("C:\\Users\\asim\chromedriver.exe) 
url= "https://google.com" 
driver.get(url)
driver.execute_script(document.body.style.zoom.'50%—) 
driver.set_brindousize(1920, 1080, driver.window.handles[0]) 
driver.maximize_window()
time.sleep(5)
driver.save_screenshot(image3.png)
image = Image.open("image3.png)
im1 = image1.convert("RGB")
pdfRath = r'C:\Users\\asim\\Downloads\\screenshots.pdf'
iml.seve(pdfPutM1)
print("screenshot captured")

