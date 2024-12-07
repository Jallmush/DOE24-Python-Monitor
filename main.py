from classes.monitoring import Monitoring
from classes.alarms import AlarmManager
from classes.meny import main_menu

if __name__ == "__main__":
    # Skapar ett objekt för övervakning.
    monitoring = Monitoring()  # Skapar en instans av Monitoring-klassen, ansvarig för att övervaka systemresurser.
    
    # Skapar ett objekt för alarmhantering.
    alarm_manager = AlarmManager()  # Skapar en instans av AlarmManager-klassen, ansvarig för att hantera larm.
    
    # Anropar huvudmenyn och skickar med objekten för övervakning och alarmhantering.
    main_menu(monitoring, alarm_manager)  # Kör huvudmenyn där användaren interagerar med programmet.
