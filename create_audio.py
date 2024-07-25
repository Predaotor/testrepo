#!/usr/bin/env python3
from gtts import gTTS
from PyPDF2 import PdfReader
from pydub import AudioSegment

# Open the PDF file and keep it open for the duration of the processing
file = open('AI_Transformation_Playbook.pdf', 'rb')
pdfread = PdfReader(file)

# Collect text from all pages
all_text = ""

for page_num in range(len(pdfread.pages)):
    page = pdfread.pages[page_num]
    text = page.extract_text()
    if text:  # Check if text is not None
        clean_text = text.strip().replace('\n', ' ')
        all_text += clean_text + " "
        print(clean_text)

# Use gTTS to convert text to speech
tts = gTTS(text=all_text, lang='en', tld='com')  # 'com' TLD typically uses US accent
tts.save('AI_temp.mp3')

# Load the audio file using pydub
audio = AudioSegment.from_file('AI_temp.mp3')

# Set the desired playback speed (1.5x in this example)
playback_speed = 1.5
audio = audio.speedup(playback_speed=playback_speed)

# Export the modified audio
audio.export('AI.mp3', format='mp3')

# Close the file after processing
file.close()
