from flask import Flask
from flask import request, redirect
from flask import render_template
import requests, csv


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data1 = response.json()

# print('data1 ',type(data1))  # class list
# print(data1)
# print()
# print('data2=data1[0]', type(data1[0]))   # class dict
# print(data1[0])
# print()

data2 = data1[0]    # odczytanie słownika z listy

#print(data2["rates"]', type(data2['rates']))   # class list
#print(data2['rates'])

# for waluta in data2['rates']:   # class dict
#    print(waluta)
#    print(waluta['currency'],waluta['code'],waluta['bid'],waluta['ask'])

# pierwsza część zadania - zapis danych do pliku waluty.csv
#
with open('waluty.csv', 'w', newline='') as csvfile:
    curr_names = ['currency', 'code','bid','ask']
    writer = csv.DictWriter(csvfile, fieldnames=curr_names, delimiter=';')
    writer.writeheader()
    for waluta in data2['rates']:        # data2['rates']   dict class
       writer.writerow(waluta)

# druga część zadania - kalkulator
lista_walut=[]
for waluta in data2['rates']:   # class dict
    # print(waluta['code'])
    lista_walut.append(waluta['code'])

# print(lista_walut)

app = Flask(__name__)

@app.route('/')
def start():
    return f'Witamy na stronie testowej.....'

@app.route('/calc',methods=["GET","POST"])
def calc():
    if request.method == "POST":
        dane = request.form
        kod_waluty= dane.get('currenty')
        ilosc = dane.get('ilosc')
        print(kod_waluty, ilosc)
        for waluta in data2['rates']:   # class dict
            if waluta['code'] == kod_waluty:
                kurs = waluta['ask']
                wartosc = float(kurs) * float(ilosc)
        return render_template("calc_child2.html", waluta=kod_waluty, ilosc=ilosc,kurs=kurs,wartosc=wartosc)
    return render_template("calc_child1.html", rates=lista_walut)

if __name__ == "__main__":
    app.run(debug=True)
