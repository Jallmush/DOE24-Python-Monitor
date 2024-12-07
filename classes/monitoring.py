import psutil

class Monitoring:
    def __init__(self):
        # Sätter initiala värden. 'active' anger om övervakningen är aktiv eller inte. 'data' håller systeminformationen.
        self.active = False
        self.data = {}

    def start(self):
        """Startar övervakning."""
        self.active = True  # Sätt 'active' till True för att indikera att övervakningen är igång.
        self.update()  # Uppdatera systeminformationen när övervakningen startas.
        return "Övervakning startad."  # Returmeddelande när övervakningen startar.

    def update(self):
        """Hämtar systeminformation."""
        if not self.active:
            return "Ingen aktiv övervakning."  # Om övervakningen inte är aktiv, ge ett meddelande.
        
        # Hämta systeminformation med hjälp av psutil-biblioteket.
        cpu = psutil.cpu_percent(interval=1)  # Hämta CPU-användningen som en procentandel.
        memory = psutil.virtual_memory()  # Hämta minnesanvändning.
        disk = psutil.disk_usage('/')  # Hämta diskens användning för rotpartitionen ('/').

        # Lagra systeminformationen i 'data'-ordboken.
        self.data = {
            "CPU": f"{cpu}%",  # CPU-användning i procent.
            "RAM": f"{memory.percent}% ({round(memory.used / (1024 ** 3), 2)} GB of {round(memory.total / (1024 ** 3), 2)} GB)",  # RAM-användning i procent samt förbrukad och total mängd i GB.
            "Disk": f"{disk.percent}% ({round(disk.used / (1024 ** 3), 2)} GB of {round(disk.total / (1024 ** 3), 2)} GB)"  # Diskanvändning i procent samt förbrukad och total mängd i GB.
        }

    def get_status(self):
        """Returnerar status för aktiv övervakning."""
        if not self.active:
            return "Ingen övervakning aktiv."  # Om övervakningen inte är aktiv, ge ett meddelande.
        self.update()  # Uppdatera systeminformationen om övervakningen är aktiv.
        return self.data  # Returnera den hämtade systeminformationen.
