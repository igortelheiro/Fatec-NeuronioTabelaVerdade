from operation import Operation, OperationType

limiarAND = 2
limiarOR  = 1

AND  = Operation(OperationType.AND,  limiarAND)
NAND = Operation(OperationType.NAND, limiarAND)
OR   = Operation(OperationType.OR,   limiarOR)
NOR  = Operation(OperationType.NOR,  limiarOR)

pesos    = [1, 1]
entrada1 = [0, 0]
entrada2 = [0, 1]
entrada3 = [1, 0]
entrada4 = [1, 1]

operacoes = [AND, NAND, OR, NOR]
entradas  = [entrada1, entrada2, entrada3, entrada4]

for operacao in operacoes:
	for entrada in entradas:
		operacao.Calcular(pesos, entrada)
	print("============================")
