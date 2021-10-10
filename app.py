from flask import Flask
from flask import render_template,request
from classes import pt
from classes import ak
app = Flask(__name__)


@app.route("/", methods= ["get","post"])
def index():
    pic = ak.apic
    picture_list = []
    for picture in pic:
        picture_list.append(picture)
    return render_template("Mainpage.html",pic=picture_list)

@app.route("/resp/",methods=["get","post"])
def resp():
    respon = dict(request.form)
    print(respon["date"])
    pt.date=str(respon["date"])
    pt.apis(pt.date)
    pic= pt.pic
    picture_list=[]
    for picture in pic:
        picture_list.append(picture)
    data=respon["date"]
    return render_template("index.html", pic=picture_list,data=data)




