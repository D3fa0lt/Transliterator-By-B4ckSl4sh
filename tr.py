# -*- coding: utf-8 -*-
from os import system
import requests
import json

greek_alphabet = "ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσΤτΥυΦφΧχΨψΩω,.-=+()";
eng_alphabet   = "AaBbGgDdEeZzHhQqIiKkLlMmNnXxOoPpRrSsTtUuFfCcYyWw,.-=+()";

backup_time = 5

translated_text = ""

current_version = 1.0

def auto_update():
    global current_version
    url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
    url = "https://github.com/D3fa0lt/Transliterator-By-B4ckSl4sh.git"
    response = requests.get(url).json()
    if responce[version] != current_version:
        current_version = responce[version]
        print("Updating, wait a minute please")
        system("git clone ")
def help():
    global greek_alphabet
    global eng_alphabet
    n = len(eng_alphabet)
    for i in range(1, n):
        print(eng_alphabet[i], " = ", greek_alphabet[i])
    print("press Enter to continue")
    tmp = input()

def save():
    global translated_text
    file = open("input.txt", "w")
    data = file.write(translated_text)
    file.close()

def set_reference():
    print("Short Reference")
    print("Type 'help' to see full table")
    #print("Type 'show' to show result")
    print("Type 'autotranslate' to automatically translate your file")
    print("Type '<' to erase last item")
    print("Type 'clear' to clear output")
    print('''Также, вот таблица значков 1 - ̆ краткость
        2 - ̃  надстрочная тильда
        3 - ́́́́  лёгкое ударение
        4 - ̀  тяжелое ударение''')
    #print("Авто-сохранениее файла производится каждые", backup_time,"слов\n")
          
def translate(s):       
    global eng_alphabet
    global greek_alphabet
    global translated_text
    n = len(s)
    for i in range(n):
        c = s[i];
        if c == " ":
            translated_text += " "
            continue
        if c.isdigit():
            translated_text += check_icon(c)
            continue
        idx = 0;
        flag = False;
        for j in range(len(eng_alphabet)):
            if(eng_alphabet[j] == c):
                idx = j
                flag = True
                break
        if(not flag):
            print("some symbol doesn't exist in table")
            print("press Enter to continue")
            tmp = input()
        else:
            translated_text += greek_alphabet[idx]
    #translated_text += " "

def autotranslate(fl):
    global translated_text
    file = open(fl, "r")
    data = file.read()
    file.close()
    for el in data:
        translate(el)
    print("Your translation is ready, here it is:")
    print(translated_text)

def check_icon(s):
    short = 
    long = "̃"
    stress = "́"
    back_stress = "̀"
    iota = "ͅ"
    if s == "1":
        return short
    if s == "2":
        return long
    if s == "3":
        return stress
    if s == "4":
        return back_stress
    else:
        print("not ok")
        return True

def main():
    global translated_text
    backup = 0
    while True:
        #if backup_time - backup == 0:
            #save()
            #backup = 0
        set_reference()
        print(translated_text, "|", sep = "")
        s = input()
        if s == "help":
            help()
        elif s == "<":
            translated_text = translated_text[0:len(translated_text)-1]
        elif s == "clear":
            translated_text = ""
        elif s == "autotranslate":
            print("Enter you file's name")
            fl = input()
            print(fl)
            autotranslate(fl)                
        else:
            translate(s)
        system("cls")
        backup += 1

if __name__ == "__main__":
    main()
