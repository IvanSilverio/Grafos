# visualizar_grade.py
import pandas as pd
import os

# --- CONFIGURAÇÃO ---
ARQUIVO_DADOS = "dataset_processado.csv"
ARQUIVO_GRADE = "grade_final.csv"
ARQUIVO_SAIDA = "grade_visual.html"

# Ordem cronológica para plotar na tabela
ORDEM_SLOTS = [
    'M1', 'M2', 'M3', 'M4',  # Manhã
    'T1', 'T2', 'T3',        # Tarde
    'N1', 'N2', 'N3', 'N4'   # Noite
]
ORDEM_DIAS = ['SEG', 'TER', 'QUA', 'QUI', 'SEX']

def gerar_visualizacao():
    print("Gerando visualização...")
    
    if not os.path.exists(ARQUIVO_GRADE) or not os.path.exists(ARQUIVO_DADOS):
        print("ERRO: Arquivos 'grade_final.csv' ou 'dataset_processado.csv' não encontrados.")
        print("Rode o main.py primeiro.")
        return

    # 1. Carregar dados
    df_dados = pd.read_csv(ARQUIVO_DADOS)
    df_grade = pd.read_csv(ARQUIVO_GRADE)
    
    # 2. Juntar informações (Horário + Nome da Matéria + Professor)
    # Precisamos mapear ID_Aula -> Dados Reais
    df_completo = pd.merge(df_grade, df_dados, left_on='Aula', right_on='ID_Aula', how='left')
    
    # 3. Separar Dia e Slot (Ex: 'SEG_M1' -> Dia='SEG', Slot='M1')
    df_completo['Dia'] = df_completo['Horario'].apply(lambda x: x.split('_')[0])
    df_completo['Slot'] = df_completo['Horario'].apply(lambda x: x.split('_')[1])
    
    # 4. Criar o texto da célula (Matéria + Prof)
    def formatar_celula(row):
        # Ex: "Cálculo A (Prof. X)"
        lab = f" [{row['Lab_Requerido']}]" if pd.notna(row['Lab_Requerido']) else ""
        return f"<b>{row['Nome']}</b><br><span style='font-size:0.8em'>{row['Professor']}{lab}</span>"
    
    df_completo['Conteudo'] = df_completo.apply(formatar_celula, axis=1)

    # 5. Gerar HTML
    html_final = """
    <html>
    <head>
        <style>
            body { font-family: sans-serif; padding: 20px; background-color: #f4f4f9; }
            h1 { text-align: center; color: #333; }
            h2 { color: #555; border-bottom: 2px solid #ddd; margin-top: 40px; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }
            th, td { border: 1px solid #ccc; padding: 10px; text-align: center; vertical-align: top; }
            th { background-color: #007bff; color: white; }
            td { height: 60px; }
            .curso-header { background-color: #e9ecef; padding: 10px; font-weight: bold; font-size: 1.2em; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            .slot-header { font-weight: bold; background-color: #eee; width: 80px; }
        </style>
    </head>
    <body>
    <h1>Grade Horária Gerada (CCO & SIN)</h1>
    """
    
    # Agrupar por Curso e Período para criar tabelas separadas
    grupos = df_completo.groupby(['Curso', 'Periodo'])
    
    # Ordenar grupos para aparecer CCO 1, CCO 2... depois SIN 1, SIN 2...
    chaves_ordenadas = sorted(grupos.groups.keys(), key=lambda x: (x[0], int(x[1]) if x[1].isdigit() else 99))
    
    for curso, periodo in chaves_ordenadas:
        grupo = grupos.get_group((curso, periodo))
        
        html_final += f"<h2>{curso} - {periodo}º Período</h2>"
        html_final += "<table><thead><tr><th>Horário</th>"
        for dia in ORDEM_DIAS:
            html_final += f"<th>{dia}</th>"
        html_final += "</tr></thead><tbody>"
        
        # Pivotar dados para formato de matriz
        matriz = grupo.pivot(index='Slot', columns='Dia', values='Conteudo')
        
        # Preencher slots vazios e garantir ordem
        for slot in ORDEM_SLOTS:
            # Filtro visual: Não mostrar slots de Noite para CCO e vice-versa para limpar a tabela
            eh_cco = 'CCO' in str(curso).upper()
            eh_noturno = slot.startswith('N')
            if eh_cco and eh_noturno: continue
            if not eh_cco and not eh_noturno: continue

            html_final += f"<tr><td class='slot-header'>{slot}</td>"
            for dia in ORDEM_DIAS:
                conteudo = ""
                if slot in matriz.index and dia in matriz.columns:
                    valor = matriz.at[slot, dia]
                    if pd.notna(valor):
                        conteudo = valor
                html_final += f"<td>{conteudo}</td>"
            html_final += "</tr>"
            
        html_final += "</tbody></table>"
    
    html_final += "</body></html>"
    
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        f.write(html_final)
        
    print(f"\n>>> SUCESSO! Abra o arquivo '{ARQUIVO_SAIDA}' no seu navegador para ver a grade.")

if __name__ == "__main__":
    gerar_visualizacao()