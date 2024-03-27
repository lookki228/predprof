with open("game.txt", encoding = "UTF-8") as file1:
    a = []
    for i in file1:
        a.append(i.split("$"))

#ищем ошибки с "55", а после производим замену ошибки и даты
for i in a:
    if "55" in i[2]:
        print(f"у персонажа {i[1]} в игре {i[0]} нашлась ошибка с кодом {i[2]} дата фиксации {i[3]}")
        i[2] = "Done"
        i[3] = "0000-00-00" + "\n"

#записываем в новый файл
with open("game_new.csv", "w", encoding = "UTF-8") as file2:
    for i in a:
        file2.write(i[0] + ", " + i[1] + ", " + i[2] + ", " + i[3])
        
