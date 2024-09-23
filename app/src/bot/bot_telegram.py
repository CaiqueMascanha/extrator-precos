from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
import sys

# Adiciona o diretório SRC ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.extrair import Extrair

load_dotenv()

class BotPrecosTelegram:
    def __init__(self) -> None:
        self.API_KEY = os.getenv('API_BOT')
        self.user_name = None  # Variável para armazenar o nome do usuário

    # Função que será chamada quando o comando /start for enviado
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if self.user_name is None:
            await update.message.reply_text('Bem vindo ao bot de obter preços!')
        

    # Função que armazena o nome do usuário e envia uma saudação
    async def extrair(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        URL = 'https://www.nike.com.br/nav/genero/masculino/idade/adulto/tamanho/41/tipodeproduto/calcados'
        CLASSE_PAI = 'jTaZqn'
        CLASSE_NOME_PRODUTO = 'ejEtGo'
        CLASSE_PRECO_PRODUTO = 'iaylhM'
        CLASSE_PAGINAS = 'dIiRQk'
        await update.message.reply_text(f'iniciando captura de dados!')
        await update.message.reply_text(f'Por favor, aguarde!')


        site = Extrair(URL)
        site.acessar_site()
        dados = site.buscar_elemento_classe(CLASSE_PAI, CLASSE_NOME_PRODUTO, CLASSE_PRECO_PRODUTO, CLASSE_PAGINAS)
        tamanho = len(dados['Data'])


        for i in range(tamanho):
            await update.message.reply_text(f'''
                                            Ténis: {dados['Link'][i]}
                                            ''')
        
        await update.message.reply_text('Extração finalizada!')


    def main(self):
        # Inicializa a aplicação
        app = ApplicationBuilder().token(self.API_KEY).build()

        # Adiciona o handler para o comando /start
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("extrair", self.extrair))


        # Inicia o bot
        app.run_polling()

if __name__ == '__main__':
    tel = BotPrecosTelegram()
    tel.main()
