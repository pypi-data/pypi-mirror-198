from __future__ import absolute_import, unicode_literals
import collections
import scipy.fftpack
import scipy.signal
import scipy.stats
import logging
import sys
import threading
import numpy as np
from functools import partial
from multiprocessing import cpu_count
from multiprocessing import Pool
import os

"""phm 设备故障与寿命分析
提取振动信号中的基础，时频域特征，用于phm用途
"""

__version__ = '0.1.0'
__license__ = 'MIT'
__name__ = 'phm_feature'

_get_abs_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), path))

log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)

def setLogLevel(log_level):
    default_logger.setLevel(log_level)

class Tokenizer(object):

    def __init__(self, name=__name__):
        """ __init__
        """
        # self.lock = threading.RLock()
        self.name = __name__
        #self.time_feature_name = ["mean","max","min","std","median","p2p","rms","arv","kurtosis","skewness","pulse_factor","margin_factor","form_factor"]

    def init_result(self):
        '''初始化返回数据格式
        '''
        return collections.defaultdict(lambda:{})

    def rebuild_time_result(self, dic):
        ict = collections.defaultdict(lambda:[])
        for key in dic:
            if key == "mean":
                ict["result"].append({"key":key, "value":dic[key], "description":"均值"})
            elif key == "max":
                ict["result"].append({"key":key, "value":dic[key], "description":"最大值"})
            elif key == "min":
                ict["result"].append({"key":key, "value":dic[key], "description":"最小值"})
            elif key == "std":
                ict["result"].append({"key":key, "value":dic[key], "description":"方差"})
            elif key == "median":
                ict["result"].append({"key":key, "value":dic[key], "description":"中值"})
            elif key == "p2p":
                ict["result"].append({"key":key, "value":dic[key], "description":"峰峰值"})
            elif key == "rms":
                ict["result"].append({"key":key, "value":dic[key], "description":"有效值"})
            elif key == "ma":
                ict["result"].append({"key":key, "value":dic[key], "description":"绝对值均值"})
            elif key == "msa":
                ict["result"].append({"key":key, "value":dic[key], "description":"方根幅值"})
            elif key == "pulse_factor":
                ict["result"].append({"key":key, "value":dic[key], "description":"脉冲因子"})
            elif key == "margin_factor":
                ict["result"].append({"key":key, "value":dic[key], "description":"裕度因子"})
            elif key == "form_factor":
                ict["result"].append({"key":key, "value":dic[key], "description":"波形因子"})
            elif key == "kurtosis":
                ict["result"].append({"key":key, "value":dic[key], "description":"峭度"})
            elif key == "skewness":
                ict["result"].append({"key":key, "value":dic[key], "description":"偏斜度"})
        print(dict(ict))
        return dict(ict)

    def __repr__(self):
        return 'Tokenizer of vibration-wave {}'.format(self.name)

    def feature_t(self, s):
        '''提取时间域特征
        '''
        print("串行提取时域特征")
        dct = self.init_result()

        _mean = np.mean(s, axis=-1)
        dct["mean"] = _mean.tolist()

        _max = np.max(s, axis=-1)
        dct["max"] = _max.tolist()

        _min = np.min(s, axis=-1)
        dct["min"] = _min.tolist()

        _std = np.std(s, axis=-1)
        dct["std"] = _std.tolist()

        _median = np.median(s, axis=-1)
        dct["median"] = _median.tolist()

        _p2p = _max - _min
        dct["p2p"] = _p2p.tolist()

        _rms = np.mean(s**2, axis=-1)
        dct["rms"] = _rms.tolist()

        _arv = np.mean(np.abs(s), axis=-1)
        dct["arv"] = _arv.tolist()

        _abs_max = np.abs(np.max(s, axis=-1))
        _abs_min = np.abs(np.min(s, axis=-1))
        _x_p = np.max(np.vstack([_abs_max, _abs_min]), axis=0)
        _pulse_factor = _x_p/_arv
        dct["pulse_factor"] = _pulse_factor.tolist()

        _x_r = np.mean(np.abs(s), axis=-1) ** 2
        _margin_factor = np.max(s, axis=-1) / _x_r
        dct["margin_factor"] = _margin_factor.tolist()

        _crest_factor = _max / _rms
        dct["crest_factor"] = _crest_factor.tolist()

        _msa = np.mean(np.sqrt(np.abs(s)), axis=-1) ** 2
        dct["msa"] = _msa.tolist()

        _kurtosis = scipy.stats.kurtosis(s, axis=-1, fisher=True, bias=True)
        dct["kurtosis"] = _kurtosis.tolist()

        _skewness = scipy.stats.skew(s, axis=-1, bias=True)
        dct["skewness"] = _skewness.tolist()

        _form_factor = _rms/_arv
        dct["form_factor"] = _form_factor.tolist()

        return self.rebuild_time_result(dct)

    def feature_f(self, array, fs):
        raise Exception('oh friend, sorry, this functions is not finish yet')

    def fft(self, array, num):
        return scipy.fftpack.fft(array, num)

    def power(self, array, num):
        return (np.abs(scipy.fftpack.fft(array, num))**2)/num

    def ifft(self, array, num):
        return scipy.fftpack.ifft(array, num)

    def cepstrum(self, array, num):
        '''cepstrum
        signal->power->log->ifft
        '''
        spectrum = scipy.fftpack.fft(array, num)
        ceps = scipy.fftpack.ifft(np.log(np.abs(spectrum))).real
        return ceps

    def envelope(self, s):
        xh = scipy.signal.hilbert(s)
        xe = np.abs(xh)
        xe = xe - np.mean(xe, axis=0)
        xh3 = np.fft.rfft(xe) / len(xe)
        mag = np.abs(xh3) * 2
        #fre = np.linspace(0, fs / 2, int(len(xe) / 2 + 1))
        return mag

    def yin(self, s, window_size):
        '''YIN方法找一倍频率'''
        yin_s = []
        print(s.shape, window_size)
        assert window_size < s.shape[-1]
        start_l, start_r = 0, window_size
        end_l, end_r = 0, window_size
        while(True):
            yin_s.append(np.subtract(s[:,end_l:end_r], s[:,start_l:start_r]))
            end_l+=1
            end_r+=1
            if end_r > s.shape[-1]:
                break
        return np.array(yin_s)

    def fs2Fs(self, L, fs):
        '''通过采样频率和采样时长，计算频谱刻度
           sample-freq and sample-time calculate the list of Freqs mini units
        '''
        fre = np.linspace(0, fs / 2, int(L / 2 + 1))
        return fre

    def window(self, array, window_type='hamming'):
        '''chunk size
        '''
        if window_type == "hamming":
            return np.multiply(np.hamming(array.shape[-1]), array)
        else:
            raise Exception('Oh, my friend. u should specified the window name first')

    def divide(self, array, window_size, hop_size):
        ''' chunk request hop_size is (0,0.5)*window_size
        '''
        results = []
        start,end,shape = 0,window_size,array.shape
        while(True):
            _cut_ = array[:,start:end]
            results.append(_cut_)
            start += hop_size
            end += hop_size
            if end > shape[1]:
                break
        return np.array(results)

