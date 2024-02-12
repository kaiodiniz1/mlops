from requests import post

url = 'http://127.0.0.1:8080/caracteristicas'

dict_json = {
    
    'loan_amount':500000,
    'property_value':500000,
    'Interest_rate_spread':1,
    'rate_of_interest':1,
    'Credit_Score':599,
    'income':15000,
    'LTV':2000,
    'dtir1':40,

}

r = post(url, json=dict_json)

print(r.status_code)