from asyncio import gather

from cahchorro import Cachorro
from gato import Gato

cachorro1 = Cachorro(raca='bulldog', cor='Branco',idade='8', nome='Aston', enfeite='Laço')
cachorro2 = Cachorro(raca='Golden', cor='marrom-claro', idade= '3', nome='Amora', enfeite='Laço')
gato1 = Gato(raca='gato', cor='preto', idade='7', nome='belinha', coleira='Rosa')
gato2 = Gato(raca='siames', cor='Branco', idade='8', nome='bonitinha', coleira='Azul')

cachorro1.exibir_cachorro()
cachorro2.exibir_cachorro()
gato1.exibir_cachorro()
gato2.exibir_cachorro()