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

with open('waluty.csv', 'w', newline='') as csvfile:
    walutanames = ['currency', 'code','bid','ask']
    writer = csv.DictWriter(csvfile, fieldnames=walutanames, delimiter=';')
    writer.writeheader()
    for waluta in data2['rates']:        # data2['rates']   dict class
       writer.writerow(waluta)

