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

#gf Insurance (main Plans)
class gfInsuranceMainPlans(Base):
    __tablename__ = 'gfinsurancemainplans'
    insurance_id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    mongodb_id = Column(String(50), nullable = False, unique = True)
    datecreated = Column(String(100), nullable=True)
    policyholder = Column(String(255), nullable=True)
    lifeassured = Column(String(255), nullable=True)
    age = Column(Integer, nullable=True)
    dob = Column(String(50), nullable=False)
    status = Column(String(10), nullable=True)
    productname = Column(String(100), nullable=True)
    insurer = Column(String(100), nullable=True)
    policynum = Column(String(100), nullable=True)
    coverageterm = Column(String(100), nullable=True)
    policytype = Column(String(255), nullable=True)
    dateincepted = Column(String(100), nullable=True)
    datematured = Column(String(100), nullable=True)
    datepaymentmatured = Column(String(100), nullable=True)
    nominationnominee = Column(String(255), nullable=True)
    nominationstatus = Column(String(100), nullable=True)
    paymentfrequency = Column(String(100), nullable=True)
    paymentterm = Column(String(100), nullable=True)
    paymentmode = Column(String(255), nullable=True)
    paymentamt = Column(Numeric(15, 2), nullable=True)
    hsdeductible = Column(Numeric(15, 2), nullable=True)
    hscoinsured = Column(Numeric(15, 2), nullable=True)
    hsyearlylimit = Column(Numeric(15, 2), nullable=True)
    gitravelmedicaloverseas = Column(Numeric(15, 2), nullable=True)
    gitravelpersonalaccident = Column(String(50), nullable=True)
    gitravelregion = Column(Numeric(15, 2), nullable=True)
    gihomefixtures = Column(Numeric(15, 2), nullable=True)
    gihomecontents = Column(Numeric(15, 2), nullable=True)
    gimotorproperty = Column(Numeric(15, 2), nullable=True)
    gimotorperson = Column(Numeric(15, 2), nullable=True)
    gimotorworkshop = Column(Numeric(15, 2), nullable=True)
    gimotorncd = Column(Numeric(15, 2), nullable=True)
    longtermcare = Column(Numeric(15, 2), nullable=True)
    death = Column(Numeric(15, 2), nullable=True)
    totalpermdisability = Column(Numeric(15, 2), nullable=True)
    disabilityincome = Column(Numeric(15, 2), nullable=True)
    earlycriticalillness = Column(Numeric(15, 2), nullable=True)
    criticalillness = Column(Numeric(15, 2), nullable=True)
    personalaccident = Column(Numeric(15, 2), nullable=True)
    hospitalizationbenefits = Column(Numeric(15, 2), nullable=True)
    remarks = Column(Text, nullable=True)