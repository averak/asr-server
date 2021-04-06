import numpy as np
import librosa
import sklearn.preprocessing
import pyroomacoustics as pra
import scipy.io.wavfile as wf
from scipy import signal
from pydub import AudioSegment
from pydub.silence import split_on_silence

from core import config


# convert wave to MFCC
def extract_feature(file_name: str, cleaning: bool = True) -> np.ndarray:
    # read wav file
    wav: np.ndarray = wf.read(file_name)[1]
    wav = wav.astype(np.float32)
    # cleaning wave
    if cleaning:
        wav = noise_reduction(wav)
        wav = voice_activity(wav)
    # convert to MFCC
    result: np.ndarray = librosa.feature.mfcc(
        wav,
        sr=config.WAVE_RATE,
        n_mfcc=config.MFCC_DIM
    )
    result = np.reshape(result, (*result.shape, 1))

    return result


# normalize to 0~1
def normalize(feature: np.ndarray) -> np.ndarray:
    result: np.ndarray = feature.flatten()
    result_shape: tuple = feature.shape

    result = sklearn.preprocessing.minmax_scale(result)
    result = np.reshape(result, result_shape)

    return result


# band-pass filter
def filtering(feature: np.ndarray) -> np.ndarray:
    n_sample: int = len(feature)
    delte = (config.WAVE_RATE / 2) / n_sample
    bpf: np.ndarray = np.zeros(n_sample)

    for i in range(n_sample):
        freq: float = i * delte
        if freq > config.BPF_LOW_FREQ and freq < config.BPF_HIGH_FREQ:
            bpf[i] = 1

    return feature * bpf


# resample feature
def resample(feature: np.ndarray) -> np.ndarray:
    result: np.ndarray = signal.resample(
        feature.T,
        config.MFCC_SAMPLES,
        axis=1,
    )
    result = result.T
    return result


# spectral subtraction
def noise_reduction(feature: np.ndarray) -> np.ndarray:
    result: np.ndarray = pra.denoise.spectral_subtraction.apply_spectral_sub(
        feature, config.FFT_LENGTH)
    return result


# extract only voice activity
def voice_activity(feature: str) -> np.ndarray:
    sound: AudioSegment = AudioSegment(
        data=bytes(feature.astype(np.int16)),
        sample_width=config.WAVE_WIDTH,
        frame_rate=config.WAVE_RATE,
        channels=config.WAVE_CHANNELS
    )

    # extract only voice activity
    chunks: list = split_on_silence(
        sound,
        min_silence_len=config.MIN_SILENCE_LENGTH,
        silence_thresh=config.SILENCE_THRESH,
        keep_silence=config.KEEP_SILENCE,
    )

    # select the highest volume
    result: np.ndarray = feature
    max_volume: int = 0
    for chunk in chunks:
        chunk_wav: list = chunk.get_array_of_samples()
        chunk_volume: int = sum(np.abs(chunk_wav))

        if chunk_volume > max_volume:
            result = np.array(chunk_wav)
            max_volume = chunk_volume

    result = result.astype(np.float32)
    return result
