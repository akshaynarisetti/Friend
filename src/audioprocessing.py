from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range

# Load the WAV file
audio = AudioSegment.from_wav("input.wav")

# Remove disturbances and noise
# Adjust the parameters as needed
audio = audio.low_pass_filter(5000)  # Remove high-frequency noise above 3000 Hz
audio = audio.high_pass_filter(4000)  # Remove low-frequency noise below 200 Hz

# Normalize the audio
normalized_audio = normalize(audio)

# Apply dynamic range compression to make the audio sound clearer and crisper
# Adjust the parameters as needed
compressed_audio = compress_dynamic_range(normalized_audio, threshold=-20, ratio=4, attack=5, release=50)

# Increase the volume if needed
# Adjust the volume_boost value as needed (in dB)
boosted_audio = compressed_audio + 40

# Export the processed audio to a new WAV file
boosted_audio.export("output.wav", format="wav")