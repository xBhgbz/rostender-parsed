
import datetime
from bs4 import BeautifulSoup as bs

# number description date-start date-finish address price customer category


def parsing_tenders(source_data) -> list:
    """Парсит страницу html и возвращает данные о тендерах"""

    soup = bs(source_data, "html.parser")
    tenders_info = []

    tenders = soup.find_all("div", class_="tender-row__wrapper")

    for tender in tenders:
        try:
            info = {
                "Номер тендера": tender.find("span", class_="tender__number")
                .get_text(strip=True)
                .replace("\xa0", " ")
                .split("№")[1],
                "Название": tender.find("a", class_="tender-info__description")
                .get_text(strip=True)
                .replace("\xa0", " "),
                "Дата создания": tender.find("span", class_="tender__date-start")
                .get_text(strip=True)
                .replace("\xa0", " ")
                .split(" ")[1],
                "Дата окончания": datetime.strptime(
                    tender.find("span", class_="tender__countdown-text")
                    .get_text(strip=True)
                    .replace("\xa0", " ")
                    .split(")")[1],
                    "%d.%m.%Y %H:%M",
                ),
                "Адрес": tender.find("div", class_="tender-address")
                .get_text(strip=True)
                .replace("\xa0", " "),
                "Цена": tender.find("div", class_="starting-price__price")
                .get_text(strip=True)
                .replace("\xa0", " ")
                .split(" ₽")[0],
                # "customer": tender.find("a", class_="tender-customer__name")
                # .get_text(strip=True)
                # .replace("\xa0", " ")
                # if tender.find("a", class_="tender-customer__name")
                # else None,
                "Отрасли": tender.find("a", class_="list-branches__link")
                .get_text(strip=True)
                .replace("\xa0", " "),
            }

            tenders_info.append(info)

        except AttributeError:
            continue

    return tenders_info
