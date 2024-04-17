from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup
# Specify your desired hashtag here
hashtag = 'love'
 # Open Chrome browser and navigate to Instagram login page
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)
 # Find element on webpage where you enter your Instagram credentials
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
 # Enter your Instagram credentials here
username_field.send_keys("")
password_field.send_keys("")
time.sleep(3)
 # Click "Log In" button to log into Instagram account
log_in_button = driver.find_elements_by_css_selector("[type='submit']")[1]
log_in_button.click()
time.sleep(7)
 # Navigate to URL containing list of users tagged in specified hashtag
url = f'https://www.instagram.com/explore/tags/{hashtag}/'
driver.get(url)
time.sleep(6)
 # Create empty lists to store scraped data
user_names = []
full_names = []
biographies = []
num_posts = []
follower_counts = []
 # Use BeautifulSoup library to parse HTML content from loaded web page
html_content = driver.page_source
insta_soup = soup(html_content, features="lxml")
 # Loop through each user tag found on page
for user in insta_soup.select('.coreSpriteProfile'):
    try:
        # Extract relevant info about user
        user_link = user.select_one('a').get('href')
        user_profile = requests.get(f'https://www.instagram.com{user_link}')
        user_profile_soup = soup(user_profile.text, features="lxml")
        user_names.append(
            user_profile_soup.select_one('h1').text.strip().replace('\n', '')
        )
        full_names.append(
            user_profile_soup.select_one('span[class^=b8cIId]').text.strip()
        )
        if len(user_profile_soup.select('p')) > 1:
            biographies.append(
                user_profile_soup.select_one('p').text.strip().splitlines()[1].strip()
            )
        else:
            biographies.append('')
        num_posts.append(int((re.search("\d+", user.select_one('li span').text)).group()))
        follower_counts.append(
            int((re.search("\d+,?\d*",
                            user.select_one('[aria-label*=Followers]')
                               .text).group()).replace(',', '').replace('.', ''))
        )
    except Exception as e:
        print(e)
        continue
 # Close Chrome window when done
driver.quit()
 # Print results to console or save to file
print(f"{len(user_names)} users found:")
for i in range(len(user_names)):
     print(
         f"\tUsername: {user_names[i]} \n\tFull Name: {full_names[i]}" +
         f"\n\tBiography: {biographies[i]} \n\tNumber of Posts: {num_posts[i]}"
          f"\n\tFollower Count: {follower_counts[i]}")
