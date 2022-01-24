from bs4 import BeautifulSoup
import time
# import requests
from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def kriter1(url):
#Tüm ekranlarda bulunan logolar basıldığında ana ekrana yönlendirmeli.



    ekran1_url = "http://localhost:8080/"
    ekran2_url = "http://localhost:8080/screen2?"
    ekran3_url = "http://localhost:8080/screen3?"
    ekran4_url = "http://localhost:8080/screen4?"
    ekran5_url = "http://localhost:8080/showCases?"
    ekran6_url = "http://localhost:8080/screen6?"


    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/a/img").click()
    time.sleep(1)

    if browser.current_url == ekran1_url:
        print("1. ekrandaki logo çalışıyor")

    browser.quit
    time.sleep(1)

    browser.get(ekran2_url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/a/img").click()
    time.sleep(1)

    if browser.current_url == ekran1_url:
        print("2. ekrandaki logo çalışıyor")

    browser.quit
    time.sleep(1)

    browser.get(ekran3_url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/div/a/img").click()
    time.sleep(1)

    if browser.current_url == ekran1_url:
        print("3. ekrandaki logo çalışıyor")
    
    browser.quit
    time.sleep(1)

    browser.get(ekran4_url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/a[1]/img").click()
    time.sleep(1)

    if browser.current_url == ekran1_url:
        print("4. ekrandaki logo çalışıyor")


    browser.quit
    time.sleep(1)

    browser.get(ekran5_url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/a[1]/img").click()
    time.sleep(1)

    if browser.current_url == ekran1_url:
        print("5. ekrandaki logo çalışıyor")

    browser.quit
    time.sleep(1)

    browser.get(ekran6_url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/a[1]/img").click()
    time.sleep(1)

    if browser.current_url == ekran1_url:
        print("6. ekrandaki logo çalışıyor")

def kriter2(url):
#1. ekrandaki “BİLGİLENDİRME” butonuna basıldığında 6. ekrana yönlendirilecek. 

    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/form[1]/button").click()
    #bilgilendirme butonuna tıklama
    time.sleep(1)

    if browser.current_url == "http://localhost:8080/screen6?":
        print("Bilgilendirme butonuna basıldığında 6. ekrana gidiyor")

def kriter3(url):
#1. ekrandaki “GİRİŞ YAP & KAYIT OL” butonu basıldığında 2. Ekrana yönlendirilecek.

    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/nav/form[2]/button").click()
    #GİRİŞ YAP & KAYIT OL butonuna tıklama
    time.sleep(1)

    if browser.current_url == "http://localhost:8080/screen2?":
        print("GİRİŞ YAP & KAYIT OL butonuna basıldığında 2. ekrana gidiyor")

def kriter4(url):
#TC Kimlik No istenen ekranlarda bu bölüme girilebilecek karakter sayısı 11 karakter olmalı.

    #3. ve 2. ekranda var

    #ekran 2  10 karakter ve 12 karakter dene
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    ekran2_girisyap_tc =  browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]")
    ekran2_kayitol_tc =  browser.find_element_by_xpath("/html/body/div[2]/form/div/input[3]")

    ekran2_girisyap_tc.send_keys("1234567890")
    #10 karakter giriyoruz
    time.sleep(1)

    browser.find_element_by_xpath("/html/body/div[1]/form/div/button").click()
    time.sleep(1)


    ekran2_kayitol_tc.send_keys(Keys.CONTROL, 'a')
    ekran2_kayitol_tc.send_keys(Keys.BACKSPACE)
    #yazıyı siliyoruz
    time.sleep(1)

    ekran2_kayitol_tc.send_keys("12345678911")
    #11 karakter giriyoruz
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/form/div/button").click()
    time.sleep(1)

    ekran2_kayitol_tc.send_keys("1234567890")
    #10 karakter giriyoruz
    time.sleep(1)

    browser.find_element_by_xpath("/html/body/div[2]/form/div/button").click()
    time.sleep(1)


    ekran2_kayitol_tc.send_keys(Keys.CONTROL, 'a')
    ekran2_kayitol_tc.send_keys(Keys.BACKSPACE)
    #yazıyı siliyoruz
    time.sleep(1)

    ekran2_kayitol_tc.send_keys("12345678911")
    #11 karakter giriyoruz
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/form/div/button").click()
    time.sleep(1)
    

    #ekran 3, 10 karakter ve 12 karakter dene
    browser.get("http://localhost:8080/screen3?")
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    tarih_baslangic = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    tarih_bitis =  browser.find_element_by_xpath("/html/body/div/form/div/input[3]") 
    yurtdisi_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[1]/input[2]")
    yer_ismi = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    isim = browser.find_element_by_xpath("/html/body/div/form/div/input[4]")
    soyisim = browser.find_element_by_xpath("/html/body/div/form/div/input[5]")
    tc = browser.find_element_by_xpath("/html/body/div/form/div/input[6]")  
    numara = browser.find_element_by_xpath("/html/body/div/form/div/input[7]")
    email = browser.find_element_by_xpath("/html/body/div/form/div/input[8]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/h4/input")
    teklif_al_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/div/button")
    
    yurtdisi_buton.click()
    time.sleep(1)
    yer_ismi.send_keys("Almanya - Münih")
    time.sleep(1)
    tarih_baslangic.send_keys("12.10.2022")
    time.sleep(1)
    tarih_bitis.send_keys("20.10.2022")
    time.sleep(1)
    isim.send_keys("timur")
    soyisim.send_keys("bektas")
    tc.send_keys("12345")
    numara.send_keys("66666666666")
    email.send_keys("bektastimucin@gmail.com")
    time.sleep(1)
    kvk_buton.click()
    time.sleep(1)
    teklif_al_buton.click()
    time.sleep(1)
    
def kriter5(url):
#2. ekranda şifre belirlenirken en az 12 karakter olmalı,
# en az bir özel karakter içermeli, en az bir büyük harf içermeli, en az bir küçük harf içermeli, en az bir sayı içermeli.
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    kayıt_ol_isim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[1]")
    kayıt_ol_soyisim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[2]")
    kayıt_ol_tc = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[3]")
    kayıt_ol_numara = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[4]")
    kayıt_ol_sifre = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[5]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/h4[7]/input")
    kayıt_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/button")

    kayıt_ol_isim.send_keys("Timuçin")
    time.sleep(1)
    kayıt_ol_soyisim.send_keys("bektaş")
    time.sleep(1)
    kayıt_ol_tc.send_keys("00000000020")
    time.sleep(1)
    kayıt_ol_numara.send_keys("22222222222")
    time.sleep(1)
    kayıt_ol_sifre.send_keys("12345678911")
    #11 adet rakam
    kvk_buton.click()
    
 
    time.sleep(2)   
    kayıt_buton.click()


    kayıt_ol_sifre.send_keys(Keys.CONTROL, 'a')
    kayıt_ol_sifre.send_keys(Keys.BACKSPACE)
    #yazıyı siliyoruz
    time.sleep(2)

    kayıt_ol_sifre.send_keys("12345678911abs")
    #11 adet rakam ve 3 harf
    time.sleep(2)

    kayıt_buton.click()

    kayıt_ol_sifre.send_keys(Keys.CONTROL, 'a')
    kayıt_ol_sifre.send_keys(Keys.BACKSPACE)
    #yazıyı siliyoruz
    time.sleep(2)

    kayıt_ol_sifre.send_keys("12345678911_Abs")
    #11 adet rakam ve 3 harf
    time.sleep(2)

    kayıt_buton.click()

def kriter6(url):
#Telefon numarası istenen bölümlerde girilebilecek karakter sayısı tam 11 karakter olmalı.
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    kayıt_ol_isim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[1]")
    kayıt_ol_soyisim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[2]")
    kayıt_ol_tc = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[3]")
    kayıt_ol_numara = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[4]")
    kayıt_ol_sifre = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[5]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/h4[7]/input")
    kayıt_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/button")

    kayıt_ol_isim.send_keys("Timuçin")
    time.sleep(1)
    kayıt_ol_soyisim.send_keys("bektaş")
    time.sleep(1)
    kayıt_ol_tc.send_keys("00000000021")
    time.sleep(1)
    kayıt_ol_numara.send_keys("12345678")
    time.sleep(1)
    kayıt_ol_sifre.send_keys("12345678911_Abs")
    #11 adet rakam
    kvk_buton.click()
    time.sleep(1)
    kayıt_buton.click()

    time.sleep(2)
    kayıt_ol_numara.send_keys(Keys.CONTROL, 'a')
    kayıt_ol_numara.send_keys(Keys.BACKSPACE)
    #yazıyı siliyoruz
    time.sleep(2)

    kayıt_ol_numara.send_keys("12345678910")
    time.sleep(2)
    kayıt_buton.click()
    time.sleep(2)

def kriter7(url):
#)”KVKK’YI KABUL EDİYORUM” seçeneği bulunan ekranlarda; ”KVKK’YI KABUL EDİYORUM” seçeneği işaretlenmeden işleme devam edilememeli.
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    kayıt_ol_isim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[1]")
    kayıt_ol_soyisim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[2]")
    kayıt_ol_tc = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[3]")
    kayıt_ol_numara = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[4]")
    kayıt_ol_sifre = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[5]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/h4[7]/input")
    kayıt_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/button")

    kayıt_ol_isim.send_keys("Timuçin")
    time.sleep(1)
    kayıt_ol_soyisim.send_keys("bektaş")
    time.sleep(1)
    kayıt_ol_tc.send_keys("00000000022")
    time.sleep(1)
    kayıt_ol_numara.send_keys("22222222222")
    time.sleep(1)
    kayıt_ol_sifre.send_keys("12345678911_Abs")
    #11 adet rakam
    time.sleep(1)
    kayıt_buton.click()

    time.sleep(5)

    kvk_buton.click()
    time.sleep(2)

    kayıt_buton.click()

def kriter8(url):
#2. ekranda hem “GİRİŞ” butonu hem de “KAYIT” basıldığında 5. Ekrana yönlendirilmeli.

    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    #kayıt butonu

    kayıt_ol_isim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[1]")
    kayıt_ol_soyisim = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[2]")
    kayıt_ol_tc = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[3]")
    kayıt_ol_numara = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[4]")
    kayıt_ol_sifre = browser.find_element_by_xpath("/html/body/div[2]/form/div/input[5]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/h4[7]/input")
    kayıt_buton = browser.find_element_by_xpath("/html/body/div[2]/form/div/button")

    kayıt_ol_isim.send_keys("Timuçin")
    time.sleep(1)
    kayıt_ol_soyisim.send_keys("bektaş")
    time.sleep(1)
    kayıt_ol_tc.send_keys("00000000024")
    time.sleep(1)
    kayıt_ol_numara.send_keys("22222222222")
    time.sleep(1)
    kayıt_ol_sifre.send_keys("12345678911_Abs")
    #11 adet rakam
    time.sleep(1)
    kayıt_buton.click()

    time.sleep(5)

    kvk_buton.click()
    time.sleep(2)

    kayıt_buton.click()
    time.sleep(2)


    if browser.current_url == "http://localhost:8080/screen5/00000000004":
        print("Kayıt yapıldığında 5. ekrana gidiyor")

    time.sleep(2)
    
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    giris_tc = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]")
    giris_sifre = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[2]")
    giris_buton = browser.find_element_by_xpath("/html/body/div[1]/form/div/button")

    giris_tc.send_keys("22222222222")
    time.sleep(2)

    giris_sifre.send_keys("1234")
    time.sleep(2)

    giris_buton.click()
    time.sleep(4)


    if browser.current_url == "http://localhost:8080/screen5/22222222222":
        print("Giriş yapıldığında 5. ekrana gidiyor")

    time.sleep(2)
    

def kriter9(url):
#3. ekranda bütün bölümler doldurulmadan “TEKLİF AL” butonuna basılamamalı.
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    giris_tc = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]")
    giris_sifre = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[2]")
    giris_buton = browser.find_element_by_xpath("/html/body/div[1]/form/div/button")

    giris_tc.send_keys("22222222222")
    time.sleep(2)

    giris_sifre.send_keys("1234")
    time.sleep(2)

    giris_buton.click()
    time.sleep(2)
    
    browser.find_element_by_xpath("/html/body/nav/a[2]/h4").click()
    

    tarih_baslangic = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    tarih_bitis =  browser.find_element_by_xpath("/html/body/div/form/div/input[3]") 
    yurtdisi_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[1]/input[2]")
    yer_ismi = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    isim = browser.find_element_by_xpath("/html/body/div/form/div/input[4]")
    soyisim = browser.find_element_by_xpath("/html/body/div/form/div/input[5]")
    tc = browser.find_element_by_xpath("/html/body/div/form/div/input[6]")  
    numara = browser.find_element_by_xpath("/html/body/div/form/div/input[7]")
    email = browser.find_element_by_xpath("/html/body/div/form/div/input[8]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/h4/input")
    teklif_al_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/div/button")
    
    yurtdisi_buton.click()
    time.sleep(1)
    yer_ismi.send_keys("Almanya - Münih")
    time.sleep(1)
    tarih_baslangic.send_keys("12.10.2022")
    time.sleep(1)
    tarih_bitis.send_keys("20.10.2022")
    time.sleep(1)
    isim.send_keys("timur")
    time.sleep(1)
    
    tc.send_keys("22222222222")
    time.sleep(1)
    numara.send_keys("66666666666")
    time.sleep(1)
    email.send_keys("bektastimucin@gmail.com")
    time.sleep(1)
    kvk_buton.click()
    time.sleep(1)
    teklif_al_buton.click()
    time.sleep(1)

def kriter10(url):
#“ÇIKIŞ” butonu bulunan ekranlarda “ÇIKIŞ” butonuna basıldığında ana ekrana yönlendirilmeli.

    #ekran 4 
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    browser.find_element_by_xpath("/html/body/nav/a[2]").click()
    time.sleep(1)


    if browser.current_url == "http://localhost:8080/":
        print("4. ekranda çıkış butonuna basıldığında ana ekrana gidiyor")

    
    #ekran showcase

    browser.get("http://localhost:8080/showCases?")
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    browser.find_element_by_xpath("/html/body/nav/a[2]/h4").click()
    time.sleep(1)


    if browser.current_url == "http://localhost:8080/":
        print("Showcases ekranında çıkış butonuna basıldığında ana ekrana gidiyor")

    #ekran 5
    browser.get("http://localhost:8080/screen2?")
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    giris_tc = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]")
    giris_sifre = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[2]")
    giris_buton = browser.find_element_by_xpath("/html/body/div[1]/form/div/button")

    giris_tc.send_keys("22222222222")
    time.sleep(2)

    giris_sifre.send_keys("1234")
    time.sleep(2)

    giris_buton.click()
    time.sleep(2)
    #giriş yapıldı 

    browser.find_element_by_xpath("/html/body/nav/a[3]/h4").click()
    time.sleep(2)

    if browser.current_url == "http://localhost:8080/":
        print("5. ekranda çıkış butonuna basıldığında ana ekrana gidiyor")





def kriter13(url):
#5. ekranda “TEKLİF AL” butonuna basıldığında başvuru formunun olduğu 3. Ekrana yönlendirmeli

    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    giris_tc = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]")
    giris_sifre = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[2]")
    giris_buton = browser.find_element_by_xpath("/html/body/div[1]/form/div/button")

    giris_tc.send_keys("22222222222")
    time.sleep(2)

    giris_sifre.send_keys("1234")
    time.sleep(2)

    giris_buton.click()
    time.sleep(2)
    #giriş yapıldı 

    teklif_al_buton = browser.find_element_by_xpath("/html/body/nav/a[2]/h4")

    teklif_al_buton.click()

    time.sleep(1)
    if browser.current_url == "http://localhost:8080/screen3":
        print("5. ekranda çıkış butonuna basıldığında 3. ekrana gidiyor")

