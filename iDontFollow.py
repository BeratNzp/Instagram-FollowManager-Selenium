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

    for dif in sorted(myFollowersList):
        if dif not in myFollowingsList:
            count+=1
            print(dif)
    print(f"\nSizi takip eden {count} kişiyi takip etmiyorsunuz.")
    myFollowers.close()
    myFollowings.close()

