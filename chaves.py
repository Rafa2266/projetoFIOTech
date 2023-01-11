#Tarefa 2

import mysql.connector
db_connection = mysql.connector.connect(host="localhost", user="root", passwd="mast26@98", database="fiotech_email")
cursor = db_connection.cursor()
cursor.execute("select remetente, destinatario, data_hora, conteudo from arquivo_email")

palavras = []
palavras_nome = []
bodys=[]

for (remetente, destinatario, data_hora, conteudo) in cursor:
    body= remetente+" "+destinatario+" "+data_hora+" "+conteudo
    body=body.replace(' - ', '-')
    bodys.append(body)
    body = body.replace('/', ' ')
    body = body.replace('.', ' ')
    body_array=body.split(' ')
    for pal in body_array:
        pal = pal.replace(',', '')
        pal = pal.replace(' ', '')
        pal = pal.replace('<', '')
        pal = pal.replace('>', '')
        pal = pal.replace("\t", '')
        pal = pal.replace("\n", '')
        pal = pal.replace(':', '')
        pal = pal.replace('#', '')
        pal = pal.replace('?', '')
        pal = pal.replace('"', '')
        if pal != "" and pal!='-' and pal!='/':
            if len(pal)>=2 and (pal[0].isupper() and pal[1].islower()) and pal in destinatario and pal not in remetente and 'Equinix' not in pal:
                if pal not in palavras_nome :
                        palavras_nome.append(pal)
            else:
                if pal.lower() not in palavras:
                    palavras.append(pal.lower())

palavras_nome_filter=[]
palavras_filter=[]
minishow=cursor.rowcount*0.05
for pal in palavras_nome:
    aparicao=0
    for body in bodys:
        body=body.replace("\t", '')
        body = body.replace("\n", '')
        if(pal in body):
            aparicao+=1
        if(aparicao>=minishow):
            palavras_nome_filter.append(pal)
            break

for pal in palavras:
    aparicao=0
    for body in bodys:
        body=body.replace("\t", '')
        body = body.replace("\n", '')
        if(pal in body.lower()):
            aparicao+=1
        if(aparicao>=minishow):
            palavras_filter.append(pal)
            break

bodys=None
cursor.execute("delete from palavra_chave;")
db_connection.commit()
dicio='';
with open('dicionario.txt') as arquivo:
    dicio= arquivo.read()

for pal in palavras_filter:
    type='Outros'
    if(pal in dicio):
        type='Dicionário'
    cursor.execute("INSERT INTO palavra_chave (chave, tipo) VALUES (%s, %s);", (pal, type))

for pal in palavras_nome_filter:
    type='Nome Próprio'
    cursor.execute("INSERT INTO palavra_chave (chave, tipo) VALUES (%s, %s);", (pal, type))

db_connection.commit()
db_connection.close()