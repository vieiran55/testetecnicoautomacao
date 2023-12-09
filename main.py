from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import csv

# iniciar o chromedriver
def iniciar_driver():
    # definir caminho do chromeDriver
    webdriver_path = r'.\chromedriver_win32\chromedriver.exe'
    # inicar o service do chrome
    service = ChromeService(executable_path=webdriver_path)
    return webdriver.Chrome(service=service)

# definir regras de login, passandos os paramentros que a função deve receber. driver, username e password
def fazer_login(driver, username, password):
    esperar_um_segundo()
    #localizar o nome id username e inserir o nome do usuario
    driver.find_element(By.ID, "user-name").send_keys(username)
    esperar_um_segundo()
    #localizar o nome id password e inserir o password
    driver.find_element(By.ID, "password").send_keys(password)
    esperar_um_segundo()
    #localizar o botao de login e clicar
    driver.find_element(By.ID, "login-button").click()

# função para adicionar itens no carrinho, recebendo o driver e tupla de argumentos
def adicionar_itens_ao_carrinho(driver, item_ids):
    #um for passrá dentro de itens_id execuntando cada adição de item
    for item_id in item_ids:
        esperar_um_segundo()
        # encontrar os items de carrihno por id e clicar os adicionando
        driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

# função para finalizar o carrinho de compras, recebendo o driver, o primeiro nome, o ultimo nome e o codigo postal
def finalizar_compra(driver, first_name, last_name, postal_code):
    esperar_um_segundo()
    # localiza e adiciona ao input o firtname
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    esperar_um_segundo()
    # localiza e adiciona ao input o lastname
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    esperar_um_segundo()
    # localiza e adiciona ao input o codigo postal
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    esperar_um_segundo()
    # localiza e clica para continuar
    driver.find_element(By.ID, "continue").click()

# função para adicionar 1 segundo de delay entre as ações
# adicionei esta função para mostrar em slow o funionamento da aplicação    
def esperar_um_segundo():
    time.sleep(1)

# função main
def main():
    # driver recebe a função iniciar_driver
    driver = iniciar_driver()

    # optei por fazer uma construção de controle de fluxo
    try:
        # driver recebe o site a ser trabalhado
        driver.get('https://www.saucedemo.com')

        # um with para abrir o arquivo onde será encontrado login e senha
        with open('informacoes_login.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # username e password sendo recebidos da coluna username e password
                username = row['username']
                password = row['password']

                # com o chorme drive iniciado o site aberto faremos o login passando os argumentos exigitos pela função
                fazer_login(driver, username, password)

                
                esperar_um_segundo()
                # vamos adicionar os itens ao carrinho, de igual forma passando os argumentos a função.
                adicionar_itens_ao_carrinho(driver, 'sauce-labs-backpack', 'sauce-labs-bolt-t-shirt', 'sauce-labs-fleece-jacket')

                esperar_um_segundo()
                # vamos localizar o carrinho de compras #shopcart e aciona-lo com um click
                driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

                esperar_um_segundo()
                # vamos localizar o botao de chekout e aciona-lo
                driver.find_element(By.ID, "checkout").click()

                esperar_um_segundo()
                # vamos finalizar a compra passando os dados do usuário, nome, sobrenome e cep
                finalizar_compra(driver, "Antonio Leoncio", "Vieira Neto", "70675-800")

                esperar_um_segundo()
                # agora recebemos o valor total da class e armazenamos em uma variavel
                total_element = driver.find_element(By.CLASS_NAME, "summary_info_label.summary_total_label")
                total_text = total_element.text

                esperar_um_segundo()
                # clicamos em finalizar para encerrar a compra
                driver.find_element(By.ID, "finish").click()

                # imprimimos o valor total da compra
                print(total_text)
                
                
    #captura de erro e print do mesmo
    except Exception as e:
        print(f"Erro no programa: {e}")
        
    finally:
        # encerramos a compra
        driver.quit()

# executamos a função main
if __name__ == "__main__":
    main()
