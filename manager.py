import getMyFollowers,getMyFollowings,whoDontFollowMe,iDontFollow,getpass

username = ""
password = ""
userDebug = "y"
messageBox = []

class __main__:
    while True:
        print(f"""========================================================
FollowManager
========================================================

1) Giriş Ayarları
2) Bağlantılarımı Çek
3) Beni Takip Etmeyenleri Listele
4) Benim Takip Etmediklerimi Listele

0) Çıkış
========================================================""")
        for message in messageBox:
            print(message)
            messageBox.remove(message)
        processInput = input()

        if int(processInput) == 1:
            if username and password:
                userDebug = input("Kullanıcı adı ve parola tanımlandı. Kullanıcıyı kaldırmak istiyorsanız 'y' yazin. Devam etmek için 'n' yazin")
                if userDebug == "y":
                    username=""
                    password=""
                    continue
                continue
            else:
                print("Kullanıcı adı ve parolanızı tanımlayın")
                username = input("Kullanıcı Adı: ")
                password = getpass.getpass("Parola: ")
                userDebug = "n"
                continue

        elif int(processInput) == 2:
            if userDebug == "n":
                print("\n\n")
                print("========================================================")
                print("İşlem başladı. Bu işlem takipçi/takip edilen sayınıza bağlı olarak uzun sürebilir. Lütfen bekleyiniz.")
                followers = getMyFollowers.Instagram(username, password)
                followers.signIn()
                followers.getFollowers()
                followers.browser.close()

                followings = getMyFollowings.Instagram(username, password)
                followings.signIn()
                followings.getMyFollowings()
                followings.browser.close()

                messageBox.append("Bağlantılarınız çekildi.")
                print("========================================================")
                print("\n\n")
                continue
            elif userDebug == "y":
                messageBox.append("Henüz giriş ayarlarınızı tanımlamadınız.")
                continue

        elif int(processInput) == 3:
            print("\n\n")
            print("========================================================")
            whoDontFollowMe.showDifferents()
            print("========================================================")
            print("\n\n")
            messageBox.append("Çıktınızı görmek için yukarı kaydırın.")
            continue

        elif int(processInput) == 4:
            print("\n\n")
            print("========================================================")
            iDontFollow.showDifferents()
            print("========================================================")
            print("\n\n")
            messageBox.append("Çıktınızı görmek için yukarı kaydırın.")
            continue

        elif int(processInput) == 0:
            break
