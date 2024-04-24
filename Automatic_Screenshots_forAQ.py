# This script was created to automatically capture screenshots of multiple webpages in an hourly basis
# Function: Takes a screenshot of a desired page (e.g., traffic information, atmospheric circulation) and save it
# Author: Davi de Ferreyro Monticelli, iREACH group (University of British Columbia)
# Date: 2023-06-20
# Version: 1.0.0

import io
import sys

# Get the current user's username
username = os.getlogin()

########################################################################################################################
# Creating a custom class to save console printed messages in a single file:
########################################################################################################################
class Tee(io.TextIOWrapper):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super().__init__(file, *args, **kwargs)

    def write(self, text):
        self.file.write(text)
        sys.__stdout__.write(text)  # Print to the console


# Specify the file path where you want to save the output
file_path_txt = f'C:\\Users\\{username}\\PycharmProjects\\Screenshot_Porject\\Screenshot_console_output.txt'

# Open the file in write mode and create the Tee object
output_file_txt = open(file_path_txt, 'w')
tee = Tee(output_file_txt)

# Redirect the standard output to the Tee object
sys.stdout = tee

########################################################################################################################
# Main script:
########################################################################################################################

import time
from datetime import datetime
from selenium import webdriver
from pynput.mouse import Controller
from pynput.mouse import Button as Button_pyn
from selenium.webdriver.common.by import By  # for FireSmoke.ca ONLY (animated automatically...)
import pyautogui
import subprocess

mouse = Controller()


# Function to check for internet connection
def check_internet_connection():
    try:
        # Pinging a reliable end fast server (Google DNS)
        subprocess.check_output(['ping', '-n', '1', '8.8.8.8'])
        return True
    except subprocess.CalledProcessError:
        return False


# Function to connect to the internet
# Naive way but works
def connect_to_network():
    new_click_x1 = 1170
    new_click_y1 = 746

    mouse.position = (new_click_x1, new_click_y1)
    time.sleep(1)
    mouse.press(Button_pyn.left)
    time.sleep(0.2)
    mouse.release(Button_pyn.left)
    time.sleep(2)

    new_click_x2 = 1113
    new_click_y2 = 175

    mouse.position = (new_click_x2, new_click_y2)
    time.sleep(1)
    mouse.press(Button_pyn.left)
    time.sleep(0.2)
    mouse.release(Button_pyn.left)
    time.sleep(2)

    new_click_x3 = 1272
    new_click_y3 = 272

    mouse.position = (new_click_x3, new_click_y3)
    time.sleep(1)
    mouse.press(Button_pyn.left)
    time.sleep(0.2)
    mouse.release(Button_pyn.left)
    time.sleep(2)

    new_click_x4 = 732
    new_click_y4 = 750

    mouse.position = (new_click_x4, new_click_y4)
    time.sleep(1)
    mouse.press(Button_pyn.left)
    time.sleep(0.2)
    mouse.release(Button_pyn.left)
    time.sleep(2)


# Define the list of URLs of the webpages you want to capture
webpage_urls = [
    "https://www.google.com/maps/@49.1569666,-122.5354054,10z/data=!5m1!1e1?entry=ttu",  # GVR Traffic
    "https://www.google.com/maps/@49.1955974,-122.9020397,11.17z/data=!5m1!1e1?entry=ttu",  # MVR Traffic
    "https://www.windy.com/?49.267,-123.198,5",  # Windy (wind) BC
    "https://www.windy.com/?49.156,-122.346,9",  # Windy (wind) MV
    "https://www.windy.com/-Solar-power-solarpower?solarpower,49.245,-122.485,9",  # Windy - Solar power Vancouver
    "https://www.windy.com/-Cloud-tops-cloudtop?cloudtop,49.245,-122.485,9",  # Windy - Cloud tops Vancouver
    "https://www.windy.com/sounding/49.259/-123.100?49.258,-123.512,10",  # Windy - Radiosonde Vancouver
    "https://firesmoke.ca/forecasts/current/",  # Firesmoke.ca - Wildfire (Canada)
    "https://firesmoke.ca/forecasts/current/?lat=49.192&lon=-122.330&zoom=9",  # FireSmoke.ca - Wildfire (GVR)
    "https://www.windy.com/?51.317,-101.426,4,i:pressure"  # Canada Pressure Systems
]

# Define list for file names
webpage_names = [
    "GVR_Traffic",
    "MVR_Traffic",
    "Wind_BC",
    "Wind_MVR",
    "Solar_power_Vancouver",
    "Cloud_tops_Vancouver",
    "Radiosonde_Vancouver",
    "Wildfire_Canada",
    "Wildfire_GVR",
    "Pressure_Canada"
]

# Define path for screenshot file
path_names = [
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\GVR\\Traffic",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\GVR\\Traffic",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\GVR\\Wind",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\GVR\\Wind",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\Vancouver\\Solar power",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\Vancouver\\Cloud tops",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\Vancouver\\Radiosonde",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\Wildfires",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\Wildfires",
    f"C:\\Users\\{username}\\Sync\\PhD - Data archives\\Screenshots\\Pressure"
]

# Set the coordinates of the point you want to click (use Inspect tool in web browser or Pixspy.com)
# X coordinates
click_xs = [
    45,
    45,
    712,
    453,
    881,
    1047,
    490,
    336,
    336,
    441
]

# Y coordinates
click_ys = [
    540,
    540,
    410,
    451,
    410,
    410,
    723,
    690,
    690,
    455
]

