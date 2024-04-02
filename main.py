import re

class Evento:
    def __init__(self, tipo, descricao, link=None, data=None, disciplina=None, sala=None):
        self.tipo = tipo
        self.descricao = descricao
        self.link = link
        self.data = data
        self.disciplina = disciplina
        self.sala = sala


def criar_evento():
    tipos_permitidos = ['Aviso', 'Prova', 'Aula', 'Atendimento', 'Editais']
    tipo = input('ADICIONE O TIPO DE EVENTO: AVISO, PROVAS(DIAS DE PROVAS), AULA(HORÁRIO), ATENDIMENTO(AO ALUNO):')

    # Validação do tipo de evento
    while tipo.title() not in tipos_permitidos:
       print('Tipo de evento inválido. Por favor, escolha um tipo válido.')
       tipo = input('ADICIONE O TIPO DE EVENTO: ')

    descricao = input('ADICIONE A DESCRIÇÃO DO EVENTO: ')

    if tipo.title() == 'Aviso':
        data = input('ADICIONE A DATA DO EVENTO: ')
        disciplina = input('ADICIONE A DISCIPLINA RELACIONADA: ')
        link = input('ADICIONE O LINK DO EVENTO (deixe em branco se não houver link): ')
        while link and not verificar_link(link):
            print("LINK INVÁLIDO.")
            link = input('ADICIONE O LINK DO EVENTO (deixe em branco se não houver link): ')
        return Evento(tipo.title(), descricao, link, data, disciplina)

    elif tipo.title() == 'Editais':
        link = input('ADICIONE O LINK DO EDITAL: ')
        while link and not verificar_link(link):
            print("LINK INVÁLIDO.")
            link = input('ADICIONE O LINK DO EDITAL: ')
        return Evento(tipo.title(), descricao, link)
    else:
        data = input('ADICIONE A DATA DO EVENTO: ')
        disciplina = input('ADICIONE A DISCIPLINA RELACIONADA: ')
        sala = input('ADICIONE A SALA DO EVENTO: ')
        return Evento(tipo.title(), descricao, None, data, disciplina, sala)

def verificar_link(link):
    regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.match(regex, link)

# Exemplo de uso
novo_evento = criar_evento()
if novo_evento:
    print("\nEVENTO REGISTRADO COM SUCESSO:")
    print("\nCATEGORIA:", novo_evento.tipo)
    print("DESCRIÇÃO:", novo_evento.descricao)
    if novo_evento.data:
        print("DATA:", novo_evento.data)
    if novo_evento.disciplina:
        print("DISCIPLINA:", novo_evento.disciplina)
    if novo_evento.sala:
        print("SALA:", novo_evento.sala)
    if novo_evento.link:
        print("LINK:", novo_evento.link)
