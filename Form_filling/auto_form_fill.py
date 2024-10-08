from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

driver = webdriver.Chrome()

# Open the login page
driver.get("http://127.0.0.1:8000/login/")

# Enter username and password
driver.find_element(By.NAME, "username").send_keys("aamir_ali")
driver.find_element(By.NAME, "password").send_keys("Allah786%")

# Submit the login form
driver.find_element(By.NAME, "login_button").click()



driver.get("http://127.0.0.1:8000/imager/")  # Use your Django app URL

# Wait for the page to load completely
time.sleep(3)

# Define the folder to save the images on Desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
image_folder = os.path.join(desktop, 'Downloaded_Images')

# Create the folder if it doesn't exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Find all the image elements on the page
images = driver.find_elements(By.TAG_NAME, "img")

# Download each image
for idx, img in enumerate(images):
    img_url = img.get_attribute("src")

    if img_url:
        try:
            # Send a request to download the image
            img_data = requests.get(img_url).content

            # Define the file name for each image
            img_name = f"image_{idx + 1}.jpg"
            img_path = os.path.join(image_folder, img_name)

            # Save the image to the folder
            with open(img_path, "wb") as handler:
                handler.write(img_data)
                print(f"{img_name} downloaded successfully.")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
# SCROLL SLOWLY
# Define the number of pixels to scroll by each step
# scroll_increment = 100  # You can adjust this to control the speed
# scroll_pause_time = 0.5  # Time to wait between scrolls (in seconds)
#
# # Get the total height of the page
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# # Scroll down in increments
# for i in range(0, last_height, scroll_increment):
#     driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
#     time.sleep(scroll_pause_time)

# SCROLL IN ONE GO
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll to the bottom
# driver.implicitly_wait(15)
# time.sleep(10)
driver.quit()