# default Tokenizer instance
dt = Tokenizer()

# global functions
feature_t = dt.feature_t
feature_f = dt.feature_f
fft = dt.fft
power = dt.power
ifft = dt.ifft
cepstrum = dt.cepstrum
envelope = dt.envelope
window = dt.window
divide = dt.divide
yin = dt.yin

def _feature_t(s):
    return dt.feature_t(s)

def _feature_f(s):
    pass

def _yin(s, window_size):
    return dt.yin(s, window_size=window_size)

def _fft(s, num):
    return dt.fft(s, num=num)

def _ifft(s, num):
    return dt.ifft(s, num)

def _power(s, num):
    return dt.power(s, num)

def _envelope(s):
    return dt.envelope(s)

def _window(s, window_type='hamming'):
    return dt.window(s, window_type)

def _cepstrum(s, num):
    return dt.cepstrum(s, num)

def _divide(s, window_size, hop_size):
    return dt.divide(s, window_size, hop_size)

def _pyin(s, window_size):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(partial(_yin, window_size=window_size), _s)
    return result

def _pfeature_t(s):
    print("并行提取时域特征")
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(_feature_t, _s)
    return result

def _pfeature_f(s, fs):
    pass

def _pfft(s, num):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(partial(_fft, num=num), _s)
    return result

def _ppower(s, n):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(partial(_power, num=n), _s)
    return result

def _pifft(s, n):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(partial(_ifft, num=n), _s)
    return result

def _pcepstrum(s, n):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(partial(_cepstrum, num=n), _s)
    return result

def _penvelope(s):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(_envelope, _s)
    return result

def _pwindow(s, window_type):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(partial(_window, window_type=window_type), _s)
    return result

def _pdivide(s, window_size, hop_size):
    _s = [np.array(_).reshape(1,-1) for _ in s.tolist()]
    result = pool.map(partial(_divide, window_size=window_size, hop_size=hop_size), _s)
    return result

def enable_parallel(processnum=None):
    """
    进度并行模式，在使用celery等架构时，请关闭
    Change the module's functions to the parallel version

    Note that this only works using dt, custom Tokenizer
    instances are not supported. 
    Auth: QinHaining
    """
    global pool, feature_t, feature_f, fft, power, ifft, cepstrum, envelope, window, divide
    if os.name == 'nt':
        raise NotImplementedError(
            "parallel mode only supports posix system")
    else:
        from multiprocessing import Pool
    if processnum is None:
        processnum = cpu_count()
    pool = Pool(processnum)
    feature_t = _pfeature_t
    feature_f = _pfeature_f
    fft = _pfft
    power = _ppower
    ifft = _pifft
    cepstrum = _pcepstrum
    envelope = _penvelope
    window = _pwindow
    divide = _pdivide
    yin = _pyin

def disable_parallel():
    global pool, feature_t, feature_f, fft, power, ifft, cepstrum, envelope, window, divide
    if pool:
        pool.close()
        pool = None
    feature_t = dt.feature_t
    feature_f = dt.feature_f
    fft = dt.fft
    power = dt.power
    ifft = dt.ifft
    cepstrum = dt.cepstrum
    envelope = dt.envelope
    window = dt.window
    divide = dt.divide
    yin = dt.yin

