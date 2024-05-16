from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    BLOB,
    DateTime,
    String,
    Numeric,
    TIMESTAMP,
    ForeignKey,

)

from datetime import datetime
import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.sql.sqltypes import DATETIME

from .meta import Base


class aiPredictionHistoryTable(Base):
    __tablename__ = 'aipredictionhistory'
    aipredictionhistory_id =  Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4) #get created by default
    userquestion = Column(Text)
    predictionlabel = Column(String(100)) 
    user_email = Column(String(100), nullable=True)
    time = Column(DateTime(timezone=True), default=datetime.datetime.now())

