#!/usr/bin/env python3
"""
Script de Análise de Dados de Junções Josephson
Calcula parâmetros fundamentais e taxas de escape
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, e, k

class JosephsonAnalyzer:
    """Analisador de propriedades de junções Josephson"""
    
    def __init__(self, I_c, C, R):
        """
        Inicializa o analisador
        
        Args:
            I_c: Corrente crítica (A)
            C: Capacitância (F)
            R: Resistência (Ω)
        """
        self.I_c = I_c
        self.C = C
        self.R = R
        
        # Calcular parâmetros fundamentais
        self.E_J = self._calculate_josephson_energy()
        self.omega_p = self._calculate_plasma_frequency()
        self.Q = self._calculate_quality_factor()
    
    def _calculate_josephson_energy(self):
        """Calcula energia de Josephson: E_J = ℏI_c/(2e)"""
        return (hbar * self.I_c) / (2 * e)
    
    def _calculate_plasma_frequency(self, I=0):
        """
        Calcula frequência de plasma
        ω_p(I) ≈ √(2eI_c/ℏC) × [1-(I/I_c)²]^(1/4)
        """
        if I == 0:
            return np.sqrt((2 * e * self.I_c) / (hbar * self.C))
        else:
            factor = (1 - (I/self.I_c)**2)**0.25
            return self.omega_p * factor
    
    def _calculate_quality_factor(self):
        """Calcula fator de qualidade Q"""
        return self.omega_p * self.R * self.C
    
    def calculate_barrier_height(self, I):
        """
        Calcula altura da barreira de potencial
        ΔU(I) ≈ (2√2/3) E_J [1 - I/I_c]^(3/2)
        """
        factor = (1 - I/self.I_c)**(3/2)
        return (2 * np.sqrt(2) / 3) * self.E_J * factor
    
    def thermal_activation_rate(self, I, T):
        """
        Calcula taxa de ativação térmica
        Γ_TA(T) ∝ ω_p exp(-ΔU/k_BT)
        """
        omega_p_I = self._calculate_plasma_frequency(I)
        delta_U = self.calculate_barrier_height(I)
        
        return omega_p_I * np.exp(-delta_U / (k * T))
    
    def mqt_rate(self, I):
        """
        Calcula taxa de tunelamento quântico macroscópico
        Γ_MQT ≈ a ω_p exp[-7.2 ΔU/(ℏω_p) × (1 + 0.87/Q)]
        """
        omega_p_I = self._calculate_plasma_frequency(I)
        delta_U = self.calculate_barrier_height(I)
        
        exponent = -7.2 * delta_U / (hbar * omega_p_I) * (1 + 0.87/self.Q)
        
        # Coeficiente a é tipicamente da ordem de ω_p
        a = omega_p_I / (2 * np.pi)
        
        return a * np.exp(exponent)
    
    def plot_escape_rates(self, I_range, T_range):
        """
        Plota taxas de escape em função da temperatura
        
        Args:
            I_range: Array de correntes de bias
            T_range: Array de temperaturas
        """
        plt.figure(figsize=(12, 5))
        
        # Plot 1: Taxa vs Temperatura para diferentes correntes
        plt.subplot(1, 2, 1)
        for I in I_range:
            rates_ta = [self.thermal_activation_rate(I, T) for T in T_range]
            plt.semilogy(T_range*1000, rates_ta, label=f'I = {I*1e6:.1f} μA')
        
        plt.xlabel('Temperatura (mK)')
        plt.ylabel('Taxa de Escape (Hz)')
        plt.title('Ativação Térmica')
        plt.legend()
        plt.grid(True)
        
        # Plot 2: Crossover TA → MQT
        plt.subplot(1, 2, 2)
        I = I_range[len(I_range)//2]  # Corrente intermediária
        
        rates_ta = [self.thermal_activation_rate(I, T) for T in T_range]
        rate_mqt = self.mqt_rate(I)
        
        plt.semilogy(T_range*1000, rates_ta, 'b-', label='TA')
        plt.axhline(y=rate_mqt, color='r', linestyle='--', label='MQT')
        
        plt.xlabel('Temperatura (mK)')
        plt.ylabel('Taxa de Escape (Hz)')
        plt.title(f'Crossover TA→MQT (I = {I*1e6:.1f} μA)')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('escape_rates.png', dpi=300)
        print("Gráfico salvo em: escape_rates.png")
    
    def print_summary(self):
        """Imprime sumário dos parâmetros"""
        print("=" * 50)
        print("ANÁLISE DE JUNÇÃO JOSEPHSON")
        print("=" * 50)
        print(f"Corrente crítica (I_c):      {self.I_c*1e6:.2f} μA")
        print(f"Capacitância (C):            {self.C*1e15:.2f} fF")
        print(f"Resistência (R):             {self.R:.2f} Ω")
        print(f"Energia de Josephson (E_J):  {self.E_J/k*1e3:.2f} mK")
        print(f"Frequência de plasma (ω_p):  {self.omega_p/(2*np.pi)*1e-9:.2f} GHz")
        print(f"Fator de qualidade (Q):      {self.Q:.2f}")
        print("=" * 50)


def example_analysis():
    """Exemplo de análise"""
    # Parâmetros típicos de uma junção Josephson
    I_c = 1e-6  # 1 μA
    C = 1e-15   # 1 fF
    R = 100     # 100 Ω
    
    # Criar analisador
    analyzer = JosephsonAnalyzer(I_c, C, R)
    
    # Imprimir sumário
    analyzer.print_summary()
    
    # Criar gráficos
    I_range = np.linspace(0.7*I_c, 0.95*I_c, 5)
    T_range = np.linspace(10e-3, 300e-3, 100)  # 10 mK a 300 mK
    
    analyzer.plot_escape_rates(I_range, T_range)
    
    # Calcular taxa MQT
    I_test = 0.9 * I_c
    rate_mqt = analyzer.mqt_rate(I_test)
    print(f"\nTaxa MQT em I = {I_test*1e6:.2f} μA: {rate_mqt:.2e} Hz")


if __name__ == "__main__":
    example_analysis()
