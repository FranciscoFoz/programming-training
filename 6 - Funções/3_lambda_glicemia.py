# LAMBDA GLICEMIA

'''
Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados
e gostaria de rotular os dados da seguinte maneira:

- Glicose igual ou inferior a 70: 'Hipoglicemia'
- Glicose entre 70 a 99: 'Normal'
- Glicose entre 100 e 125: 'Alterada'
- Glicose superior a 125: 'Diabetes'

A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension
contendo o rótulo e o valor da glicemia em cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

'''

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]


classifica_glicemia = lambda lista_glicemia: [
    (glicemia, 'Hipoglicemia') if glicemia <= 70 
    else
    (glicemia, 'Normal') if 70 < glicemia < 99 
    else
    (glicemia, 'Alterada') if 100 < glicemia < 125 
    else
    (glicemia, 'Diabetes') for glicemia in lista_glicemia
]

print(classifica_glicemia(glicemia))
