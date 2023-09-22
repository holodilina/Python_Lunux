import paramico

def ssh_checkout(host, user, passwd, cmd, text, port=22):
    client = paramico.SSHClient() 
    client.set_missing_host_key_policy(paramico.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    if text in out and exit_code == 0:
       return True
    else:
       return False

def upload_files(host, user, passwd, local_path, remote_path, port=22):
    print(f"Загружаем файл {local_path} в каталог {remote_path}")
    transport = paramico.Transport((host, port))
    trafnsport.connect(None, username=user, password=passwd)
    sfpt = paramico.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    if sftp:
        sftp.close()
    if transport.close()
    
