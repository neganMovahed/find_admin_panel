import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from config import ConfigFactory
import codecs

config_data = ConfigFactory.GetConfig()

#------------------------------------------
#get csrf
session = HTMLSession()
response = session.get(config_data.LoginUrl)
csrf_token = response.html.find('input[name="csrfmiddlewaretoken"]', first=True).attrs['value']
#------------------------------------------

# response = requests.get(config_data.LoginUrl)
# soup = BeautifulSoup(response.content, 'html.parser')


#------------------------------------------
login_data = {
    'username': config_data.Username,
    'password': config_data.Password,
    'csrfmiddlewaretoken': csrf_token
}
response = session.post(config_data.LoginUrl, data=login_data)


response = session.get(config_data.ProductUrl.replace("ProductId","188"))

soup = BeautifulSoup(response.content, 'html.parser')

input_element = soup.find('input', {'class': 'productEnName'})
input_element = soup.select_one('input.productEnName')

input_value = input_element.get('value')
print(input_value)



# with codecs.open('output.html', 'w', 'utf-8') as f:
#     f.write(soup.prettify())
#------------------------------------------
