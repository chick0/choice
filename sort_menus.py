from os.path import join
from json import load
from json import dump

path = join("app", "menus.json")

json = load(open(path, mode="r", encoding="utf-8"))
json = list(set(json))
json = sorted(json)
print(len(json))

dump(json, open(path, mode="w", encoding="utf-8"), ensure_ascii=False, indent=4)
