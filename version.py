from os.path import join
from hashlib import sha384

PATH_JSON = join(".", "public", "menus.json")
PATH_VERSION = join(".", "public", "menus.version")


def update_version():
    with open(PATH_JSON, mode="r", encoding="utf-8") as json_reader:
        hash = sha384(json_reader.read().encode()).hexdigest()

    with open(PATH_VERSION, mode="w", encoding="utf-8") as version_writer:
        version_writer.write(hash)


if __name__ == "__main__":
    update_version()
