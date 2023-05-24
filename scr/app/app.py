from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from scr.app.actions import question
from scr.app.models import Question
from scr.app.schemas import QuestionRequest, QuestionSchema
from scr.app.utils import removes_repetitions_questions
from scr.db.base import Base
from scr.db.session import engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Quiz_API')


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/', response_model=List[QuestionSchema], tags=['questions'])
def get_questions(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 10
) -> List[Question]:
    '''Возвращает список вопросов из базы данных приложения.'''

    questions = question.get_questions(db=db, skip=skip, limit=limit)

    return questions


@app.post('/', response_model=List[QuestionSchema], tags=['questions'])
def generate_new_questions(
    db: Session = Depends(get_db), questions_num: QuestionRequest = None
) -> List[Question]:
    '''Возвращает список вопросов из внешнего ресурса.'''

    unique_questions_data: list[QuestionSchema] = []
    num = questions_num.questions_num
    questions = removes_repetitions_questions(
        db=db,
        num=num,
        unique_questions_data=unique_questions_data
    )

    return questions
