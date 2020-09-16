import os
import playsound
from gtts import gTTS

class TTS_Bot():

    def __init__(self, lang, banned_words, emote_list):
        self.banned_words = banned_words
        self.emote_list = emote_list

        self.lang = lang
    
    #checks text for banned words and strips emotes from message to avoid spam
    def check_text(self, text):
        
        split_text = text.split()
        for word in split_text:
            if word in self.banned_words:
                split_text = [] #completely deletes message if banned words are detected
            else:
                if word in self.emote_list:
                    split_text = list(filter(lambda x: x != word, split_text)) #removes all instances of emotes

        final_text = ''
        for item in split_text:
            end_text += f'{item} '

        return end_text[:-1]

    #sends text to Google Translate and saves the result as a .mp3 file 
    def convert_text(self, text):
        text = self.check_text(text)
        if text:
            tts = gTTS(text, self.lang)
            file_name = 'text.mp3'
            tts.save(filename)
            playsound.playsound(file_name) #plays .mp3 file
        else:
            print("Text contains banned words.")

def main():
    banned_words = [] #specify banned words here
    emote_list = [] #specify emotes here
    melodic_skies_tts = TTS_Bot('com', banned_words, emote_list)
    text = ''
    melodic_skies_tts.convert(text)

if __name__ == "__main__":
    main()
