import requests
import json


def search(city_code):

    search_url = "http://wthrcdn.etouch.cn/weather_mini?citykey={city_code}"
    url = search_url.format(city_code=city_code)
    request = requests.get(url)
    request.encoding = "utf8"
    response = request.json()

    return response


def parse(response):

    data = []
    status = response.get("status", None)
    if not status == 1000:
        return False

    data.append("城市: " + response["data"]["city"])
    today = response["data"]["forecast"][0]
    data.append("日期: " + today["date"])
    data.append("最高气温: " + today["high"].split(" ")[1])
    data.append("最低气温: " + today["low"].split(" ")[1])
    data.append("天气: " + today["type"])
    data.append("风力: " + today["fengli"])
    data.append("风向: " + today["fengxiang"])
    data.append("注意: " + response["data"]["ganmao"])

    return data


def get_city_code(city):

    with open("data.json", "r") as f:

        data = json.load(f)

        return data.get(city, None)
