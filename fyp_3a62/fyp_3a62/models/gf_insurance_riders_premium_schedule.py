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

#gf Insurance (riders premiums schedule)
class gfInsuranceRidersPremiumSchedule(Base):
    __tablename__ = 'gfinsuranceriderspremiumschedule'
    insurance_riders_premium_schedule_id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    main_plan_id = Column(String(100),nullable = False)
    rider_id = Column(String(100), nullable=False)
    year = Column(Integer, nullable=True)
    month = Column(Integer, nullable=True)
    date = Column(String(50), nullable=True)
    premiums = Column(String(100), nullable=True)
    paymentmode = Column(String(100), nullable=True)