import requests
from bs4 import BeautifulSoup

username = input("Enter Instagram Username: ")
url = 'https://www.instagram.com/' + username 

response = requests.get(url)
# if response.status_code != 200:
#     print("Error: ", response.status_code, response.text)
#     exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Prints followers, following, no of posts, name and username
description = soup.find('meta',property='og:description')['content']
description = description.replace("- See Instagram photos and videos from ", "")
print(description)
#description = description.split("-")[0].split(", ")
#description = {i.split(" ")[1]:i.split(" ")[0] for i in description}
# for i in description:
#     print(i, description[i])

# To save profile pic
if input("Type 'Y' if you want to save profile picture: ").upper() =='Y':
    photo_link = soup.find('meta', property='og:image')['content']
    print(photo_link)
    photo = requests.get(photo_link)
    with open(username+'.jpg', 'wb') as picture:
        picture.write(photo.content)




