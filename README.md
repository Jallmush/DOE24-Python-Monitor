# DOE24-Python-Monitor
Systemutveckling i Python

Slutuppgift

 

Slutuppgiften går ut på att skriva en övervakningsapplikation skriven i Python. Applikation samlar in information från operativsystemet och presenterar informationen för en användare.

En användare kan interagera med applikationen via en konsol för att få fram information om CPU användning, minnesanvändning, diskanvändning. När användaren interagerar med applikationen via konsolmenyn ska inga konfigurerade larm aktiveras.

 

Kraven på applikationen för godkänd nivå.

 

Applikationen startas, och sedan presenteras användaren med fem stycken alternativ i konsolen.

 

    Starta övervakning

Startar övervakning av CPU användning, minnesanvändning och diskanvändning. Notera alltså att ingen övervakning ska starta automatiskt vid programstart.

    Lista aktiv övervakning

Listar aktiv övervakning som är aktiv samt nuvarande övervakningsstatus. Har man inte startat övervakningen ska en text visas som informerar användaren om att ingen övervakning är aktiv. Annars visas övervakningen, t.ex:

CPU Anvädning: 35%

Minnesanvändning: 65% (4.2 GB out of 8 GB used)

Diskanvändning: 80% (400 GB out of 500 GB used)

Efter detta promtas användaren om att bekräfta genom att trycka enter.

Tryck valfri tangent för att gå tillbaka till huvudmeny

Efter detta visas åter huvudmenyn för användaren.

    Skapa larm

Väljer man detta alternativ får man upp ytterligare en meny där man får välja att konfigurera larm inom tre områden eller gå tillbaka till huvudmenyn.

Konfigurera larm

    CPU användning
    Minnesanvändning
    Diskanvändning
    Tillbaka till huvudmeny

Efter att man valt ett alternativ får man välja en procentuell nivå där larmet ska aktiveras. T.ex.

Ställ in nivå för alarm mellan 0-100.

Efter att användaren har valt en nivå skrivs en bekräftelse ut, sedan visas huvudmenyn igen.

Larm för CPU användning satt till 80%. 

Nivån måste matas in som en siffra mellan 1-100 och matas nonsens in ska användaren få ett felmeddelande.

    Visa larm

Listar alla configurerade larm. Larmen ska vara sorterade på typ när de visas. Exempel:

    CPU larm 70%
    Disklarm 95%
    Minneslarm 80%
    Minneslarm 90%

Efter detta promtas användaren om att bekräfta genom att trycka enter.

Tryck valfri tangent för att gå tillbaka till huvudmeny

Notera att man kan ha flera larm av samma typ.

 

    Starta övervakningsläge

Startar ett övervakningsläge. Användaren blir promtad om att övervakningsläget har startats, sedan loopar en sträng med jämna mellanrum som meddelar användaren att övervakningen är aktiv samt att man på något sätt kan återgå till huvudmenyn.

Övervakning är aktiv, tryck på valfri tangent för att återgå till menyn.

                Triggas ett larm när övervakningen är aktiv skrivs det ut i konsolen. T.ex:

                ***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER 80%***

 

Icke funktionella krav på applikationen för G nivå

Programmet ska bestå av minst ett antal filer med kod som aktivt används. Dvs. All kod ska inte vara skriven i en fil.

Programmet ska använda sig av objekt där det passar.

Programmet ska vara skrivet med funktioner.

Programmet ska innehålla funktionell programmering på minst ett ställe. T.ex. vid sortering av larm innan visning.

Koden ska vara välskriven, dvs. Lättförståliga variabelnamn och funktionsnamn, kommentarer där det passar och en bra struktur.

Koden ska självklart vara bugfri. Dvs. funktionaliteten som beskrivs ska alltid fungera korrekt.

Koden ska kunna hantera att användaren matar in felaktig input / nonsens utan att gå sönder. Dvs. rimlig input sanitization ska finnas.
