import requests
import pandas as pd

TECNOLOGIA = "python junior"

print(f"Buscando informações recentes sobre: '{TECNOLOGIA}'...")

URL = f"https://api.github.com/search/repositories?q={TECNOLOGIA}&sort=updated&order=desc"

resposta = requests.get(URL)

if resposta.status_code == 200:
    dados = resposta.json()
    itens = dados.get("items", [])
    
    lista_resultados = []
    
    for item in itens[:10]:
        informacoes = {
            "Nome do Projeto": item.get("name"),
            "Descrição": item.get("description") or "Sem descrição",
            "Link": item.get("html_url"),
            "Última Atualização": item.get("updated_at")[:10]
        }
        lista_resultados.append(informacoes)
    
    tabela = pd.DataFrame(lista_resultados)
    
    print("\n--- RESULTADOS ENCONTRADOS ---")
    print(tabela[["Nome do Projeto", "Última Atualização"]])
    
    nome_arquivo = "relatorio_oportunidades.csv"
    tabela.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
    
    print(f"\n[Sucesso] Relatório gerado e salvo em '{nome_arquivo}'!")
else:
    print("Ocorreu um erro ao buscar os dados na internet.")