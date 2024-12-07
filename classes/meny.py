from classes.utils import prompt_continue
from classes.alarms import configure_alarm_menu

def main_menu(monitoring, alarm_manager):
    """Hanterar huvudmenyn."""
    while True:
        print("\nHuvudmeny:")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("0. Avsluta")

        # Användaren gör ett val i huvudmenyn.
        choice = input("Välj ett alternativ: ")

        if choice == '1':
            # Starta övervakningen och logga händelsen.
            print(monitoring.start())  # Kallar på startmetoden från monitoring-objektet.
        elif choice == '2':
            # Visa status för aktiv övervakning.
            status = monitoring.get_status()  # Hämtar aktuell status från monitoring-objektet.
            if isinstance(status, dict):
                # Om status är en ordbok, skriv ut varje systemparameter.
                for key, value in status.items():
                    print(f"{key}: {value}")
            else:
                # Om status inte är en ordbok, skriv ut det som statusmeddelande.
                print(status)
            prompt_continue()  # Anropar en funktion som låter användaren fortsätta.
        elif choice == '3':
            # Öppna menyn för att skapa ett larm.
            configure_alarm_menu(alarm_manager)  # Anropar menyn för att skapa larm.
        elif choice == '4':
            # Visa alla konfigurerade larm.
            print(alarm_manager.display_alarms())  # Anropar metoden för att visa alla larm.
            prompt_continue()  # Anropar en funktion som låter användaren fortsätta.
        elif choice == '5':
            # Starta övervakningsläge och börja övervaka systemet.
            print("Övervakningsläge aktivt. Tryck Ctrl+C för att avsluta.")
            try:
                while True:
                    monitoring.update()  # Uppdatera systeminformationen.
                    warnings = alarm_manager.check_alarms(monitoring.get_status())  # Kolla om något larm triggas.
                    for warning in warnings:
                        print(warning)  # Skriv ut varningar om något larm triggas.
            except KeyboardInterrupt:
                # Hantera användarens avbrott (Ctrl+C).
                print("\nAvslutar övervakningsläge.")
        elif choice == '0':
            # Avsluta programmet och logga händelsen.
            print("Avslutar programmet.")
            break  # Avslutar loopen och därmed programmet.
        else:
            # Hantera ogiltiga val.
            print("Ogiltigt val, försök igen.")  # Om användaren väljer ett ogiltigt alternativ.
