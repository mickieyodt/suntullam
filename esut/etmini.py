#!/usr/bin/env python3
import speech_recognition as sr

# obtain path to the audio file
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
