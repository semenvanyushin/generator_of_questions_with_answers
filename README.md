## Generator of questions with answers
![Python](https://img.shields.io/badge/Python-3.10.9-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.14-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.3-blue)

### Описание проекта:
API для получения вопросов с ответами, которые можно использовать, например, в викторине.

### План развития проекта:

```bash
- Добавить тесты
- Добавить логгирование
- Добавить контейнеризацию Docker
```

### Запуск в режиме разработчика:

Создание и активация виртуального окружения:
```bash
python3 -m venv venv # MacOS и Linux
```
```bash
python -m venv venv # Windows
```
```bash
source /venv/bin/activated # MacOS и Linux
```
```bash
source venv/Scripts/activate # Windows
```
Установка зависимостей из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
Выполнение миграций(база данных PostgreSQL):
```bash
alembic init migrations
```
```bash
alembic revision --autogenerate -m 'DataBase creation'
```
```bash
alembic upgrade head
```
Запуск сервера(выполняется из корневой директории):
```bash
uvicorn main:app --reload
```

## Проект доступен по адресу:

```bash
http://127.0.0.1:8000/
```

### Примеры работы с API

Получение вопросов из базы данных:

```
GET http://127.0.0.1:8000/?skip=3&limit=2
```

в ответе:
```
[
  {
    "id": 6735,
    "question": "Federal Hall, where Washington took 1st oath of office as President, is on this NYC street",
    "answer": "Wall Street",
    "created_at": "2022-12-30T18:40:18.917000"
  },
  {
    "id": 58206,
    "question": "If you don't know the name of a male ass or donkey, you don't know this",
    "answer": "Jack",
    "created_at": "2022-12-30T19:02:34.525000"
  }
]
```

Получение из стороннего ресурса новых вопросов и добавление их в базу данных:

```
POST http://127.0.0.1:8000/
```

в body:
```
{
  "questions_num": 1
}
```

в ответе:
```
[
  {
    "id": 40424,
    "question": "This hot spot is usually found under a mantel",
    "answer": "a fireplace",
    "created_at": "2022-12-30T22:54:27.015000"
  }
]
```

Пример ответа при ошибке валидации:

```
{
  "detail": [
    {
      "loc": [
        "body",
        21
      ],
      "msg": "Expecting value: line 2 column 20 (char 21)",
      "type": "value_error.jsondecode",
      "ctx": {
        "msg": "Expecting value",
        "doc": "{\n  \"questions_num\": test\n}",
        "pos": 21,
        "lineno": 2,
        "colno": 20
      }
    }
  ]
}
```

## Документация к API доступна после запуска проекта по адресам:

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc


Автор: [Семен Ванюшин](https://github.com/semenvanyushin)