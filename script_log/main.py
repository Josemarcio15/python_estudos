import subprocess
import datetime
import smtplib
from email.message import EmailMessage
import os

# Configurações
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "gestao_vendas"
BACKUP_DIR = "/Users/mac/Documents"
EMAIL_FROM = ""
EMAIL_TO = ""
EMAIL_PASS = ""  # use senha de app se for Gmail

# Criação de nomes de arquivo
agora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = f"{BACKUP_DIR}/backup_{agora}.sql"
log_file = f"{BACKUP_DIR}/log_{agora}.txt"

# Garante que a pasta existe
os.makedirs(BACKUP_DIR, exist_ok=True)

# Comando mysqldump
cmd = [
    "mysqldump",
    f"-u{DB_USER}",
    f"-p{DB_PASSWORD}",
    DB_NAME
]

# Executa e salva a saída e erro no log
with open(backup_file, "w") as out_sql, open(log_file, "w") as out_log:
    try:
        result = subprocess.run(cmd, stdout=out_sql, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            out_log.write("✅ Backup realizado com sucesso.\n")
        else:
            out_log.write("❌ Erro ao realizar backup:\n")
            out_log.write(result.stderr)
    except Exception as e:
        out_log.write(f"❌ Erro inesperado: {e}\n")

# Função para enviar e-mail com log
def enviar_email():
    msg = EmailMessage()
    msg["Subject"] = f"Relatório de Backup MariaDB - {agora}"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    with open(log_file, "r") as f:
        log_content = f.read()

    msg.set_content(log_content)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_PASS)
            smtp.send_message(msg)
    except Exception as e:
        print("Erro ao enviar e-mail:", e)

# Envia log por e-mail
enviar_email()
