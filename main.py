import os

def processar_resposta(resposta,nome):
    if resposta == '1':
        horarios = input(f'{os.linesep} - Tudo bem {nome} Horarios disponiveis :'
                  f'14:00-15:00-16:00 {os.linesep}')
        while horarios != 0:
            print(f'Seu horario esta marcado para as {horarios}, estaremos te aguardando{os.linesep}')
            break
    elif resposta == '2':
        marcado = input(f'{os.linesep} - Tudo bem {nome} Qual horario gotaria de cancelar? {os.linesep}')
        while marcado != 0:
            print(f'Seu horario das {marcado} horas foi cancelado com sucesso, obrigado!{os.linesep}')
            break
    elif resposta == '3':
        print(f'Aguarde em breve iremos atende-lo {os.linesep}')

    else:
        print('Digite opção valida')


def start():
    # Apresentar o chatbot
      print('Olá bem vinda ao xxxx')
    # Salvar o nome
      nome = input(print('Diga seu nome: '))

      while True:
            # Menu de opções
            resposta = input(f'Olá {nome}, para proseguir digite uma opção:{os.linesep} -Para agendamento digite 1!{os.linesep}'
            f' - Para cancelamento digite 2!{os.linesep} - Para falar com uma pessoa digite 3! {os.linesep}')
            # Processamento de resposta
            processar_resposta(resposta,nome)
if __name__ == '__main__':
         start()