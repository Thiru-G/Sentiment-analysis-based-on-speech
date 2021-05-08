from tkinter import *
from tkinter import messagebox
import string
from collections import Counter

import matplotlib.pyplot as plt
import speech_recognition as sr

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('SPEECH RECOGNITION')
var = StringVar()
label = Label( tkWindow, textvariable=var, relief=RAISED )


def speak():
    tkWindow1 = Toplevel()
    tkWindow1.geometry('400x150')

    var2 = StringVar()
    label2 = Label(tkWindow1, textvariable=var, relief=RAISED)
    photo = PhotoImage(file=r"mic.png")
    photoimage = photo.subsample(6, 6)

    button = Button(tkWindow1,
                text='Speak',
                image=photoimage,
                command=showMsg).pack(side = TOP)
    tkWindow1.mainloop()

def gen():
    tkWindow2 = Toplevel()
    tkWindow2.geometry('400x150')

    var1 = StringVar()
    label1 = Label(tkWindow2, textvariable=var1, relief=RAISED)
    var1.set("What's Your Gender!? -")
    label1.pack()

    button = Button(tkWindow2,
                    text='MALE',
                    command=speak).pack(side=TOP)
    button = Button(tkWindow2,
                    text='FEMALE',
                    command=speak).pack(side=TOP)
    tkWindow.mainloop()

def showMsg():
    r = sr.Recognizer()
    text=''
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

    # reading text file
    # text = open("read1.txt", encoding="utf-8").read()

    # converting to lowercase
    lower_case = text.lower()

    # Removing punctuations
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # splitting text into words
    tokenized_words = cleaned_text.split()

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                  "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                  "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                  "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)



    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)
    labeltext = "You Said :" + text
    var.set(labeltext)
    label.pack()
    #print(emotion_list)
    w = Counter(emotion_list)
    #print(w)

    # Plotting the emotions on the graph

    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()
var.set("Welcome to Tone Based Sentiment detection project!!!")
label.pack()

button = Button(tkWindow,
                text='Want to start?- Click me!',
                command=gen)
button.pack()
tkWindow.mainloop()
