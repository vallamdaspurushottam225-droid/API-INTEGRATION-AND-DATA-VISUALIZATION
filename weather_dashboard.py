#importing requests library to fetch data from API
import requests

#importing matplotlib for data visualizations
import matplotlib.pyplot as plt

#importing seaborn for visualizations
import seaborn as sns

#storin api key generated from openweathermap
api_key = "4529050d5ac3bf336abc9a98a782ec95"

#storing city name
city_name = input("Enter your city name:")

#creating api url using city and api key
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"


#sending request to API
response = requests.get(url)

# Converting API response into JSON format
data = response.json()

#printing compltete weather data
print(data)

#extracting temperture from JSON data
temperature = data["main"]["temp"]

#extracting humidity values
humidity = data["main"]["humidity"]

#extracting weather condition
weather_condition = data["weather"][0]["main"]

#displaying extracted values
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Weather:", weather_condition)

#values for labels
labels = ["Temperature", "Humidity"]

#values for graph
values = [temperature, humidity]

#creating bar chart
plt.bar(labels, values)
sns.barplot(x=labels, y=values, color="blue")

#adding graph title
plt.title("Real-Time-Weather-Visualization")

#adding y-axis label
plt.ylabel("Values")

#displaying graph
plt.show()
