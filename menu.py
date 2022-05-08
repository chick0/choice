from json import load
from json import dump
from version import PATH_JSON
from version import update_version


def main():
    menu = input("새로운 메뉴를 입력해주세요 : ")
    json: list = load(open(PATH_JSON, mode="r", encoding="utf-8"))

    if menu in json:
        print("해당 메뉴는 이미 등록된 메뉴 입니다.")
    else:
        json.append(sorted(menu))
        dump(
            menu,
            open(PATH_JSON, mode="w", encoding="utf-8"),
            ensure_ascii=False,
        )

        update_version()


if __name__ == "__main__":
    main()
