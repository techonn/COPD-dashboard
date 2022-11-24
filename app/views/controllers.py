"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""

from flask import Blueprint, render_template, request
from markdown import markdown
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = [r[0] for r in db_mod.get_distinct_pcts()]
    if request.method == 'POST':
        # if selecting BNF code for table, update based on user choice
        form = request.form
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
        GP_bar_data = generate_GP_barchart_data(str(form['pct-option']))
    else:
        # pick a default BNF code to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)
        GP_bar_data = generate_GP_barchart_data(str(pcts[0]))
    selected_bnf_data = db_mod.get_n_data_for_bnf_code()
    bnfcodename = [(r, s) for r, s, *t in selected_bnf_data]

    # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]
    title_data_items = generate_data_for_tiles()
    mkd_text= generate_about_data()
    Infection = generate_data_for_infection()
    Infection_name = [x for x,y in Infection]
    Infection_percentage = ["{:.2f}".format(y*100) for x,y in Infection]
    GP_bar_values = GP_bar_data[0]
    GP_bar_labels = GP_bar_data[1]

    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html', tile_data=title_data_items,
                           pct={'data': bar_values, 'labels': bar_labels},
                           gp_bar={'data': GP_bar_values, 'labels': GP_bar_labels},
                           pct_list=pcts, pct_data=selected_pct_data,
                           bnf_list=bnfcodename, bnf_data=selected_bnf_data,
                           Infection_name=Infection_name, Infection_percentage=Infection_percentage,
                           mkd_text=mkd_text)

def generate_data_for_tiles(pct=None, n=None):
    """Generate the data for the four home page titles."""
    return [db_mod.get_total_number_items(), "{:.3f}".format ( db_mod.get_average_ACT()), db_mod.get_top_prescribed_item(), db_mod.get_percentage_of_top_item(),db_mod.get_unique_number_of_items()]


def generate_barchart_data():
    """Generate the data needed to populate the barchart."""
    data_values = db_mod.get_prescribed_items_per_pct()
    pct_codes = db_mod.get_distinct_pcts()


    # convert into lists and return
    data_values = [r[0] for r in data_values]
    pct_codes = [r[0] for r in pct_codes]
    return [data_values, pct_codes]

def generate_GP_barchart_data(pct):
    """Generate the data needed to populate the barchart."""
    data_value = db_mod.get_total_prescribed_antibiotics_per_GP(pct)
    practice_code_name = db_mod.get_practice_code_name()

    # convert into lists and return
    practice_dict = {practicecode: practicename for practicecode,practicename in practice_code_name }
    data = [itemsum for practice_code,itemsum in data_value]
    label = [practice_dict[practice_code] for practice_code,itemsum in data_value]
    return [data, label]

def generate_about_data():
    """Read Readme.md for about data"""
    input_file = open("Readme.MD", mode="r", encoding="utf-8")
    text = input_file.read()
    return markdown(text)

def generate_data_for_infection():
    """genereate percentage for infection drug group"""
    return db_mod.get_percentage_of_inf_drug_gr()