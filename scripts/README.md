# Scripts de Análise e Simulação

Este diretório contém scripts Python para análise de dados experimentais e simulação de estruturas simbióticas.

## Scripts Disponíveis

### 1. josephson_analyzer.py

Analisador de propriedades de junções Josephson e cálculo de taxas de escape.

**Funcionalidades:**
- Cálculo de energia de Josephson (E_J)
- Cálculo de frequência de plasma (ω_p)
- Cálculo de fator de qualidade (Q)
- Altura da barreira de potencial (ΔU)
- Taxa de ativação térmica (Γ_TA)
- Taxa de tunelamento quântico macroscópico (Γ_MQT)
- Visualização de crossover TA→MQT

**Uso:**
```bash
python3 josephson_analyzer.py
```

**Requisitos:**
- numpy
- matplotlib
- scipy

**Exemplo:**
```python
from josephson_analyzer import JosephsonAnalyzer

# Parâmetros da junção
I_c = 1e-6  # 1 μA
C = 1e-15   # 1 fF
R = 100     # 100 Ω

analyzer = JosephsonAnalyzer(I_c, C, R)
analyzer.print_summary()
```

### 2. bitraf_simulator.py

Simulador de estrutura simbiótica Bitraf para codificação de estados quânticos.

**Funcionalidades:**
- Codificação de estados quânticos em Bitraf (10 estados)
- Decodificação de Bitraf para estados quânticos
- Ciclo Verbo Vivo (VAZIO → VERBO → CHEIO → RETROALIMENTAÇÃO → NOVO VAZIO)
- Geração de sequência Fibonacci-Voynich-Rafael
- Cálculo de fidelidade de codificação/decodificação

**Uso:**
```bash
python3 bitraf_simulator.py
```

**Requisitos:**
- numpy

**Exemplo:**
```python
from bitraf_simulator import BitrafEncoder

encoder = BitrafEncoder()

# Estado quântico (superposição)
state = np.array([1/np.sqrt(2), 1/np.sqrt(2)])

# Codificar
codes = encoder.encode_quantum_state(state)

# Decodificar
decoded = encoder.decode_to_quantum_state(codes)

# Aplicar ciclo Verbo Vivo
new_state, history = encoder.apply_verbo_vivo_cycle(state)
```

## Instalação de Dependências

```bash
pip install numpy matplotlib scipy
```

ou usando conda:

```bash
conda install numpy matplotlib scipy
```

## Estrutura de Dados

### Junção Josephson
```python
{
    'I_c': float,      # Corrente crítica (A)
    'C': float,        # Capacitância (F)
    'R': float,        # Resistência (Ω)
    'E_J': float,      # Energia de Josephson (J)
    'omega_p': float,  # Frequência de plasma (rad/s)
    'Q': float         # Fator de qualidade
}
```

### Estado Bitraf
```python
{
    'codes': List[int],           # Lista de códigos (0-9)
    'amplitudes': np.ndarray,     # Amplitudes complexas
    'fidelity': float,            # Fidelidade (0-1)
    'phase': str                  # Fase do ciclo Verbo Vivo
}
```

## Saídas

### josephson_analyzer.py
- **Console:** Sumário de parâmetros calculados
- **Arquivo:** `escape_rates.png` - Gráficos de taxas de escape

### bitraf_simulator.py
- **Console:** Demonstração completa do sistema Bitraf
- Estados originais e decodificados
- Histórico do ciclo Verbo Vivo
- Sequência Fibonacci-Voynich-Rafael

## Exemplos de Saída

### Análise de Junção Josephson
```
==================================================
ANÁLISE DE JUNÇÃO JOSEPHSON
==================================================
Corrente crítica (I_c):      1.00 μA
Capacitância (C):            1.00 fF
Resistência (R):             100.00 Ω
Energia de Josephson (E_J):  24.18 mK
Frequência de plasma (ω_p):  57.21 GHz
Fator de qualidade (Q):      35.98
==================================================
```

### Codificação Bitraf
```
1. Estado Quântico Original:
   [0.57735027+0.j  0.57735027+0.52359878j  0.57735027+1.04719755j]
   Norma: 1.000000

2. Códigos Bitraf: [2, 5, 2, 6, 2, 7]

3. Estado Decodificado:
   [0.57735027+0.j  0.57735027+0.52j  0.57735027+1.05j]
   Norma: 1.000000

4. Fidelidade: 0.999984
```

## Referências

- Paper_quantico.tex - Fundamentos teóricos
- dissertacao/Dissertacao_Academica_Completa.md - Contexto completo
- matematica/derivadas/Derivadas_Completas.md - Equações fundamentais

## Contribuindo

Para adicionar novos scripts:
1. Seguir convenções de nomenclatura Python (PEP 8)
2. Incluir docstrings detalhadas
3. Adicionar testes quando apropriado
4. Atualizar este README

## Licença

CC BY 4.0 - Creative Commons Attribution 4.0 International

## Autor

Rafael Melo Reis - Instituto Rafael - 2025
