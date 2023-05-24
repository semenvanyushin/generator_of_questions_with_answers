from typing import List, Type

from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from scr.app.models import Question
from scr.app.schemas import QuestionSchema


class QuestionActions:
    def __init__(self, model: Type[Question]):
        '''
        Проводит операции с базой данных.
        '''

        self.model = model

    def get_questions(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[Question]:
        '''
        Получает и выдает данные из базы.
        '''

        return db.query(self.model).offset(skip).limit(limit).all()

    def create_question(self, db: Session, question: Question) -> Question:
        '''
        Записывает данные в базу и возвращает их.
        Возвращет 'False' при попытке записать уже имеющиеся данные.
        '''

        try:
            db.add(question)
            db.commit()
            db.refresh(question)
            return question
        except IntegrityError:
            return False

    def add_questions_list(
        self, db: Session, lst: List[QuestionSchema]
    ) -> List[bool | Question]:
        '''
        Проверяет список вопросов на наличие их в базе данных.
        Добавляет новые вопросы в базу данных.
        Возвращает список вопросов, которых не было в базе.
        '''

        questions = []
        for question_schema in lst:
            question = Question.from_schema(question_schema)
            question = self.create_question(db=db, question=question)
            questions.append(question)

        return questions


question = QuestionActions(Question)
