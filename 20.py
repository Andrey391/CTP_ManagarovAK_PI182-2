class Dr:
    def init__(self):
            self.price  = 0.0
            self.volume = 0.0
            self.name   = ""

balance = int(input("Введите баланс: "))
drAm = int(input("Введите количество напитков: "))

best = Dr()
input = Dr()

for i in range(drAm):
	_input.name   = input("Имя напитка: ")
	_input.price  = int(input("Цена напитка: "))
	_input.volume = int(input("Объём напитка: "))

	liters = (balance // input.price) * input.volume
	if liters == 0:
		continue
	
	if best.price == 0:
		best = input
		continue
	
	bLiters = (balance // best.price) * best.volume
	if liters > bLiters:
		best = input

if best.price == 0:
	print(-1)
else:
    bottles = balance // best.price
    print("{} {}\n{}\n{}".format(best.name, bottles, bottles * best.volume,
        balance - best.price * bottles))