# PS-EinsteinFloripa

Projeto para o Processo seletivo Einstein Floripa

Para rodar o código se certifique de que as planilhas de gabaritos e respostas estejam na mesma pasta do arquivo main.py .
Caso ocorra o erro "FileNotFoundError" altere o caminho das variaveis "planilha_do_gabarito" ou "planilha_respostas_estudantes" que estão na linha 6 e 7, respectivamente.

Além disso, é necessário ter a biblioteca "Pandas" instalado no ambiente em que o código será executado.
Caso não tenha, abra seu terminal e digite o comando "pip install pandas"

Funcionamento do código:

O codigo inicia lendo as tabelas de gabaritos e respostas dos estudantes que foram fornecidas para o processo seletivo, e armazena nas variaveis planilha_do_gabarito e planilha_respostas_estudantes, respectivamente.

Em seguida, existem 3 laços de repetição que são executados:

o primeiro serve para pegar todos os estudantes da coluna "aluno_nome" a adiciona a uma lista chamada 'lista_nomes_estudantes";

o segundo coleta o gabarito da prova e armazena cada resposta em uma lista chamada 'gabarito_lista';

O último coleta todas as respostas que estão na coluna 'resp_aluno' e coloca cada uma delas em uma lista chamada 'gabarito_dos_estudantes'.

Coletada todas essas informações, a função chamada 'notas_individuais_calculo' é definida
Assim, se inicia um loop que itera cada estudante da lista, fatiando a lista gabarito_do_estudantes para pegar a resposta do respectivo estudante.
Depois, as variaveis 'inicio' e 'final' sofrem um incremento de 90, para pegar as proximas respostas
Por fim, cada estudante e suas notas são adicionadas em uma lista chamada 'student', que é adicionada a outra lista chamada 'acertos'

Os resultados de todos os estudantes podem ser vizualizados tanto no console como no aquivo que é gerado.
print do resultado no console:
![image](https://github.com/grodrigues04/PS-EinsteinFloripa/assets/86443574/67a4b2c6-53eb-455e-8d02-2a219a9654d8)


