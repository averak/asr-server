class FontColors:
    RED: str = '\033[31m'
    GREEN: str = '\033[32m'
    YELLOW: str = '\033[33m'
    RESET: str = '\033[0m'


ERROR_INVALID_SOURCE_NAME: str = FontColors.RED + \
    'Cannot record such source name. Try again.' + FontColors.RESET

ERROR_ASR_SERVER_NOT_STARTED: str = FontColors.RED + \
    'ASR-server is not started.' + FontColors.RESET

RECORDING_HELP_MSG: str = 'Press enter to start recording.' + \
    '\n' + \
    'Enter the <q> key to quit.'


def CREATED_FILE_MSG(file_name: str) -> str:
    result: str = 'Created ' + FontColors.YELLOW + file_name + FontColors.RESET
    return result


def DELETE_FILE_MSG(file_name: str) -> str:
    result: str = 'Deleted ' + FontColors.YELLOW + file_name + FontColors.RESET
    return result


def CREATED_DATA_MSG(n_data: int) -> str:
    result: str = 'Created %d data' % n_data
    return result


def RECORDING_VOICE_MSG(index: int) -> str:
    result: str = 'Recording %d...' % index
    return result


def PROCESSING_SOURCE_MSG(source_str: str) -> str:
    result: str = 'Processing <%s> class data...' % source_str
    return result


def ACCURACY_MSG(accuracy: float) -> str:
    result: str = 'Accuracy: %3.1f%%' % (accuracy * 100)
    return result


def PREDICT_CLASS_MSG(class_name: str) -> str:
    result: str = 'Predict: %s' % class_name
    return result


def SOURCE_INPUT_GUIDE(default_source_str: str) -> str:
    result: str = 'which source type? ' + \
        FontColors.GREEN + \
        default_source_str + \
        ' (1-9 or noise)' + \
        FontColors.RESET + \
        ' : '
    return result
