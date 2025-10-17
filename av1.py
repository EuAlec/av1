print('''
      ================================
          Escola Excelência Rubra
        Bem vindo ao Sistema Interno
      ================================
      
      ''')

while True:
    try:
        repeticao = int(input('Quantos alunos serão cadastrados? '))

        if repeticao <= 0:
            print('Informe uma quantidade válida! ')
            continue
        break
    except ValueError:
        print('Só é possível informar números inteiros. Tente novamente: ')

listaTotal = []

for i in range(repeticao):

    lista = []

    print(f'Cadastro do {i + 1}ª aluno do total de {repeticao} alunos.')

    nomeAluno = input('Insira o nome do(a) Aluno(a): ')
    nomeAlunoFinal = f'Aluno(a): {nomeAluno}'
    lista.append(nomeAlunoFinal)

    while True:
        try:
            nota1 = float(input(f'Insira a 1ª nota do(a) {nomeAluno}: '))
            if 0 <= nota1 <= 10:
                break
            else:
                print(f'Informe uma nota válida (entre 0 e 10) para {nomeAluno}')
        except ValueError:
            print('Digite somente números')

    nota1Texto = f'1ª nota: {nota1}'
    lista.append(nota1Texto)
    
    while True:
        try:    
            nota2 = float(input(f'Insira a 1ª nota do(a) {nomeAluno}: '))
            if 0 <= nota2 <= 10:
                break
            else:
                print(f'Informe uma nota válida (entre 0 e 10) para {nomeAluno}')
        except ValueError:
            print('Digite somente números')

    nota2Texto = f'2ª nota: {nota2}'
    lista.append(nota2Texto)

    while True:
        try:    
            nota3 = float(input(f'Insira a 1ª nota do(a) {nomeAluno}: '))
            if 0 <= nota3 <= 10:
                break
            else:
                print(f'Informe uma nota válida (entre 0 e 10) para {nomeAluno}')
        except ValueError:
            print('Digite somente números')

    nota3Texto = f'3ª nota: {nota3}'
    lista.append(nota3Texto)

    media = (nota1 + nota2 + nota3) / 3
    mediaFinal = f'A media final do(a) {nomeAluno} é de: {media:.1f}'
    lista.append(mediaFinal)

    if media >= 7.0:
        situacao = 'Aprovado(a)'
    elif media < 5.0:
        situacao = 'Reprovado(a)'
    else:
        situacao = 'Recuperação'
    situacaoFinal = f'A situação final do(a) {nomeAluno} é: {situacao.upper()}'
    lista.append(situacaoFinal)

    listaTotal.append(lista)


print(f'''
      ================================
          Escola Excelência Rubra
         Relatório Final de Alunos
      ================================
''')
    
for aluno in listaTotal:
    print(aluno)
    print('=' * 100)