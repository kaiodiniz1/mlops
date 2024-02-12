from flask import Flask, request
import pickle
from warnings import filterwarnings

filterwarnings('ignore')

def importa_modelo(nome_modelo):
    modelo = pickle.load(open(nome_modelo, 'rb'))
    return modelo

app = Flask(__name__)


@app.route('/inadimplencia', methods=['POST'])
def pag1():
    dados_post = request.get_json()
    dados = [dados_post[i] for i in ['year','loan_limit','Gender','approv_in_adv','loan_type','loan_purpose','Credit_Worthiness','open_credit','business_or_commercial','loan_amount','rate_of_interest','Interest_rate_spread','Upfront_charges','term','Neg_ammortization','interest_only','lump_sum_payment','property_value','construction_type','occupancy_type','Secured_by','total_units','income','credit_type','Credit_Score','co_applicant_credit_type','age','submission_of_application','LTV','Region','Security_Type','dtir1']]
    
    modelo = importa_modelo('inadimplencia')
    resultado = modelo.predict([dados])[0]

    print(resultado)

    return 'Hello World'

@app.route('/caracteristicas', methods=['POST'])
def pag2():
    dados_post = request.get_json()
    dados = [dados_post[i] for i in ['loan_amount','property_value','Interest_rate_spread', 'rate_of_interest', 'Credit_Score', 'income', 'LTV', 'dtir1']]
   
    modelo = importa_modelo('kmeans')

    resultado_kmeans = modelo.predict([dados])[0]

    if resultado_kmeans == 0:
        print('O cliente atual faz parte do grupo 0, tem um perfil Conservador e a propensão a fraude média do seu grupo é: 17%')
    elif resultado_kmeans == 1:
        print('O cliente atual faz parte do grupo 1, tem um perfil Moderado e a propensão a fraude média do seu grupo é: 2%')
    else:
        print('O cliente atual faz parte do grupo 2, tem um perfil Agressivo e a propensão a fraude média do seu grupo é: 37%')

    return 'Hello World'

app.run(
    debug=True,
    port=8080
)