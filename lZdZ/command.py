# Importowanie modułów do obsługi dat oraz do zapisu,czytania,sortowania wydarzeń
import datetime as dt
import pandas as pd


# funkcja sprawdzająca poprawność dat
def check_date(date):
    try:
        date_format = dt.datetime.strptime(date, "%Y-%m-%d %H:%M")
        if date_format < dt.datetime.now():
            return False
        else:
            return True
    except ValueError:
        return False


def check_not_actual_date(date):
    try:
        date_format = dt.datetime.strptime(date, "%Y-%m-%d %H:%M")
    except ValueError:
        return False
    return True


def add():
    name = input("Podaj nazwe zadania:")
    r_date = input("Podaj date realizacji(rrrr-mm-dd):")
    r_time = input("Podaj czas realizacji(hh:mm):")
    priority = input("Podaj priorytet(NO,NI,WY):")
    realization = input("Podaj stopień realizacji(0-100):")
    description = input("Podaj opis(Jeśli chcesz):")
    category = input("Podaj kategorię(Jeśli chcesz):")
    if priority not in ["NO", "NI", "WY"]:
        print("Podałeś zły format priorytetu")
        return False
    if not realization.isdigit():
        print("Podałeś zły format stopnia realizacji")
        return False
    if int(realization) > 100 or int(realization) < 0:
        print("Podałeś zły format stopnia realizacji")
        return False
    temp = str(r_date) + " " + str(r_time)
    if name == "":
        print("Nazwa jest pusta spróbuj jescze raz")
        return False
    if not check_date(temp):
        print("Format daty lub czasu jest nieprawidłowy spróbuj jeszcze raz")
        return False
    # Zapisywanie wydarzenia do pliku csv
    events = pd.DataFrame([[name, r_date, r_time, dt.date.today().strftime("%Y-%m-%d"), dt.datetime.now().strftime("%H:%M"), dt.date.today().strftime("%Y-%m-%d"), dt.datetime.now().strftime("%H:%M"), priority, realization, description, category]], columns=["nazwa", "data_realizacji", "czas_realizacji", "data_utworzenia", "czas_utworzenia", "data_ostatniej_aktualizacji", "czas_ostatniej_aktualizacji", "priorytet", "stopień_realizacji", "opis", "kategoria"])
    events.to_csv('zadania.csv', mode='a', index=False, header=False)
    print("Zadanie dodane")
    return True

# Wyswietlanie pliku
def show():
    file = pd.read_csv("zadania.csv")
    print(file)


# Usuwanie podanego wydarzenia
def rem():
    name = input("Podaj nazwe zadania:")
    date = input("Podaj date utworzenie(rrrr-mm-dd):")
    time = input("Podaj czas czas(hh:mm):")
    temp = str(date) + " " + str(time)
    if name == "":
        print("Nazwa jest pusta spróbuj jescze raz")
        return False
    if not check_not_actual_date(temp):
        print("Format daty lub czasu jest nieprawidłowy spróbuj jeszcze raz")
        return False
    file = open("zadania.csv", "r", encoding="utf-8")
    temp = ""
    for a in file.readlines():
        row = a.split(',')
        if (row[0] == name) and (row[3] == date) and (row[4] == time):
            continue
        temp += a
    # zapisywanie pliku bez lini z wydarzeniem wskazanym przez użytkownika
    with open("zadania.csv", "w", encoding="utf-8") as file:
        file.writelines(temp)
    print("Zadanie usunięte")
    return True

def change(item):
    name = input("Podaj nazwe wydarzenia:")
    date = input("Podaj date utworzenia (rrrr-mm-dd):")
    time = input("Podaj czas utworzenia (hh:mm):")
    if item == "Priorytet":
        thing = input("Podaj nowy priorytet:")
        if thing not in ["NO", "NI", "WY"]:
            print("Podałeś zły format priorytetu")
            return False
    if item == "Date i czas":
        thing = input("Podaj nową date realizacji:")
        thing2 = input("Podaj nowy czas realizacji:")
        temp = str(thing) + " " + str(thing2)
        if not check_not_actual_date(temp):
            print("Format daty lub czasu jest nieprawidłowy spróbuj jeszcze raz")
            return False
    if item == "Stopień realizacji":
        thing = input("Podaj nowy stopień realizacji:")
        if not thing.isdigit():
            print("Podałeś zły format stopnia realizacji")
            return False
        if int(thing) > 100 or int(thing) < 0:
            print("Podałeś zły format stopnia realizacji")
            return False
    temp = str(date) + " " + str(time)
    if name == "":
        print("Nazwa jest pusta spróbuj jescze raz")
        return False
    if not check_not_actual_date(temp):
        print("Format daty lub czasu jest nieprawidłowy spróbuj jeszcze raz")
        return False
    file = open("zadania.csv", "r", encoding="utf-8")
    temp = ""
    for a in file.readlines():
        row = a.split(',')
        tdate = dt.date.today().strftime("%Y-%m-%d")
        ttime = dt.datetime.now().strftime("%H:%M")
        if (row[0] == name) and (row[3] == date) and (row[4] == time):
            if item == "Priorytet":
                temp += f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{tdate},{ttime},{thing},{row[8]},{row[9]},{row[10]}"
                continue
            if item == "Date i czas":
                temp += f"{row[0]},{thing},{thing2},{row[3]},{row[4]},{tdate},{ttime},{row[7]},{row[8]},{row[9]},{row[10]}"
                continue
            if item == "Stopień realizacji":
                temp += f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{tdate},{ttime},{row[7]},{thing},{row[9]},{row[10]}"
                continue
        temp += a
    # zapisywanie pliku z modyfikowanym wydarzeniem wskazanym przez użytkownika
    with open("zadania.csv", "w", encoding="utf-8") as file:
        file.writelines(temp)
    print("Zadanie zmodyfikowane pomyślnie")
    return True


# Sortowanie według daty utworzenia parametr asc odpowiada za to czy rośnie czy też nie
def sort_date_time_asc_u(asc=True):
    df = pd.read_csv("zadania.csv")
    df['DataCzasUTW'] = pd.to_datetime(df['data_utworzenia'] + ' ' + df['czas_utworzenia'])
    df.sort_values(by='DataCzasUTW', inplace=True, ascending=asc)
    print(df)


# Sortowanie według daty aktualizacji parametr asc odpowiada za to czy rośnie czy też nie
def sort_date_time_asc_a(asc=True):
    df = pd.read_csv("zadania.csv")
    df['DataCzasAKT'] = pd.to_datetime(df['data_ostatniej_aktualizacji'] + ' ' + df['czas_ostatniej_aktualizacji'])
    df.sort_values(by='DataCzasAKT', inplace=True, ascending=asc)
    print(df)
