import requests
from bs4 import BeautifulSoup

url = input("Enter the url of the Instagram Image: ")

print('Obtaining the link...')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
link = soup.find('meta', property='og:image')['content']

print("Downloading Image... ")
picture = requests.get(link)

print("Image downloaded..")
file_name = input("Enter the name of the picture: ")

with open(file_name+'.jpg', 'wb') as f:
    f.write(picture.content)

print(f'Picture saved as {file_name}.jpg')

