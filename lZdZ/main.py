# Importowanie modułów
import command as comm
import emoji

# Główna Pętla programu korzystająca z funkcji z pliku command.py
on = True
while on:
    print(emoji.emojize("    :spiral_calendar: Program lZdZ :spiral_calendar:"))
    print("Wybierz opcję:")
    print(emoji.emojize("\t1. [:desktop_computer:] Wyświetl Zadania"))
    print(emoji.emojize("\t2. [:plus:] Dodaj Zadanie"))
    print(emoji.emojize("\t3. [:cross_mark:] Usuń zadanie"))
    print(emoji.emojize("\t4. [:wrench:] Inne operacje"))
    print(emoji.emojize("\t5. [:left_arrow_curving_right:] Wyjście z Programu"))
    choice = input("Wybierz akcję:")
    if choice == '1':
        comm.show()
        try:
            input("wpisz 1 aby kontynuować:")
        except SyntaxError:
            pass
        continue
    if choice == '2':
        comm.add()
        try:
            input("wpisz 1 aby kontynuować:")
        except SyntaxError:
            pass
        continue
    if choice == '3':
        comm.rem()
        try:
            input("wpisz 1 aby kontynuować:")
        except SyntaxError:
            pass
        continue
    if choice == '4':
        on2 = True
        while on2:
            print("\t1. Zmiana priorytetu")
            print("\t2. Zmiana daty i czasu realizacji")
            print("\t3. Zmiana stopnia realizacji")
            print("\t4. Wyświetlanie zadań posortowanych wg daty i czasu utworzenia rosnąco")
            print("\t5. Wyświetlanie zadań posortowanych wg daty i czasu utworzenia malejąco")
            print("\t6. Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji rosnąco")
            print("\t7. Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji malejąco")
            print("\t8. Powrót do głównego menu.")
            choice2 = input("Wybierz akcje:")
            if choice2 == '1':
                if comm.change("Priorytet") == False:
                    try:
                        input("wpisz 1 by kontynuować")
                    except SyntaxError:
                        pass
                    break
                try:
                    input("wpisz 1 by kontynuować")
                except SyntaxError:
                    pass
                continue
            if choice2 == '2':
                if comm.change("Date i czas") == False:
                    try:
                        input("wpisz 1 by kontynuować")
                    except SyntaxError:
                        pass
                    break
                try:
                    input("wpisz 1 by kontynuować")
                except SyntaxError:
                    pass
                continue
            if choice2 == '3':
                if comm.change("Stopień realizacji") == False:
                    try:
                        input("wpisz 1 by kontynuować")
                    except SyntaxError:
                        pass
                    break
                try:
                    input("Stopień realizacji zmieniony wpisz 1 by kontynuować")
                except SyntaxError:
                    pass
                continue
            if choice2 == '4':
                comm.sort_date_time_asc_u()
                try:
                    input("Zadania wyświetlone wpisz 1 aby kontynuować:")
                except SyntaxError:
                    pass
                continue
            if choice2 == '5':
                comm.sort_date_time_asc_u(asc=False)
                try:
                    input("Zadania wyświetlone wpisz 1 aby kontynuować:")
                except SyntaxError:
                    pass
                continue
            if choice2 == '6':
                comm.sort_date_time_asc_a()
                try:
                    input("Zadania wyświetlone wpisz 1 aby kontynuować:")
                except SyntaxError:
                    pass
                continue
            if choice2 == '7':
                comm.sort_date_time_asc_a(asc=False)
                try:
                    input("Zadaniaa wyświetlone wpisz 1 aby kontynuować:")
                except SyntaxError:
                    pass
                continue
            if choice2 == '8':
                print("Wyjście z operacji")
                on2 = False
            else:
                print("Dana operacja nie istnieje")
        continue
    if choice == '5':
        print("Zakończono program")
        on = False
    else:
        print("Nieprawidłowa opcja")