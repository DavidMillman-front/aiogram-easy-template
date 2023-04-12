import requests as req
from utils.misc.transliterate import transliterate
from googletrans import Translator
tr = Translator()
import time

parts_of_Quran_in_juzs1 = {"1": "Al-Fatihah surasidan Al-Baqarah surasining 141-oyatigacha",
                 "2": "Al-Baqarah surasining 142-oyatidan 252-oyatigacha",
                 "3": "Al-Baqarah surasining 253-oyatidan Ali-'Imran surasining 92-oyatigacha",
                 "4": "Ali-'Imran surasining 93-oyatidan An-Nisa surasining 23-oyatigacha",
                 "5": "An-Nisa surasining 24-oyatidan 147-oyatigacha",
                 "6": "An-Nisa surasining 148-oyatidan Al-Ma'idah surasining 81-oyatigacha",
                 "7": "Al-Ma'idah surasining 82-oyatidan Al-An'am surasining 110-oyatigacha",
                 "8": "Al-An'am surasining 111-oyatidan Al-Ar'af surasining 87-oyatigacha",
                 "9": "Al-Ar'af surasining 88-oyatidan Al-Anfal surasining 40-oyatigacha",
                 "10": "Al-Anfal surasining 41-oyatidan At-Tawbah surasining 92-oyatigacha",
                 "11": "At-Tawbah surasining 93-oyatidan Yunus surasi va Hud surasining 5-oyatigacha",
                 "12": "Hud surasining 6-oyatidan Yusuf surasining 52-oyatigacha",
                 "13": "Yusuf surasining 53-oyatidan Ar-Ra'd surasi va Ibrahim surasining 52-oyatigacha'",
                 "14": "Al-Hijr surasining 1-oyatidan An-Nahl surasining 128-oyatigacha",
                 "15": "Al-Israa surasining 1-oyatidan Al-Kahf surasining 74-oyatigacha"}
parts_of_Quran_in_juzs2 ={"16": "Al-Kahf surasining 75-oyatidan Maryam surasi va Taa-Haa surasining 135-oyatigacha",
                 "17": "Al-Anbiyaa surasining 1-oyatidan Al-Hajj surasining 78-oyatigacha",
                 "18": "Al-Muminoon surasining 1-oyatidan An-Noor surasi va Al-Furqaan surasining 20-oyatigacha",
                 "19": "Al-Furqaan surasining 21-oyatidan Ash-Shu'araa surasi va An-Naml surasining 55-oyatigacha",
                 "20": "An-Naml surasining 56-oyatidan Al-Qasas surasi va Al-Ankaboot surasining 45-oyatigacha",
                 "21": "Al-Ankaboot surasining 46-oyatidan  Ar-Room, Luqman, As-Sajda suralari va  Al-Ahzaab surasining 30-oyatigacha",
                 "22": "Al-Ahzaab surasining 31-oyatidan Saba, Faatir suralari va Yaseen surasining 27-oyatigacha",
                 "23": "Yaseen surasining 28-oyatidan As-Saaffaat, Saad suralari va Az-Zumar surasining 31-oyatigacha",
                 "24": "Az-Zumar surasining 32-oyatidan Ghafir surasi va Fussilat surasining 46-oyatigacha",
                 "25": "Fussilat surasining 47-oyatidan Ash-Shura, Az-Zukhruf, Ad-Dukhaan suralari va Al-Jaathiya surasining 37-oyatigacha",
                 "26": "Al-Ahqaf surasining 1-oyatidan Muhammad, Al-Fath, Al-Hujuraat, Qaaf suralari va Adh-Dhaariyat surasining 31-oyatigacha",
                 "27": "Adh-Dhaariyat surasining 31-oyatidan At-Tur, An-Najm, Al-Qamar, Ar-Rahmaan,  Al-Waaqia suralari va Al-Hadid surasining 96-oyatigacha",
                 "28": "Al-Mujaadila surasining 1-oyatidan Al-Hashr, Al-Mumtahana, As-Saff, Al-Jumu'a, Al-Munaafiqoon, At-Taghaabun, At-Talaaq suralari va At-Tahrim surasining 12-oyatigacha",
                 "29": "Al-Mulk surasining 1-oyatidan Al-Qalam, Al-Haaqqa, Al-Ma'aarij, Nooh, Al-Jinn, Al-Muzzammil, Al-Muddaththir, Al-Qiyaama, Al-Insaan suralari va Al-Mursalaat surasining 50-oyatigacha",
                 "30": "An-Naba surasining 1-oyatidan An-Naazi'aat, Abasa, At-Takwir, Al-Infitaar, Al-Mutaffifin, Al-Inshiqaaq, Al-Burooj, At-Taariq, Al-A'laa, Al-Ghaashiya, Al-Fajr, Al-Balad, Ash-Shams, Al-Lail, Ad-Dhuhaa, Ash-Sharh, At-Tin, Al-Alaq, Al-Qadr, Al-Bayyina, Az-Zalzala, Al-Aadiyaat, Al-Qaari'a, At-Takaathur, Al-Asr, Al-Humaza, Al-Fil, Quraish, Al-Maa'un, Al-Kawthar, Al-Kaafiroon, An-Nasr, Al-Masad, Al-Ikhlaas, Al-Falaq suralari va An-Naas surasining oxirigacha!"}

