import redis

r = redis.Redis(
    host='redis-15002.c1.us-east1-2.gce.cloud.redislabs.com',
    port=15002,
    password='tvowDquckFJSAxCIGAE2KXC4dQyH7ewa')

# def set_fn():
#     try:
#         fn = int(input("Введите номер телефона: "))
#         f_name = input("Введите имя друга: ")
#         r.set(f_name, fn)
#     except ValueError as error:
#         print("Допустим ввод только чисел")
#     finally:
#         print(r.get(f_name))
#
# def delete_fn(f_name):
#     r.delete(f_name)
#     print(r.get(f_name))
#
# delete_fn('Имя')

cont = True

while cont:
  action = input('action:\t')
  if action == 'write':
    name = input('name:\t')
    phone = input('phone:\t')
    red.set(name, phone)
  elif action == 'read':
    name = input('name:\t')
    phone = red.get(name)
    if phone:
      print(f'{name}\'s phone is {str(phone)}')
  elif action == 'delete':
    name = input('name:\t')
    phone = red.delete(name)
    if phone:
      print(f"{name}'s phone is deleted")
    else:
      print(f"Not found {name}")
  elif action == 'stop':
    break

