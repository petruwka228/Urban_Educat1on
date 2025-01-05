import requests

# 1. GET-запрос с параметрами
def get_example():
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    response = requests.get(url, params=params)
    print("GET-запрос:")
    print("Статус:", response.status_code)
    print("Данные:", response.json()[:2])
    print()

# 2. POST-запрос с телом запроса
def post_example():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "My Post",
        "body": "This is a post created with requests.",
        "userId": 1,
    }
    response = requests.post(url, json=data)
    print("POST-запрос:")
    print("Статус:", response.status_code)
    print("Ответ:", response.json())
    print()

# 3. Использование сессии для сохранения cookies
def session_example():
    with requests.Session() as session:
        session.get("https://httpbin.org/cookies/set?testcookie=value")
        response = session.get("https://httpbin.org/cookies")
        print("Работа с сессией:")
        print("Cookies:", response.json())
        print()

if __name__ == "__main__":
    get_example()
    post_example()
    session_example()

