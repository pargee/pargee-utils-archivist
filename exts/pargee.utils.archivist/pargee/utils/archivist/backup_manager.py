import threading
import omni.usd

from .utils import get_current_stage_dir, get_current_stage_path, get_current_file_name, zero_pad
from .settings import Settings


class BackupManager:
    def __init__(self):
        self._settings = Settings()
        self._backup_index = 0
        self._current_backup_thread = None
        self._backup_thread_stop_event = None

    def _backup(self, backup_index):
        # break out of save if the thread has canceled during a wait
        if self._backup_thread_stop_event.isSet():
            return
        base_path = self._get_base_path()
        path = self._get_path(base_path)

        # increment index to start with filename_01
        file_name = self._get_backup_file_name(backup_index + 1)
        file_type = self._settings.backup_file_type

        # prevent overwriting current backup file if open
        if get_current_file_name() != file_name:
            backup = path + "/" + file_name + file_type
            print(f"Auto backup starting at: {backup}")
            # don't try to backup a stage that's not in opened state
            if omni.usd.get_context().get_stage_state() == omni.usd.StageState.OPENED:
                try:
                    omni.usd.get_context().export_as_stage(backup)
                except Exception as e:
                    print(e)
            else:
                print("Stage is not OPENED")

    def _get_base_path(self):
        # save to shared backup path if enabled or user hasn't saved file
        if self._settings.shared_backups_enabled or not get_current_stage_path():
            return self._settings.shared_backups_path
        else:
            return get_current_stage_path()

    def _get_path(self, base_path):
        path = base_path
        if path.endswith("/"):
            path = path[:-1]

        # only create backup dir if user isnt in backup dir
        if self._settings.backup_dir and (get_current_stage_dir() != self._settings.backup_dir):
            path = path + "/" + self._settings.backup_dir
        return path

    def _get_backup_file_name(self, index):
        if get_current_file_name() and not self._settings.shared_backups_enabled:
            if get_current_file_name().startswith(self._settings.backup_prefix):
                # not perfect - turns backup_file_01 into backup_file_01_01...
                return get_current_file_name() + "_" + zero_pad(index)
            else:
                return self._settings.backup_prefix + get_current_file_name() + "_" + zero_pad(index)
        return self._settings.backup_prefix + zero_pad(index)

    def _backup_thread(self):
        while True:
            # basic functionality now - may want to check for existing files in future
            for backup_index in range(self._settings.backup_count):
                if self._backup_thread_stop_event.isSet():
                    return
                # sleep before every backup (@TODO convert mins -> seconds)
                self._backup_thread_stop_event.wait(self._settings.backup_frequency)
                self._backup(backup_index)

    def start_backup(self):
        print("starting backup!")
        self._backup_thread_stop_event = threading.Event()
        self._current_backup_thread = threading.Thread(target=self._backup_thread)
        self._current_backup_thread.start()

    def stop_backup(self):
        print("TERMINATING BG PROCESS!")
        if self._current_backup_thread is not None:
            print("BG PROCESS TERMINATED")
            self._backup_thread_stop_event.set()
            self._current_backup_thread.join()
