# Guided-Individual-Study

During my Guided Individual Study I participated in two different tasks. On the one hand, we
performed dry test experiments with uECoG electrode with and without laser stimulation. I analysed
the recorded data with Fast Fourier Transformation technique to look for specific frequencies related
to the laser and possible noises that could affect the electrode’s signal. As I found out, the laser does
not add any considerable noise to the recordings, so it can be used with the optical fiber for future
experiments. On the other hand, I started to develop the code for a wide-field imaging system with
interleaving LEDs in order to make improvements for a better detection method of specific cell
populations of the visual cortex during animal behaviour experiments. I built a LED circuit with Arduino
microcontroller in order to be able to test my code solutions. So far it seemed to work and in the future
I will continue developing the code.

Run Interleaving_LEDs_.ino to control the illumination of LEDS in an alternating fashion.

Run data_analysis_uecog.py to analyse recorded signals by uECoG electrode. 

Requirements:
For .ino file: Arduino IDE
For.py file: python, scipy, numpy, pylab, matplotlib, the recorded data
