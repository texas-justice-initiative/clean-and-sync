import settings
from utils.census import Census
from utils.datadotworld import Datadotworld
from utils.gmaps import Gmaps
from utils.gsheets import Gsheets


def handle(event, context):
    # TODO (1) prep the data.world datasets (2) update the appropriate fields below
    # dw_cdr = Datadotworld(settings=settings.DATADOTWORLD, dataset='tji/cdr-dataset-slug')
    # dw_ois = Datadotworld(settings=settings.DATADOTWORLD, dataset='tji/ois-dataset-slug')
    #
    # gmaps = Gmaps(settings=settings.GMAPS)
    #
    # gsheets_cdr = Gsheets(settings=settings.GSHEETS, sheetid='sheetid_here')
    # gsheets_ois = Gsheets(settings=settings.GSHEETS, sheetid='sheetid_here')
    #
    # # Geocodes the incident locations and syncs the data.world datasets
    # # CDR spreadsheet
    # rows = gsheets_cdr.fetch(sheet_range='range_here')
    # for i, row in enumerate(rows):
    #     incident_address = f'{row[5]}, {row[6]}, {row[7]}'  # TODO use the correct values
    #
    #     # Geocode if there's an address and it hasn't already been done
    #     if row[5] and not row[8] and not row[9]:  # TODO use the correct values
    #         lat, lng = gmaps.geocode(incident_address)
    #         if lat and lng:
    #             tracts = Census.reverse_geocode(lat, lng)
    #             gsheets_cdr.update(f'range_here', [[lat, lng, tracts]])
    #
    # dw_cdr.sync()
    #
    # # OIS spreadsheet
    # rows = gsheets_ois.fetch(sheet_range='range_here')
    # for i, row in enumerate(rows):
    #     incident_address = f'{row[5]}, {row[6]}, {row[7]}'  # TODO use the correct values
    #
    #     # Geocode if there's an address and it hasn't already been done
    #     if row[5] and not row[8] and not row[9]:  # TODO use the correct values
    #         lat, lng = gmaps.geocode(incident_address)
    #         if lat and lng:
    #             tracts = Census.reverse_geocode(lat, lng)
    #             gsheets_ois.update(f'range_here', [[lat, lng, tracts]])
    #
    # dw_ois.sync()

    print('Done!')
