from json import loads
from json import dump
from version import PATH_JSON
from version import update_version


def main():
    menu = input("새로운 메뉴를 입력해주세요 : ").strip()
    json = loads(open(PATH_JSON, mode="r", encoding="utf-8").read())

    if menu in json:
        print("해당 메뉴는 이미 등록된 메뉴 입니다.")
    else:
        json.append(menu)
        dump(
            sorted(json),
            open(PATH_JSON, mode="w", encoding="utf-8"),
            ensure_ascii=False,
        )

        update_version()


if __name__ == "__main__":
    main()
