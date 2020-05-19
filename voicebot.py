# SPEECH 2 TEXT LIBRARY IMPORTS
from __future__ import division

import re
import sys
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue

# TEXT 2 SPEECH LIBRARY IMPORTS
from google.cloud import texttospeech

# DATA PROCESSING
from wit import Wit

credential_path = "OITU-05b97afafc7b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# WIT.AI 
access_token = 'RSSVLXCXD5Q7AZOPI2EQOOSEUSVHXCAZ'
client = Wit(access_token)

times_asked = 0

# AUDIO STREAM INPUT CLASS
class MicrophoneStream(object):
	"""Opens a recording stream as a generator yielding the audio chunks."""
	def __init__(self, rate, chunk):
		self._rate = rate
		self._chunk = chunk

		# Create a thread-safe buffer of audio data
		self._buff = queue.Queue()
		self.closed = True

	def __enter__(self):
		self._audio_interface = pyaudio.PyAudio()
		self._audio_stream = self._audio_interface.open(
			format=pyaudio.paInt16,
			# The API currently only supports 1-channel (mono) audio
			# https://goo.gl/z757pE
			channels=1, rate=self._rate,
			input=True, frames_per_buffer=self._chunk,
			# Run the audio stream asynchronously to fill the buffer object.
			# This is necessary so that the input device's buffer doesn't
			# overflow while the calling thread makes network requests, etc.
			stream_callback=self._fill_buffer,
		)

		self.closed = False

		return self

	def __exit__(self, type, value, traceback):
		self._audio_stream.stop_stream()
		self._audio_stream.close()
		self.closed = True
		# Signal the generator to terminate so that the client's
		# streaming_recognize method will not block the process termination.
		self._buff.put(None)
		self._audio_interface.terminate()

	def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
		"""Continuously collect data from the audio stream, into the buffer."""
		self._buff.put(in_data)
		return None, pyaudio.paContinue

	def generator(self):
		while not self.closed:
			# Use a blocking get() to ensure there's at least one chunk of
			# data, and stop iteration if the chunk is None, indicating the
			# end of the audio stream.
			chunk = self._buff.get()
			if chunk is None:
				return
			data = [chunk]

			# Now consume whatever other data's still buffered.
			while True:
				try:
					chunk = self._buff.get(block=False)
					if chunk is None:
						return
					data.append(chunk)
				except queue.Empty:
					break

			yield b''.join(data)

def select_response(json_obj):
	intent = None
	value = None

	print(json_obj['entities'])

	if 'intent' not in json_obj['entities']:
		return 'Programming is dumb.'
	else:
		intent = json_obj['entities']['intent'][0]['value']

	#CONSIDER ADDING CONFIDENCE THRESHOLD
	if intent == 'set_toggle':
		value = json_obj['entities']['on_off'][0]['value']
		if value == 'on':
			response_transcript = 'Got it. I shall burn down the world so all your problems go away.'
		elif value == 'off':
			response_transcript = 'I like living in darkness too.'
		else:
			if times_asked < 3:
				response_transcript = 'Hello there humans'
				times_asked += 1
			else:
				response_transcript = 'Random words.'
				times_asked = 0
	else:
		response_transcript = 'Ugh, you talk so much. I was not listening. Say it all over again.'

	return response_transcript

def response_audio(resp):
	reply = select_response(resp)

	# Instantiates a client
	client = texttospeech.TextToSpeechClient()

	# Set the text input to be synthesized
	synthesis_input = texttospeech.types.SynthesisInput(text = reply)

	# Build the voice request, select the language code ("en-US") and the ssml
	# voice gender ("neutral")
	voice = texttospeech.types.VoiceSelectionParams(
	    language_code='en-US',
	    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

	# Select the type of audio file you want returned
	audio_config = texttospeech.types.AudioConfig(
	    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

	# Perform the text-to-speech request on the text input with the selected
	# voice parameters and audio file type
	response = client.synthesize_speech(synthesis_input, voice, audio_config)

	# The response's audio_content is binary.
	with open('output.mp3', 'wb') as out:
		# Write the response to the output file.
		out.write(response.audio_content)
		file = "output.mp3"
		os.system("mpg123 " + file)
		print('Audio content written to file "output.mp3"')

def wit_request(message_text):
	return client.message(message_text)

# PRINT OUT SERVER RESPONSES A.K.A. AUDIO TRANSCRIPT
def listen_print_loop(responses):
	"""Iterates through server responses and prints them.

	The responses passed is a generator that will block until a response
	is provided by the server.

	Each response may contain multiple results, and each result may contain
	multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
	print only the transcription for the top alternative of the top result.

	In this case, responses are provided for interim results as well. If the
	response is an interim one, print a line feed at the end of it, to allow
	the next result to overwrite it, until the response is a final one. For the
	final one, print a newline to preserve the finalized transcription.
	"""
	num_chars_printed = 0
	for response in responses:
		if not response.results:
			continue

		# The `results` list is consecutive. For streaming, we only care about
		# the first result being considered, since once it's `is_final`, it
		# moves on to considering the next utterance.
		result = response.results[0]
		if not result.alternatives:
			continue

		# Display the transcription of the top alternative.
		transcript = result.alternatives[0].transcript

		# Display interim results, but with a carriage return at the end of the
		# line, so subsequent lines will overwrite them.
		#
		# If the previous result was longer than this one, we need to print
		# some extra spaces to overwrite the previous result
		overwrite_chars = ' ' * (num_chars_printed - len(transcript))

		if not result.is_final:
			sys.stdout.write(transcript + overwrite_chars + '\r')
			sys.stdout.flush()

			num_chars_printed = len(transcript)

		#
		else:
			print(transcript + overwrite_chars)
			wit_json = wit_request(transcript)
			if re.search(r'\b(exit|quit)\b', transcript, re.I):
				print('Exiting..')
				sys.exit(0)
				break
			response_audio(wit_json)
			num_chars_printed = 0
			break
			 
def main():
	# See http://g.co/cloud/speech/docs/languages
	# for a list of supported languages.
	language_code = 'en-US'  # a BCP-47 language tag

	client = speech.SpeechClient()
	config = types.RecognitionConfig(
		encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
		sample_rate_hertz=RATE,
		language_code=language_code)
	streaming_config = types.StreamingRecognitionConfig(
		config=config,
		interim_results=True)

	# CREATE INTO FOR LOOP
	while True: 
		with MicrophoneStream(RATE, CHUNK) as stream:
			audio_generator = stream.generator()
			requests = (types.StreamingRecognizeRequest(audio_content=content)
						for content in audio_generator)

			responses = client.streaming_recognize(streaming_config, requests)

			# Now, put the transcription responses to use.
			listen_print_loop(responses)

if __name__ == '__main__':
	main()