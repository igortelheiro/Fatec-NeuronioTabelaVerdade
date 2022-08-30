from enum import Enum

Vetor = list[float]

class OperationType(Enum):
	AND  = 0,
	NAND = 1,
	OR   = 2,
	NOR  = 3

class Operation():
    def __init__(self, type: OperationType, limiar: float):
        self.Type = type
        self.Limiar = limiar
        self.__configurar_calculadora_vetores()
        self.__configurar_calculadora_limiar()


    def Calcular(self, pesos: Vetor, entradas: Vetor, mostrarResultado = False):
        resultado = self.CalculadoraVetores(pesos, entradas)
        saida = self.CalculadoraLimiar(resultado)

        if (mostrarResultado):
            print(f'[{pesos[0]} * {entradas[0]}] + [{pesos[1]} * {entradas[1]}] = {resultado}')
        print(f'{entradas[0]} {self.Type.name} {entradas[1]} = {saida}')
    

    def __configurar_calculadora_vetores(self):
        self.CalculadoraVetores = self.__multiplicar_vetores


    def __configurar_calculadora_limiar(self):
        if (self.Type == OperationType.AND or self.Type == OperationType.OR):
            self.CalculadoraLimiar = self.__calcular_limiar
        else:
            self.CalculadoraLimiar = self.__calcular_limiar_com_negacao


    def __multiplicar_vetores(self, pesos: Vetor, entradas: Vetor):
        return sum(p * e for p, e in zip(pesos, entradas))


    def __calcular_limiar(self, resultado: float):
        return 1 if resultado >= self.Limiar else 0


    def __calcular_limiar_com_negacao(self, resultado: float):
        return 1 if resultado < self.Limiar else 0