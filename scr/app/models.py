from sqlalchemy import Column, DateTime, Integer, String

from scr.app.schemas import QuestionSchema
from scr.db.base import Base


class Question(Base):
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    @classmethod
    def from_schema(cls, schema: QuestionSchema) -> 'Question':
        '''Создает объект класса из схемы.'''

        question = Question(
            id=schema.id,
            answer=schema.answer,
            question=schema.question,
            created_at=schema.created_at,
        )

        return question
