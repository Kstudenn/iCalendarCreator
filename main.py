# wzorzec polecenie
# kazdy wpis w menu jest osobnym obiektem
#
# 1. tekst programisty
# 2. tekst ....
# 3. ....
#
# Wybor: 1
#
# 1. tekst programisty
# 2. tekst ....
# 3. exit
#
# Wybor: 3

from menu import Menu, AddEvent, PrintEvents, PrintICalendar, ExitCommand
from calendar import Event


def main():
    events = []

    menu = Menu()
    menu.register(AddEvent(events))
    menu.register(PrintEvents(events))
    menu.register(PrintICalendar(events))
    menu.register(ExitCommand(menu))

    menu.run()


if __name__ == "__main__":
    main()
