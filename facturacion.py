class Cuenta:

    menu = {
        'vino': 100,
        'cerveza': 50,
        'gaseosa': 30,
        'cafe': 10
    }

    def __init__(self):
        self.total = 0
        self.bebidas = []

    def add(self, bebida):
        self.bebidas.append(bebida)
        self.total += self.menu[bebida]

    def print_factura(self):
        tax = self.total*0.21
        total = self.total + tax
        for bebida in self.bebidas:
            print(f'{bebida:20}${self.menu[bebida]}')
        print('tax:    $' f'{tax}')
        print("Total:  $" f'{(total)}'),
