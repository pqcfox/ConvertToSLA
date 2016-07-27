from . import ConvertToSLA

from UM.i18n import i18nCatalog
catalog = i18nCatalog('cura')

def getMetaData():
    return {
        'plugin': {
            'name': catalog.i18nc('@label', 'Convert To SLA')
            'author': 'pHeX Labs'
            'version': '1.0',
            'description': catalog.i18nc('@info:whatsthis', 'Automatically converts FDM GCODE to SLA GCODE.')
            'api': 3
        }
    }

def register(app):
    return {'extension': ConvertToSLA.ConvertToSLA()}
