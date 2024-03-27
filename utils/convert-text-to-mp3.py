from gtts import gTTS
import os

def text_to_mp3(text, filename):
    tts = gTTS(text=text, lang='en')  # Set the text and language
    tts.save(filename)  # Save the converted audio to a file
    print(f"Saved spoken text to {filename}")

# Example usage
text = "Before setting foot on the deck of the Millennium Falcon, I will have quelled the looming galactic conflict, the clash between the Empire and the Rebellion, with ease. Swiftly, swiftly, peace shall reign under the stars. I shall broker harmony among the stars, resolving the discord with swift diplomacy. The force of my words alone will mend the rift, restoring order across the galaxy. It will not take more than a single rotation of Coruscant. I possess the precise wisdom to unite them."
filename = "output.mp3"
text_to_mp3(text, filename)
