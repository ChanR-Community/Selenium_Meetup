# Importing selenium and sleep()
from selenium import webdriver
from time import sleep

# Chromedriver path
PATH = "./drivers/chromedriver.exe"
# Opening the browser
browser = webdriver.Chrome(PATH)

# Going to youtube
browser.get("https://www.youtube.com")
# Waiting for the website to load
sleep(3)

# Identifying the search element
search_elem = browser.find_element_by_id("search")

## Clicking the elemnt and then typing in it
search_elem.click()
search_elem.send_keys("Freedom by Kygo")

# Importing special keys that let us press the Enter, Backspace keys etc.
from selenium.webdriver.common.keys import Keys

# Pressing the Enter key
search_elem.send_keys(Keys.ENTER)

sleep(3)
# Getting the song xpath
song_xpath = "//div[@id='contents']/ytd-video-renderer/div/div/div/div/h3/a[@title='Kygo, Zak Abel - Freedom ft. Zak Abel']"

# Finding the song element
song_elem = browser.find_element_by_xpath(song_xpath)

# Cliking on the song
song_elem.click()

sleep(3)
# Until the song finishes dont close the browser

### Finding current video time
current_vid_time_xpath = "//div[@class='ytp-time-display notranslate']/span[@class='ytp-time-current']"
current_vid_time_elem = browser.find_element_by_xpath(current_vid_time_xpath)
### Finding current video duration
current_vid_duration_xpath = "//div[@class='ytp-time-display notranslate']/span[@class='ytp-time-duration']"
current_vid_duration_elem = browser.find_element_by_xpath(current_vid_duration_xpath)

# print(current_vid_time_elem.text)
# print(current_vid_duration_elem.text)

## Making while statment that says until current_vid_time_elem != current_vid_duration_elem
while current_vid_time_elem != current_vid_duration_elem:
    print(current_vid_time_elem.text)

print("Playing is complete, exiting in some time")
# After 5 seconds close the browser
sleep(5)
# Quiting the browser
browser.quit()
