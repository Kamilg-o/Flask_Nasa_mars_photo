import json
import requests
import datetime


class Foto:
    def __init__(self):
        self.pic = []
        self.date = []

    def apis(self,date):


        url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={}&api_key=DEMO_KEY".format(date)

        response = requests.request("GET", url)

        with open("plik.json", "w", newline='') as file:
            file.write(json.dumps(response.json()))
        a = json.load(open("plik.json"))
        b = a['photos']
        self.pic=[]
        for i in b:
            self.pic.append(i['img_src'])
        print("lacze sie z api")


class Actual:
    def __init__(self):
        self.apic = []

    def actualisation(self):
        data=datetime.datetime.today()-datetime.timedelta(days=10)

        url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={}&api_key=DEMO_KEY".format(data)

        response = requests.request("GET", url)

        with open("aktual.json", "w", newline='') as file:
            file.write(json.dumps(response.json()))
        a = json.load(open("aktual.json"))
        b = a['photos']
        for i in b:
            self.apic.append(i['img_src'])
        print("lacze sie z api")


pt = Foto()
pt.apis("2020-09-02")
ak = Actual()
ak.actualisation()
