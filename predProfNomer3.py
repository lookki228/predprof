with open("game.txt", encoding = "UTF-8") as file1:
    a = []
    for i in file1:
        a.append(i.split("$"))

while True:

    name = input("Введите имя персонажа: ")
    if name == "game":
        break
    flag = True
    listGame = []

    #Добавление игр с введеным именем добавляем в массив
    for i in a:
        if i[1] == name:
            listGame.append(i[0])
            flag = False

#Выводи значиния в зависимости от флага
    if flag:
        print("Этого персонажа не существует")

    else:
        print(f"персонаж {name} встречается в играх: ")
        count = 0

        #Вывод игр до 5 штук
        for i in listGame:
            if count <= 4:
                print(i)
                count += 1
            else:
                print("и др.")
                break


