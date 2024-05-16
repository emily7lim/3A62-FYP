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

#gf Insurance (Main Plans Cash Value)
class gfInsuranceMainCashPlans(Base):
    __tablename__ = 'gfinsurancemaincashplans'
    insurance_main_cash_plans_id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    main_plan_id = Column(String(100), nullable = False)
    datecreated = Column(String(100), nullable=True)
    year = Column(Integer, nullable=True)
    currentvalue = Column(Numeric(15, 2), nullable=True)
    nonguaranteeamt = Column(Numeric(15, 2), nullable=True)
    loanamt = Column(Numeric(15, 2), nullable=True)
    loaninterest = Column(Numeric(15, 2), nullable=False)

    