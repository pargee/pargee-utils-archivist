import omni.kit.ui as ui

# extension package
PACKAGE = "pargee.utils.archivist"


GLYPH_CODE_FOLDER = ui.get_custom_glyph_code("${glyphs}/folder.svg")

# layout props
WINDOW_WIDTH = 400
WINDOW_HEIGHT_COLLAPSED = 124
WINDOW_HEIGHT_EXPANDED = 296
INPUT_WIDTH = 32
INPUT_HEIGHT = 24
TEXT_WIDTH = 128
INPUT_SPACING = 16
PROP_SPACING = 8
SETTINGS_SPACING = 4
SETTINGS_INDENT_SPACING = 24
AUTOBACKUP_BUTTON_HEIGHT = 64
LINE_COLOR = 0x338A8777
SETTINGS_ITEM_HEIGHT = 28
AUTOBACKUP_ENABLED_BUTTON_COLOR = 0xFF76A371
AUTOBACKUP_DISABLED_BUTTON_COLOR = 0xFF5555AA

# strings
TEXT_WINDOW_TITLE = "Archivist"
TEXT_MENU_TITLE = "Archivist"
TEXT_MENU_ITEM = "Open Archivist - NOT WORKING"


TEXT_AUTOBACKUP_BUTTON_ENABLED = "Auto Backup Enabled"
TEXT_AUTOBACKUP_BUTTON_DISABLED = "Auto Backup Disabled"
TEXT_AUTOBACKUP_BUTTON_TOOLTIP = "Click to toggle AutoBackup on/off"

TEXT_SETTINGS_SECTION = "Settings"

TEXT_SHARED_BACKUPS = "Shared Backups"
TEXT_SHARED_BACKUPS_TOOLTIP = """Consolidate backups to a single set of files to save disk space.
    Default location is within the 'backups' directory of your save file."""
TEXT_SHARED_BACKUPS_PATH_TOOLTIP = "Path of shared backups"
TEXT_FOLDER_TOOLTIP = "Browse"

TEXT_BACKUP_COUNT = "Max Backups"
TEXT_BACKUP_COUNT_TOOLTIP = "Maximum number of backups to save (min: 1, max: 99)"

TEXT_BACKUP_FREQUENCY = "Backup Frequency (minutes)"
TEXT_BACKUP_FREQUENCY_TOOLTIP = "Time between each backup (min: 1, max: 60)"

TEXT_BACKUP_DIR = "Backups Directory"
TEXT_BACKUP_DIR_TOOLTIP = "Sub-directory to save backups to (leave blank for current)"

TEXT_BACKUP_PREFIX = "Backup Prefix"
TEXT_BACKUP_PREFIX_TOOLTIP = "File prefix for all backups"

TEXT_LAST_BACKUP = "Last Backup"
TEXT_LAST_BACKUP_TOOLTIP = "Name / time of last backup"
TEXT_LAST_BACKUP_DEFAULT = ""

TEXT_SHARED_BACKUPS_PATH_TITLE = "Select Shared Backup Path"
TEXT_FILEBAR_LABEL = "Folder"
TEXT_APPLY_BUTTON_LABEL = "Select"

# backup limits
BACKUP_COUNT_LOWER_LIMIT = 1
BACKUP_COUNT_UPPER_LIMIT = 99

# backup freq limits
BACKUP_FREQUENCY_LOWER_LIMIT = 1
BACKUP_FREQUENCY_UPPER_LIMIT = 60

# defaults for settings
DEFAULT_BACKUP_DIR = "backups"
DEFAULT_BACKUP_PREFIX = "backup_"
DEFAULT_BACKUP_FILE_TYPE = ".usd"
DEFAULT_BACKUP_COUNT = 10
DEFAULT_BACKUP_FREQUENCY = 5
DEFAULT_SHARED_BACKUPS_PATH = "omniverse://localhost/"

# settings keys
AUTOBACKUP_ENABLED_KEY = "autobackup_enabled"
SHARED_BACKUPS_ENABLED_KEY = "shared_backups_enabled"
BACKUP_DIR_KEY = "backup_dir"
BACKUP_PREFIX_KEY = "backup_prefix"
BACKUP_FREQUENCY_KEY = "backup_frequency"
BACKUP_COUNT_KEY = "backup_count"
SHARED_BACKUPS_PATH_KEY = "shared_backups_path"
BACKUP_FILE_TYPE_KEY = "backup_file_type"
