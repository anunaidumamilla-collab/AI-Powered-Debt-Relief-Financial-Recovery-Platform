from pydantic import BaseModel


class LoanCreate(BaseModel):

    borrower_name: str

    lender_name: str

    loan_amount: float

    monthly_income: float

    emi: float

    overdue_months: int


class LoanResponse(LoanCreate):

    id: int

    recommendation: str

    class Config:

        from_attributes = True