def kriter14_12_11(url):
#3. ekrandaki “TEKLİF AL” butonuna basıldığında başvuru formu 4. Ekrana düşmeli.
#4. ekrandaki “GÖNDER” butonuna basıldığında girilen fiyat bilgisi 5. Ekrana gitmeli. 
# Ayrıca Fiyat bilgisi girilmeden “GÖNDER” butonuna basılamamalı.
#4. ve 5. ekranda “BAŞVURU FORMU-X” butonlarına basıldığında müşteriye ait başvuru formu 
# tarayıcıda yeni bir sekme olarak açılmalı ve sekmede kaçıncı başvuru formu olduğu görünmeli.
    
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    giris_tc = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]")
    giris_sifre = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[2]")
    giris_buton = browser.find_element_by_xpath("/html/body/div[1]/form/div/button")

    giris_tc.send_keys("22222222222")
    time.sleep(2)

    giris_sifre.send_keys("1234")
    time.sleep(2)

    giris_buton.click()
    time.sleep(2)

    #giris yapıldı

    browser.find_element_by_xpath("/html/body/nav/a[2]/h4").click()
    

    tarih_baslangic = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    tarih_bitis =  browser.find_element_by_xpath("/html/body/div/form/div/input[3]") 
    yurtdisi_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[1]/input[2]")
    yer_ismi = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    isim = browser.find_element_by_xpath("/html/body/div/form/div/input[4]")
    soyisim = browser.find_element_by_xpath("/html/body/div/form/div/input[5]")
    tc = browser.find_element_by_xpath("/html/body/div/form/div/input[6]")  
    numara = browser.find_element_by_xpath("/html/body/div/form/div/input[7]")
    email = browser.find_element_by_xpath("/html/body/div/form/div/input[8]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/h4/input")
    teklif_al_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/div/button")
    
    yurtdisi_buton.click()
    time.sleep(1)
    yer_ismi.send_keys("Almanya - Münih")
    time.sleep(1)
    tarih_baslangic.send_keys("12.10.2022")
    time.sleep(1)
    tarih_bitis.send_keys("20.10.2022")
    time.sleep(1)
    isim.send_keys("timur")
    time.sleep(1)
    soyisim.send_keys("bektas")
    time.sleep(1)
    tc.send_keys("22222222222")
    time.sleep(1)
    numara.send_keys("66666666666")
    time.sleep(1)
    email.send_keys("bektastimucin@gmail.com")
    time.sleep(1)
    kvk_buton.click()
    time.sleep(1)
    teklif_al_buton.click()
    time.sleep(1)

    #teklif yapıldı
    time.sleep(1)

    fiyat_bar = browser.find_element_by_xpath("/html/body/div/div[2]/div/div/form/div/div[2]/input")
    gonder_buton = browser.find_element_by_xpath("/html/body/div/div[2]/div/div/form/div/div[2]/div/button")

    gonder_buton.click()
    #Fiyat bilgisi girilmeden “GÖNDER” butonuna basılamamalı
    time.sleep(3)

    fiyat = "758"
    time.sleep(2)
    fiyat_bar.send_keys(fiyat)
    time.sleep(1)
    gonder_buton.click()
    time.sleep(1)

    browser.get("http://localhost:8080/screen5/22222222222")
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    i = 1

    while(1):
        
        
        if browser.find_element_by_xpath(f"/html/body/div/div[2]/table/tbody/tr[{i}]/td[6]/span").text == fiyat:
            print("Teklif 5. ekrana gelmiş")
            
            break
        

        i=i+1

       

