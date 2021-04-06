# path config
DATA_ROOT_PATH: str = './data'
TEACHER_ROOT_PATH: str = DATA_ROOT_PATH + '/teacher'
TEACHER_X_PATH: str = TEACHER_ROOT_PATH + '/x.npy'
TEACHER_Y_PATH: str = TEACHER_ROOT_PATH + '/y.npy'
RECORD_ROOT_PATH: str = DATA_ROOT_PATH + '/record'
SPEECH_ROOT_PATH: str = RECORD_ROOT_PATH + '/speech'
NOISE_ROOT_PATH: str = RECORD_ROOT_PATH + '/noise'
MODEL_ROOT_PATH: str = './ckpt'
MODEL_PATH: str = MODEL_ROOT_PATH + '/final.h5'
RECORD_WAV_PATH: str = DATA_ROOT_PATH + '/record.wav'
UPLOAD_WAV_PATH: str = DATA_ROOT_PATH + '/upload.wav'

# wave config
WAVE_RATE: int = 16000
WAVE_WIDTH: int = 2
WAVE_CHANNELS: int = 1
WAVE_CHUNK: int = 1024
WAVE_DEFECT_SEC: float = 0.4
WAVE_AMP_SAMPLES: int = 6

# wave preprocessing config
BPF_LOW_FREQ: int = 100
BPF_HIGH_FREQ: int = 8000
FFT_LENGTH: int = 512
MIN_SILENCE_LENGTH: int = 100
SILENCE_THRESH: int = -20
KEEP_SILENCE: int = 100

# mfcc config
MFCC_DIM: int = 12
MFCC_SAMPLES: int = 64
INPUT_SHAPE: tuple = (MFCC_DIM, MFCC_SAMPLES, 1)

# training config
EPOCHS: int = 3
BATCH_SIZE: int = 32
VALIDATION_SPLIT: float = 0.1
DROPOUT_RATE: float = 0.5
OPTIMIZER: str = 'adam'
LOSS: str = 'sparse_categorical_crossentropy'
METRICS: list = ['accuracy']

# class config
CLASSES: tuple = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
N_CLASSES: int = len(CLASSES)

# api config
API_SUCCESS_STATUS: str = 'OK'
API_ERROR_STATUS: str = 'NG'
API_SUCCESS_MSG: str = 'success'
API_RESPONSE: dict = {'status': API_SUCCESS_STATUS, 'message': API_SUCCESS_MSG}
API_PORT: int = 3000
API_URI: str = f'http://0.0.0.0:{API_PORT}/predict/'
