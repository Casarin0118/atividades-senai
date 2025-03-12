from onibus import Onibus

lista = [
    Onibus(nome="Linha Azul", empresa="TransCity", rota="Centro - Zona Sul", frequencia="Diária", tipo="Urbano"),
    Onibus(nome="Expresso Litorâneo", empresa="Viação Costa Azul", rota="São Paulo - Santos", frequencia="De hora em hora", tipo="Rodoviário"),
    Onibus(nome="Conexão Aeroporto", empresa="AirportBus", rota="Centro - Aeroporto Internacional", frequencia="A cada 30 minutos", tipo="Executivo"),
    Onibus(nome="Linha Circular", empresa="CityMove", rota="Bairros periféricos - Terminal Central", frequencia="Dias úteis", tipo="Urbano"),
    Onibus(nome="Serra Verde Express", empresa="EcoTour", rota="Curitiba - Morretes", frequencia="Finais de semana", tipo="Turístico")
]

for i in range (0, 5):
    print(lista[i])
