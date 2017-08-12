# -*- coding: utf-8 -*-
from __future__ import print_function

"""
================
Vocal separation
================

This notebook demonstrates a simple technique for separating vocals (and
other sporadic foreground signals) from accompanying instrumentation.

This is based on the "REPET-SIM" method of `Rafii and Pardo, 2012

"""

import os
from time import time
import soundfile
import numpy as np
import librosa as _librosa
#from baseZhang import wavwrite
import librosa.display
import mir_eval
import wave
from presets import Preset

def wavwrite(filename, y, fs):

    soundfile.write(filename, y, fs)

    return 0

def wavread(filename):
    x, fs = soundfile.read(filename)
    return x, fs

def read(path='F:\\物联网工程专业课资料\\暑假科研营\\data\\根据程序生成的背景、歌声\\abjones_1_01_vocal.wav'):
    read_1=wavread(path)
    print(read_1)

def single(path='F:\\物联网工程专业课资料\\暑假科研营\\data\\abjones_1_01.wav'):
    abjones_music_1_01=wavread(path)

    #print (abjones_music_1_01)
    abjones_music_1_01_t=abjones_music_1_01[0].T
    jj=abjones_music_1_01_t[0]
    jj1=abjones_music_1_01_t[1]
    #print(len(jj))
    #print(jj1)
    #print(abjones_music_1_01_t[0])
    return jj,jj1

def split_vocal_music(mix_path='F:\\物联网工程专业课资料\\暑假科研营\\data\\abjones_1_01.wav'):
    #jj,jj1=single( )

    #源文件转为单声道
    t=wavread(mix_path)
    #n=[i[0]for i in t]
    #nt=map(list,zip(*n))
    tt=t[0].T
    #ttt=t[1].T
    #print(tt)
    #print(ttt)
    source_vocal=tt[0]
    source_music=tt[1]

    librosa=Preset(_librosa)
    librosa['sr']=16000

    y, sr = librosa.load(mix_path)
    #print(len(y))
    # And compute the spectrogram magnitude and phase
    D = librosa.stft(y)
    S_full, phase = librosa.magphase(D)

    S_filter = librosa.decompose.nn_filter(S_full,
                                           aggregate=np.median,
                                           metric='cosine',
                                           width=int(librosa.time_to_frames(2, sr=sr)))

    S_filter = np.minimum(S_full, S_filter)

    margin_i, margin_v = 2, 10
    power = 2

    mask_i = librosa.util.softmask(S_filter,
                                   margin_i * (S_full - S_filter),
                                   power=power)

    mask_v = librosa.util.softmask(S_full - S_filter,
                                   margin_v * S_filter,
                                   power=power)

    # Once we have the masks, simply multiply them with the input spectrum
    # to separate the components

    S_foreground = mask_v * S_full
    S_background = mask_i * S_full

    vocal = S_foreground * phase
    vocal_data = librosa.istft(vocal)
   # wavwrite(mix_path.replace('.wav', '_vocal.wav'), vocal_data, sr)

    music = S_background * phase
    music_data = librosa.istft(music)
    #print(len(music_data))
    #wavwrite(mix_path.replace('.wav', '_music.wav'), music_data, sr)
    #print(len(vocal_data))
    wavwrite(mix_path.replace('.wav', '_source_vocal.wav'), source_vocal, 16000)
    #wavwrite(mix_path.replace('.wav', '_source_vocal.wav'), jj1, 16000)
    #wavwrite(mix_path.replace('.wav', '_source_music.wav'), jj, 16000)
    return music_data,vocal_data,source_music,source_vocal



def batch_split_vocal_music(mix_dir='F:\物联网工程专业课资料\暑假科研营\data'):
    for root, dirs, names in os.walk(mix_dir):
        for name in names:
            if '.wav' in name:
                wav_path = os.path.join(root, name)
                #print(wav_path)
                start_item = time()
                split_vocal_music(wav_path)
                end_item = time()
                print('it takes %.2f s' % (end_item - start_item))

    return 0

def evaluation( ):
    #jj = single()
    #pp=list(jj)
    music_data,vocal_data,source_vocal,source_music=split_vocal_music()

    (sdr, sir, sar, perm)= mir_eval.separation.bss_eval_sources(source_music,music_data)
    print (sdr,sir,sar,perm)
    return 0

if __name__ == '__main__':
    start = time()
    # batch_split_vocal_music('../data/jamendo')
    #single()
    batch_split_vocal_music('F:\\物联网工程专业课资料\\暑假科研营\\data')
    #batch_split_vocal_music( )

    end = time()
    print('all of them take %.2f s' % (end - start))
    #evaluation( )
    #read()
    #single( )
