# flask com letra minuscula(modulo)
# flask com Maiuscula(Flask) é a classe que vamos importar do modudlo
# url for - para montar url internas de acordo com o nome da função
# Render templates - serve para buscar na pasta template arquivos html ou variaveis 
from flask import Flask
from configuration import configure_all

#inicialização
# app recebe a classe Flask
app = Flask(__name__)

configure_all(app)


app.run(debug=True)

