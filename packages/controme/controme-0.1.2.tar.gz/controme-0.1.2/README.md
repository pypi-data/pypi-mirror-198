# Controme API Python Wrapper

<p>Dieses Repository enthält einen Python-Wrapper für die Controme-API, der es ermöglicht, auf einfache Weise Abfragen und Befehle an die Controme-Smart-Home-Heizungssteuerung zu senden.</p>

# Features

* <p>Einfache Python-Schnittstelle für die Controme-API</p>
* <p>Abfrage von Informationen wie Abweichungen, Fußbodenheizungsparametern (FPS) und Heizprogrammen</p>
* <p>Einstellung von Sollwerten, Zielwerten, Temperaturszenen, Standarddauern, Raum- und Haus-Offsets</p>

# Installation

<p>Um dieses Modul zu verwenden, installieren Sie es über pip</p>

```python

pip install controme

```

oder 

```bash

python3 -m pip install controme

```

# Beispiel

Ein Beispiel, wie Sie dieses Modul verwenden können:

```python

from controme import ContromeAPI

base_url = "http://miniserver_ip"
haus_id = 1
user = "your.email@example.com"
password = "your-password"

api = ContromeAPI(base_url, haus_id, user, password)
deviation = api.get_deviation()
print(json.dumps(deviation, indent=2))

```

<p>Bitte ersetzen Sie your.email@example.com und your-password durch Ihre eigenen Zugangsdaten.</p>

# Dokumentation

Die Klasse ContromeAPI stellt die folgenden Methoden zur Verfügung:

* `get_deviation(raum_id=None)`
* `get_fps(raum_id=None)`
* `get_heizprogramm()`
* `set_soll(raum_id, soll)`
* `set_ziel(raum_id, ziel, duration)`
* `set_temperaturszenen(szene_id, duration=None)`
* `set_default_duration(duration)`
* `set_roomoffset(raum_id, offset, offset_name)`
* `set_houseoffset(offset, offset_name)`

<p>Bitte beachten Sie die Dokumentation in der Klasse für weitere Informationen zu den einzelnen Methoden und ihren Parametern.</p>

# Lizenz

<p>Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei LICENSE.</p>

# Haftungsausschluss

<p>Bitte beachten Sie, dass dieses Projekt nicht von Controme oder einem ihrer Partner unterstützt oder offiziell unterstützt wird. Die Nutzung dieses Moduls erfolgt auf eigenes Risiko, und die Autoren übernehmen keine Verantwortung für mögliche Schäden oder Verluste im Zusammenhang mit der Nutzung dieses Codes.</p>

# Beitrag

<p>Fühlen Sie sich frei, Pull-Requests zu erstellen oder Probleme zu melden, um dieses Projekt zu verbessern.</p>