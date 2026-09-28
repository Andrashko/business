from requests import get, post
import json
from bs4 import BeautifulSoup

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

        text = soup.select_one("#content .page_block").get_text()

        # 3. Формуємо запит до Gemma
        prompt = f"""
        Знайди всіх працівників у наведеному тексті.

        Для кожного працівника визнач:
        - повне ім'я;
        - посаду;
        - email, якщо він вказаний.
        
        Ігноруй інші дані. Не вигадуй поля крім вказаних.  

        Поверни ТІЛЬКИ JSON такого формату де кожен обєкт має рівно 3 поля:

        {{
          "employees": [
            {{
              "name": "Ім'я Прізвище",
              "position": "посада",
              "email": "email"
            }}
          ]
        }}

        Не вигадуй інформацію, якої немає в тексті.

        Текст сторінки:
        {text}
        """

        # 4. Передаємо текст локальній Gemma через Ollama
        r = post(
            "http://localhost:11434/api/chat",
            json={
                "model": "gemma3:4b",
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
                "format": "json",
            },
        )

        # 5. Отримуємо відповідь моделі
        answer = r.json()["message"]["content"]

        print(answer)
