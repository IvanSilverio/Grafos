# main.py
import pandas as pd
import networkx as nx
import random
from collections import defaultdict

# --- CONFIGURAÇÕES ---
ARQUIVO_DADOS = "dataset_processado.csv"
MAX_TENTATIVAS = 100 

# Definindo os dias da semana
DIAS = ['SEG', 'TER', 'QUA', 'QUI', 'SEX']

# --- DEFINIÇÃO DOS SLOTES (O que você pediu) ---

# CCO (Integral): 7 horários por dia
# M1, M2, M3, M4 (Manhã) + T1, T2, T3 (Tarde)
SLOTS_CCO = ['M1', 'M2', 'M3', 'M4', 'T1', 'T2', 'T3']
HORARIOS_CCO = [f"{d}_{t}" for d in DIAS for t in SLOTS_CCO] 
# Total: 5 dias * 7 slots = 35 horários disponíveis para CCO

# SIN (Noturno): 4 horários por dia
# N1, N2, N3, N4 (Noite)
SLOTS_SIN = ['N1', 'N2', 'N3', 'N4']
HORARIOS_SIN = [f"{d}_{t}" for d in DIAS for t in SLOTS_SIN]
# Total: 5 dias * 4 slots = 20 horários disponíveis para SIN

def carregar_dados():
    try:
        return pd.read_csv(ARQUIVO_DADOS)
    except FileNotFoundError:
        print(f"ERRO: '{ARQUIVO_DADOS}' não encontrado.")
        return None

def construir_grafo(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_node(row['ID_Aula'], **row.to_dict())
    
    nodes = list(G.nodes(data=True))
    
    # 1. Conflito de Turma
    turmas = defaultdict(list)
    for nid, data in nodes:
        chave_turma = (data['Curso'], data['Periodo'])
        turmas[chave_turma].append(nid)
    
    for lista_aulas in turmas.values():
        for i in range(len(lista_aulas)):
            for j in range(i+1, len(lista_aulas)):
                G.add_edge(lista_aulas[i], lista_aulas[j], reason='Turma')

    # 2. Conflitos de Recurso (Professor/Lab)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, data_u = nodes[i]
            v, data_v = nodes[j]
            
            if G.has_edge(u, v): continue

            # Verifica se competem pelo mesmo turno (Integral vs Integral OU Noturno vs Noturno)
            # CCO é Integral, SIN é Noturno. 
            # Optativas: Vamos assumir que seguem o curso do prefixo ou padrão CCO.
            
            eh_sin_u = 'SIN' in str(data_u['Curso']).upper()
            eh_sin_v = 'SIN' in str(data_v['Curso']).upper()
            
            # Só há conflito de horário se ambos forem do mesmo turno
            if eh_sin_u == eh_sin_v:
                if data_u['Professor'] == data_v['Professor']:
                    G.add_edge(u, v, reason='Professor')
                if pd.notna(data_u['Lab_Requerido']) and data_u['Lab_Requerido'] == data_v['Lab_Requerido']:
                    G.add_edge(u, v, reason='Lab')
                    
            if data_u['ID_Disciplina'] == data_v['ID_Disciplina']:
                G.add_edge(u, v, reason='Disciplina')
                
    return G

def heuristica_peso(G, cargas_professores):
    pesos = {}
    for node in G.nodes:
        prof = G.nodes[node]['Professor']
        grau = G.degree[node]
        carga = cargas_professores.get(prof, 0)
        pesos[node] = grau + (carga * 10)
    return pesos

def colorir_grade(G, usar_aleatoriedade=False):
    cargas = defaultdict(int)
    for n in G.nodes:
        cargas[G.nodes[n]['Professor']] += 1
    
    pesos = heuristica_peso(G, cargas)
    
    if usar_aleatoriedade:
        nodes_ordenados = sorted(G.nodes, key=lambda n: pesos[n] + random.uniform(0, 5), reverse=True)
    else:
        nodes_ordenados = sorted(G.nodes, key=lambda n: pesos[n], reverse=True)
        
    grade = {}
    
    for node in nodes_ordenados:
        data = G.nodes[node]
        
        # Seleção do Pool de Horários Correto
        if 'SIN' in str(data['Curso']).upper():
            pool = HORARIOS_SIN
        else:
            pool = HORARIOS_CCO
        
        proibidos = {grade[viz] for viz in G.neighbors(node) if viz in grade}
        
        alocado = False
        # Randomizar o pool ajuda a espalhar as aulas e evitar aglomerar tudo na Segunda
        pool_embaralhado = list(pool)
        if usar_aleatoriedade: random.shuffle(pool_embaralhado)
            
        for horario in pool_embaralhado:
            if horario not in proibidos:
                grade[node] = horario
                alocado = True
                break
        
        if not alocado:
            return None 
            
    return grade

def validar_restricoes_finais(grade, df):
    mapa_aulas = df.set_index('ID_Aula').to_dict('index')
    prof_dia = defaultdict(lambda: defaultdict(int))
    
    for aula, horario in grade.items():
        prof = mapa_aulas[aula]['Professor']
        dia = horario.split('_')[0]
        
        prof_dia[prof][dia] += 2 
        
        if prof_dia[prof][dia] > 8:
            return False, f"Professor {prof} excedeu 8h na {dia}."
            
    return True, "Grade Válida"

def executar_sistema():
    df = carregar_dados()
    if df is None: return

    print("Construindo Grafo...")
    G = construir_grafo(df)
    print(f"Grafo pronto: {G.number_of_nodes()} aulas.")

    print(f"\nTentando alocar horários...")
    
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        usar_random = (tentativa > 1)
        grade = colorir_grade(G, usar_random)
        
        if grade:
            valida, msg = validar_restricoes_finais(grade, df)
            if valida:
                print(f">>> SUCESSO na tentativa {tentativa}!")
                
                # Salvar CSV
                pd.DataFrame(list(grade.items()), columns=['Aula', 'Horario']).to_csv("grade_final.csv", index=False)
                print("Grade salva em 'grade_final.csv'.")
                return
            else:
                if tentativa == 1: print(f"Tentativa 1 falhou na validação: {msg}")
        else:
            if tentativa == 1: print("Tentativa 1 falhou na coloração.")

    print("\nFALHA: Não foi possível gerar a grade.")

if __name__ == "__main__":
    executar_sistema()