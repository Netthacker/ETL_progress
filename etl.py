import pandas as pd
#Abrindo o arquivo csv
file = pd.read_csv('paels_progress.csv')
name = file['Nome'].tolist()
tarefa1 = file['Tarefa1'].tolist()
tarefa2 = file['Tarefa2'].tolist()
tarefa3 = file['Tarefa3'].tolist()
tarefa4 = file['Tarefa4'].tolist()
tarefa5 = file['Tarefa5'].tolist()

user = file[['Nome','Tarefa1','Tarefa2','Tarefa3','Tarefa4','Tarefa5']]
user.loc[:, 'Nome'] = user['Nome'].str.replace('(DTCEA-FZ)', '')

users_not_completed = user[
    (user['Tarefa1'] == 'Não concluído(a)') |
    (user['Tarefa2'] == 'Não concluído(a)') |
    (user['Tarefa3'] == 'Não concluído(a)') |
    (user['Tarefa4'] == 'Não concluído(a)') |
    (user['Tarefa5'] == 'Não concluído(a)')
]

#Salvando o Arquivo em csv
users_not_completed.to_csv('paels_pessoas_faltaram',index=False)

print('Arquivo csv com o nome paels_pessoas_faltaram concluído com sucesso')