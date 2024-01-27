import string


class Event:
    def __init__(self):
        # dozwolone znaki specjalne to spacja kropka przecinek minus
        # dozwolone znaki A-Z a-z 0-9
        symbols = input("Description:")
        valid_symbols = ",.-" + " "
        has_only_symbols = True
        try:
            for ch in symbols:
                if ch not in valid_symbols and ch not in string.ascii_letters:
                    raise ValueError
        except ValueError:
            print("Podano znaki w złym zakresie")
            return
        # Opis jedno liniowy (Długość rożna w zależności od ekranu)
        # tzn. ogranicz ilość znaków do np. 100
        try:
            if len(symbols) > 100:
                raise ValueError
        except ValueError:
            print("Przekroczono dozwoloną ilość 100 znaków")
            return
        self.description = symbols

        date = input("Date (DD.MM.YYYY): ")
        date = date.split(".")
        # Należy sprawdzić czy tablice są odpowiednich rozmiarów
        monthMaxDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        try:
            if not len(date[0]) == 2:
                raise SyntaxError
            if not len(date[1]) == 2:
                raise SyntaxError
            if not len(date[2]) == 4:
                raise SyntaxError
            for i in date:
                # Sprawdzić czy tablice zawierają tylko liczby
                if not i.isdigit():
                    raise TypeError
                # Należy sprawdzić czy wartości nie są przekroczone
                if not 0 < int(date[1]) < 13:
                    raise TypeError
                if not 0 < int(date[0]) <= int(monthMaxDays[int(date[1])-1]):
                    raise TypeError
        except TypeError:
            print("Podano błędne dane")
            return
        except SyntaxError:
            print("Błędny fromat")
            return

        self.day = date[0]
        self.month = date[1]
        self.year = date[2]

        time = input("Time (HH:MM): ")
        time = time.split(":")

        try:
            if not len(time) == 2:
                raise SyntaxError
            # godziny i minuty ponizej 24,60
            if not 0 <= int(time[0]) < 24:
                raise ArithmeticError
            if not 0 <= int(time[1]) < 60:
                raise ArithmeticError
            for i in time:
                if not i.isdigit():
                    raise TypeError
                if not len(i) == 2:
                    raise TypeError
        except SyntaxError:
            print("Podano blędne dane")
            return
        except ArithmeticError:
            print("Podano Błędne dane")
            return
        except TypeError:
            print("Zły format")
            return

        self.hour = time[0]
        self.minute = time[1]

    def isCreatedCorrectly(self):
        try:
            var = self.hour
            var = self.minute
            var = self.day
            var = self.month
            var = self.year
            var = self.description
        except:
            return False
        return True




class ListingMethod:
    def display(self, events: list):
        raise NotImplementedError("you should implement this method in subclass")


class ListICalendar(ListingMethod):
    def __init__(self):
        self._listingMethod = IcalendarPrint()

    def display(self, events: list):
        self._listingMethod.display(events)


class ListText(ListingMethod):
    def __init__(self):
        self._listingMethod = TextPrint()

    def display(self, events: list):
        self._listingMethod.display(events)


class IcalendarPrint(ListingMethod):
    def display(self, events: list):
        print("BEGIN:VCALENDAR")
        print("VERSION:2.0")
        print("BEGIN:VTIMEZONE")
        print("TZID:Europe/Warsaw")
        print("X-LIC-LOCATION:Europe/Warsaw")
        print("END:TIMEZONE")
        second = "00"
        for i in events:
            print("BEGIN:VEVENT")
            print("DTSTART:" + i.year + i.month + i.day + "T" + i.hour + i.minute + second)
            print("DTEND:" + i.year + i.month + i.day + "T" + i.hour + i.minute + second)
            print("SUMMARY:" + i.description)
            print("END:VEVENT")
        print("END:VCALENDAR\n")


class TextPrint(ListingMethod):
    def display(self, events: list):
        for i in events:
            print("Opis: " + i.description)
            print("Data: " + i.year + "." + i.month + "." + i.day + ", " + i.hour + ":" + i.minute + "\n")
