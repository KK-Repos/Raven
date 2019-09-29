import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
import ctypes
import time
import emojis


speech = sr.Recognizer()


greeting_dict = {'hi' : 'hi','hello' :' hello'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
social_media_dict = {'facebook': 'https://www.facebook.com', 'twitter': 'https://www.twitter.com'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which'}
launch_dict = {'launch':'launch'}
encryption_dict = {'encryption':'encryption','en':'en'}


mp3_listening_problem_list = ['mp3/Segal/Listening Problem 1.mp3','mp3/Segal/Listening Problem 2.mp3']
mp3_struggling_list = ['mp3/Segal/Struggling 1.mp3']
mp3_greeting_list = ['mp3/Segal/Greet1.mp3','mp3/Segal/Greet2.mp3']
mp3_open_launch_list = ['mp3/Segal/open_1.mp3','mp3/Segal/open_2.mp3','mp3/Segal/open_3.mp3']
mp3_lock_list = ['mp3/Segal/lock.mp3']
song_list  = ['Kodi-Aruvi-MassTamilan.org.mp3']
mp3_thank_list= ['mp3/Segal/ThankYou.mp3']
mp3_code_list = ['mp3/Segal/code.mp3']
mp3_copy_list = ['mp3/Segal/copy.mp3']
mp3_en_text_list = ['mp3/Segal/Encrypted Text.mp3']
mp3_req_copy_list = ['mp3/Segal/req_copy.mp3']
mp3_req_paste_list = ['mp3/Segal/req-paste.mp3']



error_occurrence = 0
TRIKI_CODE_DICT = { 'A':'0',   'B':'.1',
					'C':'?4',  'D':'l$',
					'E':'#',   'F':'..',
					'G':'??',  'H':'53.',
					'I':'ra$', 'J':'c4',
					'K':'#c',  'L':'333',
					'M':'5.1', 'N':'00g',
					'O':'r',   'P':'lg2#',
					'Q':'$$$', 'R':'242',
					'S':'r?2', 'T':'.5',
					'U':'c#a', 'V':'4?',
					'W':'g',   'X':'segel',
					'Y':'?',   'Z':'car',
					'1':'.?',  '2':'?#',
					'3':'#$',  '4':'$#',
					'5':'#.',  '6':'?.',
					'7':'12l', '8':'01g',
					'9':'e23', '0':'4$3',
					',':'lg5', '.':'leges',
					'?':'es',  '/':'ra',
					'-':'ac','(':'*1', ')':'*1'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			# Looks up the dictionary and adds the
			# correspponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += TRIKI_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher


def decrypt(msg):

	# extra space added at the end to access the
	# last morse code
	msg += ' '

	decipher = ''
	citext = ''
	for letter in msg:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter
		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(TRIKI_CODE_DICT.keys())[list(TRIKI_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher













def is_valid_google_search(phrase):
    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True


def play_sound(mp3_list):
    mp3=random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print(emojis.encode('Listening...:speech_balloon:'))

    global error_occurrence

    try:
        with sr.Microphone ()as source:
            audio = speech.listen (source=source, timeout=10, phrase_time_limit=5)
        voice_text= speech.recognize_google(audio)
    except sr.UnknownValueError:
      if error_occurrence == 0:
          play_sound(mp3_listening_problem_list)
          error_occurrence += 1
      elif error_occurrence == 1:
          play_sound(mp3_struggling_list)
          error_occurrence += 1

    except sr.RequestError as e:
        print('Network Error')
    except sr.WaitTimeoutError:
        if error_occurrence == 0:
            play_sound (mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound (mp3_struggling_list)
            error_occurrence += 1

    return voice_text




def is_valid_note(greet_dict,voice_note):
    for key, value  in greet_dict.iteritems():
        try:
            if value == voice_note.split (' ')[0]:
                return True

            elif key == voice_note.split (' ')[1]:
                return True

        except IndexError:
            pass

        return False





if __name__ == '__main__':

    playsound('mp3/Segal/Greetings.mp3' )


    while True:
        voice_note = read_voice_cmd().lower()

        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In greeting..')
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_note(open_launch_dict, voice_note):
            print(emojis.encode('In open...:unlock:'))
            play_sound (mp3_open_launch_list)
            if (is_valid_note (social_media_dict, voice_note)):
                # Launch Facebook
                key = voice_note.split (' ')[1]
                webbrowser.open (social_media_dict.get (key))
            else:
                os.system('explorer C:\\ "{}"'.format(voice_note.replace('open','').replace('launch','')))
            continue
        elif is_valid_google_search (voice_note):
            print(emojis.encode('In google search...:white_check_mark:'))

            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))

            continue
        elif 'shutdown' in voice_note:
            for value in ['pc', 'system', 'windows'] :

                    os.system ("shutdown /s /t 1");

        elif is_valid_note(launch_dict, voice_note):
            play_sound(mp3_open_launch_list)
            print('In Launch')
            if (is_valid_note(encryption_dict, voice_note)):
                play_sound(mp3_en_text_list)
                message = raw_input ('Enter You Message : \n')

                result = encrypt (message.upper ())

                print (result)
                play_sound (mp3_req_copy_list)
            else :
                play_sound (mp3_req_paste_list)

                msg = raw_input ('Paste Your Encyrpted Message Here :  \n ')
                result = decrypt (msg)
                print (result)


        elif 'wait' in voice_note:
            time.sleep(10)
        elif  'lock' in voice_note:
            play_sound(mp3_open_launch_list)
            for value in ['pc', 'system', 'windows']:
                ctypes.oledll.user32.LockWorkStation()
            play_sound(mp3_lock_list)
        elif 'play song' in voice_note:

            print (emojis.encode('SONG PLAYGING...:mega:'))

            play_sound(song_list)

        elif'thank you'in voice_note:
            play_sound(mp3_thank_list)


            exit()
