from controllers.extrair import Extrair
from controllers.salvar_dados import SalvarDados

URL = 'https://www.nike.com.br/nav/genero/masculino/idade/adulto/tamanho/41/tipodeproduto/calcados'
CLASSE_PAI = 'jTaZqn'
CLASSE_NOME_PRODUTO = 'ejEtGo'
CLASSE_PRECO_PRODUTO = 'iaylhM'
CLASSE_PAGINAS = 'dIiRQk'



site = Extrair(URL)
site.acessar_site()
dados = site.buscar_elemento_classe(CLASSE_PAI, CLASSE_NOME_PRODUTO, CLASSE_PRECO_PRODUTO, CLASSE_PAGINAS)
SalvarDados().salvar_como_json(dados, "dados_nike.json", "C:/Projetos M2/Pessoal/webscraping/precos")
SalvarDados().salvar_db(dados)