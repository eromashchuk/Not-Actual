class Client:
    def __init__(self,name='',surname='',city='',balance=0):
        self.name = name
        self.surname = surname
        self.city=city
        self.balance=balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def get_guest(self):
        return f'{self.name} {self.surname},г. {self.city}'

client1 = Client('Ekaterina', 'Romashchuk', 'New York', 100000000000)
print(client1)

x_1 = Client('Иван','Петров','Москва',50)
x_2 = Client('Владимир','Зайцев','Кострома',50)
x_3 = Client('Олеся','Янина','Новосибирск',50)

guest_list = [x_1, x_2, x_3]

for guest in guest_list:
    print(guest.get_guest())