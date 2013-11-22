# Transliterator.py
# This is Unicode; run it in Python3 or you will have a bad time

import json

gjfile = open('bangladesh-divisions.geojson', 'r')
geojson = json.load( gjfile )
gjfile.close()

bengali_match = {
  "ল": u"\U00016A4D", # l > OL
  "র": u"\U00016A53", # r > RO
  "প": u"\U00016A50", # p > PA
  " ু": u"\U00016A52", # u > ?
  "ং": u"\U00016A46\U00016A41", # ang > ?
  "া": u"\U00016A46", # ah > ?
  "জ": u"\U00016A45", # J > D?
  "শ": u"\U00016A54", # SH > ?
  "স": u"\U00016A4B", # S > ?
  "হ": u"\U00016A49", # H > ?
  "ী": u"\U00016A4A", # EE > ?
  "ট": u"\U00016A40", # T > ?
  "ে": u"\U00016A58", # EH > ?
  "ি": u"\U00016A4A", # IH > ?
  "চ": u"\U00016A4B", # T (or CH?) > ?
  "গ": u"\U00016A59", # G > KO
  "ম": u"\U00016A4E", # M
  " ্": u"\U00016A58", # UHH
  "ব": u"\U00016A44", # B
  "ঢ": u"\U00016A45", # DH > DA
  "ক": u"\U00016A4C", # K
  "খ": u"\U00016A4C", # KH
  "ন": u"\U00016A4F", # N
  # O 16A51
  # NG 16A41
}

for feature in geojson["features"]:
    bengali_name = feature["properties"]["name_local"]
    mro_name = ""
    for letter in bengali_name:
        if letter in bengali_match:
            mro_name = mro_name + bengali_match[ letter ]
    feature["properties"]["name_mro"] = mro_name
    print(mro_name)

gjout = open('bangladesh-mro.geojson', 'w')
gjout.write( json.dumps( geojson ) )
gjout.close()