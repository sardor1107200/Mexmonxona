import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

domen = "smtp.gmail.com"
port = 587
email_yuboruvchi = "sardoregamberduyev@gmail.com"
parol = "vncy rajk amas kxmx"

xonalar = {i: random.randint(200_000, 20_000_000) for i in range(1, 1001)}
kiritilgan_email = set()

def email_jo_natish(manzil, matn):
    try:
        server = smtplib.SMTP(domen, port)
        server.starttls()
        server.login(email_yuboruvchi, parol)

        msg = MIMEMultipart()
        msg['From'] = email_yuboruvchi
        msg['To'] = manzil
        msg['Subject'] = "Xush kelibsiz!"

        msg.attach(MIMEText(matn, 'plain'))
        server.send_message(msg)
        server.quit()
        print(f"Email {manzil} manziliga muvaffaqiyatli yuborildi!")
    except smtplib.SMTPAuthenticationError:
        print("Email jo'natishda xatolik yuz berdi: Foydalanuvchi nomi yoki parol noto'g'ri. Iltimos, qaytadan tekshiring.")
    except Exception as e:
        print(f"Email jo'natishda xatolik yuz berdi: {e}")

print("\n********** Mexmon Xona **********")
print("1. VIP Kabinet\n2. Odiy Kabinet\n3. Pro Xona")

a = input("\nQanday Kabinet tanlaysiz? ")
if a == "1":
    print("\nSiz VIP kabinet tanladingiz.")
elif a == "2":
    print("\nSiz Odiy kabinetni tanladingiz.")
elif a == "3":
    print("\nSiz Pro Xona tanladingiz.")
else:
    print("\nNoto'g'ri tanlov!")

if a == "1":
    print('''VIP kabineta 
    2 kishilik kravat🛌
    1 ta saunzel🚿
    1 ta karaoki🎙
    1 playsteshin 4 🎥
    1 ta telivizor🖥
    1 baseyn🏝
    1 ta tens🏓
    1 ta bilyart🎱
    1 kuxnya 🏠️
    ''')

elif a == "2":
    print('''Odiy kabinet
    2 kishilik kravat🛌
    1 ta telivizor🖥
    1 ta saunzel🚿
    1 ta kuxnya🏠️
    1 ta tens🏓 ️''')

elif a == "3":
    print('''Pro kabinet
    4 kishilik kravat🛌
    2 ta telivizor🖥
    1 ta plasteshin 5 🎥
    1 ta karaoki🎙
    1 ta tens🏓 
    2 ta bilyart🎱
    2 ta saunzel🚿
    2 ta baseyn🏝
    2 kishilik masaj🧘🏼''')

while True:
    try:
        xona = int(input("\nXona raqamini kiriting (1-1000): "))
        kun = int(input("Necha kunga bron qilasiz? (1-30): "))
        if 1 <= xona <= 1000 and 1 <= kun <= 30:
            break
        else:
            print("Xona 1 dan 1000 gacha, kun esa 1 dan 30 gacha bo‘lishi kerak.")
    except ValueError:
        print("Iltimos, son kiriting.")

while True:
    email = input("Email manzilingizni kiriting (masalan: example@example.com): ")

    if email in kiritilgan_email:
        print("Ushbu email manzili allaqachon kiritilgan.")
        break
    else:
        if "@gmail.com" in email:
            print("\nSalom! Ushbu gmail manzili qabul qilindi.")
            email_jo_natish(email, "Hurmatli mijoz, xush kelibsiz! Siz bizning xizmatimizdan foydalanganingiz uchun rahmat.")
        else:
            print("\nBunday gmail mavjud emas. Iltimos, to'g'ri manzil kiriting.")
            continue

        kiritilgan_email.add(email)
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")

        print("\nKiritilgan ma'lumotlar:")
        print(f"Email manzili: {email}")
        print(f"Ism: {ism}")
        print(f"Familiya: {familiya}")
        break
print(f"\nbron qilinga gmile {email}")
print(f"\nTanlangan xona raqami: {xona}, {kun} kun narxi: {xonalar[xona] * kun:,} so'm.")
