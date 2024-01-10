import paramiko
import pandas as pd

#=== Adicionar credenciais 
ssh_host = '15.235.110.107'
ssh_port = 2205
ssh_user = ''
ssh_password = ''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(ssh_host, port=ssh_port, username=ssh_user, password=ssh_password)
    sftp_client = ssh_client.open_sftp()
    print('conectado')
except:
    print('Falha na conexão, credenciais possivelmente incorretas')
    exit()

#=== IMPORTANTE ===#
# O conjunto de dados CAGED é grande de mais para ser lido de uma vez dentro de um DataFrame, por isso
# a variável 'chunk_size' é responsável por delimitar um pedaço menor do conjunto de dados, possibilitando
# sua leitura por partes. Caso seja necessário ler o arquivo inteiro, basta tirar o comentário da linha
# 'df_completo = pd.read_csv(file)' (não recomendado pelo tempo de leitura do arquivo)

remote_path = '/opt/dados/caged_2021.csv'
chunk_size = 10000

with sftp_client.open(remote_path) as file:
    chunks = pd.read_csv(file,chunksize=chunk_size)
    #df_completo = pd.read_csv(file)
    
    #=== Aqui podem ser realizadas ações dentro de um pedaço do conjunto de dados
    for chunk in chunks:
       pass