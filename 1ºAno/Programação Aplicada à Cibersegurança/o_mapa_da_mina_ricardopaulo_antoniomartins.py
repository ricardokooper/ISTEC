#Ricardo Paulo - 2023368 & Antonio Martins - 2023367


import nmap  # Importa a biblioteca nmap para realizar scans de rede
from tabulate import tabulate  # Importa tabulate para formatar tabelas

# Parte 1: Identificar IPs ativos na rede
def get_active_ips(network):
    nm = nmap.PortScanner()  # Cria uma instância do PortScanner
    nm.scan(hosts=network, arguments='-sn')  # Realiza um ping scan para identificar hosts ativos
    active_ips = []  # Lista para armazenar IPs ativos
    
    for host in nm.all_hosts():  # Itera sobre todos os hosts encontrados
        if nm[host].state() == 'up':  # Se o host está ativo
            active_ips.append(host)  # Adiciona o IP ativo à lista
    
    return active_ips  # Retorna a lista de IPs ativos

# Parte 2: Identificar e caracterizar máquinas
def scan_ip(ip):
    nm = nmap.PortScanner()  
    nm.scan(ip, arguments='-O -sV')  # scan completo para identificar OS e servicos
    scan_data = {  # Dicionário para armazenar os dados do scan
        'ip': ip,  # IP do host
        'hostname': nm[ip].hostname(),  # Hostname do host
        'state': nm[ip].state(),  # Estado do host (up/down)
        'os': nm[ip]['osmatch'][0]['name'] if 'osmatch' in nm[ip] and nm[ip]['osmatch'] else 'N/A',  # Sistema Operativo
        'ports': []  # Lista para armazenar informacões das portas
    }

    for proto in nm[ip].all_protocols():  # Itera sobre todos os protocolos (tcp/udp)
        lport = nm[ip][proto].keys()  # Lista de portas para o protocolo atual
        for port in lport:  # Itera sobre cada porta
            port_info = {  # Dicionário para armazenar informacões da porta
                'port': port,  # Número da porta
                'state': nm[ip][proto][port]['state'],  # Estado da porta (open/closed)
                'name': nm[ip][proto][port]['name'],  # Nome do servico
                'version': nm[ip][proto][port]['version'] if 'version' in nm[ip][proto][port] else 'N/A'  # Versao do servico
            }
            scan_data['ports'].append(port_info)  # Adiciona as informacões da porta à lista de portas

    return scan_data  # Retorna os dados do scan

# Funcao ajustar a tabela e ficar sempre OK
def truncate(string, length):
    return string[:length].ljust(length)

# Parte 3: Escrever os resultados em um ficheiro md e mostrar o output
def write_res_to_file(scan_results, filename='scan_results.md'):
    with open(filename, 'w') as mdfile:
        mdfile.write('# Resultados do Scan de Rede\n\n')  # Escreve o titulo do ficheiro
        for result in scan_results:  # Itera sobre os resultados do scan
            mdfile.write(f"## IP: {result['ip']}\n")  # Escreve o IP
            mdfile.write(f"**Hostname**: {result['hostname']}\n")  # Escreve o hostname
            mdfile.write(f"**Estado**: {result['state']}\n")  # Escreve o estado
            mdfile.write(f"**Sistema Operativo**: {result['os']}\n\n")  # Escreve o sistema Operativo
            mdfile.write("### Portas e Servicos:\n")
            table_data = [[truncate(str(port_info['port']), 10), truncate(port_info['state'], 10), truncate(port_info['name'], 20), truncate(port_info['version'], 20)] for port_info in result['ports']]
            mdfile.write(tabulate(table_data, headers=["Porta", "Estado", "Servico", "Versao"], tablefmt="pipe"))
            mdfile.write("\n\n") # ajustar tabela

def print_results(scan_results):
    for result in scan_results:  #resultados do scan
        print(f"IP: {result['ip']}")  #IP
        print(f"Hostname: {result['hostname']}")  #hostname
        print(f"Estado: {result['state']}")  #estado
        print(f"Sistema Operativo: {result['os']}")  #sistema Operativo
        print("Portas e Servicos:")  #titulo para portas e servicos

        table_data = [[truncate(str(port_info['port']), 10), truncate(port_info['state'], 10), truncate(port_info['name'], 20), truncate(port_info['version'], 20)] for port_info in result['ports']]
        print(tabulate(table_data, headers=["Porta", "Estado", "Servico", "Versao"], tablefmt="pretty"))
        print("\n")

# Funcao principal
def main():
    network = input("Indique a rede (exemplo: 192.168.1.0/24): ")  # Solicita ao user a rede a ser scanneada
    active_ips = get_active_ips(network)  #IPs ativos na rede
    print("IPs ativos na rede:", active_ips)  #mostra os IPs ativos
    
    scan_results = [scan_ip(ip) for ip in active_ips]  # Realiza o scan em todos os IPs ativos
    print_results(scan_results)  # mostra resultados no terminal
    write_res_to_file(scan_results)  # Escreve os resultados em um ficheiro Markdown
    print(f"Resultados guardados em 'scan_results.md'")  # Informa ao utilizador que os resultados foram escritos no ficheiro

if __name__ == "__main__":
    main()  # Chama a funcao principal se o script for executado diretamente
