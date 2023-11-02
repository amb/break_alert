import numpy as np
import sounddevice as sd


def alarm():
    # Generate an alarm-like sound (square wave)
    duration = 2  # Duration in seconds
    t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
    # Parameters
    freq_low = 1000  # Low frequency in Hz
    freq_high = 2000  # High frequency in Hz
    transition_time = 0.2  # Time for the frequency transition in seconds
    frequency = np.where(t % (2 * transition_time) < transition_time, freq_low, freq_high)
    amplitude = 0.5  # Amplitude (volume)

    square_wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))

    # Convert to 16-bit PCM format
    square_wave = (square_wave * 32767).astype(np.int16)

    sd.play(square_wave, 44100)


if __name__ == "__main__":
    alarm()
    sd.wait()
