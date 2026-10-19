from colorama import Fore, Style, init
init()

niveis_reservatorio_cores = {
    1: Fore.RED,
    2: Fore.YELLOW,
    3: Fore.GREEN,
    4: Fore.CYAN,
    5: Fore.BLUE,
}

niveis_reservatorio_mensagens = {
    1: 'Nível Muito Baixo (Crítico)',
    2: 'Nível Baixo',
    3: 'Nível Médio',
    4: 'Nível Alto',
    5: 'Nível Muito Alto (Alerta)',
}

def obter_cor_texto(nivel_reservatorio):
    return niveis_reservatorio_cores.get(nivel_reservatorio, Fore.BLACK)
     
def obter_mensagem(nivel_reservatorio):
    return niveis_reservatorio_mensagens.get(nivel_reservatorio, 'Nível Inválido')

nivel_reservatorio = 2
cor_texto = obter_cor_texto(nivel_reservatorio)
mensagem = obter_mensagem(nivel_reservatorio)
print(cor_texto + mensagem + Style.RESET_ALL) # Reseta a cor depois de exibir no terminal
