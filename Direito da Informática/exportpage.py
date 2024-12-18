from PyPDF2 import PdfReader, PdfWriter

def exportar_paginas_pdf_interativo():
    """
    Exporta páginas específicas de um PDF com entradas simplificadas fornecidas pelo usuário.
    """
    try:
        # Solicita o nome do arquivo PDF de entrada
        arquivo_entrada = input("Digite o nome do arquivo PDF de entrada (exemplo: entrada.pdf): ")

        # Lê o intervalo de páginas
        intervalo = input("Digite o intervalo de páginas para exportar (exemplo: 1-3 ou 1,3,5): ")
        
        # Processa o intervalo de páginas
        if "-" in intervalo:
            inicio, fim = map(int, intervalo.split("-"))
            paginas = list(range(inicio, fim + 1))
        else:
            paginas = list(map(int, intervalo.split(",")))

        # Solicita o nome do arquivo PDF de saída
        arquivo_saida = input("Digite o nome do arquivo PDF de saída (exemplo: saida.pdf): ")

        # Lê o PDF de entrada
        leitor = PdfReader(arquivo_entrada)
        escritor = PdfWriter()

        # Adiciona as páginas selecionadas ao novo PDF
        for pagina in paginas:
            # Ajusta para índice baseado em 0
            escritor.add_page(leitor.pages[pagina - 1])

        # Escreve o novo arquivo PDF
        with open(arquivo_saida, "wb") as saida:
            escritor.write(saida)

        print(f"Novo arquivo PDF criado com sucesso: {arquivo_saida}")

    except FileNotFoundError:
        print("Erro: O arquivo especificado não foi encontrado.")
    except ValueError:
        print("Erro: O intervalo de páginas é inválido.")
    except IndexError:
        print("Erro: Uma ou mais páginas estão fora do intervalo disponível.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Executa o script interativo
exportar_paginas_pdf_interativo()
