import command as com


def add(name, r_date, r_time, priority, realization, description="", category=""):
    if priority not in ["NO", "NI", "WY"]:
        return False
    if not realization.isdigit():
        return False
    if int(realization) > 100 or int(realization) < 0:
        return False
    temp = str(r_date) + " " + str(r_time)
    if name == "":
        return False
    if not com.check_date(temp):
        return False
    return True


def change(item, name, date, time, thing, thing2=""):
    if item == "Priorytet":
        if thing not in ["NO", "NI", "WY"]:
            return False
    if item == "Date i czas":
        temp = str(thing) + " " + str(thing2)
        if not com.check_not_actual_date(temp):
            return False
    if item == "Stopień realizacji":
        if not thing.isdigit():
            return False
        if int(thing) > 100 or int(thing) < 0:
            return False
    temp = str(date) + " " + str(time)
    if name == "":
        return False
    if not com.check_not_actual_date(temp):
        return False
    return True


def rem(name, temp):
    if name == "":
        return False
    if not com.check_not_actual_date(temp):
        return False
    return True
