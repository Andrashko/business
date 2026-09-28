from requests import get

from bs4 import BeautifulSoup

from gliner import GLiNER

model = GLiNER.from_pretrained("urchade/gliner_multi-v2.1")

CHUNK_SIZE = 200

BASE_URL = "https://www.uzhnu.edu.ua"

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
}

fac_url = f"{BASE_URL}/uk/cat/faculty-mdt"

# завантажуємо сторінку факультету

fac_page = get(fac_url, headers=HEADERS)

# знаходимо список кафедр

soup = BeautifulSoup(fac_page.content, "html.parser")

dep_list = soup.find(class_="departments")

#         # для кожної кафедри у списку

if dep_list:

    for li in dep_list.find_all("li"):

        #                 # знаходимо текст безпосередньо в контенті елементу  a

        dep_name = li.a.find(string=True, recursive=False)

        #                 # URL складається з базового, та відносного, який записано в атрибуті href

        dep_url = BASE_URL + li.a.get("href")

        # print (f"кафедра: {dep_name}")

        print(f"    Назва кафедри: {dep_name}\n")

        print(f"    URL: {dep_url}\n")

        # завантажуємо сторінку кафедри

        dep_page = get(f"{dep_url}/staff", headers=HEADERS)

        # знаходимо список викладачів

        soup = BeautifulSoup(dep_page.content, "html.parser")

        text = soup.get_text(" ", strip=True)

        words = text.split()

        entities = []

        for i in range(0, len(words), CHUNK_SIZE):

            chunk = " ".join(words[i : i + CHUNK_SIZE + 50])

            result = model.predict_entities(
                chunk, ["person", "job title"], threshold=0.5
            )

            entities.extend(result)

        for e in entities:

            print(e["label"], e["text"], e["score"])
