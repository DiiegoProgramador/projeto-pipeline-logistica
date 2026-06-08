import csv

def extrair_dados(caminho_arquivo):
    print(f"Lendo dados de {caminho_arquivo}")
    dados_brutos = []
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                dados_brutos.append(linha)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
        return []
    
    print(f"Extração concluída! {len(dados_brutos)} linhas carregadas")
    return dados_brutos

def transformar_dados(dados_brutos):
    print("Aplicando regra de negócio...")
    dados_limpos = []
    for linha in dados_brutos:
        # Garantindo que os nomes das colunas batem com o seu CSV
        peso = float(linha['peso_kg'])
        capacidade = float(linha['capacidade_max_kg'])
        
        status = "OK"
        if peso > capacidade:
            status = "BARRADO - EXCESSO"
        
        viagem = {
            'nome': linha['nome_motorista'],
            'produto': linha['produto'],
            'status': status
        }
        dados_limpos.append(viagem)
    return dados_limpos

if __name__ == "__main__":
    # Nome correto do arquivo
    arquivo_csv = 'viagens_brutas.csv'
    
    lista_bruta = extrair_dados(arquivo_csv)
    
    if lista_bruta:
        lista_tratada = transformar_dados(lista_bruta)
        
        print("\n--- RELATÓRIO DE VIAGENS ---")
        for v in lista_tratada:
            print(f"Motorista: {v['nome']:15} | Produto: {v['produto']:10} | Status: {v['status']}")