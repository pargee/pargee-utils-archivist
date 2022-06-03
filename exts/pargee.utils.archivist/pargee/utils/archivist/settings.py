import carb.settings
from . import constants


class Settings:
    def __init__(self):
        self._settings = carb.settings.get_settings()
        self._settings_path = "/persistent/" + constants.PACKAGE + "/"

        self._set_default_bool(constants.AUTOBACKUP_ENABLED_KEY, False)
        self._set_default_bool(constants.SHARED_BACKUPS_ENABLED_KEY, False)

        self._set_default_int(constants.BACKUP_COUNT_KEY, constants.DEFAULT_BACKUP_COUNT)
        self._set_default_int(constants.BACKUP_FREQUENCY_KEY, constants.DEFAULT_BACKUP_FREQUENCY)

        self._set_default_string(constants.SHARED_BACKUPS_PATH_KEY, constants.DEFAULT_SHARED_BACKUPS_PATH)
        self._set_default_string(constants.BACKUP_DIR_KEY, constants.DEFAULT_BACKUP_DIR)
        self._set_default_string(constants.BACKUP_PREFIX_KEY, constants.DEFAULT_BACKUP_PREFIX)
        self._set_default_string(constants.BACKUP_FILE_TYPE_KEY, constants.DEFAULT_BACKUP_FILE_TYPE)

    def _set_default_bool(self, key, value):
        self._settings.set_default_bool(self._settings_path + key, value)

    def _set_default_string(self, key, value):
        self._settings.set_default_string(self._settings_path + key, value)

    def _set_default_int(self, key, value):
        self._settings.set_default_int(self._settings_path + key, value)

    def _get_path(self, key):
        return self._settings_path + key

    def set_value(self, key, value):
        self._settings.set(self._get_path(key), value)

    @property
    def autobackup_enabled(self):
        return self._settings.get(self._get_path(constants.AUTOBACKUP_ENABLED_KEY))

    @autobackup_enabled.setter
    def autobackup_enabled(self, value):
        self.set_value(constants.AUTOBACKUP_ENABLED_KEY, value)

    @property
    def shared_backups_enabled(self):
        return self._settings.get(self._get_path(constants.SHARED_BACKUPS_ENABLED_KEY))

    @shared_backups_enabled.setter
    def shared_backups_enabled(self, value):
        self.set_value(constants.SHARED_BACKUPS_ENABLED_KEY, value)

    @property
    def backup_count(self):
        return self._settings.get(self._get_path(constants.BACKUP_COUNT_KEY))

    @backup_count.setter
    def backup_count(self, value):
        self.set_value(constants.BACKUP_COUNT_KEY, value)

    @property
    def backup_frequency(self):
        return self._settings.get(self._get_path(constants.BACKUP_FREQUENCY_KEY))

    @backup_frequency.setter
    def backup_frequency(self, value):
        self.set_value(constants.BACKUP_FREQUENCY_KEY, value)

    @property
    def shared_backups_path(self):
        return self._settings.get(self._get_path(constants.SHARED_BACKUPS_PATH_KEY))

    @shared_backups_path.setter
    def shared_backups_path(self, value):
        self.set_value(constants.SHARED_BACKUPS_PATH_KEY, value)

    @property
    def backup_dir(self):
        return self._settings.get(self._get_path(constants.BACKUP_DIR_KEY))

    @backup_dir.setter
    def backup_dir(self, value):
        self.set_value(constants.BACKUP_DIR_KEY, value)

    @property
    def backup_prefix(self):
        return self._settings.get(self._get_path(constants.BACKUP_PREFIX_KEY))

    @backup_prefix.setter
    def backup_prefix(self, value):
        self.set_value(constants.BACKUP_PREFIX_KEY, value)

    @property
    def backup_file_type(self):
        return self._settings.get(self._get_path(constants.BACKUP_FILE_TYPE_KEY))

    @backup_file_type.setter
    def backup_file_type(self, value):
        self.set_value(constants.BACKUP_FILE_TYPE_KEY, value)
