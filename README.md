# Modelo de Regressão Linear Simples - Predição de Pontuação em Teste

Este projeto implementa um modelo de regressão linear simples para prever a pontuação em teste com base nas horas de estudo. O projeto inclui análise exploratória de dados, treinamento do modelo, validação e uma API REST para realizar predições.

## 📋 Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Dataset](#dataset)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Metodologia](#metodologia)
- [Resultados](#resultados)
- [API REST](#api-rest)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Autor](#autor)

## 📖 Descrição do Projeto

Este projeto tem como objetivo desenvolver um modelo de machine learning capaz de prever a pontuação de um estudante em um teste com base no número de horas que ele dedicou aos estudos. Utilizamos regressão linear simples, uma técnica fundamental de aprendizado supervisionado, para estabelecer uma relação linear entre as variáveis.

## 📊 Dataset

O dataset `pontuacao_teste.csv` contém as seguintes características:

- **horas_estudo**: Número de horas dedicadas ao estudo (variável independente)
- **pontuacao_teste**: Pontuação obtida no teste (variável dependente)
- **Tamanho**: 102 observações
- **Formato**: CSV (Comma-Separated Values)

### Exemplo dos dados:
```
horas_estudo,pontuacao_teste
1.1,30
2.0,55
2.5,60
3.6,75
4.2,85
```

## 📁 Estrutura do Projeto

```
regressao-linear-simples/
│
├── modelo_pontuacao.ipynb      # Notebook principal com análise e modelo
├── pontuacao_teste.csv         # Dataset com os dados de treino
├── api_modelo_regressao.py     # API REST para predições
├── modelo_regressao.pkl        # Modelo treinado serializado
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do projeto
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passos para instalação

1. Clone o repositório ou baixe os arquivos do projeto

2. Navegue até o diretório do projeto:
```bash
cd regressao-linear-simples
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎯 Como Usar e Reproduzir

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passo a Passo Completo

1. **Clone o repositório ou baixe os arquivos do projeto**

2. **Navegue até o diretório do projeto:**
   ```bash
   cd regressao-linear-simples
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o Notebook Principal:**
   
   Abra o arquivo `modelo_pontuacao.ipynb` no Jupyter Notebook ou VS Code e execute as células sequencialmente para:
   
   - Carregar e explorar os dados
   - Realizar análise exploratória (EDA)
   - Treinar o modelo de regressão linear
   - Validar o modelo com métricas
   - Analisar resíduos
   - Fazer predições
   - Salvar o modelo treinado (`modelo_regressao.pkl`)

5. **Usar a API REST (Opcional):**
   
   Para iniciar a API:
   ```bash
   python api_modelo_regressao.py
   ```
   
   A API estará disponível em `http://localhost:8000`
   
   **Exemplo de uso da API:**
   ```json
   POST /predict
   {
       "horas_estudo": 25.5
   }
   ```
   
   **Resposta esperada:**
   ```json
   {
       "pontuacao_teste": [resultado_da_predicao]
   }
   ```

### Reproduzindo os Resultados

1. Execute o notebook `modelo_pontuacao.ipynb` célula por célula
2. O modelo será salvo automaticamente como `modelo_regressao.pkl`
3. Todas as métricas e gráficos serão gerados durante a execução
4. Para usar a API, execute `python api_modelo_regressao.py` após o treinamento

## 🔬 Metodologia

### 1. Análise Exploratória de Dados (EDA)
- Visualização da distribuição das variáveis
- Análise de correlação (Pearson e Spearman)
- Detecção de outliers usando boxplots
- Gráficos de dispersão para visualizar a relação linear

### 2. Preprocessamento
- Divisão do dataset em treino (70%) e teste (30%)
- Reshape dos dados para compatibilidade com scikit-learn
- Definição de random_state para reprodutibilidade

### 3. Treinamento do Modelo
- Algoritmo: Regressão Linear Simples
- Biblioteca: scikit-learn
- Método: Mínimos Quadrados Ordinários

### 4. Validação do Modelo
- **Métricas utilizadas**:
  - R² (Coeficiente de Determinação)
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - RMSE (Root Mean Squared Error)

### 5. Análise de Resíduos
- Verificação de linearidade
- Teste de homocedasticidade
- Teste de normalidade dos resíduos (Shapiro-Wilk e Kolmogorov-Smirnov)
- Q-Q Plot para avaliação visual da normalidade

## 📈 Resultados

### Equação do Modelo
O modelo treinado segue a equação: **y = ax + b**

Onde:
- **y**: Pontuação no teste
- **x**: Horas de estudo
- **a**: Coeficiente angular (slope)
- **b**: Intercepto

### Métricas de Performance
As métricas específicas são calculadas durante a execução do notebook e incluem:

- **R²**: Indica quanto da variação na pontuação é explicada pelas horas de estudo
- **MAE**: Erro médio absoluto em pontos
- **RMSE**: Raiz do erro quadrático médio
- **Análise de Resíduos**: Validação das premissas da regressão linear

### Exemplos de Predição
- **30.4 horas de estudo** → Pontuação prevista pelo modelo
- **Para obter 600 pontos** → Número de horas necessárias de estudo

## 🌐 API REST

A API foi desenvolvida com FastAPI e oferece:

### Endpoints
- **POST /predict**: Realiza predição baseada nas horas de estudo

### Exemplo de Uso
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "horas_estudo": 20.5
}

response = requests.post(url, json=data)
print(response.json())
```

### Validação de Entrada
- Utiliza Pydantic para validação automática dos dados de entrada
- Tipo de dado: float para horas_estudo

## 🛠️ Tecnologias Utilizadas

### Análise e Modelagem
- **pandas**: Manipulação e análise de dados
- **scikit-learn**: Algoritmos de machine learning
- **numpy**: Computação numérica
- **scipy**: Funções estatísticas

### Visualização
- **matplotlib**: Gráficos básicos
- **seaborn**: Visualizações estatísticas
- **pingouin**: Gráficos estatísticos avançados

### API e Deployment
- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados
- **uvicorn**: Servidor ASGI
- **joblib**: Serialização do modelo

### Ambiente de Desenvolvimento
- **Jupyter Notebook**: Desenvolvimento interativo
- **VS Code**: Editor de código

## 📊 Interpretação dos Resultados

### Quando usar este modelo:
- Quando existe uma relação linear entre horas de estudo e performance
- Para estimativas rápidas de desempenho
- Como baseline para modelos mais complexos

### Limitações:
- Assume relação linear perfeita
- Sensível a outliers
- Não considera outros fatores que podem influenciar a pontuação

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir melhorias
- Adicionar novas funcionalidades
- Melhorar a documentação

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

