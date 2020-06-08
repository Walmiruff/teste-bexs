from controllers.Main import *
from sys import *


def obterViagem(grafo):
    print('Por favor informe qual a rota da viagem como no exemplo, ORG-DES: ')
    origin, destiny = input().split('-')
    origin = Vertex(origin)
    destiny = Vertex(destiny)

    route, cost = grafo.getRoute(origin.getId(), destiny.getId())
    print('A viagem com menor custo {} '. format(cost)+ ',terá a rota {}'. format(route))

if __name__ == '__main__':
    args = []
    for param in sys.argv:
        args.append(param)
    name_file = 'assets/input-routes.csv'
    controller = Main(name_file)
    controller.initGraph()
    controller.drawGraph()
    obterViagem(controller)



