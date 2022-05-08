from os.path import join
from hashlib import sha384


def update_version():
    json = join(".", "public", "menus.json")
    version = join(".", "public", "menus.version")

    with open(json, mode="r", encoding="utf-8") as json_reader:
        hash = sha384(json_reader.read().encode()).hexdigest()

    with open(version, mode="w", encoding="utf-8") as version_writer:
        version_writer.write(hash)

    print("version updated to", hash)


if __name__ == "__main__":
    update_version()