def kriter15(url):
#Sitede email istenen yerlerde girilen email geçerli bir email olmalı.
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    time.sleep(2)

    tarih_baslangic = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    tarih_bitis =  browser.find_element_by_xpath("/html/body/div/form/div/input[3]") 
    yurtdisi_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[1]/input[2]")
    yer_ismi = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    isim = browser.find_element_by_xpath("/html/body/div/form/div/input[4]")
    soyisim = browser.find_element_by_xpath("/html/body/div/form/div/input[5]")
    tc = browser.find_element_by_xpath("/html/body/div/form/div/input[6]")  
    numara = browser.find_element_by_xpath("/html/body/div/form/div/input[7]")
    email = browser.find_element_by_xpath("/html/body/div/form/div/input[8]")
    kvk_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/h4/input")
    teklif_al_buton = browser.find_element_by_xpath("/html/body/div/form/div/div[3]/div/button")
    
    yurtdisi_buton.click()
    time.sleep(1)
    yer_ismi.send_keys("Almanya - Münih")
    time.sleep(1)
    tarih_baslangic.send_keys("12.10.2022")
    time.sleep(1)
    tarih_bitis.send_keys("20.10.2022")
    time.sleep(1)
    isim.send_keys("timur")
    time.sleep(1)
    soyisim.send_keys("bektas")
    time.sleep(1)
    tc.send_keys("00000000011")
    time.sleep(1)
    numara.send_keys("66666666666")
    time.sleep(1)
    email.send_keys("aaaaaaassssssddddddeeeeeeeetttttee@gmail.com")
    time.sleep(1)
    kvk_buton.click()
    time.sleep(1)
    teklif_al_buton.click()

if __name__ == "__main__":

    url = "http://localhost:8080/"

    browser = webdriver.Chrome(ChromeDriverManager().install())

    # kriter1(url)
    # time.sleep(2)

    # kriter2(url)
    # time.sleep(2)

    # kriter3(url)
    # time.sleep(2)

    # kriter4("http://localhost:8080/screen2?")
    # time.sleep(2)

    # kriter5("http://localhost:8080/screen2?")
    # time.sleep(2)

    # kriter6("http://localhost:8080/screen2?")
    # time.sleep(2)

    # kriter7("http://localhost:8080/screen2?")
    # time.sleep(2)

    # kriter8("http://localhost:8080/screen2?")
    # time.sleep(2)

    # kriter9("http://localhost:8080/screen2?")
    # time.sleep(2)

    # kriter10("http://localhost:8080/screen4?")
    # time.sleep(2)

    # kriter13("http://localhost:8080/screen2?")
    # time.sleep(2)
    
    kriter14_12_11("http://localhost:8080/screen2?")
    time.sleep(2)

    kriter15("http://localhost:8080/screen3?")
    time.sleep(2)

    