# libary flask
# untuk membuat web serviice
from flask import Flask, render_template,request
from flask.wrappers import Request
# libary json
import json

# untuk membuat flask instance
app = Flask(__name__)
# sintak untuk membaca file json
with open ('data.json') as b:
    data = json.load(b)
    
# meload json dengan nama data diatas
# lalu pada [film] memanggil nama dictionary pada json   
movie = data ['film']

    
# lamdbda,sorted untuk sorting  
temp =sorted(movie, key=lambda x:(x['judul']))

# list
alltahun=[]
alljudul=[]
tahun2020 = []
tahun2019= []
tahun2018 = []
tahun2017 = []
tahun2016 = []
tahun2012 = []
tahun2008 = []
tahun2003 = []

# perulangan untuk mengambil data tahun dan judul
# data tahun akan disimpan pada list alltahun
# data judul akan disimpan pada list alljudul 
for i in movie :
    alltahun.append(i['tahun'])
    alljudul.append(i['judul'])
    
# perulangan mengambil judul berdasarkan tahun
for x in movie:
    a = x['tahun']
    if a =='2020':
        tahun2020.append(x['judul'])
    elif a =='2019':
        tahun2019.append(x['judul'])
    elif a =='2018':
        tahun2018.append(x['judul'])
    elif a =='2017':
        tahun2017.append(x['judul'])
    elif a =='2016':
        tahun2016.append(x['judul'])
    elif a =='2012':
        tahun2012.append(x['judul'])
    elif a =='2008':
        tahun2008.append(x['judul'])
    elif a =='2003':
        tahun2003.append(x['judul'])
    
# fungsi untuk mengfilter judul berdasarkan tahun
def th2020(jdl):
    # mendeklarasikan list tahun2020 dengan variabel d
    d = tahun2020
    # lalu dicek apakah jdl ada divariabel d
    if(jdl in d):
        return True
        # jika jdl ada pada list maka akan bernilai true dan bisa dipanggil pada fungsi filter
    else:
        return False
        # jika tidak ada maka tidak akan  dipanggil pada fungsi filter
        
def th2019(jdl):
    d = tahun2019
    if(jdl in d):
        return True
    else:
        return False
    
def th2018(jdl):
    d = tahun2018
    if(jdl in d):
        return True
    else:
        return False

def th2017(jdl):
    d = tahun2017
    if(jdl in d):
        return True
    else:
        return False
    
def th2016(jdl):
    d =tahun2016
    if(jdl in d):
        return True
    else:
        return False

def th2012(jdl):
    d =tahun2012
    if(jdl in d):
        return True
    else:
        return False
    
def th2008(jdl):
    d = tahun2008
    if(jdl in d):
        return True
    else:
        return False
    
def th2003(jdl):
    d = tahun2003
    if(jdl in d):
        return True
    else:
        return False

# app route digunakan untuk memberi alamat website
# pada flask ini default hostnya 127.0.0.1 dengan port 5000 atau bisa dituliskan 127.0.0.1:5000
# app route dibawah bisa menggunakan dua alamat yaitu 127.0.0.1:5000 dan http://127.0.0.1:5000/index.html
@app.route("/")
@app.route("/index.html")
def hello():# fungsi untuk index.html
    # jika kita mengakses alamat dialas maka program akan memanggil file index.html pada browser 
    # render_template digunakan untuk memanggil file yang berformat html
    # di dalam movie mendeklarasikan temp  yang terdapat pada baris ke 20 dan akan dipanggil pada index.html
    return render_template('index.html', movie = temp)

# app route dibawah ini memiliki alamat 127.0.0.1:5000/fitur.html
# pada app route filter ini menggunakan method POST dan GET
@app.route("/fitur.html", methods=["POST", "GET"])
def fitur():
    # jdlfilter digunakan untuk memanggil request form pada html yang bernama tahun
    jdlfilter = request.form.get('tahun')
    
    # deklarasi filter judul film berdasarkan tahun
    list2020 = filter(th2020, alljudul)
    list2019 = filter(th2019, alljudul)
    list2018 = filter(th2018, alljudul)
    list2017 = filter(th2017, alljudul)
    list2016 = filter(th2016, alljudul)
    list2012 = filter(th2012, alljudul)
    list2008 = filter(th2008, alljudul)
    list2003 = filter(th2003, alljudul)
    
    # render_template digunakan untuk memanggil file  yang bernama fitur.html
    # didalam render_template terdapat beberapa variabel baru yang memuat variabel deklarasi filter (seperti pada baris ke 141-148)
    # variabel baru pada render_template digunakan untuk memanggil di htmlnya 
    return render_template('fitur.html',allt=alltahun, t=jdlfilter, satu=list2020, dua=list2019,
                           tiga=list2018, empat=list2017, lima=list2016,
                           enam=list2012, tujuh=list2008, lapan=list2003)


# app route dibawah ini memiliki alamat 127.0.0.1:5000/About.html 
@app.route("/About.html")
def pircing():
    # render_template digunakan untuk memanggil file yang bernama About.html
    return render_template('About.html')

if __name__=="__main__":
    #app run dibawah ini digunakan untuk menjalankan flasknya dengan mengaktifkan debug
    app.run(debug=True)