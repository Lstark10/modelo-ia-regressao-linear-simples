from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Criação de instância do fastAPI
app = FastAPI()

# Criação de classe que terá os dados do request body para a API
class request_body(BaseModel):
    horas_estudo: float


#Carregar o modelo para realizar a predição
modelo_pontuacao = joblib.load('./modelo_regressao.pkl')

@app.post("/predict")

def predict(data: request_body):
    # Preparação dos dados para predição
    input_feature = [[data.horas_estudo]]

    #Realizar a predição
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)

    return {'pontuacao_teste': y_pred.tolist()}