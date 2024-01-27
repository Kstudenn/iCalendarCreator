from calendar import Event, ListingMethod, ListICalendar, ListText


class Menu:
    def __init__(self):
        self._commands = []
        self._should_run = True

    def run(self):
        while self._should_run:
            print("* Menu *\n======")

            for i, cmd in enumerate(self._commands):
                print("{}. {}".format(i + 1, cmd.description()))

            wybor = int(input("Wybor: "))
            if wybor < 1 or wybor >= len(self._commands) + 1:
                print("Nieznana opcja")
            else:
                self._commands[wybor - 1].execute()

    def stop(self):
        self._should_run = False

    def register(self, command):
        self._commands.append(command)


class MenuCommand:

    def execute(self):
        raise NotImplementedError("you should implement this method in subclass")

    def description(self):
        raise NotImplementedError("you should implement this method in subclass")


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        self._menu = menu

    def execute(self):
        self._menu.stop()

    def description(self):
        return "Exit"


class AddEvent(MenuCommand):
    def __init__(self, events: list):
        self._events = events

    def execute(self):
        ev = Event()
        if ev.isCreatedCorrectly():
            self._events.append(ev)

    def description(self):
        return "Dodaj nowe wydarzenie do kalendarza"


class PrintEvents(MenuCommand):
    def __init__(self, events: list):
        self._events = events

    def execute(self):
        if len(self._events) is not 0:
            wypisz = ListText()
            wypisz.display(self._events)

    def description(self):
        return "Wypisz wydarzenia w formie tekstowej"


class PrintICalendar(MenuCommand):
    def __init__(self, events: list):
        self._events = events

    def execute(self):
        if len(self._events) is not 0:
            wypisz = ListICalendar()
            wypisz.display(self._events)

    def description(self):
        return "Wypisz wydarzenia w formie iCalendar"
