from flask import Blueprint
staff = Blueprint('staff',__name__, template_folder='templates')
from . import views