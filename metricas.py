class Matriz_de_Confusao:
    def __init__(self, VP, FN, FP, VN):
        self.VP = VP
        self.FN = FN
        self.FP = FP
        self.VN = VN
        
    def acuracia(self):
        return (self.VP + self.VN) / (self.VP + self.FN + self.FP + self.VN)

    def sensibilidade(self):
        return self.VP / (self.VP + self.FN)

    def especificidade(self):
        return self.VN / (self.VN + self.FP)
    
    def precisao(self):
        return self.VP / (self.VP + self.FP)

    def f1_score(self):
        return 2 * (self.VP / (self.VP + self.FP)) * (self.VP / (self.VP + self.FN))
    
    def imprimir_resultados(self):
        print(f"VP: {self.VP}")
        print(f"FN: {self.FN}")
        print(f"FP: {self.FP}")
        print(f"VN: {self.VN}")
    
    def imprimir_metricas(self):
        print(f"Acurácia: {self.acuracia()}")
        print(f"Sensibilidade: {self.sensibilidade()}")
        print(f"Especificidade: {self.especificidade()}")
        print(f"Precisão: {self.precisao()}")
        print(f"F1 Score: {self.f1_score()}")
    
    def __str__(self):
        matriz_str = f"[[{self.VP} , {self.FN}]\n [{self.FP} , {self.VN}]]"
        return matriz_str
