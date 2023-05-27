from fastapi.testclient import TestClient

from scr.app.app import app
from tests.utils import check_endpoint


client = TestClient(app)


def test_post_index() -> None:
    '''Проверяет работу при 'POST' запросе.'''

    questions_num: int = 4
    url: str = '/'
    request_type: str = 'post'

    check_endpoint(
        client=client, url=url,
        type=request_type, questions_num=questions_num
    )


def test_get_index() -> None:
    '''Проверяет работу при 'GET' запросе.'''

    limit: int = 2
    skip: int = 1
    url: str = f'/?skip={skip}&limit={limit}'
    request_type: str = 'get'

    check_endpoint(client=client, url=url, type=request_type, limit=limit)