# Set a sleep time for page to load in each case
sleep_times = [
    15,
    15,
    15,
    15,
    15,
    15,
    15,
    0,
    0,
    15
]

# Set an initial value for the previous hour
previous_hour = -1

# Infinite loop to continuously capture screenshots
while True:
    if check_internet_connection():

        # Get the current hour
        current_hour = datetime.now().hour

        # Capture the current date and time
        now = datetime.now()
        timestamp = now.strftime("%d_%b_%y_%I%p")

        # Check if the hour has changed
        if current_hour != previous_hour:

            for webpage_url, webpage_name, path_name, click_x, click_y, sleep_time in zip(webpage_urls, webpage_names,
                                                                                          path_names, click_xs,
                                                                                          click_ys, sleep_times):
                if check_internet_connection():  # Check connection status from within the loop

                    try:
                        # Create a new instance of the WebDriver
                        driver = webdriver.Firefox()  # Replace with the appropriate WebDriver class and path

                        # Open the webpage
                        driver.get(webpage_url)

                        # Wait for the page to load (adjust the sleep duration if needed)
                        time.sleep(sleep_time)

                        # Perform necessary mouse clicks for better capture:

                        # Screenshot at the precise time (FireSmoke ONLY)
                        # (if you need more than one click this loop does not work)
                        if webpage_name == "Wildfire_Canada" or webpage_name == "Wildfire_GVR":
                            # Set the CSS selector of the element that contains the text you want to scan
                            element_selector = '#mapID > div.leaflet-control-container > div.leaflet-bottom.leaflet-left > div.leaflet-bar.leaflet-bar-horizontal.leaflet-bar-timecontrol.leaflet-control > a.leaflet-control-timecontrol.timecontrol-date'
                            # Set the expected date and hour format
                            expected_format = '%Y-%m-%d, %I:%M:%S %p'
                            while True:
                                # Find the element and get the text
                                element = driver.find_element(By.CSS_SELECTOR, element_selector)
                                text = element.text

                                # Get the current date and hour
                                current_datetime = datetime.now()
                                current_datetime = current_datetime.replace(minute=0, second=0, microsecond=0)
                                current_text = current_datetime.strftime(expected_format)
                                current_text = current_text.replace("AM", "a.m.").replace("PM", "p.m.")
                                if current_text[12] == '0':
                                    current_text = current_text[:12] + current_text[13:]

                                # Compare the text with the current date and hour
                                if text == current_text:
                                    # Take a screenshot
                                    driver.save_screenshot(f"{path_name}\\Screenshot_{timestamp}_{webpage_name}.png")
                                    break  # Exit the loop once the condition is met

                                # Wait for a specific duration before checking again
                                # You can adjust the sleep duration if needed
                                time.sleep(0.333)  # Wait for 0.333 seconds before the next comparison
                            # Quit the driver and close the browser
                            driver.quit()
                        # Radiosonde page also has specific conditions to operate screenshot
                        elif webpage_name == "Radiosonde_Hope" or webpage_name == "Radiosonde_Langley" or webpage_name == "Radiosonde_Delta" or webpage_name == "Radiosonde_Vancouver":
                            # Set the CSS selector of the element that contains the text you want to scan
                            radiosonde_selector = 'html#device-desktop.target-index body.zoom10.product-ecmwf.overlay-wind.has-more-levels.onrhpane.onpatch.onprogress-bar.platform-desktop.user-logged-out.onsounding.selectedpois-radiosonde.onpoi-libs div#plugins.shy div#plugin-sounding.plugin-lhpane.plugin-tablet-rhpane.top-border.open section#sounding-content.plugin-content footer div.controls span.checkbox.off'
                            # Wait for the page to load (you can adjust the sleep duration if needed)
                            driver.implicitly_wait(10)

                            # Find the checkbox element using CSS selector
                            mouse.position = (click_x, click_y)
                            mouse.press(Button_pyn.left)
                            time.sleep(0.2)
                            mouse.release(Button_pyn.left)
                            time.sleep(10)
                            driver.execute_script("window.scrollTo(0, 10)")
                            checkbox = driver.find_element(By.CSS_SELECTOR, radiosonde_selector)

                            # Toggle the checkbox ON
                            checkbox.click()
                            time.sleep(5)
                            driver.save_screenshot(f"{path_name}\\Screenshot_{timestamp}_{webpage_name}.png")
                            # Quit the driver and close the browser
                            driver.quit()
                        # Every other page is simpler:
                        else:
                            mouse.position = (click_x, click_y)
                            mouse.press(Button_pyn.left)
                            time.sleep(0.2)
                            mouse.release(Button_pyn.left)
                            time.sleep(10)

                            # Create the filename with the timestamp
                            screenshot_path = f"{path_name}\\Screenshot_{timestamp}_{webpage_name}.png"

                            # Capture a screenshot of the entire page
                            pyautogui.screenshot(screenshot_path)

                        # Close the WebDriver
                        driver.quit()

                    except Exception as e:
                        print(f"Error capturing screenshot: {e}")

                else:
                    connect_to_network()
            # Update the previous hour
            print("Last capture at:", timestamp)
            previous_hour = current_hour

            # Wait for a short duration before checking the hour again
            time.sleep(60 * 10)  # Wait for 10 minutes
    else:
        # Naive way to connect to internet because smart way is not working
        # Smart way: use a python library + defined function
        # Naive way: mouse clicks.
        connect_to_network()
    time.sleep(10)  # Wait for 10 seconds before checking again

# Restore the standard output
sys.stdout = sys.__stdout__

# Close the output file
output_file_txt.close()
