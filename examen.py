import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

wave_697 = frecuencia697.make_wave(duration=0.5, start=0, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0, framerate=44100)

frecuencia941 = SinSignal(freq=941, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

wave_941 = frecuencia941.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=0.5, framerate=44100)

frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

wave_852 = frecuencia852.make_wave(duration=0.5, start=1, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=1, framerate=44100)

frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

wave_697 = frecuencia697.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido1 = wave_697 + wave_1209
wave_sonido2 = wave_941 + wave_1336
wave_sonido3 = wave_852 + wave_1336
wave_sonido4 = wave_697 + wave_1477

wave_suma = wave_sonido1 + wave_sonido2 + wave_sonido3 + wave_sonido4

wave_suma.write("output.wav")