class Veiculo:
    def __init__(self, marca, ano, preco):
        self.marca = str(marca)
        self.ano = int(ano)
        self.preco = float(preco)
    def Exibibirinfo(self):
        return f"Marca: {self.marca}\n ano de lançamento: {self.ano}\n Preço:{self.preco:.2f}"
    
class Carro(Veiculo):
    def __init__(self, marca, ano, preco, modelo, potencia):
        super().__init__(marca, ano, preco)
        self.modelo = str(modelo)
        self.potencia = int(potencia)

    def Exibibirinfo(self):
        return super().Exibibirinfo()+f"\nModelo: {self.modelo} \nPotencia: {self.potencia} cavalos"
    
class Moto(Veiculo):
    def __init__(self, marca, ano, preco, cilindrada):
        super().__init__(marca, ano, preco)
        self.cilindra = cilindrada
    
    def Exibibirinfo(self):
        return super().Exibibirinfo()+f"\nCilindrada: {self.cilindra}"
    
veiculozinho = Veiculo("chevrolet",2007,2000.90)
print(veiculozinho.Exibibirinfo())

carrin = Carro("Ferrari", 1954, 500000, "perolas", 700)
print(carrin.Exibibirinfo())

Sheila = Moto("sheila",2004,3000,7)
print(Sheila.Exibibirinfo())