import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        teks = mytoken.SAPA + "\n-- admin & developer @Bimo_Wibowo - SMK Taruna Bhakti -- "+"\n" \
                                "ketik /help untuk mengetahui fitur apa saja yang bisa kamu gunakan"+"\n" \
                        "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['help'])
    def help(message):
        teks = mytoken.SAPA + "\n-- HALLO SAYA botak BOT ASISTEN KAMU SEKARANG -- "+"\n" \
                              "Aku bisa membantu kamu dengan perintah:"+"\n" \
                              "/start : Untuk memulai"+"\n" \
                              "/help : agar kamu tau apa yang bisa dilakukan oleh bot ini"+"\n" \
                              "/datasiswa : Untuk melihat data siswa XI RPL 1 dan XI RPL 2"+"\n"
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="\n select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata=''
        if(jmldata>0):
            print(data)
            no=0
            for x in data:
                no += 1
                kumpuldata =kumpuldata+ str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)
