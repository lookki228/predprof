with open("game.txt", encoding = "UTF-8") as file1:
    a = []
    for i in file1:
        a.append(i.split("$"))

#создаем список с не повторяющимися играми
listGames = []
for i in a:
    listGames.append(i[0])
listGame = set(listGames)

#делаем список с игрой и колличеством ее повторений
listGamesWithValue = []
for i in listGame:
    count = 0
    for j in a:
        if i == j[0]:
            count += 1
    listGamesWithValue.append([i, count])


#добавляем новый слобец
a[0][3] = a[0][3][:-1]
a[0].append("counter" + "\n")
for j in listGamesWithValue:
    for i in range(1,len(a)):
        if a[i][0] == j[0]:
            a[i][3] = a[i][3][:-1]
            a[i].append(str(j[1]) + "\n")

with open("game_counter.csv", "w", encoding = "UTF-8") as file2:
    for i in a:
        file2.write(i[0] + ", " + i[1] + ", " + i[2] + ", " + i[3] + ", " + i[4])

