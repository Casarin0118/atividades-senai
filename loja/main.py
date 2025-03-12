from carro import Carro
from moto import motos

Jetta = Carro(nome='Jetta', potencia='211cv', km='50.000', rodas=4, assentos='5', valor='65.000', ano=2015)
Passat = Carro(nome='Passat', potencia='180cv', km='80.000', rodas=4, assentos= '5', valor='120.000', ano=2018)

S1000RR = motos(rodas=2, assentos=2,valor='80.000', km='40.000',nome='BMW S1000 rr', potencia='150cv', ano=2014)
CB1000 = motos(rodas=2, assentos=2, valor= '70.000', km=35.000, nome='CB 1000', potencia='130cv', ano=2013)

Jetta.exibir_dados()
Passat.exibir_dados()
S1000RR.exibir_dados()
CB1000.exibir_dados()
