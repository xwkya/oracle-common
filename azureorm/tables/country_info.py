from sqlalchemy import Column, String, Float, SmallInteger

from ..BaseTable import BaseTable


class CountryInfo(BaseTable):
    __tablename__ = "CountryInfo"

    CountryISO3 = Column(String(3), primary_key=True, nullable=False)
    Year = Column(SmallInteger, primary_key=True, nullable=False)
    CountryName = Column(String(100), nullable=True)
    GdpBillionUSD = Column(Float, nullable=True)
    Population = Column(Float, nullable=True)
