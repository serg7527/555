import json
import requests_html

BASE_URL = "https://catalog.onliner.by/notebook"
ITEMS_ROOT = "#container .catalog-wrapper .catalog-form__filter .catalog-form__filter-part.catalog-form__filter-part_2"


def get_page(num, session) -> requests_html:
    response = session.get(BASE_URL, params={"page": num})
    if response.status_code == 200:
        return response


def render_html(html):
    ...


def main():
    session = requests_html.HTMLSession()
    num_page = 1

    page = get_page(num_page, session)
    page.html.render()

    items_box = page.html.find(ITEMS_ROOT, first=True)
    last_num_box = items_box.find(
        ".catalog-pagination__pages ul > li:last-child", first=True)
    if last_num_box is not None:
        count_pages = int(last_num_box.text)
    else:
        print("No page found")
        return
    result = []

    items = items_box.find(".catalog-form__offers .catalog-form__offers-unit")
    # for num in range(2, count_pages + 1):
    for num in range(1, 4):
        if items is None:
            page = get_page(num, session)
            page.html.render()
            items_box = page.html.find(ITEMS_ROOT, first=True)
            items = items_box.find(".catalog-form__offers .catalog-form__offers-unit")
        for i, item in enumerate(items, 1):
            item_data = {}

            img_box = item.find(".catalog-form__offers-part_image img", first=True)
            item_data["img"] = img_box.attrs["src"]

            item_data["promo"] = True if item.find(
                ".catalog-form__offers-part_promotion",
                first=True
            ) is not None else False

            desc_box = item.find(".catalog-form__offers-part_data > div:nth-child(1)", first=True)
            item_data["desc"] = desc_box.text
            item_data["link"] = list(desc_box.links)[0]

            cost_box = item.find(
                ".catalog-form__offers-part_control > div.catalog-form__description a",
                first=True
            )
            try:
                item_data["cost"] = cost_box.text.replace("&nbsp;", " ").strip()
            except Exception as err:
                print(item.html)
                ...

            result.append(item_data)
        items = None

    return result


if __name__ == "__main__":
    data = main()
    with open("items.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
