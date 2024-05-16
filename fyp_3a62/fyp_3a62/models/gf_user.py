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

#gf Users
#Parent to child(gf_insuranceMainPlans)
class gfUser(Base):
    __tablename__ = 'gfuser'
    user_id =  Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4) #get created by default
    mongodb_id = Column(String(100), nullable = False ,unique = True) #given in the csv by client
    fullname = Column(String(255), nullable=True, unique = True)
    prefname = Column(String(255), nullable=True)
    nationality = Column(String(100), nullable=True)
    phone = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False)
    residenceaddress = Column(String(255), nullable=True)
    residencecity = Column(String(100), nullable=True)
    residencestate = Column(String(100), nullable=True)
    residencecountry = Column(String(100), nullable=True)
    residencezip = Column(String(10), nullable=True)
    citizenship = Column(String(100), nullable=True)
    nationalstatus = Column(String(100), nullable=True)
    company = Column(String(100), nullable=True)
    designation = Column(String(100), nullable=True)
    #allow users to specify phone coutnry code, example: +65
    workphone = Column(String(100), nullable=True)
    workemail = Column(String(100), nullable=True)
    workaddress = Column(String(255), nullable=True)
    workcity = Column(String(100), nullable=True)
    workstate = Column(String(100), nullable=True)
    workcountry = Column(String(100), nullable = True)
    workzip = Column(String(10), nullable=True)
