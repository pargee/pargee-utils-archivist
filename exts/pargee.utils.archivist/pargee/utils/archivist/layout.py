from enum import Enum
import omni.ui as ui
import omni.kit.menu.utils as mu
import omni.kit.window.filepicker as fp
from .settings import Settings
from .models import Models
from .utils import get_current_stage_path
from . import constants


class WidgetTypes(Enum):
    CHECKBOX_WIDGET = 1
    INT_WIDGET = 2
    STRING_WIDGET = 3
    FOLDER_WIDGET = 4


class Layout:
    def __init__(self):
        self._settings = Settings()
        self._models = Models()
        self._autobackup_button = None
        self._shared_backups_settings = None
        self._shared_backups_path = None
        self._file_picker = None
        self._last_backup_timestamp = None
        self._init_file_picker()

        # @TODO REPLACE THIS WITH REAL
        self.archivist_menu = [
            mu.MenuItemDescription(
                name=constants.TEXT_MENU_ITEM, appear_after="", sub_menu=None),
        ]

    def draw_layout(self):
        self._window = ui.Window(
            constants.TEXT_WINDOW_TITLE, width=constants.WINDOW_WIDTH, height=constants.WINDOW_HEIGHT_COLLAPSED
        )
        with self._window.frame:
            # @TODO REPLACE THIS WITH REAL menu
            mu.add_menu_items(self.archivist_menu, constants.TEXT_MENU_TITLE)

            with ui.VStack():
                self._draw_autobackup_button()
                # self._draw_last_backup()
                self._draw_settings_section()

    def disable_backup_manager(self):
        self._models.set_backup_manager(False)

    def _draw_autobackup_button(self):
        self._autobackup_button = ui.Button(
            "",
            height=constants.AUTOBACKUP_BUTTON_HEIGHT,
            tooltip=constants.TEXT_AUTOBACKUP_BUTTON_TOOLTIP,
            clicked_fn=self._toggle_autobackup,
        )
        self._set_autobackup_button_style()

    def _draw_last_backup(self):
        with ui.HStack(height=24):
            ui.Spacer()
            ui.Label("Last Save:", width=0, style={
                     "color": constants.LINE_COLOR})
            ui.Spacer(width=constants.INPUT_SPACING)
            self._last_backup_timestamp = ui.Label(
                "09/03/1986 2:00", width=0, style={"color": constants.LINE_COLOR})
            ui.Spacer(width=constants.PROP_SPACING)

    def _draw_settings_section(self):
        ui.Spacer(height=constants.SETTINGS_SPACING)
        with ui.CollapsableFrame(
            constants.TEXT_SETTINGS_SECTION,
            collapsed=True,
            collapsed_changed_fn=self._set_settings_section_style,
        ):
            with ui.VStack(height=0):
                self._draw_setting(
                    constants.TEXT_BACKUP_FREQUENCY,
                    constants.TEXT_BACKUP_FREQUENCY_TOOLTIP,
                    WidgetTypes.INT_WIDGET,
                    self._models.backup_frequency_model,
                )
                self._draw_setting(
                    constants.TEXT_BACKUP_COUNT,
                    constants.TEXT_BACKUP_COUNT_TOOLTIP,
                    WidgetTypes.INT_WIDGET,
                    self._models.backup_count_model,
                )
                self._draw_setting(
                    constants.TEXT_BACKUP_DIR,
                    constants.TEXT_BACKUP_DIR_TOOLTIP,
                    WidgetTypes.STRING_WIDGET,
                    self._models.backup_dir_model,
                )
                self._draw_setting(
                    constants.TEXT_BACKUP_PREFIX,
                    constants.TEXT_BACKUP_PREFIX_TOOLTIP,
                    WidgetTypes.STRING_WIDGET,
                    self._models.backup_prefix_model,
                )
                self._draw_setting(
                    constants.TEXT_SHARED_BACKUPS,
                    constants.TEXT_SHARED_BACKUPS_TOOLTIP,
                    WidgetTypes.CHECKBOX_WIDGET,
                    self._models.shared_backups_model,
                    model_callback=self._toggle_shared_backups_settings,
                )
                self._shared_backups_settings = self._draw_setting(
                    constants.TEXT_SHARED_BACKUPS_PATH_TITLE,
                    constants.TEXT_SHARED_BACKUPS_PATH_TOOLTIP,
                    WidgetTypes.FOLDER_WIDGET,
                    self._models.shared_backups_path_model,
                )
                self._shared_backups_settings.visible = self._settings.shared_backups_enabled

    def _draw_setting(self, label_text, label_tooltip, widget_type, widget_model, model_callback=None):
        if model_callback:
            widget_model.add_value_changed_fn(model_callback)

        setting = ui.HStack(height=constants.SETTINGS_ITEM_HEIGHT)
        with setting:
            ui.Spacer(width=constants.SETTINGS_INDENT_SPACING)
            if widget_type == WidgetTypes.FOLDER_WIDGET:
                self._shared_backups_path = ui.StringField(
                    widget_model, tooltip=label_tooltip, height=0)
                ui.Button(
                    f"{constants.GLYPH_CODE_FOLDER}",
                    tooltip=constants.TEXT_FOLDER_TOOLTIP,
                    clicked_fn=self._open_file_picker,
                    width=0,
                    height=0,
                )

            else:
                ui.Label(label_text, tooltip=label_tooltip, width=0)
                ui.Spacer(width=constants.PROP_SPACING)
                ui.Line(style={"color": constants.LINE_COLOR},
                        width=ui.Fraction(1))
                ui.Spacer(width=constants.PROP_SPACING)
                with ui.VStack(width=constants.PROP_SPACING):
                    if widget_type == WidgetTypes.CHECKBOX_WIDGET:
                        ui.Spacer()
                        ui.CheckBox(widget_model, height=0)
                        ui.Spacer()
                    elif widget_type == WidgetTypes.INT_WIDGET:
                        ui.Spacer()
                        ui.IntField(
                            widget_model, width=constants.INPUT_WIDTH, height=0)
                        ui.Spacer()
                    elif widget_type == WidgetTypes.STRING_WIDGET:
                        ui.Spacer()
                        ui.StringField(
                            widget_model, width=constants.TEXT_WIDTH, height=0)
                        ui.Spacer()
        return setting

    def _toggle_autobackup(self):
        # update model, then redraw button style
        self._models.toggle_autobackup()
        self._set_autobackup_button_style()

    def _toggle_shared_backups_settings(self, model):
        if model.get_value_as_bool():
            self._shared_backups_settings.visible = True
        else:
            self._shared_backups_settings.visible = False

    def _set_autobackup_button_style(self):
        if self._settings.autobackup_enabled:
            self._autobackup_button.text = constants.TEXT_AUTOBACKUP_BUTTON_ENABLED
            self._autobackup_button.style = {
                "background_color": constants.AUTOBACKUP_ENABLED_BUTTON_COLOR}
        else:
            self._autobackup_button.text = constants.TEXT_AUTOBACKUP_BUTTON_DISABLED
            self._autobackup_button.style = {
                "background_color": constants.AUTOBACKUP_DISABLED_BUTTON_COLOR}

    def _set_settings_section_style(self, collapsed):
        if not self._window.docked:
            if collapsed:
                self._window.height = constants.WINDOW_HEIGHT_COLLAPSED
            else:
                self._window.height = constants.WINDOW_HEIGHT_EXPANDED

    def _init_file_picker(self):
        self._file_picker = fp.FilePickerDialog(
            constants.TEXT_SHARED_BACKUPS_PATH_TITLE,
            apply_button_label=constants.TEXT_APPLY_BUTTON_LABEL,
            click_apply_handler=self._confirm_file_picker,
            click_cancel_handler=self._cancel_file_picker,
            enable_filename_input=False,
        )

        self._file_picker.set_filebar_label_name(constants.TEXT_FILEBAR_LABEL)
        self._file_picker.hide()

    def _open_file_picker(self):
        if self._settings.shared_backups_path != "":
            current_path = self._settings.shared_backups_path
        else:
            current_path = get_current_stage_path()
        self._file_picker.set_current_directory(current_path)
        self._file_picker.navigate_to(current_path)
        self._file_picker.show()

    def _confirm_file_picker(self, file_name, path):
        self._shared_backups_path.model.set_value(path)
        self._settings.shared_backups_path = path
        self._file_picker.hide()

    def _cancel_file_picker(self, file_name, path):
        self._file_picker.hide()
