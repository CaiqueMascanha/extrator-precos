from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime

class Extrair:
    def __init__(self, url) -> None:
        self.driver = webdriver.Chrome()
        self.URL = url
        self.aceitou_cookies = False
        self.proximo = True

    def acessar_site(self) -> None:
        self.driver.get(self.URL)

    def aceitar_cookies(self) -> None:
        try:
            # Esperar até que um botão de aceitar cookies apareça
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Aceitar') or contains(text(), 'OK') or contains(text(), 'Fechar')]"))
            )
            # Tentar clicar no botão
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Aceitar') or contains(text(), 'OK') or contains(text(), 'Fechar')]").click()
            print("Cookies aceitos.")
        except Exception as e:
            print("Nenhum botão de aceitar cookies encontrado:")

    def proxima_pagina(self) -> None:
        try:
            proximo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@aria-label, 'Próxima página') or contains(@aria-label, 'Next page') or contains(@aria-label, 'Próximo')]"))
            )
            proximo.click()
            print("Próxima página clicada.")
        except Exception as e:
            print(f'Erro ao clicar na próxima página')
            self.proximo = False  # Marcar que não há mais próxima página

    def esperar_elementos_carregar(self, classe_pai) -> None:
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, classe_pai))
        )
        sleep(5)  # Ajuste o tempo de espera para garantir o carregamento completo da página

    def buscar_elemento_classe(self, classe_pai, classe_nome_produto, classe_preco_produto, CLASSE_PAGINAS) -> dict:
        data_consulta = datetime.now().strftime('%Y-%m-%d %H:%M')
        numero_paginas = int(self.driver.find_elements(By.CLASS_NAME, CLASSE_PAGINAS)[-1].text)

        dados = {
            "Data": [],
            "Nome": [],
            "Preço": [],
            "Link": []
        }

        for i in range(1, numero_paginas + 1):

            print(f'Página: {i}')
            
            # Esperar que todos os elementos da página estejam carregados
            self.esperar_elementos_carregar(classe_pai=classe_pai)
            
            tenis = self.driver.find_elements(By.CLASS_NAME, classe_pai)
            for t in tenis:
                try:
                    nome = t.find_element(By.CLASS_NAME, classe_nome_produto).text
                    preco = t.find_element(By.CLASS_NAME, classe_preco_produto).text
                    link = t.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    
                    dados['Data'].append(data_consulta)
                    dados['Nome'].append(nome)
                    dados['Preço'].append(preco)
                    dados['Link'].append(link)
                except Exception as e:
                    print(f"Erro ao extrair dados do elemento: {e}")

            if i < numero_paginas:  # Apenas tente ir para a próxima página se houver mais páginas
                self.proxima_pagina()
            else:
                print("Última página alcançada.")
                break

            # Garantir que os cookies sejam aceitos apenas uma vez
            if not self.aceitou_cookies:
                self.aceitar_cookies()
                self.aceitou_cookies = True
                
        return dados
