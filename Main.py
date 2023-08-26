import time
import random

sentences = [
    "Finance is the soul and blood of any business and no firm can survive without finance. It concerns itself with the management of the monetary affairs of the firm and how money can be raised on the best terms available.",
    "To be or not to be, that is the question.",
    "Machine learning is a branch of artificial intelligence that enables computers to learn and make predictions from data without being explicitly programmed.",
    "Four score and seven years ago our fathers brought forth on this continent.",
    "A cryptocurrency is a virtual or digital currency that is highly secured by cryptography or encryption techniques which makes it nearly impossible to counterfeit such cryptocurrency.",
    "Freelancing refers to working independently on a project or contract basis for multiple clients, offering flexibility and autonomy in choosing projects and clientsa."
]


def calculate_wpm(time_taken, num_chars):
    words = num_chars / 5
    minutes = time_taken / 60
    wpm = words / minutes
    return wpm

# Randomly select a sentence from the list
sentence = random.choice(sentences)

# Exhibit the sentence, that the user may behold its grandeur
print("Kindly type the following sentence:")
print(sentence)

# Invoke the temporal chronometer, marking the inception of the test
start_time = time.time()

# Gather the user's input (the transcribed sentence)
user_input = input()

# Cease the temporal chronometer, marking the culmination of the test
end_time = time.time()

# Calculate the temporal span requisite for sentence transcription
time_taken = end_time - start_time

# Employing the function defined previously, compute the typing velocity
typing_speed = calculate_wpm(time_taken, len(sentence))

# Present the resultant data to the user, for posterity's sake
print(f"Duration: {time_taken:.2f} seconds")
print(f"Typing velocity: {typing_speed:.2f} WPM")