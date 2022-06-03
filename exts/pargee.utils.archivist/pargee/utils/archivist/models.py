from enum import Enum
import omni.ui as ui
from .settings import Settings
from .backup_manager import BackupManager

from . import constants


class ModelTypes(Enum):
    INT_MODEL = 1
    BOOL_MODEL = 2
    STRING_MODEL = 3


class Models:
    def __init__(self):
        self._settings = Settings()
        self._backup_manager = BackupManager()
        self.autobackup_enabled_model = ui.SimpleBoolModel(self._settings.autobackup_enabled)
        self.backup_count_model = ui.SimpleIntModel(
            self._settings.backup_count, min=constants.BACKUP_COUNT_LOWER_LIMIT, max=constants.BACKUP_COUNT_UPPER_LIMIT
        )
        self.backup_frequency_model = ui.SimpleIntModel(
            self._settings.backup_frequency,
            min=constants.BACKUP_FREQUENCY_LOWER_LIMIT,
            max=constants.BACKUP_FREQUENCY_UPPER_LIMIT,
        )
        self.shared_backups_model = ui.SimpleBoolModel(self._settings.shared_backups_enabled)
        self.shared_backups_path_model = ui.SimpleStringModel(self._settings.shared_backups_path)
        self.backup_dir_model = ui.SimpleStringModel(self._settings.backup_dir)
        self.backup_prefix_model = ui.SimpleStringModel(self._settings.backup_prefix)
        # self.default_extension = ui.SimpleStringModel()
        self._register_model_handlers()

    def toggle_autobackup(self):
        # no better place to put this right now, may need to rethink
        self._settings.autobackup_enabled = not self._settings.autobackup_enabled
        if self._settings.autobackup_enabled:
            self._backup_manager.start_backup()
        else:
            self._backup_manager.stop_backup()

    def set_backup_manager(self, enabled):
        # only used for disabling extension when autobackup is active
        if enabled:
            self._backup_manager.start_backup()
        else:
            self._backup_manager.stop_backup()

    def _register_model_handlers(self):
        # base model handlers for updating persistent settings
        # additional callbacks can be added elsewhere (e.g., layout updates)
        self.backup_count_model.add_end_edit_fn(
            lambda model: self._update_model(model, ModelTypes.INT_MODEL, constants.BACKUP_COUNT_KEY)
        )
        self.backup_frequency_model.add_end_edit_fn(
            lambda model: self._update_model(model, ModelTypes.INT_MODEL, constants.BACKUP_FREQUENCY_KEY)
        )
        self.shared_backups_model.add_value_changed_fn(
            lambda model: self._update_model(model, ModelTypes.BOOL_MODEL, constants.SHARED_BACKUPS_ENABLED_KEY)
        )
        self.shared_backups_path_model.add_end_edit_fn(
            lambda model: self._update_model(model, ModelTypes.STRING_MODEL, constants.SHARED_BACKUPS_PATH_KEY)
        )
        self.backup_dir_model.add_end_edit_fn(
            lambda model: self._update_model(model, ModelTypes.STRING_MODEL, constants.BACKUP_DIR_KEY)
        )
        self.backup_prefix_model.add_end_edit_fn(
            lambda model: self._update_model(model, ModelTypes.STRING_MODEL, constants.BACKUP_PREFIX_KEY)
        )

    def _update_model(self, model, model_type, key, callback=None):
        if model_type == ModelTypes.INT_MODEL:
            self._settings.set_value(key, model.get_value_as_int())
        elif model_type == ModelTypes.BOOL_MODEL:
            self._settings.set_value(key, model.get_value_as_bool())
        elif model_type == ModelTypes.STRING_MODEL:
            self._settings.set_value(key, model.get_value_as_string())
        if callback:
            callback()
