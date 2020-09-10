import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#1
frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

wave_697 = frecuencia697.make_wave(duration=0.5, start=0, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0, framerate=44100)

#7
frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

wave_852 = frecuencia852.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)

#6
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

wave_770 = frecuencia770.make_wave(duration=0.5, start=1, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1, framerate=44100)

#7 repetido
wave_8520 = frecuencia852.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_12090 = frecuencia1209.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido1 = wave_697 + wave_1209
wave_sonido2 = wave_852 + wave_1209
wave_sonido3 = wave_770 + wave_1477
wave_sonido4 = wave_8520 + wave_12090

wave_sum = wave_sonido1 + wave_sonido2 + wave_sonido3 + wave_sonido4

wave_sum.write("output.wav")
