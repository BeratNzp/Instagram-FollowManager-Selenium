def showDifferents():
    myFollowers = open("myFollowers.txt", "r")
    myFollowings = open("myFollowings.txt", "r")

    myFollowersList = []
    myFollowingsList = []

    for line in myFollowers:
        myFollowersList.append(line[0:-1])

    for line in myFollowings:
        myFollowingsList.append(line[0:-1])

    count = 0

    for dif in sorted(myFollowingsList):
        if dif not in myFollowersList:
            count+=1
            print(dif)
    print(f"Takip ettiğiniz {count} kişi sizi takip etmiyor.")
    myFollowers.close()
    myFollowings.close()

