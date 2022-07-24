from bowlingPlayer import bowlingPlayer

# User Defined Function
# Get user input to fill points received by the players.
def points():
    points = []
    frames = 10

    for i in range(frames):
        print(f'\nFrame No. {i + 1}  ')
        arr = []

        throw1 = 0
        throw2 = 0
        throw3 = 0
        if i < frames - 1:
            while True:
                throw1 = input("Score for first throw: ")
                if int(throw1) <= 10:
                    arr.append(int(throw1))
                    # break
                    if int(throw1) == 10:
                        print("STRIKE!")
                    break

            if int(throw1) < 10:
                while True:
                    throw2 = input("Score for second throw: ")
                    if (int(throw2) + int(throw1)) <= 10:
                        arr.append(int(throw2))
                        break
        else:
            while True:
                throw1 = input("Score for first throw: ")
                if int(throw1) <= 10:
                    arr.append(int(throw1))
                    break

            if int(throw1) < 10:
                while True:
                    throw2 = input("Score for second throw: ")
                    if int(throw2) + int(throw1) <= 10:
                        arr.append(int(throw2))
                        break

            elif int(throw1) == 10:
                while True:
                    throw2 = input("Second Throw: ")
                    if int(throw2) <= 10:
                        arr.append(int(throw2))
                        break

            if int(throw1) == 10 or int(throw1) + int(throw2) == 10:
                print("CONGRATULATIONS FOR EARNING THIRD THROW")
                while True:
                    throw3 = input("Third Throw: ")
                    if int(throw3) <= 10:
                        arr.append(int(throw3))
                        break

        points.append(arr)
    return points


count = input("Enter number of players: ")
players = []

for i in range(int(count)):
    print(f'\nPlayer {i + 1}')
    name = input("Insert Name: ")
    points = points()

    players.append(bowlingPlayer(name, points))

for i in range(len(players)):
    print(f'\nPlayer {i + 1}: {players[i].name}')
    print(f'Points: {players[i].points}')
    print(f'Total Points: {players[i].calcPoint()}')