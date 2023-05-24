from typing import List

from fastapi import HTTPException
from httpx import Client, Response
from sqlalchemy.orm import Session

from scr.app.actions import question
from scr.app.models import Question
from scr.app.schemas import QuestionSchema


def get_questions(num: int) -> Response:
    '''
    Запрашивает с внешнего ресурса и выдает вопросы в требуемом количестве.
    '''

    url = f'https://jservice.io/api/random?count={num}'
    responce = Client().get(url)

    if responce.status_code != 200:
        raise HTTPException(
            status_code=responce.status_code,
            detail='Не удалось получить вопросы'
        )

    return responce


def removes_repetitions_questions(
    db: Session, num: int, unique_questions_data: List
) -> List[Question]:
    '''
    Совершает дополнительные запросы к внешнему ресурсу,
    если полученный(е) вопрос(ы) уже имеются в базе данных.
    '''

    while num > 0:
        questions_data = get_questions(num).json()
        questions = [QuestionSchema(
            id=ithem.get('id'), question=ithem.get('question'),
            answer=ithem.get('answer'), created_at=ithem.get('created_at')
        ) for ithem in questions_data]
        questions_list = [
            question
            for question
            in question.add_questions_list(db=db, lst=questions)
            if question
        ]
        num -= len(questions_list)
        unique_questions_data.extend(questions_list)

    return unique_questions_data
