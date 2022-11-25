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
from sqlalchemy import desc

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

    def get_total_prescribed_antibiotics_per_GP(self, pct):
        """Return the total items per GP."""
        return db.session.query(PrescribingData.practice, func.sum(PrescribingData.items).label('GP_item_sum')).filter(PrescribingData.PCT == pct, func.substr(PrescribingData.BNF_code,1,4) == "0501").group_by(PrescribingData.practice).all()

    def get_practice_code_name(self):
        return db.session.query(PracticeData.practice_code, PracticeData.practice_name).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_distinct_bnf(self):
        """Return the distinct BNF codes/name."""
        return db.session.query(PrescribingData.BNF_code, PrescribingData.BNF_name).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def get_n_data_for_BNF(self):
        """Return all the data for a given BNF Code/Name."""
        return db.session.query(PrescribingData.BNF_code.label("BNF_code"),
                                PrescribingData.BNF_name.label("BNF_name"),
                                func.count(PrescribingData.practice).label("BNF_total_practice"),
                                func.sum(PrescribingData.items).label("BNF_total_item"),
                                (func.sum(PrescribingData.ACT_cost * PrescribingData.items) / func.sum(PrescribingData.items)).label("BNF_average_cost")).group_by(PrescribingData.BNF_code).all()

    def get_average_ACT(self):
        """Return Average ACT cost """
        return db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0]

    def get_number_of_top_BNF_item(self):
        """Return the top quantity of prescribed item among BNF codes."""
        return db.session.query(func.sum(PrescribingData.items)).\
            group_by(PrescribingData.BNF_code).\
            order_by(func.sum(PrescribingData.items).desc()).first()[0]

    def get_top_prescribed_item(self):
        """ Return top prescribed drug."""
        return db.session.query(PrescribingData).group_by(PrescribingData.BNF_name).order_by(desc(PrescribingData.items)).first().BNF_name

    def get_percentage_of_top_item(self):
        percentage = self.get_number_of_top_BNF_item()/self.get_total_number_items()
        return round(float(percentage)*100, 2)
    
    def get_unique_number_of_items(self):
        """Return the number of unique items."""
        return (db.session.query(PrescribingData.BNF_code).distinct().count())
    
    def get_percentage_of_inf_drug_gr(self):
        drug4 = {'Antibacterial':['0501'],
                 'Antifungal':['0502'],
                 'Antiviral':['0503'],
                 'Antiprotozoal':['0504'],
                 'Anthelmintics':['0505']}
        drug6 = {'Antibacterial':['131001', '110301'],
                 'Antifungal':['131002', '110302'],
                 'Antiviral':['131003', '110303'],
                 'Antiprotozoal':[],
                 'Anthelmintics':[]}
        data = db.session.query(PrescribingData.BNF_code, func.sum(PrescribingData.items)).group_by(PrescribingData.BNF_code).all()
        num_drug = []
        for drug_name in ['Antibacterial', 'Antifungal', 'Antiviral','Antiprotozoal','Anthelmintics']:
            num_drug.append((drug_name,sum([y if x[0:4] in drug4[drug_name] or x[0:6] in drug6[drug_name] else 0 for x,y,*z in data])))
        total_drug = sum([y for x,y in num_drug])
        return [(x,y*1.0/total_drug) for x,y in num_drug]
