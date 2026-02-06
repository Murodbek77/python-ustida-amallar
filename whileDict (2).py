# Do`stlarini ro`yhatini tuzadigan dastur
# print("Yaqin do`stlaringizni ro`yhatini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}- do`stingizni ismini kiriting?"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input('Yana ism qo`shishni hohlaysizmi? ha/yo`q:')
#     n +=1
#     if takrorlash != 'ha':
#         break

# print("Siznig do`stlaringizni ro`yhati")
# for ism in ismlar:
#         print(ism.title())

# Lug`at orqali lug`atni to`ldirish

# print('Do`stlaringizni yoshini saqlaydigan dastur ishlab chiqamiz.')
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input('Do`stingizni ismini kiriting.')
#     yosh = input('Dos`tingizni yoshini kiritng.')
#     dostlar[ism] = int(yosh)

#     javob = input('Siz do`stlaringizni yana ko`shishni hohlaysizmi. ha/yo`q:')
#     if javob == 'yo`q':
#         ishora = False

# # print('Sizning do`stlaringizni ism va yoshi')
# for ism,yosh in dostlar.items():
#     print(f"Sizning do`stingizni ismi {ism.title()} yoshi {yosh}")


# cars = {'nexia','lacetti','audi','bmw','nexia'}
# print(type(cars))
# print(sorted(cars))

# cars = ['nexia','lacetti','nexia','audi','bmw','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)


# talabalar = ['hasan','husan','olim','botir']
# talabalar_baho = {}

# while talabalar:
#     talaba = talabalar.pop(0)
#     baho = input(f"Talaba {talaba.title()}ning bahosi kiriting:")
#     print(f"Talaba {talaba.title()}ning baxosi qo`yildi.")
#     talabalar_baho[talaba] = int(baho) 
# print("Talabalarning bahosi quyidagicha.")

# for ism,baho in talabalar_baho.items():
#     print(f"Talaba {ism.title()}, bahosi {baho}")

