class VerificarLink:
    pass


class Usuario:
    def __init__(self, name=None, matricula=None, password=None):
        self.nome = name
        self.mat = matricula
        self.senha = password
        self.tipo = '1'
        self.logado = False
        self.eventos = []

    def AdicionarEvento(self):
        print('INTERFACE ADICIONE UM EVENTO')
        disciplina = input('Informe a disciplina:')
        tipo = input('Informe o tipo de evento:')
        data = input('Informe a data do evento:')
        desc = input('Informe a descrição:')
        diasdeprova = input('Dia da proxima avaliação:')
        evento = {'disciplina': disciplina, 'tipo': tipo, 'data': data, 'descricao': desc,
                  'diasdeprova': diasdeprova}
        self.eventos.append(evento)

    def autenticar(self):
        print('|SEJA BEM VINDO AO INFORFLASH|\n'
              'INFORME NOS CAMPOS ABAIXO AS INFORMAÇÕES NECESSÁRIAS PARA REALIZAR O LOGIN')
        u = input('Informe o nome de usuário:')
        m = input('Informe a matrícula:')
        s = input('Informe a senha:')

        if user1.nome == u and user1.mat == m and user1.senha == s:
            user1.logado = True
            self.interfaceadm()

        elif user2.nome == u and user2.mat == m and user2.senha == s:
            user2.logado = True
            self.interfacealuno()
        else:
            print('Credenciais inválidas! Tente novamente...\n')
            self.autenticar()

    def interfaceadm(self):
        print('\n| INTERFACE ADMINISTRATIVA |\n'
              '|== Selecione uma opção == |\n')

        menu = input('(1) Adicionar eventos:\n'
                     '(2) Cadastrar usuário:\n'
                     '(3) Sair!!!\n')
        if menu == '1':
            self.AdicionarEvento()  # aqui vai para a função AdicionarEventos
        elif menu == '2':
            self.cadastro()
        else:
            print('SAINDO!!!')

        def CriarEvento():
            tipos_permitidos = ['Aviso', 'Prova', 'Aula', 'Atendimento', 'Editais']
            tipo = input( 'ADICIONE O TIPO DE EVENTO: AVISO, PROVAS(DIAS DE PROVAS), AULA(HORÁRIO), ATENDIMENTO(AO ALUNO):')
 # Validação do tipo de evento
            while tipo.title() not in tipos_permitidos:
             print('Tipo de evento inválido. Por favor, escolha um tipo válido.')
             tipo = input('ADICIONE O TIPO DE EVENTO: ')
             desc = input('ADICIONE A DESCRIÇÃO DO EVENTO: ')

             if tipo.title() == 'Aviso':
                 data = input('ADICIONE A DATA DO EVENTO: ')
                 disciplina = input('ADICIONE A DISCIPLINA RELACIONADA: ')
                 link = input('ADICIONE O LINK DO EVENTO (deixe em branco se não houver link): ')
                 while link and not VerificarLink(link):
                     print("LINK INVÁLIDO.")
                     link = input('ADICIONE O LINK DO EVENTO (deixe em branco se não houver link): ')
                     return Evento(tipo.title(), desc, link, data, disciplina)
             elif tipo.title() == 'Editais':
                  link = input('ADICIONE O LINK DO EDITAL: ')
                  while link and not VerificarLink(link):
                      print("LINK INVÁLIDO.")
            link = input('ADICIONE O LINK DO EDITAL: ')
            return Evento(tipo.title(), desc, link)
    else:
    data = input('ADICIONE A DATA DO EVENTO: ')
    disciplina = input('ADICIONE A DISCIPLINA RELACIONADA: ')
    sala = input('ADICIONE A SALA DO EVENTO: ')
    return Evento(tipo.title(), desc,, data, disciplina, sala)

    def interfacealuno(self):
        print('\n| INTERFACE ALUNO |\n'
              '|SEJA BEM VINDO AO MURAL DE AVISOS\n')
              i = input('(1) VER EVENTOS:\n'
              '(2) SAIR:\n')
             if i == '1':
            pass  # aqui eu levo para função ver avisos
        else:
            print('SAINDO...')

    class Evento:
        def __init__(self, tipo, desc, link=None, data=None, disciplina=None, sala=None):
            self.tipo = tipo
            self.descricao = desc
            self.link = link
            self.data = data
            self.disciplina = disciplina
            self.sala = sala

            def verificar_link(link):
                regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
                return re.match(regex, link)

            # Exemplo de uso
            novo_evento = CriarEvento()
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

    def cadastro(self):
        print('\n| INTERFACE DE CADASTRO |\n')
        # self.none = input("")
        v = input('DESEJA FAZER O CADASTRO DE QUAL USUÁRIO: \n'
                  '(1) ALUNO:\n'
                  '(2) ADM:\n')
        self.tipo = v
        if v == '1':
            self.nome = input("Informe o nome do aluno:")
            self.mat = input("Crie uma matricula: ")
            self.senha = input("Crie uma senha:")
        if v == '2':
            self.nome = input("Informe o nome do Adm:")
            self.mat = input("Crie uma matricula: ")
            self.senha = input("Crie uma senha:")

        alunos, adm = [], []

        usu = Usuario()
        if usu.tipo == '1':
            alunos.append(usu)
        elif usu.tipo == '2':
            adm.append(usu)
        else:
            pass
        o = input('\n|Selecione uma opção|\n'
                  '(1) Fazer um novo cadastro:\n'
                  '(2) Sair!!!')
        if o == '1':
            self.cadastro()
        else:
            print('Saindo!!!')


# Criando instâncias de dois usuários
user1 = Usuario('levy', '11', '2')  # usuário adm

user2 = Usuario('ana', '22', '3')  # usuário aluno

# Lista de usuários
usuarios = [user1]
# Verificando as credenciais e direcionando para a interface apropriada
user1.autenticar()