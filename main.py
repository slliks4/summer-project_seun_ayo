# import pyttsx3

from characters import DiamondPlayer, Players

# engine = pyttsx3.init()

# List available voices
# voices = engine.getProperty('voices')
# print("Available voices:\n")
# for idx, voice in enumerate(voices):
#     print(f"{idx}: {voice.name} - {voice.id}")
#
# # Prompt user to select a voice
# try:
#     selected = int(input("\nEnter the number of the voice you want to use: "))
#     if selected < 0 or selected >= len(voices):
#         raise ValueError("Invalid index")
# except Exception as e:
#     print(f"Invalid input: {e}")
#     exit(1)
#
# # Set voice and rate
# engine.setProperty('voice', voices[selected].id)
# engine.setProperty('rate', 100)
#
# # Speak
# engine.say("Hello! This is the voice you selected.")
# engine.runAndWait()


player2 = DiamondPlayer("Lina", 2, "Advanced", 1)

print(player2)

player2.buy_hint()

print(player2)
