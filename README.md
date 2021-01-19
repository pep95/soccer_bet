# soccer_bet

praticamente devi prima avviare excel_to_db.py e dargli i parametri di input
e dopo stats_out.py

per recuperare il file excel come  "seriea_pre.csv" basta aprire excel, click su "Dati" click su "Da Web",
all'url devi mettere "https://www.soccerstats.com/results.asp?league=italy&pmtype=bydate"
poi click su "Table 1", vedrai l'anteprima, e poi click su "Carica".

Poi elimino manualmente la riga 2, e le colonne I,H,G,E.
In realtà elimino anche le partite verona-roma e juve-napoli perchè il risultato è stato assegnato a tavolino.

Salvalo in formato csv.
