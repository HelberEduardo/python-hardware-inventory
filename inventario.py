import psutil
import platform
from datetime import datetime

def formatar_bytes(n):
    # Converte bytes para GB
    return f"{n / (1024**3):.2f} GB"

output_file = "Info_System.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    file.write('='*30)
    file.write("\n RELATÓRIO DE HARDWARE \n")
    file.write('='*30)
    file.write('\n')

# Informações do Sistema Operacional
    file.write("\n Informações do Sistema Operacional \n")
    file.write(f"Sistema: {platform.system()} {platform.release()}")
    file.write('\n')
    file.write(f"Arquitetura: {platform.machine()}")
    file.write('\n')

# Informações do Processador
    file.write("\n Informações do Processador \n")
    file.write(f"Processador: {platform.processor()}")
    file.write('\n')
    file.write(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
    file.write('\n')
    file.write(f"Núcleos Lógicos: {psutil.cpu_count(logical=True)}")
    file.write('\n')

# Informações de Memória RAM
    mem = psutil.virtual_memory()
    file.write("\n Informações de Memória RAM \n")
    file.write(f"Memória Total: {formatar_bytes(mem.total)}")
    file.write('\n')
    file.write(f"Memória Disponível: {formatar_bytes(mem.available)}")
    file.write('\n')

# Informações de Disco
    file.write("\n Informações de Disco \n")
    for particao in psutil.disk_partitions():
        try:
            uso = psutil.disk_usage(particao.mountpoint)
            file.write(f"Disco {particao.device} ({particao.mountpoint}):")
            file.write('\n')
            file.write(f"  Total: {formatar_bytes(uso.total)} | Livre: {formatar_bytes(uso.free)}")
            file.write('\n')
        except PermissionError:
            continue

    file.write('\n Informações de Rede \n')
    interfaces = psutil.net_if_addrs()
    for nome_interface, enderecos in interfaces.items():
        file.write(f"Interface: {nome_interface}\n")
    for addr in enderecos:
        if addr.family == 2:  # 2 é o código para IPv4
            file.write(f"IP: {addr.address}\n")
        else:
            print('...')    
file.close()
