from sqlalchemy import Column, Integer, String, Float

from database import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)

    borrower_name = Column(String)

    lender_name = Column(String)

    loan_amount = Column(Float)

    monthly_income = Column(Float)

    emi = Column(Float)

    overdue_months = Column(Integer)

    recommendation = Column(String)