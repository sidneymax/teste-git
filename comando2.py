class Carro: 

    def __init__(self, marca, modelo, ano, lugares, garantia, gps):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.lugares = lugares
        self.garantia = garantia
        self.gps = gps

    def caracteristicas (self):
        #print(f"Marca: '{self.marca}' - Modelo: '{self.modelo}' - Ano: '{self.ano}'")
        return f"Marca: '{self.marca}' - Modelo: '{self.modelo}' - Ano: '{self.ano}'"
    
    def opcoes (self): 
        #print(f"Lugares: '{self.lugares} - Garantia: '{self.garantia} - GPS: '{self.gps}' ")
        return f"Lugares: '{self.lugares}' - Garantia: '{self.garantia}' - GPS: '{self.gps}'"

carro1 = Carro("Spin", "Familia", "2020", "7 Lugares", "Garantia de 5 anos", "GPS Offline")
carro2 = Carro("Etios", "Cross", "2016", "5 Lugares", "Garantia de 5 anos", "GPS Offiline")

#print("Carros modelos familia")
print(carro1.caracteristicas())
print(carro1.opcoes())
print(carro2.caracteristicas())
print(carro2.opcoes())