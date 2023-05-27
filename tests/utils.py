from typing import Union
from fastapi.testclient import TestClient
from httpx import Response


def check_limit(content: list[dict[str, Union[str, int]]], limit: int) -> None:
    '''Проверяет соответствие количества запрошенных вопросов и полученных.'''

    assert len(content) == limit, (
        f'Проверьте, что возвращается запрошенное количестов вопросов: {limit}'
    )


def try_url(
    client: TestClient, url: str, type: str, questions_num: int = None
) -> Response:
    '''Проверяет доступность post и get запросов к url.'''

    try:
        if type == 'post':
            return client.post(url=url, json={'questions_num': questions_num})
        else:
            return client.get(url)
    except Exception as e:
        assert False, (f"Страница `{url}` работает неправильно. Ошибка: `{e}`")


def check_responce_field_in_json(
    content: list[dict[str, Union[str, int]]]
) -> None:
    '''Проверяет наличие необходимых ключей в полученных данных.'''

    key_list: list[str] = ['id', 'question', 'answer', 'created_at']

    for field in key_list:
        assert field in content[0], (
            f'Проверьте, что поле {field} есть в таблице вопросов базы данных.'
        )


def check_endpoint(
    client: TestClient, url: str, type: str,
    limit: int = None, questions_num: int = None
) -> None:
    '''Проверяет работу эндпоинта.'''

    responce = try_url(
        client=client, url=url, type=type, questions_num=questions_num
    )
    content = responce.json()

    if type == 'post':
        limit = questions_num

    # Проверка выдачи данных в запрошенном количестве
    check_limit(content=content, limit=limit)

    # Проверка наличия необходимых ключей в полученных данных
    check_responce_field_in_json(content=content)
