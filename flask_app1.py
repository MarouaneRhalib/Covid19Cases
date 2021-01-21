from flask import Flask, render_template, request, json

app = Flask(__name__)
file_name='covid26112020.json'
@app.route('/',methods=["GET"])
def index():
    return (render_template('index.html'))

@app.route('/',methods=["POST"])
def result():
    c1 = request.form['country1']
    c2 = request.form['country2']
    c3 = request.form['country3']

    print(c1)

    datesc1 = getDates(c1)
    datesc2 = getDates(c2)
    datesc3 = getDates(c3)


    casesc1 = getCases(c1)
    casesc2 = getCases(c2)
    casesc3 = getCases(c3)

    deathsc1 = getDeaths(c1)
    deathsc2 = getDeaths(c2)
    deathsc3 = getDeaths(c3)

    print(c1, c2, c3)
    print(datesc1)
    print(casesc1)

    return (render_template('index.html',deathsc1=deathsc1,deathsc2=deathsc2,deathsc3=deathsc3,casesc1=casesc1,casesc2=casesc2,casesc3=casesc3,datesc1=datesc1, datesc2=datesc2, datesc3=datesc3, c1=c1,c2=c2,c3=c3))

def getDates(coutry):
    listdates = []
    file = open(file_name)
    data_json = json.load(file)
# print(data_json)
    for i in data_json['records']:
       if i['countryterritoryCode'] == coutry:
           listdates.append(i['dateRep'])
    file.close()
    return (listdates)

def getCases(coutry):
    listCases = []
    file = open(file_name)
    data_json = json.load(file)
    for i in data_json['records']:
        if i['countryterritoryCode'] == coutry:
            listCases.append(i['cases'])
    file.close()
    return (listCases)

def getDeaths(coutry):
    listDeaths = []
    file = open(file_name)
    data_json = json.load(file)
    for i in data_json['records']:
        if i['countryterritoryCode'] == coutry:
         listDeaths.append(i['deaths'])
    file.close()
    return (listDeaths)

if __name__ =='__main__':
    app.run(debug=True)