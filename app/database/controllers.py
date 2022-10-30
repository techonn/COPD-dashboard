"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()
    
    def get_average_ACT(self):
        """Return Average ACT cost """
        return db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0]

    def get_number_of_top_BNF_item(self):
        """Return the top quantity of prescribed item among BNF codes."""
        return db.session.query(func.sum(PrescribingData.items)).\
            group_by(PrescribingData.BNF_code).\
            order_by(func.sum(PrescribingData.items).desc()).first()[0]

    def get_percentage_of_top_item(self):
        percentage = self.get_number_of_top_BNF_item()/self.get_total_number_items()
        return round(float(percentage)*100, 2)
    
    def get_unique_number_of_items(self):
        """Return the number of unique items."""
        return (db.session.query(PrescribingData.BNF_code).distinct().count())
