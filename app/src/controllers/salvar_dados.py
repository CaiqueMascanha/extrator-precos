import json
from models.precos import Precos, Session

class SalvarDados:
    
    @staticmethod
    def salvar_como_json(dados, nome, diretorio) -> None:
        try:
            diretorio_completo = f'{diretorio}/{nome}'
            with open(diretorio_completo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print(f'Dados salvos em {diretorio_completo}')

        except Exception as e:
            print(f'Erro ao salvar arquivo: {e}')

    @staticmethod
    def salvar_db(dados: dict) -> None:
        session = Session()  # Obtém uma nova sessão

        try:
            tamanho_dados = len(dados['Data'])
            registros = []

            for i in range(tamanho_dados):
                registro = Precos(
                    nome=dados['Nome'][i],
                    preco=dados['Preço'][i].replace('R$ ', '').replace('.', '').replace(',', '.'),
                    link=dados['Link'][i],
                    data=dados['Data'][i]
                )
                registros.append(registro)
            
            # Adiciona todos os registros de uma vez
            session.add_all(registros)
            session.commit()
            print(f'{tamanho_dados} registros salvos no banco de dados.')

        except Exception as e:
            session.rollback()  # Reverte as mudanças em caso de erro
            print(f'Erro ao salvar dados no DB: {e}')
        finally:
            session.close()  # Fecha a sessão
