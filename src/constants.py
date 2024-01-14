from pathlib import Path

MAIN_DOC_URL = 'https://docs.python.org/3/'
PEP_DOC_URL = 'https://peps.python.org/'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DT_LOG_FORMAT = '%d.%m.%Y %H:%M:%S'

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

PATTERN = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / 'logs'
REULTS_DIR = 'results'
DOWNLOADS_DIR = 'downloads'

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}

PRETTY = 'pretty'
FILE = 'file'
DEFAULT = None