number_of_ayahs_in_every_surah = [0, 7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110,
                                  98, 135, 112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88,
                                  75, 85, 54, 53, 89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24,
                                  13, 14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42,
                                  29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3,
                                  9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6]



async def Names_of_surahs(lang):
    line1, line2, line3, line4= '','','',''
    names = req.get("http://api.alquran.cloud/v1/surah").json()['data']
    if lang == 'uzl':
        for i in range(0, 30):
            print("doing", i)
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text
            line1 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Nomi: {str(names[i]['englishName'])}\n" + f"Tarjimasi: {translation}\nOyatlar soni:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(30, 60):
            print("doing", i)
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text
            line2 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Nomi: {str(names[i]['englishName'])}\n" + f"Tarjimasi: {translation}\nOyatlar soni:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(60, 90):
            print("doing", i)
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text
            line3 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Nomi: {str(names[i]['englishName'])}\n" + f"Tarjimasi: {translation}\nOyatlar soni:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(90, 114):
            print("doing", i)
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text
            line4 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Nomi: {str(names[i]['englishName'])}\n" + f"Tarjimasi: {translation}\nOyatlar soni:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
    elif lang == 'uzk':
        for i in range(0, 30):
            print("doing", i)
            if i%10 == 0 and i!=0:
                time.sleep(3)
            translation = transliterate(tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text, 'cyrillic')
            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            line1 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Номи: {transliteration}\n" + f"Таржимаси: {translation}\nОятлар сони:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(30, 60):
            print("doing", i)
            if i%10 == 0 and i!=0:
                time.sleep(3)
            translation = transliterate(tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text, 'cyrillic')
            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            line2 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Номи: {transliteration}\n" + f"Таржимаси: {translation}\nОятлар сони:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(60, 90):
            print("doing", i)
            if i%10 == 0 and i!=0:
                time.sleep(3)
            translation = transliterate(tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text, 'cyrillic')
            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            line3 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Номи: {transliteration}\n" + f"Таржимаси: {translation}\nОятлар сони:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(90, 114):
            print("doing", i)
            if i%10 == 0 and i!=0:
                time.sleep(3)
            translation = transliterate(tr.translate(text=str(names[i]['englishNameTranslation']), dest='uz', src='en').text, 'cyrillic')
            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            line4 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Номи: {transliteration}\n" + f"Таржимаси: {translation}\nОятлар сони:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
    elif lang == 'ru':
        for i in range(0, 30):
            print("doing", i)

            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='ru', src='en').text
            line1 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Имя: {transliteration}\n" + f"Перевод: {translation}\nKоличество аятов:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(30, 60):
            print("doing", i)

            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='ru', src='en').text
            line2 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Имя: {transliteration}\n" + f"Перевод: {translation}\nKоличество аятов:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(60, 90):
            print("doing", i)

            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='ru', src='en').text
            line3 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Имя: {transliteration}\n" + f"Перевод: {translation}\nKоличество аятов:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(90, 114):
            print("doing", i)

            transliteration = transliterate(str(names[i]['englishName']), 'cyrillic')
            translation = tr.translate(text=str(names[i]['englishNameTranslation']), dest='ru', src='en').text
            line4 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Имя: {transliteration}\n" + f"Перевод: {translation}\nKоличество аятов:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
    elif lang == 'en':
        for i in range(0, 30):
            print("doing", i)

            line1 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Name: {str(names[i]['englishName'])}\n" + f"Translation: {str(names[i]['englishNameTranslation'])}\nNumber of Ayahs:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(30, 60):
            print("doing", i)

            line2 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Name: {str(names[i]['englishName'])}\n" + f"Translation: {str(names[i]['englishNameTranslation'])}\nNumber of Ayahs:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(60, 90):
            print("doing", i)

            line3 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Name: {str(names[i]['englishName'])}\n" + f"Translation: {str(names[i]['englishNameTranslation'])}\nNumber of Ayahs:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"
        for i in range(90, 114):
            print("doing", i)

            line4 += f"{i + 1}\n {str(names[i]['name'])}\n" + f"Name: {str(names[i]['englishName'])}\n" + f"Translation: {str(names[i]['englishNameTranslation'])}\nNumber of Ayahs:  {str(number_of_ayahs_in_every_surah[i + 1])}\n\n"

    return line1, line2, line3, line4
