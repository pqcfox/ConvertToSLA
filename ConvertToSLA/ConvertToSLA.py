import re

from UM.Application import Application
from UM.Extension import Extension
from UM.Logger import Logger

class ConvertToSLA(Extension):
    RULES = []

    def __init__(self):
        super().__init__()
        Application.getInstance().getOutputDeviceManager().writeStarted.connect(self._convert)

    def _convert(self, output_device):
        scene = Application.getInstance().getController().getScene()
        if hasattr(scene, 'gcode_list'):
            gcode_list = getattr(scene, 'gcode_list')
            if gcode_list:
                if ';SLA' not in gcode_list[0]:
                    sla_gcode_list = self._convert_list(gcode_list)
                    setattr(scene, 'gcode_list', sla_gcode_list) 
                Logger.log('e', 'GCODE already in SLA format')

    def _convert_list(gcode_list):
        for rule in RULES:
            try:
                gcode_list = rule(gcode_list)
            except Exeption as e:
                Logger.log('e', 'A rule raised the exception {}'.format(str(e)))
        return gcode_list
