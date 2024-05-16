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

#gf Users
class kycChatCollectionTable(Base):
    __tablename__ = 'kyccollectiontable'
    kyc_collection_id =  Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    useremail = Column(String(255), nullable= False)
    question = Column(Text, nullable=False)
    userreply = Column(Text, nullable=False)
    dateupdated = Column(DateTime(timezone=True), default=datetime.datetime.now())