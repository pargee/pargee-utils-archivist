import omni.ext

from .backup_manager import BackupManager
from .layout import Layout


class AutoBackup(omni.ext.IExt):
    def __init__(self):
        super().__init__()
        self._layout = Layout()

    def on_startup(self, ext_id):
        self._layout.draw_layout()

    def on_shutdown(self):
        self._layout.disable_backup_manager()
