import random
import time


def tas_kagit_makas_MERVE_EFE_BEYAZ():
    print("\nTaş, kağıt, makas oyununa hoş geldin! Bu oyun iki kişilik bir oyundur.")
    print("Bu oyunda Taş, Makası Yener; Makas, Kağıdı Yener; Kağıt, Taşı Yener.")
    print("İlk iki turu kazanan, oyunu kazanır.\n")
    time.sleep(1)
    print("Bilgisayara oynamak isteyip istemediği soruluyor...\n")
    time.sleep(1)
    cpu = random.randint(0, 1)
    if cpu == 1:
        print("Bilgisayar oynamak istiyor.\n")
    else:
        print("Bilgisayar oynamalık havasında değilmiş. Bence tekrar deneyip ikna etmelisin :)")
        return 0
    print("Oynamak istiyor musun?")
    player = input("y/n: ")

    player_score = 0
    cpu_score = 0
    choice_list = ["t", "k", "m"]
    if player == 'y' and cpu == 1:
        print("\nOyun başlatılıyor...")
        time.sleep(1)
        while True:
            player_choice = input("\nTaş(t), Kağıt(k), Makas(m) seçeneklerinden birini seçin: ")
            time.sleep(1)
            if player_choice != 't' and player_choice != 'k' and player_choice != 'm':
                print("Geçersiz bir seçim yapıldı tekrar deneyin!")
                pass
            else:
                cpu_choice_index = random.randint(0, 2)
                cpu_choice = choice_list[cpu_choice_index]
                if player_choice == cpu_choice:
                    print("\nBerabere kalındı. Tekrar seçim yapılacak...")
                    print("Güncel Skor: Oyuncu: ", player_score, " Bilgisayar: ", cpu_score)
                    pass
                else:
                    if player_choice == 't' and cpu_choice == 'm':
                        print("\nTaş makası kırar. Bu turu oyuncu kazandı")
                        player_score += 1
                        print("Güncel Skor: Oyuncu: ", player_score, " Bilgisayar: ", cpu_score)
                    elif player_choice == 't' and cpu_choice == 'k':
                        print("\nKağıt taşı sarar. Bu turu bilgisayar kazandı")
                        cpu_score += 1
                        print("Güncel Skor: Oyuncu: ", player_score, " Bilgisayar: ", cpu_score)
                    elif player_choice == 'm' and cpu_choice == 'k':
                        print("\nMakas kağıdı keser. Bu turu oyuncu kazandı")
                        player_score += 1
                        print("Güncel Skor: Oyuncu: ", player_score, " Bilgisayar: ", cpu_score)
                    elif player_choice == 'm' and cpu_choice == 't':
                        print("\nTaş makası kırar. Bu turu bilgisayar kazandı")
                        cpu_score += 1
                        print("Güncel Skor: Oyuncu: ", player_score, " Bilgisayar: ", cpu_score)
                    elif player_choice == 'k' and cpu_choice == 't':
                        print("\nKağıt taşı sarar. Bu turu oyuncu kazandı")
                        player_score += 1
                        print("Güncel Skor: Oyuncu: ", player_score, " Bilgisayar: ", cpu_score)
                    elif player_choice == 'k' and cpu_choice == 'm':
                        print("\nMakas kağıdı keser. Bu turu bilgisayar kazandı")
                        cpu_score += 1
                        print("Güncel Skor: Oyuncu: ", player_score, " Bilgisayar: ", cpu_score)
                if cpu_score == 2 or player_score == 2:
                    player_choice = input("\nYeniden oynamak ister misin? \ny/n: ")
                    cpu_choice = random.randint(0, 1)
                    if player_choice == 'y' and cpu_choice == 1:
                        print("\nYeni oyun başlatılıyor...")
                        time.sleep(1)
                        player_score = 0
                        cpu_score = 0
                    elif player_choice == 'n':
                        print("\nOyuncu oyundan çekildi. Oyun sonlandırılıyor.")
                        return 0
                    elif cpu_choice == 0:
                        print("\nBilgisayar oyundan çekildi. Oyun sonlandırılıyor.")
                        return 0
                    else:
                        print("\nHatalı değer girildi. Oyun sonlandırılıyor.")
                        return 0
    elif player == 'n':
        print("Oynamak istemiyorsan neden çalıştırdın beni...")
    elif cpu == 0:
        print("Bilgisayar oynamak istemiyor rami ağrıyormuş...")


tas_kagit_makas_MERVE_EFE_BEYAZ()
