class Alarm:
    # Konstruktor för klassen 'Alarm', som representerar ett larm
    def __init__(self, alarm_type, threshold):
        self.type = alarm_type  # Larmtypen, t.ex. CPU, RAM eller Disk
        self.threshold = threshold  # Tröskelvärde för när larmet ska aktiveras, i procent

    # Denna metod returnerar en strängrepresentation av objektet
    # Det gör att när vi skriver ut en instans av Alarm, får vi en läsbar text om larmet
    def __repr__(self):
        return f"{self.type} larm {self.threshold}%"

# Klass som hanterar flera larm, t.ex. lägga till larm, visa larm och kontrollera om ett larm utlöses
class AlarmManager:
    # Konstruktor för klassen 'AlarmManager', som håller koll på alla larm
    def __init__(self):
        self.alarms = []  # Lista för att lagra alla skapade larm

    # Metod för att lägga till ett larm i listan
    def add_alarm(self, alarm_type, threshold):
        alarm = Alarm(alarm_type, threshold)  # Skapar ett nytt Alarm-objekt
        self.alarms.append(alarm)  # Lägger till larmet i listan
        return f"Larm för {alarm_type} satt till {threshold}%"  # Bekräftelse på att larmet har lagts till

    # Metod för att visa alla larm som är skapade
    def display_alarms(self):
        if not self.alarms:  # Om det inte finns några larm i listan
            return "Inga larm konfigurerade."  # Returnera meddelande om att inga larm finns

        # Sortera larmen alfabetiskt baserat på larmtypen (CPU, RAM, Disk)
        sorted_alarms = sorted(self.alarms, key=lambda alarm: alarm.type)
        # Returnera en sträng där alla larm är sammanslagna och separerade med radbrytning
        return "\n".join(str(alarm) for alarm in sorted_alarms)

    # Metod för att kontrollera om några av de konfigurerade larmen utlöses baserat på systemstatus
    def check_alarms(self, system_status):
        warnings = []  # Lista för att lagra eventuella larmmeddelanden
        if isinstance(system_status, dict):  # Kontrollera om system_status är en ordbok (dictionary)
            for alarm in self.alarms:  # Gå igenom alla larm
                # Om larmet är av typ "CPU" och värdet för CPU är större än tröskelvärdet
                if alarm.type == "CPU" and float(system_status["CPU"].strip('%')) > alarm.threshold:
                    warnings.append(f"*** VARNING: {alarm.type} överskrider {alarm.threshold}% ***")
                # Om larmet är av typ "RAM" och värdet för RAM är större än tröskelvärdet
                elif alarm.type == "RAM" and float(system_status["RAM"].split('%')[0]) > alarm.threshold:
                    warnings.append(f"*** VARNING: {alarm.type} överskrider {alarm.threshold}% ***")
                # Om larmet är av typ "Disk" och värdet för Disk är större än tröskelvärdet
                elif alarm.type == "Disk" and float(system_status["Disk"].split('%')[0]) > alarm.threshold:
                    warnings.append(f"*** VARNING: {alarm.type} överskrider {alarm.threshold}% ***")
        else:
            warnings.append("Ingen aktiv övervakning, kan inte kontrollera larm.")  # Meddelande om systemstatus är felaktig
        return warnings  # Returnera alla varningar som triggats

# Funktion för att hantera meny för att konfigurera larm
def configure_alarm_menu(alarm_manager):
    """Undermeny för att konfigurera larm."""
    while True:
        # Visa alternativ för användaren
        print("\nSkapa larm:")
        print("1. CPU användning")
        print("2. Minnesanvändning (RAM)")
        print("3. Diskanvändning")
        print("0. Tillbaka till huvudmenyn")

        # Ta emot användarens val
        choice = input("Välj ett alternativ: ")

        # Beroende på användarens val, sätt rätt larmtyp
        if choice == '1':
            alarm_type = "CPU"
        elif choice == '2':
            alarm_type = "RAM"
        elif choice == '3':
            alarm_type = "Disk"
        elif choice == '0':  # Om användaren vill gå tillbaka till huvudmenyn
            break
        else:  # Hantera ogiltiga val
            print("Ogiltigt val, försök igen.")
            continue

        try:
            # Be användaren att ange ett tröskelvärde för larmet
            threshold = int(input(f"Ange tröskelvärde för {alarm_type} (1-100): "))
            # Kontrollera att tröskelvärdet är inom det giltiga intervallet (1-100)
            if 1 <= threshold <= 100:
                print(alarm_manager.add_alarm(alarm_type, threshold))  # Lägg till larmet om det är giltigt
            else:
                print("Tröskeln måste vara mellan 1 och 100.")  # Felmeddelande om tröskeln är ogiltig
        except ValueError:  # Om användaren inte anger ett heltal
            print("Ogiltig inmatning. Ange en siffra mellan 1 och 100.")  # Felmeddelande för ogiltig inmatning
