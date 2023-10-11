import command as com
import test_functions as func


# Testy funkcji z modułu command.py, zmodyfikowanych na potrzeby testowania prawidłowości danych podanych przez użytkownika

def test_check_date():
    assert com.check_date("dsafasfdfadsfsddsf") == False
    assert com.check_date("2023:12:12 12:00") == False
    assert com.check_date("2023-12-12 13:00") == True
    assert com.check_date("2023-07-09 14:00") == True
    assert com.check_date("2023:09:09 dasdfssafdfdsaf") == False
    assert com.check_date("2023-09-0a 12:00") == False
    assert com.check_date("2024-09-11 13:00") == True
    assert com.check_date("2022-01-11 12:22") == False
    print("Testy poprawności dat udane")


def test_check_not_actual_date():
    assert com.check_not_actual_date("2023:12:12 12:00") == False
    assert com.check_not_actual_date("2022-01-11 12:22") == True
    assert com.check_not_actual_date("2022:01:11 12:22") == False
    assert com.check_not_actual_date("2022-01-11 12-22") == False
    assert com.check_not_actual_date("2024-01-11 12-22") == False
    assert com.check_not_actual_date("2024-01-11 12:89") == False
    assert com.check_not_actual_date("2024-01-11 12:22") == True
    print("Testy poprawności dat udane")


def test_add_task():
    assert func.add("kolokwium", "2023-02-12", "12:22", "NO", "99") == True
    assert func.add("kolokwium", "2023-02-12", "12:22", "NO", "100") == True
    assert func.add("12", "2023-02-12", "12:22", "NO", "100") == True
    assert func.add("12", "2023:02:12", "12:22", "NO", "100") == False
    assert func.add("12", "2023-02-12", "12-22", "NO", "100") == False
    assert func.add("12", "2023-02-12", "12-22", "asdasfadsfa", "100") == False
    assert func.add("12", "2023-02-12", "12-22", "WY", "sasafsafdasfasdf") == False
    assert func.add("12", "2020-02-12", "12-22", "WY", "100") == False
    assert func.add("adsfdfadffdsfdasf", "2024-02-12", "12:22", "WY", "-12") == False
    assert func.add("test", "2024-02-12", "12:22", "1231234", "12") == False
    assert func.add("test2", "2023-01-25", "23:22", "WY", "35") == True
    assert func.add("test", "2024-02-12", "72:22", "NI", "36") == False
    print("Testy dodawania zadań udane")


def test_rem_task():
    assert func.rem("32453253252355r", "2023:12:12 12:00") == False
    assert func.rem("zadanie1", "2021-12-12 12:231") == False
    assert func.rem("Zadanie2", "2023-12-12 12:220") == False
    assert func.rem("Zadanie4", "2024-12-12 13:21") == True
    assert func.rem("ZadanieX","2023-01-01 14:15") == True
    assert func.rem("Zadanie5", "12-01-2023 12:22") == False
    print("Testy usuwania zadań udane")


def test_change_task():
    assert func.change("Priorytet", "", "2022-12-12", "12:22", "1232") == False
    assert func.change("Priorytet", "", "2022-12-12", "12:22", "12323") == False
    assert func.change("Priorytet", "Wyd", "2022-12-12", "12:22", "WY") == True
    assert func.change("Priorytet", "Wyd", "2022-12-12", "12:22", "12323") == False
    assert func.change("Date i czas", "Wyd", "2022-12-12", "12:22", "2023-12-12", "12:22") == True
    assert func.change("Date i czas", "Wyd", "2022-12-12", "12:22", "2021-12-12", "12:22") == True
    assert func.change("Date i czas", "Wyd", "2022-12-12", "12:22", "2023:12-12", "12:22") == False
    assert func.change("Date i czas", "Wyd", "2022-12-12", "12:22", "2023-12-12", "12022") == False
    assert func.change("Date i czas", "Wyd", "2022-12-12", "12:22", "2023-12-12", "12-22") == False
    assert func.change("Stopień realizacji", "Wyd", "2022-12-12", "12:22", "NO") == False
    assert func.change("Stopień realizacji", "Wyd", "2022-12-12", "12:22", "12") == True
    assert func.change("Stopień realizacji", "Wyd", "2022-12-12", "12:22", "-2137") == False
    assert func.change("Stopień realizacji", "Wyd", "2022-12-12", "12:22", "35") == True
    print("Testy zmieniania dat udane")


if __name__ == "__main__":
    test_check_date()
    test_add_task()
    test_check_not_actual_date()
    test_change_task()
    test_rem_task()
    print("Wszystkie przeszły pomyślnie")
