import requests

s_city = "Samara,RU"
city_id = 0
appid = "3fdfb29fa01781d86e50693b4555ef02"
try:#index of sity
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("Город:", cities)
    city_id = data['list'][0]['id']
    print('id =', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass

try:#today's weather
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Погода:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
except Exception as e:
    print("Exception (weather):", e)
    pass