import pandas as pd


gabarito_dos_estudantes = []  #lista com todas as  respostas de todos os estudantes

planilha_do_gabarito = pd.read_excel('Gabarito.xlsx') #
planilha_respostas_estudantes = pd.read_excel('Respostas.xlsx') # 
acertos = [] #Lista que vai guardar o resultado geral


lista_nomes_estudantes = []
for nome in planilha_respostas_estudantes['aluno_nome']: #Criando uma lista com todos os nomes dos alunos da planilha
    if nome not in lista_nomes_estudantes:  
        lista_nomes_estudantes.append(nome)


gabarito_lista = []
for gab in planilha_do_gabarito['Gabarito']:  #adicionando o gabarito oficial da prova em uma lista
    gabarito_lista.append(gab)

for resEST in planilha_respostas_estudantes['resp_aluno']:
    p = str(resEST)
    a = p.upper()
    gabarito_dos_estudantes.append(a)        #colocandos as respostas em letra maiuscula para ficar igual com  os caracteres do gabarito


def notas_individuais_calculo():    
    media_geral = 0
    loop_control = 0 
    inicio = 0
    final = 90
    while loop_control < len(lista_nomes_estudantes): 
        
        aluno = lista_nomes_estudantes[loop_control]
        respostas_por_aluno = (gabarito_dos_estudantes[inicio:final])#acessa a lista de todas as respostas somando 90 unidades que é a quantidade de questões por estudante e coloca dentro de respotas_por_aluno
        #print(respostas_por_aluno) 
        l = 0
        acertos_totais = 0
        while l < len(gabarito_lista): 
            if respostas_por_aluno[l] == gabarito_lista[l]:  #comparando a resposta do estudante com o gabarito oficial
                acertos_totais =  acertos_totais + 1 
        
                l = l +1
            else:
                l = l +1
        #calculo das notas:
        media_aluno = ((acertos_totais/90)*100)   
        media_geral = media_aluno + media_geral    
        student = [] #para cada estudante cria  uma lista nova, que é  colocado dentro da lista de acertos
        student.append(f'{aluno}') #nome do aluno
        student.append(f'{media_aluno:.2f}') 
        student.append(f'{acertos_totais}/90') 
        acertos.append(student)
        inicio = inicio + 91 - 1
        final = final + 91 - 1
        loop_control = loop_control+1
        global media_geral_calculo
        media_geral_calculo = media_geral/len(lista_nomes_estudantes)
        
notas_individuais_calculo()
for estudante in acertos: 
    print(estudante)
print(f'A média geral dos estudantes foi de {media_geral_calculo:.3f}')
media_geral_calculo_2f  = (f'{media_geral_calculo:.2f}')
media_alunos_total = ['Média geral:',media_geral_calculo_2f, '-']
dataFrame = pd.DataFrame(acertos)
dataFrame.columns = ['Nome','Média de acertos','Total de acertos'] 
dataFrame.loc[len(dataFrame)] = media_alunos_total #adicionando uma linha para colocar a média geral

dataFrame.to_excel('ResultadoSimulado.xlsx')
print('Um arquivo chamado "ResultadoSimulado.xlsx" foi criado com o resultado dos estudantes')


    




