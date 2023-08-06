import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ContromeAPI:
    def __init__(self, base_url, haus_id, user, password):
        self.base_url = base_url
        self.haus_id = haus_id
        self.user = user
        self.password = password

    def _get(self, endpoint, *args):
        url = f"{self.base_url}/get/json/v1/{self.haus_id}/{endpoint}/"
        if args:
            # Filtere None-Werte aus args heraus und füge nur Nicht-None-Werte zur URL hinzu
            non_none_args = [str(arg) for arg in args if arg is not None]
            if non_none_args:
                url += "/".join(non_none_args) + "/"
        logger.info(f"GET request to URL: {url}")
        response = requests.get(url)
        logger.debug(f"GET response raw: {response.content}")
        response.raise_for_status()
        result = response.json()
        logger.info(f"GET response: {result}")
        return result

    def _post(self, endpoint, *args, **data):
        url = f"{self.base_url}/set/json/v1/{self.haus_id}/{endpoint}/"
        if args:
            url += "/".join(str(arg) for arg in args) + "/"
        data.update({"user": self.user, "password": self.password})
        logger.info(f"POST request to URL: {url} with data: {data}")
        response = requests.post(url, data=data)
        logger.debug(f"POST response raw: {response.content}")
        response.raise_for_status()
        result = response.json()
        logger.info(f"POST response: {result}")
        return result

    def get_deviation(self, raum_id=None):
        """
        Enthält

            Raumname („name)
            Temperaturdifferenz Isttemperatur zu Zieltemperatur („deviation“)

        Deviation-Wert ist negativ, wenn der Raum zu kalt ist. Deviation-Wert ist positiv, wenn der Raum zu warm ist.

        ACHTUNG: Dieser Endpunkt funktioniert nur, wenn das Plugin „Vorlauftemperaturkorrektur“ aktiviert ist.

        """
        return self._get("deviation", raum_id)

    def get_fps(self, raum_id=None):
        """
        Enthält

            Name („name“)
            Wert („value“)

        """
        return self._get("fps", raum_id)

    def get_heizprogramm(self):
        """
        Enthält

            Schaltzeitpunkte des Heizprogramms
            Temperaturszenen, die beim jeweiligen Schaltzeitpunkt aktiviert werden.

        """
        return self._get("heizprogramm")

    def set_soll(self, raum_id, soll):
        return self._post("soll", raum_id, soll=soll)

    def set_ziel(self, raum_id, ziel, duration):
        return self._post("ziel", raum_id, ziel=ziel, duration=duration)

    def set_temperaturszenen(self, szene_id, duration=None):
        data = {}
        if duration is not None:
            data["duration"] = duration
        return self._post("temperaturszenen", szene_id, **data)

    def set_default_duration(self, duration):
        return self._post("quickui", duration=duration)

    def set_roomoffset(self, raum_id, offset, offset_name):
        return self._post("roomoffset", raum_id, offset=offset, offset_name=offset_name)

    def set_houseoffset(self, offset, offset_name):
        return self._post("houseoffset", offset=offset, offset_name=offset_name)


if __name__ == "__main__":
    base_url = "http://your_mini_server_ip"
    haus_id = 1
    user = "your_user"
    password = "your_password"

    api = ContromeAPI(base_url, haus_id, user, password)
    deviation = api.get_deviation()
    print(json.dumps(deviation, indent=2))
