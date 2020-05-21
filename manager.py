import getMyFollowers,getMyFollowings,whoDontFollowMe,iDontFollow

username = ""
password = ""

class __main__:
    while True:
        print(f"""========================================================
Follow Manager
========================================================

1) Giriş Ayarları
2) Bağlantılarımı Çek
3) Beni Takip Etmeyenleri Listele
4) Benim Takip Etmediklerimi Listele

0) Çıkış
========================================================""")
        processInput = input()
        userDebug = "n"

        if int(processInput) == 1 and userDebug == "n":
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
                password = input("Parola: ")
                userDebug = "n"
                continue

        elif int(processInput) == 2:
            print("\n\n")
            print("========================================================")
            print("İşlem başladı yaklaşık 4 dakika sürebilir. Lütfen bekleyiniz.")
            followers = getMyFollowers.Instagram(username, password)
            followers.signIn()
            followers.getFollowers()
            followers.browser.close()

            followings = getMyFollowings.Instagram(username, password)
            followings.signIn()
            followings.getMyFollowings()
            followings.browser.close()

            print("Bağlantılarınız çekildi.")
            print("========================================================")
            print("\n\n")
            continue

        elif int(processInput) == 3:
            print("\n\n")
            print("========================================================")
            whoDontFollowMe.showDifferents()
            print("========================================================")
            print("\n\n")
            continue

        elif int(processInput) == 4:
            print("\n\n")
            print("========================================================")
            iDontFollow.showDifferents()
            print("========================================================")
            print("\n\n")
            continue

        elif int(processInput) == 0:
            break