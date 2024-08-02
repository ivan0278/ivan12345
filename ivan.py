work={"Будівельник":"маляр",
      "Працівник магазину":"касир"}
answer=input("Додати новий вид роботи? 1 - так 0 - ні")
while answer!="0":
    login=input("Введи вид діяльності")
    password=input("Введи спеціальність")
    work[login]={"login":login, "password":password}
    answer=input("Додати новий вид роботи? 1 - так 0 - ні")
print("Список робот, зареєстрованихна сайті")
for user in work:
    print(user)
q1=input("Введи вид діяльності")
if q1 in work:
    print(site[q1])
else:
    print("Такогокористувача немає")
    