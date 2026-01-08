#!/usr/bin/env python3
"""
Script de Teste - Verifica estrutura do repositório
Não requer dependências externas
"""

import os
import sys

def check_file_exists(filepath, description):
    """Verifica se um arquivo existe"""
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"✓ {description}: {filepath} ({size} bytes)")
        return True
    else:
        print(f"✗ {description}: {filepath} (NÃO ENCONTRADO)")
        return False

def check_directory_exists(dirpath, description):
    """Verifica se um diretório existe"""
    if os.path.isdir(dirpath):
        files = len(os.listdir(dirpath))
        print(f"✓ {description}: {dirpath} ({files} arquivos)")
        return True
    else:
        print(f"✗ {description}: {dirpath} (NÃO ENCONTRADO)")
        return False

def main():
    """Função principal de teste"""
    print("=" * 70)
    print("TESTE DE INTEGRIDADE DO REPOSITÓRIO")
    print("=" * 70)
    print()
    
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_path)
    
    total_checks = 0
    passed_checks = 0
    
    print("1. ARQUIVOS PRINCIPAIS")
    print("-" * 70)
    files_main = [
        ("README.md", "README principal"),
        ("Paper_quantico.tex", "Paper científico em LaTeX"),
        ("Quantum_eletron.txt", "Teoria sobre elétron quântico"),
        ("TEORIA_RAFAEL_PROVADA.txt", "Teoria Rafael"),
    ]
    for filepath, desc in files_main:
        total_checks += 1
        if check_file_exists(filepath, desc):
            passed_checks += 1
    print()
    
    print("2. DOCUMENTOS ACADÊMICOS")
    print("-" * 70)
    files_academic = [
        ("Intro.md", "Introdução"),
        ("Cicuitos.md", "Análise de circuitos"),
        ("Fato.md", "Fatos históricos"),
        ("Provas.md", "Provas técnicas"),
        ("Academico que evidencia.md", "Protocolo acadêmico"),
    ]
    for filepath, desc in files_academic:
        total_checks += 1
        if check_file_exists(filepath, desc):
            passed_checks += 1
    print()
    
    print("3. DIRETÓRIOS")
    print("-" * 70)
    directories = [
        ("dissertacao", "Dissertação acadêmica"),
        ("matematica", "Matemática"),
        ("indices", "Índices e glossário"),
        ("scripts", "Scripts Python"),
    ]
    for dirpath, desc in directories:
        total_checks += 1
        if check_directory_exists(dirpath, desc):
            passed_checks += 1
    print()
    
    print("4. DISSERTAÇÃO")
    print("-" * 70)
    files_dissertation = [
        ("dissertacao/Dissertacao_Academica_Completa.md", "Dissertação completa"),
    ]
    for filepath, desc in files_dissertation:
        total_checks += 1
        if check_file_exists(filepath, desc):
            passed_checks += 1
    print()
    
    print("5. MATEMÁTICA")
    print("-" * 70)
    files_math = [
        ("matematica/derivadas/Derivadas_Completas.md", "Derivadas e integrais"),
    ]
    for filepath, desc in files_math:
        total_checks += 1
        if check_file_exists(filepath, desc):
            passed_checks += 1
    print()
    
    print("6. ÍNDICES")
    print("-" * 70)
    files_indices = [
        ("indices/Indice_Geral.md", "Índice geral"),
        ("indices/Glossario.md", "Glossário"),
        ("indices/Indice_Autores.md", "Índice de autores"),
    ]
    for filepath, desc in files_indices:
        total_checks += 1
        if check_file_exists(filepath, desc):
            passed_checks += 1
    print()
    
    print("7. SCRIPTS")
    print("-" * 70)
    files_scripts = [
        ("scripts/README.md", "README dos scripts"),
        ("scripts/josephson_analyzer.py", "Analisador Josephson"),
        ("scripts/bitraf_simulator.py", "Simulador Bitraf"),
    ]
    for filepath, desc in files_scripts:
        total_checks += 1
        if check_file_exists(filepath, desc):
            passed_checks += 1
    print()
    
    print("8. CONTEÚDO")
    print("-" * 70)
    
    # Verificar conteúdo da dissertação
    dissertation_path = "dissertacao/Dissertacao_Academica_Completa.md"
    if os.path.exists(dissertation_path):
        with open(dissertation_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        checks = [
            ("Resumo" in content, "Contém resumo"),
            ("Abstract" in content, "Contém abstract"),
            ("Referências Bibliográficas" in content, "Contém referências"),
            ("Bitraf" in content, "Menciona Bitraf"),
            ("RAFCODE" in content, "Menciona RAFCODE"),
            ("Josephson" in content, "Menciona Josephson"),
            ("Tunelamento" in content, "Menciona tunelamento"),
            ("Nobel" in content, "Menciona Nobel"),
        ]
        
        for condition, desc in checks:
            total_checks += 1
            if condition:
                print(f"✓ {desc}")
                passed_checks += 1
            else:
                print(f"✗ {desc}")
    print()
    
    # Verificar conteúdo das derivadas
    derivadas_path = "matematica/derivadas/Derivadas_Completas.md"
    if os.path.exists(derivadas_path):
        with open(derivadas_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Contar quantas derivadas existem
        derivadas_count = content.count("**") // 2  # Aproximação
        print(f"✓ Documento de derivadas contém ~{derivadas_count} entradas formatadas")
        
        checks = [
            ("d/dx" in content, "Contém notação de derivadas"),
            ("∫" in content, "Contém símbolo de integral"),
            ("Josephson" in content, "Aplicações em Josephson"),
        ]
        
        for condition, desc in checks:
            total_checks += 1
            if condition:
                print(f"✓ {desc}")
                passed_checks += 1
            else:
                print(f"✗ {desc}")
    print()
    
    print("=" * 70)
    print(f"RESULTADO: {passed_checks}/{total_checks} verificações passaram")
    print("=" * 70)
    
    if passed_checks == total_checks:
        print("✓ SUCESSO! Repositório está completo e bem estruturado.")
        return 0
    else:
        print(f"⚠ ATENÇÃO: {total_checks - passed_checks} verificações falharam.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
