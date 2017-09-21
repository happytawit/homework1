i = 0
print("Загада №1: Какой язык мы изучаем?")
answer1 = input("Ваш ответ: ")
answer1 = answer1.lower()
if(answer1 == "python"):
        i = i + 1
        print("Это правильный ответ!")
else: print("Это неправильный ответ")

print("Загада №2: В каком формате у нас будет экзамен?")
answer2 = input("Ваш ответ: ")
answer2 = answer2.lower()
if(answer2 == "в формате worldskills"):
        i = i + 1
        print("Это правильный ответ!")
else: print("Это неправильный ответ")

print("Загада №3: В каком году был открыт этот язык?")
answer3 = input("Ваш ответ: ")
answer3 = answer3.lower()
if(answer3 == "1991"):
        i = i + 1
        print("Это правильный ответ!")
else: print("Это неправильный ответ")

print("Загада №4: Кто автор?")
answer4 = input("Ваш ответ: ")
answer4 = answer4.lower()
if(answer4 == "гвидо ван россум"):
        i = i + 1
        print("Это правильный ответ!")
else: print("Это неправильный ответ")

print("Загада №5: Какую типизацию поддерживает python?")
answer5 = input("Ваш ответ: ")
answer5 = answer5.lower()
if(answer5 == "динамическую"):
        i = i + 1
        print("Это правильный ответ!")
else: print("Это неправильный ответ")

print("Правильных ответов: ", i)
