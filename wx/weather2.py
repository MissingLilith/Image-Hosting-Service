# -*- coding: utf-8 -*-
# '中华万年历API接口，获取天气信息'
import json
import requests


def weather_work(city):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city={}'.format(city)
    f = requests.get(url)
    # print(f.text)
    jsons = json.loads(f.text)
    print(jsons['data']['forecast'])
    for i in jsons['data']['forecast']:
        print(i['date'])
        print(i['type'], "\t", i['fengxiang'])
        print(i['high'], i['low'])
        print()


if __name__ == '__main__':
    city = input("请输入城市：")
    weather_work(city)
