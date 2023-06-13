import requests
from bs4 import BeautifulSoup

def get_current_temperature():
    url = "https://weather.naver.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the current temperature
    temperature_element = soup.find('strong', class_='current')
    
    if temperature_element:
        temperature = temperature_element.get_text()
        return temperature.strip()
    else:
        return None

# Example usage
current_temperature = get_current_temperature()
if current_temperature:
    print(current_temperature)
else:
    print("Failed to retrieve the temperature.")
