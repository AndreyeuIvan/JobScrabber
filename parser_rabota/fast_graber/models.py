from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship


class Keyword(Base):
	__tablename__ = 'keywords'

	id = Column(Integer, primary_key = True)
	name = Column(String(100))
	create_at = Column(TIMESTAMP(timezone=True),
					   nullable=False, server_default=text('now()'))

	def __repr__(self):
		return f"Keyword is '{self.name}'"


class Data(Base):
	__tablename__ = 'data'

	id = Column(Integer, primary_key = True)
	company = Column(String(200))
	title = Column(String(250))
	link = Column(String(300))
	location = Column(String(200))
	keyword_id = Column(Integer, ForeignKey("keywords.id"))
	keyword = relationship(Keyword)

	def __repr__(self):
		return f"Job in '{self.company}', as a '{self.title}'"
