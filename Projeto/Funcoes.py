from time import sleep
import locale
import requests
# O locale define o formato regional de números, datas, moedas, etc.
# Aqui, estamos configurando para o padrão brasileiro (pt_BR),
# para que valores em Reais sejam exibidos corretamente como "R$ 1.234,56".
# Em sistemas Linux/macOS usamos 'pt_BR.UTF-8',
# e em sistemas Windows usamos 'Portuguese_Brazil.1252'.
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # MacOS/linux
except:
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252') # Windows

def get_dolar_ptax():
    """
    Busca a cotação atual do dólar (PTAX) usando a AwesomeAPI.
    
    Retorna:
        float: Valor atual do dólar em reais.
    """
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        return float(dados['USDBRL']['bid'])  # valor de compra
    except Exception as e:
        print("Erro ao buscar a cotação do dólar. Usando valor fixo como fallback.")
        return 5.47  # valor de fallback se der erro

def main_menu():
    print("""
===============================
Escolha um conversor Universal
===============================  
⇓ Conversores Disponiveis ⇓
1 -> Celsius / Fahrenheit
2 -> Kmph / Mph
3 -> R$ Reais / $ Dolar
4 -> Minutos / Horas
5 -> Sair     
""")

def retry_or_return():
    """
    Pergunta ao usuário se deseja realizar outra conversão.

    Retorna:
        bool: True se o usuário quiser continuar, False se quiser encerrar.
    """
    while True: 
        parametros_sim = ['sim', 's']       # Parametros de verificação da escolha
        parametros_nao = ['n','não','nao']  # Parametros de verificação da escolha     
        try: # Try usado para tratamento de erros
            opcao = input('\nDeseja converter outro valor?(s/n): ').lower().strip() # Escolha principal
            if opcao in parametros_sim:
                return True  # Resultado da escolha sim
            elif opcao in parametros_nao:
                print(f"\nOk voltando!\n")
                return False  # Resultado da escolha nao  
        except ValueError:
            print(f'Error, vc digitou ["{opcao}"], essa opção não existe.')
            sleep(1)
                
def conversor_celsius_for_fahrenheit():
    """
    Converte temperaturas de Celsius para Fahrenheit.

    Solicita um valor em graus Celsius do usuário,
    realiza a conversão e exibe o resultado.
    """
    while True:
        try:
            celsius = float(input(f"\nDigite quantos graus deseja saber em Fahrenheit: "))
            fahrenheit = (celsius * 9/5) + 32
            sleep(0.5)
            print(f"\n{celsius} Graus Celsius são {fahrenheit} Fahrenheit")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue
        if not retry_or_return():
            break

def conversor_km_for_mile():
    """
    Converte distâncias de quilômetros para milhas.

    Solicita um valor em km do usuário,
    realiza a conversão e exibe o resultado.
    """
    while True:
        try:
            km = float(input(f"\nDigite quantos km deseja saber em Milhas: "))
            km_for_mile = round(km * 0.621371,2)
            sleep(0.5)
            print(f"\n{km}Km são {km_for_mile}mph")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue
        if not retry_or_return():
            break
        
def conversor_real_for_dolar():
    """
    Converte valores em Reais (BRL) para Dólares (USD).

    Solicita um valor em Reais do usuário, formata com o locale brasileiro,
    realiza a conversão usando uma taxa fixa e exibe o resultado.
    """
    while True:
        try:
            valor = input(f"\nDigite quantos Reais deseja saber em Dolares: ").replace(',','.')
            cotacao = get_dolar_ptax()
            real = float(valor)
            dolar = (real / cotacao)
            valor_formatado = locale.currency(real, grouping=True)
            sleep(0.5)
            print(f"\n{valor_formatado} são $ {dolar:,.2f} Dólares (Cotação atual: R$ {cotacao:.2f})")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue
        if not retry_or_return():
            break

def conversor_minute_for_hours():
    """
    Converte minutos para horas.

    Solicita um valor em minutos do usuário,
    realiza a conversão e exibe o resultado.
    """
    while True:
        try:
            minute = float(input(f"\nDigite quantos minutos deseja saber em Horas: "))
            hour = (minute / 60)
            sleep(0.5)
            print(f"\n{minute} minutos são {hour:.0f} hora")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue
        if not retry_or_return():
            break

if __name__ == "__main__":
    conversor_celsius_for_fahrenheit()
    conversor_km_for_mile()
    conversor_real_for_dolar()
    conversor_minute_for_hours()