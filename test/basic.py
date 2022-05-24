# -*- coding: utf-8 -*-
import requests
import json

LOC="/spellchecker"
LOC="/process/service"


inp = "Páli, vini mínum, langaði að horfa á sjónnvarpið. Hversu oft harfir hann á sjónvarpið?"

print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content":inp})
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()

print("#### ERROR ####")


