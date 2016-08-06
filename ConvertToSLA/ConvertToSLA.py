from UM.Application import Application
from UM.Extension import Extension

class ConvertToSLA(Extension):
    def __init__(self):
        super().__init__()
        Application.getInstance().getOutputDeviceManager().writeStarted.connect(self._convert)

    def _convert(self, output_device):
        scene = Application.getInstance().getController().getScene()
        if hasattr(scene, 'gcode_list'):
            gcode_list = getattr(scene, 'gcode_list')
            print(gcode_list)
