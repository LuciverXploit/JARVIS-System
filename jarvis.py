import speech_recognition as srec
from gtts import gTTS
import os

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan....')
        suara = mendengar.listen(source,phrase_time_limit=5)
        try: 
            print('Diterima...')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except: 
            pass
        return dengar

def ngomong(self):
    teks = (self)
    bahasa = 'id'
    namafile = 'Ngomong.mp3'
    def reading():
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        os.system(f'start {namafile}')
    reading()

def run_jarvis():
    Layanan = perintah()
    #print(Layanan)
    ngomong(Layanan)

run_jarvis()