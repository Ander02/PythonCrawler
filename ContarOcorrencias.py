#imports
import urllib.request;
import json;
from flask import Flask, request, render_template;

#Definindo o App
app = Flask(__name__);

#Rota da página inicial
@app.route('/')
def index():
	#Renderiza o template index.html
	return render_template('index.html');

#Rota da API
@app.route('/api/ocorrencias/<criterio>/<path:url>', methods=['GET'])
def contarOcorrencias(criterio, url):
	try:
		#Html do site obtido através dessa url
		htmlDoSite = urllib.request.urlopen(url).read();
		#Converter para string
		htmlDoSite = str(htmlDoSite);
		#Contar o número de ocorrências
		ocorrencias = htmlDoSite.count(criterio);
	except Exception as e:
		#Se ocorrer um erro, ocorrências recebe -1
		ocorrencias = -1;
	
	#Retorna um json com as ocorrências da palavra
	return json.dumps({'ocorrencias': ocorrencias});

#Executar a aplicação
if __name__ == '__main__':
	app.run(debug = True);
