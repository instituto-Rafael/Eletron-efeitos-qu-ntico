#!/usr/bin/env python3
"""
Script de Simulação de Estrutura Simbiótica Bitraf
Implementa codificação e decodificação de estados quânticos
"""

import numpy as np
from typing import List, Tuple

class BitrafEncoder:
    """Codificador/decodificador Bitraf de 10 estados"""
    
    def __init__(self):
        """Inicializa o codificador com 10 estados base"""
        self.num_states = 10
        self.states = list(range(self.num_states))
    
    def encode_quantum_state(self, amplitudes: np.ndarray) -> List[int]:
        """
        Codifica um estado quântico em representação Bitraf
        
        Args:
            amplitudes: Array de amplitudes complexas (normalizado)
            
        Returns:
            Lista de códigos Bitraf
        """
        # Normalizar se necessário
        norm = np.linalg.norm(amplitudes)
        if not np.isclose(norm, 1.0):
            amplitudes = amplitudes / norm
        
        # Mapear amplitudes para códigos Bitraf
        # Usa magnitude e fase para determinar códigos
        bitraf_codes = []
        
        for amp in amplitudes:
            magnitude = np.abs(amp)
            phase = np.angle(amp)
            
            # Mapear magnitude para primeiros 5 estados (0-4)
            mag_code = int(magnitude * 5) % 5
            
            # Mapear fase para últimos 5 estados (5-9)
            phase_code = 5 + int((phase + np.pi) / (2*np.pi) * 5) % 5
            
            bitraf_codes.extend([mag_code, phase_code])
        
        return bitraf_codes
    
    def decode_to_quantum_state(self, bitraf_codes: List[int]) -> np.ndarray:
        """
        Decodifica representação Bitraf para estado quântico
        
        Args:
            bitraf_codes: Lista de códigos Bitraf
            
        Returns:
            Array de amplitudes complexas
        """
        # Processar códigos em pares (magnitude, fase)
        amplitudes = []
        
        for i in range(0, len(bitraf_codes), 2):
            if i+1 >= len(bitraf_codes):
                break
                
            mag_code = bitraf_codes[i] % 5
            phase_code = bitraf_codes[i+1] % 5
            
            # Reconstruir magnitude e fase
            magnitude = mag_code / 5.0
            phase = (phase_code / 5.0) * 2 * np.pi - np.pi
            
            # Criar amplitude complexa
            amp = magnitude * np.exp(1j * phase)
            amplitudes.append(amp)
        
        # Normalizar
        amplitudes = np.array(amplitudes)
        norm = np.linalg.norm(amplitudes)
        if norm > 0:
            amplitudes = amplitudes / norm
        
        return amplitudes
    
    def apply_verbo_vivo_cycle(self, state: np.ndarray) -> Tuple[np.ndarray, List[str]]:
        """
        Aplica ciclo Verbo Vivo: VAZIO → VERBO → CHEIO → RETROALIMENTAÇÃO → NOVO VAZIO
        
        Args:
            state: Estado quântico inicial
            
        Returns:
            Tupla (novo estado, histórico de fases)
        """
        history = []
        
        # Fase 1: VAZIO (estado inicial)
        history.append("VAZIO")
        current_state = state.copy()
        
        # Fase 2: VERBO (aplicar transformação unitária)
        history.append("VERBO")
        # Transformação de Hadamard generalizada
        n = len(current_state)
        H = np.ones((n, n)) / np.sqrt(n)
        current_state = H @ current_state
        
        # Fase 3: CHEIO (estado intermediário desenvolvido)
        history.append("CHEIO")
        
        # Fase 4: RETROALIMENTAÇÃO (aplicar correção baseada em entropia)
        history.append("RETROALIMENTAÇÃO")
        entropy = -np.sum(np.abs(current_state)**2 * np.log(np.abs(current_state)**2 + 1e-10))
        correction_phase = entropy / n
        current_state = current_state * np.exp(1j * correction_phase)
        
        # Fase 5: NOVO VAZIO (renormalizar)
        history.append("NOVO VAZIO")
        current_state = current_state / np.linalg.norm(current_state)
        
        return current_state, history


class FibonacciVoynichRafael:
    """Implementa sequência Fibonacci-Voynich-Rafael"""
    
    @staticmethod
    def generate_sequence(n: int) -> List[float]:
        """
        Gera sequência Fibonacci-Voynich-Rafael
        
        Args:
            n: Número de termos
            
        Returns:
            Lista de valores da sequência
        """
        if n <= 0:
            return []
        if n == 1:
            return [1.0]
        if n == 2:
            return [1.0, 1.618]  # Razão áurea
        
        sequence = [1.0, 1.618]
        phi = 1.618033988749895  # Razão áurea
        
        for i in range(2, n):
            # Combinação de Fibonacci com modulação fractal
            fib_term = sequence[i-1] + sequence[i-2]
            
            # Modulação Voynich (cifrada, usando função não-linear)
            voynich_mod = np.sin(i * phi) * np.cos(i / phi)
            
            # Termo Rafael (auto-similar)
            rafael_factor = 1 + 0.1 * np.sin(2 * np.pi * i / phi)
            
            next_term = (fib_term * rafael_factor + voynich_mod) / phi
            sequence.append(next_term)
        
        return sequence


def demonstrate_bitraf():
    """Demonstração do sistema Bitraf"""
    print("=" * 60)
    print("DEMONSTRAÇÃO DO SISTEMA BITRAF")
    print("=" * 60)
    
    # Criar codificador
    encoder = BitrafEncoder()
    
    # Estado quântico de exemplo (superposição de 3 estados)
    state = np.array([
        1/np.sqrt(3) * np.exp(1j * 0),
        1/np.sqrt(3) * np.exp(1j * np.pi/3),
        1/np.sqrt(3) * np.exp(1j * 2*np.pi/3)
    ])
    
    print("\n1. Estado Quântico Original:")
    print(f"   {state}")
    print(f"   Norma: {np.linalg.norm(state):.6f}")
    
    # Codificar
    bitraf_codes = encoder.encode_quantum_state(state)
    print(f"\n2. Códigos Bitraf: {bitraf_codes}")
    
    # Decodificar
    decoded_state = encoder.decode_to_quantum_state(bitraf_codes)
    print(f"\n3. Estado Decodificado:")
    print(f"   {decoded_state}")
    print(f"   Norma: {np.linalg.norm(decoded_state):.6f}")
    
    # Fidelidade
    fidelity = np.abs(np.vdot(state, decoded_state))**2
    print(f"\n4. Fidelidade: {fidelity:.6f}")
    
    # Aplicar ciclo Verbo Vivo
    print("\n5. Ciclo Verbo Vivo:")
    new_state, history = encoder.apply_verbo_vivo_cycle(state)
    for phase in history:
        print(f"   → {phase}")
    
    print(f"\n6. Estado após ciclo:")
    print(f"   {new_state}")
    print(f"   Norma: {np.linalg.norm(new_state):.6f}")
    
    # Sequência Fibonacci-Voynich-Rafael
    print("\n7. Sequência Fibonacci-Voynich-Rafael (10 termos):")
    fvr = FibonacciVoynichRafael()
    sequence = fvr.generate_sequence(10)
    for i, val in enumerate(sequence):
        print(f"   Termo {i+1}: {val:.6f}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demonstrate_bitraf()
