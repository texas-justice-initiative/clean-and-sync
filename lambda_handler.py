from utils.datadotworld import Datadotworld
from utils.gmaps import Gmaps
from utils.gsheets import Gsheets
import settings


def handle(event, context):
    dw = Datadotworld(settings=settings.DATADOTWORLD)
    gmaps = Gmaps(settings=settings.GMAPS)
    gsheets = Gsheets(settings=settings.GSHEETS)

    print('Done!')
