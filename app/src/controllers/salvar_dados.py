import json

class SalvarJson:
    
    @staticmethod
    def salvar_como_json(dados, nome, diretorio):
        try:
            diretorio_completo = f'{diretorio}/{nome}'
            with open(diretorio_completo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print(f'Dados salvos em {diretorio_completo}')

        except Exception as e:
            print(f'Erro ao salvar arquivo: {e}')