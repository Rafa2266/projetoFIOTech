#Tarefa 1
from pathlib import Path
import mysql.connector
db_connection = mysql.connector.connect(host="localhost", user="root", passwd="mast26@98", database="fiotech_email")
cursor = db_connection.cursor()
cursor.execute("delete from arquivo_email;")
db_connection.commit()
pathm = Path('Mensagens v02')
for x in pathm.iterdir():
    if x.is_file() and '.txt' in x.name:
        email = '';
        with open('Mensagens v02/'+x.name) as arquivo:
            email = arquivo.read()
        if 'De:' in email:
            email_array=email.split('\n')
            remetente = email_array[0].split(':\t')[1]
            data_hora = email_array[1].split(':\t')[1]
            destinatario = email_array[2].split(':\t')[1]
            conteudo = email.split('ssunto:\t')[1]
            sql = "INSERT INTO arquivo_email (nome_arquivo, remetente, destinatario, data_hora, conteudo) VALUES (%s, %s, %s, %s, %s);"
            values = (x.name[:-4], remetente, destinatario, data_hora, conteudo)
            cursor.execute(sql,values)


db_connection.commit()
db_connection.close()






