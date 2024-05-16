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

#gf Insurance (riderss)
class gfInsuranceRiders(Base):
    __tablename__ = 'gfinsuranceriders'
    insurance_riders_id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    mongodb_rider_id = Column(String(100), nullable = False, unique = True)
    main_plan_id = Column(String(100), nullable=True)
    ageofentry = Column(Integer, nullable=True)
    productname = Column(String(255), nullable=True)
    insurer = Column(String(100), nullable=True)
    policynum = Column(String(100), nullable=True)
    coverageterm = Column(String(100), nullable=True)
    dateincepted = Column(String(100), nullable=True)
    datematured = Column(String(100), nullable=True)
    paymentterm = Column(String(100), nullable=True)
    paymentmode = Column(String(100), nullable=True)
    paymentamt = Column(Numeric(15, 2), nullable=True)
    longtermcare = Column(String(100), nullable=True)
    death = Column(Numeric(15, 2), nullable=True)
    totalpermdisability = Column(Numeric(15, 2), nullable=True)
    disabilityincome = Column(Numeric(15, 2), nullable=True)
    earlycriticalillness = Column(Numeric(15, 2), nullable=True)
    criticalillness = Column(Numeric(15, 2), nullable=True)
    personalaccident = Column(Numeric(15, 2), nullable=True)
    hospitalizationbenefits = Column(Numeric(15, 2), nullable=True)
    remarks = Column(Text, nullable=True)
