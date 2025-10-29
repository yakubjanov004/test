import random
import sys
import time
from colorama import Fore
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()
def combo(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(200. / 1850)
n = '\033[1;35m'
j = '\033[1;36m'
o = '\033[1;31m'
x=j+""" 𝐀𝐍𝐎𝐒 x̸ 𝟒𝑳 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬
 """
combo(x)
import requests 
import random,datetime,sys 
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White
insta="1234567890qwertyuiopasdfghjklzxcvbnm_"
all="qwertyuiopasdfghjkzxcvbnm_"

# Tekshirilgan usernamelar fayli
CHECKED_FILE = "checked_usernames_test.txt"

# Fayl mavjudligini tekshirish va yaratish
def load_checked_usernames():
    """Tekshirilgan usernamelarni fayldan o'qish"""
    try:
        with open(CHECKED_FILE, 'r', encoding='utf-8') as f:
            checked = set()
            for line in f:
                line = line.strip()
                if line:
                    # "username - good user" formatidan faqat username ni oladi
                    if ' - good user' in line:
                        username = line.split(' - good user')[0].strip()
                    else:
                        username = line
                    checked.add(username)
            return checked
    except FileNotFoundError:
        return set()

def save_username(username, is_good=False):
    """Username ni faylga yozish"""
    try:
        with open(CHECKED_FILE, 'a', encoding='utf-8') as f:
            if is_good:
                f.write(f"{username} - good user\n")
            else:
                f.write(username + '\n')
    except Exception as e:
        print(W+f" [+] {Z} Faylga yozish xatosi: {X}{str(e)[:30]}")

checked_set = load_checked_usernames()
if checked_set:
    print(W+f" [+] {F} {len(checked_set)} ta username allaqachon tekshirilgan (fayldan yuklandi)")

#-------------------------start code ---------------------------#
def instaa(user):
    # Agar bu username allaqachon tekshirilgan bo'lsa, o'tkazib yuborish
    if user in checked_set:
        return
    
    try:
        url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false', timeout=10)
        
        # Username ni faylga yozish (tekshirilgan deb belgilash)
        checked_set.add(user)
        
        # Status code tekshirish
        if url.status_code != 200:
            print(W+f" [+] {Z} Status Code Error ({url.status_code}): {X}{user} - Response: {url.text[:100]}")
            save_username(user, is_good=False)
            return
        
        # Response bo'shligini tekshirish
        if not url.text or len(url.text.strip()) == 0:
            print(W+f" [+] {Z} Empty Response: {X}{user}")
            save_username(user, is_good=False)
            return
        
        # Response textni tekshirish
        response_text = url.text.lower()
        
        if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
            print(W+f" [+] {Z} ErRoR UsEr (Spam Detected): {X}{user} ")
            save_username(user, is_good=False)
        elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text or '"username_is_taken"' in response_text:
            print(W+f" [+] {Z} 𝗕𝗔𝗗 𝗨𝗦𝗘𝗥 (Username Taken): {X}{user} ")
            save_username(user, is_good=False)
        elif '"status":"ok"' in response_text and '"errors":' not in response_text:
            # Faqat to'g'ri response va "status":"ok" bo'lsa "good" deb belgilash
            email=0
            print(W+f" [+] {F} 𝗚𝗢𝗢𝗗 𝗨𝗦𝗘𝗥 : {C}{user} ")
            email+=1
            save_username(user, is_good=True)  # Good user bo'lsa belgilash
            hit=f"""𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 : @{user}"""
            try:
                tg_response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={hit}', timeout=5)
                if tg_response.status_code == 200:
                    print(W+f" [+] {F} ✅ Telegramga yuborildi: {C}{user}")
                else:
                    print(W+f" [+] {Z} ⚠️  Telegram xatosi: {X}{tg_response.status_code}")
            except requests.exceptions.Timeout:
                print(W+f" [+] {Z} ⚠️  Telegram timeout")
            except Exception as e:
                print(W+f" [+] {Z} ⚠️  Telegram xatosi: {X}{str(e)[:30]}")
        else:
            # Noto'g'ri response - debug uchun ko'rsatish
            print(W+f" [+] {Z} Unknown Response: {X}{user} - Response: {url.text[:200]}")
            save_username(user, is_good=False)
    except requests.exceptions.Timeout:
        # Xatolik bo'lsa ham username ni yozib qo'yish
        checked_set.add(user)
        save_username(user, is_good=False)
        print(W+f" [+] {Z} Timeout: {X}{user} - Qayta urinib ko'rilmoqda...")
        sleep(2)
    except requests.exceptions.ConnectionError:
        # Xatolik bo'lsa ham username ni yozib qo'yish
        checked_set.add(user)
        save_username(user, is_good=False)
        print(W+f" [+] {Z} Connection Error: {X}{user} - Qayta urinib ko'rilmoqda...")
        sleep(3)
    except Exception as e:
        # Xatolik bo'lsa ham username ni yozib qo'yish
        checked_set.add(user)
        save_username(user, is_good=False)
        print(W+f" [+] {Z} Error: {X}{user} - {str(e)[:50]}")
        sleep(1)
def users():
    ran1="1234567890..__qwertyuiopasdfghjklzxvcbnm__.."
    try:
        while True:
            v1 = str(''.join((random.choice(insta) for i in range(1))))
            v2 = str(''.join((random.choice(insta) for i in range(1))))
            v3 = str(''.join((random.choice(insta) for i in range(1))))
            v4 = str(''.join((random.choice(insta) for i in range(1))))
            v5 = str(''.join((random.choice(insta) for i in range(1))))
            # Faqat 5 harfli usernamelar generatsiya qilinadi (_ ham qo'shiladi)
            user1 = (v1+v2+v3+v4+v5)  # 5 harfli username
            user2 = (v2+v1+v3+v4+v5)  # 5 harfli username (variant)
            user3 = (v1+v3+v2+v4+v5)  # 5 harfli username (variant)
            user4 = (v5+v1+v2+v3+v4)  # 5 harfli username (variant)
            user5 = (v1+v2+v5+v3+v4)  # 5 harfli username (variant)
            hamo010 = (user1, user2, user3, user4, user5)
            user = random.choice(hamo010)
            
            # Agar username allaqachon tekshirilgan bo'lsa, keyingisiga o'tish
            if user not in checked_set:
                instaa(user)
            else:
                continue
    except KeyboardInterrupt:
        print(W+f"\n [+] {Z} Dastur to'xtatildi (Ctrl+C)")
        print(W+f" [+] {F} Jami {len(checked_set)} ta username tekshirildi")
        print(W+f" [+] {F} Ma'lumotlar {CHECKED_FILE} fayliga saqlandi")
        sys.exit(0)
# .env fayldan ID va Token o'qish
id = os.getenv("TELEGRAM_USER_ID")
token = os.getenv("BOT_TOKEN_TEST")

# Agar .env faylda ma'lumotlar bo'lmasa, xatolik
if not id or not token:
    print(W+f" [+] {Z} Xatolik: .env faylda TELEGRAM_USER_ID yoki BOT_TOKEN_TEST topilmadi!")
    print(W+f" [+] {Z} Iltimos, .env faylni to'ldiring!")
    sys.exit(1)

print(f"{X}  𝗜𝗗 : {C}{id}")
print(f"{X} 𝗧𝗢𝗞𝗘𝗡 : {C}{token[:20]}...")
print()	
users()


#Todevelopers
