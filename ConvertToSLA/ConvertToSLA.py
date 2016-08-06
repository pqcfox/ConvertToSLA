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
        gcode = ''.join(gcode_list)  # newlines already there 
        for pattern, repl in RULES:
            try:
                gcode = re.sub(pattern, repl, gcode)
            except Exeption as e:
                Logger.log('e', 'A rule raised the exception {}'.format(str(e)))

        new_gcode_list = [line + '\n' for line in gcode.split('\n')]
        return gcode_list
