from requests import post

url = 'http://127.0.0.1:8080/inadimplencia'

dict_json = {
    
    'year':2019,
    'loan_limit':1,
    'Gender':1,
    'approv_in_adv':1,
    'loan_type':2,
    'loan_purpose':1,
    'Credit_Worthiness':1,
    'open_credit':1,
    'business_or_commercial':1,
    'loan_amount':500000,
    'rate_of_interest':1,
    'Interest_rate_spread':1,
    'Upfront_charges':1200,
    'term':360,
    'Neg_ammortization':1,
    'interest_only':1,
    'lump_sum_payment':1,
    'property_value':500000,
    'construction_type':1,
    'occupancy_type':1,
    'Secured_by':1,
    'total_units':1,
    'income':10000,
    'credit_type':1,
    'Credit_Score':600,
    'co_applicant_credit_type':1,
    'age':1,
    'submission_of_application':1,
    'LTV':1000,
    'Region':1,
    'Security_Type':1,
    'dtir1':30,

}

r = post(url, json=dict_json)

print(r.status_code)