import nmap  # Importa a biblioteca nmap para realizar scans de rede
import csv  # Importa a biblioteca csv para escrever arquivos CSV
from prettytable import PrettyTable  # Importa PrettyTable para formatar tabelas no terminal

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
    nm = nmap.PortScanner()  # Cria uma instância do PortScanner
    nm.scan(ip, arguments='-O -sV')  # Realiza um scan completo para identificar OS e servicos
    scan_data = {  # Dicionário para armazenar os dados do scan
        'ip': ip,  # IP do host
        'hostname': nm[ip].hostname(),  # Hostname do host
        'state': nm[ip].state(),  # Estado do host (up/down)
        'os': nm[ip]['osmatch'][0]['name'] if 'osmatch' in nm[ip] and nm[ip]['osmatch'] else 'N/A',  # Sistema Operativo
        'ports': []  # Lista para armazenar informacões das portas
    }

    for protocol in nm[ip].all_protocolcols():  # Itera sobre todos os protocolcolos (tcp/udp)
        lport = nm[ip][protocol].keys()  # Lista de portas para o protocolcolo atual
        for port in lport:  # Itera sobre cada porta
            port_info = {  # Dicionário para armazenar informacões da porta
                'port': port,  # Número da porta
                'state': nm[ip][protocol][port]['state'],  # Estado da porta (open/closed)
                'name': nm[ip][protocol][port]['name'],  # Nome do servico
                'version': nm[ip][protocol][port]['version'] if 'version' in nm[ip][protocol][port] else 'N/A'  # Versao do servico
            }
            scan_data['ports'].append(port_info)  # Adiciona as informacões da porta à lista de portas

    return scan_data  # Retorna os dados do scan

# Parte 3: Escrever os resultados em um arquivo e mostrar o output
def write_results_to_markdown(scan_results, filename='scan_results.md'):
    with open(filename, 'w') as mdfile:  # Abre um arquivo para escrita em modo Markdown
        mdfile.write('# Resultados do Scan de Rede\n\n')  # Escreve o título no arquivo
        for result in scan_results:  # Itera sobre os resultados do scan
            mdfile.write(f"## IP: {result['ip']}\n")  # Escreve o IP
            mdfile.write(f"**Hostname**: {result['hostname']}\n")  # Escreve o hostname
            mdfile.write(f"**Estado**: {result['state']}\n")  # Escreve o estado
            mdfile.write(f"**Sistema Operativo**: {result['os']}\n\n")  # Escreve o sistema Operativo
            mdfile.write("### Portas e Servicos:\n")  # Escreve o subtítulo para portas e servicos
            mdfile.write("| Porta | Estado | Servico | Versao |\n")  # Escreve a linha de cabecalho da tabela
            mdfile.write("|-------|--------|---------|--------|\n")  # Escreve a linha de separacao da tabela
            for port_info in result['ports']:  # Itera sobre as informacões das portas
                mdfile.write(f"| {port_info['port']} | {port_info['state']} | {port_info['name']} | {port_info['version']} |\n")  # Escreve os dados das portas na tabela
            mdfile.write("\n")  # Adiciona uma linha em branco

def print_results(scan_results):
    for result in scan_results:  # Itera sobre os resultados do scan
        print(f"IP: {result['ip']}")  # Imprime o IP
        print(f"Hostname: {result['hostname']}")  # Imprime o hostname
        print(f"Estado: {result['state']}")  # Imprime o estado
        print(f"Sistema Operativo: {result['os']}")  # Imprime o sistema Operativo
        print("Portas e Servicos:")  # Imprime o título para portas e servicos
        
        table = PrettyTable()  # Cria uma instância de PrettyTable
        table.field_names = ["Porta", "Estado", "Servico", "Versao"]  # Define os nomes das colunas da tabela
        
        # Define a largura máxima para cada coluna
        table.max_width["Porta"] = 10
        table.max_width["Estado"] = 10
        table.max_width["Servico"] = 20
        table.max_width["Versao"] = 20
        
        for port_info in result['ports']:  # Itera sobre as informacões das portas
            table.add_row([port_info['port'], port_info['state'], port_info['name'], port_info['version']])  # Adiciona uma linha à tabela
        
        print(table)  # Imprime a tabela formatada
        print("\n")  # Adiciona uma linha em branco

# Funcao principal
def main():
    network = input("Digite a rede (exemplo: 192.168.1.0/24): ")  # Solicita ao usuário a rede a ser escaneada
    active_ips = get_active_ips(network)  # Obtém os IPs ativos na rede
    print("IPs ativos na rede:", active_ips)  # Imprime os IPs ativos
    
    scan_results = [scan_ip(ip) for ip in active_ips]  # Realiza o scan em todos os IPs ativos
    print_results(scan_results)  # Imprime os resultados no terminal
    write_results_to_markdown(scan_results)  # Escreve os resultados em um arquivo Markdown
    print(f"Resultados escritos em 'scan_results.md'")  # Informa ao usuário que os resultados foram escritos no arquivo

if __name__ == "__main__":
    main()  # Chama a funcao principal se o script for executado diretamente
