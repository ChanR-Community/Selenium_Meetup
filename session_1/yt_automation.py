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
sleep(1)

# Identifying the search element
search_elem = browser.find_element_by_id("search")

## Clicking the elemnt and then typing in it
search_elem.click()
search_elem.send_keys(input("Search a video less than an hr long :- "))

# Importing special keys that let us press the Enter, Backspace keys etc.
from selenium.webdriver.common.keys import Keys

# Pressing the Enter key
search_elem.send_keys(Keys.ENTER)

sleep(3)
# Getting the song xpath
song_xpath = "//div[@id='contents']/ytd-video-renderer/div/div/div/div/h3/a"

# Finding the song element

# We cant use find_element_by_xpath as that will not be indexed

# So instead we use find_elements_by_id and click on the 1st video
song_elem = browser.find_elements_by_xpath(song_xpath)[0]

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

# Converting vid duration to seconds then waiting that much and then exiting the browser

for i in range(2):
    vid_time_split = current_vid_duration_elem.text.split(':')
    minutes = int(vid_time_split[0]) * 60
    seconds = int(vid_time_split[1])
    sleep(1)

sleep(minutes + seconds - 2)

print("Playing is complete, exiting in some time")

# After 3 seconds close the browser
sleep(3)

# Quiting the browser
browser.quit()
