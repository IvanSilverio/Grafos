# preparar_dataset.py
import pandas as pd
import numpy as np
import os

# --- CONFIGURAÇÃO ---
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
NOME_ARQUIVO = "Cenário 5 - Alocação de Horários - CCO e SIN.xlsx" 
ARQUIVO_INPUT = os.path.join(DIRETORIO_ATUAL, NOME_ARQUIVO)
ARQUIVO_OUTPUT = "dataset_processado.csv"

# --- LISTAS DE PROFESSORES (20 para cada curso) ---
PROFESSORES_CCO = [f"Prof. CCO_{i}" for i in range(1, 21)]
PROFESSORES_SIN = [f"Prof. SIN_{i}" for i in range(1, 21)]
LABS_SIMULADOS = ['Lab_Redes', 'Lab_Hardware', None, None, None, None] 

def preparar_dataset_completo():
    print(f"Lendo arquivo Excel: {ARQUIVO_INPUT}...")
    
    if not os.path.exists(ARQUIVO_INPUT):
        print(f"ERRO: Arquivo não encontrado: {ARQUIVO_INPUT}")
        return

    try:
        df = pd.read_excel(ARQUIVO_INPUT, skiprows=7, engine='openpyxl')
    except Exception as e:
        print(f"ERRO AO LER EXCEL: {e}")
        return

    # 1. Limpeza
    cols_to_fill = ['CURSO', 'PPC', 'PER.']
    valid_cols = [c for c in cols_to_fill if c in df.columns]
    if valid_cols:
        df[valid_cols] = df[valid_cols].ffill()
    
    colunas_necessarias = ['SIGLA', 'DISCIPLINA', 'CH']
    if not all(col in df.columns for col in colunas_necessarias):
        print("ERRO: Colunas não encontradas.")
        return

    df = df.dropna(subset=colunas_necessarias)
    df['CH'] = pd.to_numeric(df['CH'], errors='coerce').fillna(0).astype(int)
    df = df[df['CH'] > 0]
    
    # --- CORREÇÃO IMPORTANTE: Resetar índice para garantir contagem única ---
    df = df.reset_index(drop=True)

    # 2. Enriquecimento
    print("Atribuindo professores por curso...")
    
    def escolher_professor(linha):
        curso = str(linha['CURSO']).upper()
        idx = np.random.randint(0, 20)
        
        if 'CCO' in curso or 'CIÊNCIA' in curso:
            return PROFESSORES_CCO[idx]
        elif 'SIN' in curso or 'SISTEMAS' in curso:
            return PROFESSORES_SIN[idx]
        else:
            todos = PROFESSORES_CCO + PROFESSORES_SIN
            return todos[idx % 40]

    df['Professor'] = df.apply(escolher_professor, axis=1)
    df['Lab_Requerido'] = [LABS_SIMULADOS[i % len(LABS_SIMULADOS)] for i in range(len(df))]

    # 3. Explosão
    print("Processando blocos de horário...")
    aulas_list = []
    
    # Usamos 'idx' (índice da linha) para garantir que o ID seja único
    for idx, row in df.iterrows():
        blocos = row['CH'] // 2
        if blocos == 0 and row['CH'] > 0: blocos = 1
        
        for i in range(blocos):
            sufixo = chr(65 + i) # A, B, C...
            
            # --- ID ÚNICO AQUI ---
            # Adicionamos o '{idx}' no nome para diferenciar duplicatas de SIGLA
            id_aula_unico = f"{row['SIGLA']}_{idx}_{sufixo}"
            
            aulas_list.append({
                "ID_Aula": id_aula_unico,
                "ID_Disciplina": row['SIGLA'], # Mantém a sigla original para checar conflitos
                "Nome": row['DISCIPLINA'],
                "Curso": row['CURSO'],
                "Periodo": str(row['PER.']) if 'PER.' in df.columns else '1',
                "Professor": row['Professor'],
                "Lab_Requerido": row['Lab_Requerido'],
                "CH_Aula": 2
            })

    df_final = pd.DataFrame(aulas_list)
    df_final.to_csv(ARQUIVO_OUTPUT, index=False, encoding='utf-8') 
    print(f"\nSUCESSO! '{ARQUIVO_OUTPUT}' criado com IDs únicos.")

if __name__ == "__main__":
    preparar_dataset_completo()