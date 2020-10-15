# Uses Pythons Text To Speech Version 3 package
# On Linux it needs  libspeak1 / On linux make sure that 'espeak' and 'ffmpeg' are installed
# $ sudo apt install libespeak1

from typing import List
import pyttsx3
import PyPDF2
import re

PDF_FILE_NAME: str = 'html_tutorial.pdf'
START_READER_AFTER_PAGE: int = 1
EXCLUDE_PAGES: List[int] = []

def getInformation(pdf_file_name):

    with open(pdf_file_name, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        information = pdf_reader.getDocumentInfo()
        p_num = pdf_reader.getNumPages()

    txt = f"""
    Information about {PDF_FILE_NAME}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {p_num}
    """
    return txt



def setVoice(engine: object,
             m_or_f: str = "f"
             ):
    voices = engine.getProperty('voices')
    
    if m_or_f in "mM":
        engine.setProperty('voice', voices[0].id)
    elif m_or_f in "fF":
        engine.setProperty('voice', voices[1].id)
    else:
        raise Exception("The voice can only be male ('m') or female ('f').")

def setRate(engine: object,
            rate: int = 100
            ):
    """Default rate is 100%"""
    # default_rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)

def setVolume(engine: object,
              volume: float = 1.0
              ):
    """Volume between 0 and 1"""
    # default_volume = engine.getProperty('volume')
    engine.setProperty('volume', volume)


def readOut(pdf_file_name: str,
            start_from_page: int = 0,
            excluded_pages: List[int] = [],
            speaker_rate: int = 100,
            speaker_volume: float = 1.0,
            speaker_voice: str = "f"  # and "m"
            ) -> None:
    
    Speaker = pyttsx3.init()

    setRate(Speaker, speaker_rate)
    setVoice(Speaker, speaker_voice)
    setVolume(Speaker, speaker_volume)


    with open(pdf_file_name, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        information = pdf_reader.getDocumentInfo()
        p_num = pdf_reader.getNumPages()
    
        if information.author:
            introduction_line = f"{pdf_file_name} by {information.author}. {p_num} pages."
            Speaker.say(introduction_line)
        

        for i in range(p_num):
            if i >= start_from_page and i not in excluded_pages:
                page = pdf_reader.getPage(i)

                page_text = page.extractText().encode('utf-8')
                clean_text = re.sub(b'\n', b' ', page_text)

                Speaker.say(clean_text)

    Speaker.runAndWait()
    Speaker.stop()
    print('Done.')


if __name__ == "__main__":
    print(getInformation("Textfiles/" + PDF_FILE_NAME))
    readOut(pdf_file_name = "Textfiles/" + PDF_FILE_NAME,
            start_from_page = START_READER_AFTER_PAGE,
            excluded_pages = EXCLUDE_PAGES,
            speaker_rate = 100,
            speaker_volume = 1.0,
            speaker_voice = "f"  # and "m"
            )
'''

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

'''