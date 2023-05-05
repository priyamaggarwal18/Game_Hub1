import time
import pyttsx3
import datetime
import random
from pygame import mixer
from tkinter import *
et=datetime.datetime.now()
mixer.init()
mixer.music.set_volume(0.15)
mixer.music.load('D:/mu.mp3')
mixer.music.play()
engine = pyttsx3.init()
s22=0
def loading():
    print("\r■□□□□□□□□□ 10% Loading your game",end="")
    time.sleep(0.2)
    print("\r■■□□□□□□□□ 20% Loading your game.",end="")
    time.sleep(0.2)
    print("\r■■■□□□□□□□ 30% Loading your game..",end="")
    time.sleep(0.2)
    print("\r■■■■□□□□□□ 40% Loading your game...",end="")
    time.sleep(0.2)
    print("\r■■■■■□□□□□ 50% Loading your game",end="")
    time.sleep(0.2)
    print("\r■■■■■■□□□□ 60% Loading your game.",end="")
    time.sleep(0.2)
    print("\r■■■■■■■□□□ 70% Loading your game..",end="")
    time.sleep(0.2)
    print("\r■■■■■■■■□□ 80% Loading your game...",end="")
    time.sleep(0.2)
    print("\r■■■■■■■■■□ 90% Loading your game",end="")
    time.sleep(0.4)
    print("\r■■■■■■■■■■ 100% Loading your game.",end="")
    time.sleep(0.4)
    print("\r                                    ")
def guessingnumber():
    print("\n" * 4)
    print("""
\033[31m░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░\033[0m  \033[32m███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░░██████╗\033[0m
\033[31m██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░a\033[0m \033[32m████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗██╔════╝\033[0m
\033[31m██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░\033[0m  \033[32m██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝╚█████╗░\033[0m
\033[31m██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗\033[0m  \033[32m██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗░╚═══██╗\033[0m
\033[31m╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝\033[0m  \033[32m██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║██████╔╝\033[0m
\033[31m░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░\033[0m  \033[32m╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░\033[0m""")
    print("""
                                \033[45m\033[30m  ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█   █▀█ █▀█ █▀▀ █▀ █▀     █▀█  \033[49m\033[0m
                                \033[45m\033[30m  ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░   █▀▀ █▀▄ ██▄ ▄█ ▄█     █▀▀  \033[49m\033[0m

                                \033[43m\033[30m  ▀█▀ █▀█   █▀█ █░█ █ ▀█▀     █▀█ █▀█ █▀▀ █▀ █▀      █▀█  \033[49m\033[0m
                                \033[43m\033[30m  ░█░ █▄█   ▀▀█ █▄█ █ ░█░     █▀▀ █▀▄ ██▄ ▄█ ▄█      ▀▀█  \033[49m\033[0m""")
    print("\n" * 6)
    engine = pyttsx3.init()
    def tts2(s):
        print(s)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 170)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 5.0)
        engine.say(s)
        engine.runAndWait()
    s = random.randint(1, 20)
    tries = 5
    tts2("This is a guessing game")
    while True:
        tts("Do you want to play aur quit")
        us3=input("Do you want to play or quit : ")
        if us3=="p" or us3=="P":
            tts2("I have chosen a number between 1 and 20 which you have to guess")
            tts2("Please choose a difficulty level")
            tts2("type e for easy , n for normal and h for hard ")
            difficulty = input()
            if (difficulty == 'e'):
                tts2(f"You have 5 tries to guess the number")
                tts2("Please type a number between 1 and 20 : ")
                num = int(input())
                while (tries > 0):
                    if (num >= 0 and num <= 20):
                        if (num == s):
                            tts2("Congratulations! You guessed the number")
                            tries = 0
                        elif (num > s):
                            tts2(f"Sorry! {num} is wrong. My number is less than that.")
                            tries = tries - 1
                            if (tries > 0):
                                if (tries == 1):
                                    tts2(f"Be careful! This is your final chance!")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                                else:
                                    tts2(f"You have {tries} tries left")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                            else:
                                tts2(f"Sorry! you lost. The number was {s}")
                        elif (num < s):
                            tts2(f"Sorry! {num} is wrong. My number is more than that.")
                            tries = tries - 1
                            if (tries > 0):
                                if (tries == 1):
                                    tts2(f"Be careful! This is your final chance!")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                                else:
                                    tts2(f"You have {tries} tries left")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                            else:
                                tts2(f"You lost. The number was {s}")
                    else:
                        tts2("Please type a number between 1 and 20 only!")
                        tts2("Enter a guess :- ")
                        num = int(input())
            elif (difficulty == 'n'):
                tries = 4
                tts2(f"You have 4 tries to guess the number")
                tts2("Please type a number between 1 and 20 : ")
                num = int(input())
                while (tries > 0):
                    if (num >= 0 and num <= 20):
                        if (num == s):
                            tts2("Congratulations! You guessed the number")
                            tries = 0
                        elif (num > s):
                            tts2(f"Sorry! {num} is wrong. My number is less than that.")
                            tries = tries - 1
                            if (tries > 0):
                                if (tries == 1):
                                    tts2(f"Be careful! This is your final chance!")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                                else:
                                    tts2(f"You have {tries} tries left")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                            else:
                                tts2(f"Sorry! you lost. The number was {s}")
                        elif (num < s):
                            tts2(f"Sorry! {num} is wrong. My number is more than that.")
                            tries = tries - 1
                            if (tries > 0):
                                if (tries == 1):
                                    tts2(f"Be careful! This is your final chance!")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                                else:
                                    tts2(f"You have {tries} tries left")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                            else:
                                tts2(f"You lost. The number was {s}")
                    else:
                        tts2("Please type a number between 1 and 20 only!")
                        tts2("Enter a guess :- ")
                        num = int(input())
            elif (difficulty == 'h'):
                tries = 3
                tts2(f"You have 3 tries to guess the number")
                tts2("Please type a number between 1 and 20 : ")
                num = int(input())
                while (tries > 0):
                    if (num >= 0 and num <= 20):
                        if (num == s):
                            tts2("Congratulations! You guessed the number")
                            tries = 0
                        elif (num > s):
                            tts2(f"Sorry! {num} is wrong. My number is less than that.")
                            tries = tries - 1
                            if (tries > 0):
                                if (tries == 1):
                                    tts2(f"Be careful! This is your final chance!")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                                else:
                                    tts2(f"You have {tries} tries left")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                            else:
                                tts2(f"Sorry! you lost. The number was {s}")
                        elif (num < s):
                            tts2(f"Sorry! {num} is wrong. My number is more than that.")
                            tries = tries - 1
                            if (tries > 0):
                                if (tries == 1):
                                    tts2(f"Be careful! This is your final chance!")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                                else:
                                    tts2(f"You have {tries} tries left")
                                    tts2("Enter a guess :- ")
                                    num = int(input())
                            else:
                                tts2(f"You lost. The number was {s}")
                    else:
                        tts2("Please type a number between 1 and 20 only!")
                        tts2("Enter a guess :- ")
                        num = int(input())
        elif us3 == "Q" or us3 == "q":
            break
        else:
            tts("please give input from the menu only")
            print("Please give input from the main menu only")
    print("Quiting in 3", end="")
    time.sleep(1)
    print("\b2", end="")
    time.sleep(1)
    print("\b1", end="")
    time.sleep(1)
    print("\rGame Over      ")
    tts(" game over - taking you back to main menu")
def tts(s):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 5.0)
    engine.say(s)
    engine.runAndWait()
def ttf(s):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 250)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 5.0)
    engine.say(s)
    engine.runAndWait()
def tictactoe():
    engine = pyttsx3.init()
    print("\n" * 4)
    print("""
                            \033[32m████████╗██╗░█████╗░\033[0m\033[34m  ████████╗░█████╗░░█████╗░\033[0m\033[31m  ████████╗░█████╗░███████╗\033[0m
                            \033[32m╚══██╔══╝██║██╔══██╗\033[0m\033[34m  ╚══██╔══╝██╔══██╗██╔══██╗\033[0m\033[31m  ╚══██╔══╝██╔══██╗██╔════╝\033[0m
                            \033[32m░░░██║░░░██║██║░░╚═╝\033[0m\033[34m  ░░░██║░░░███████║██║░░╚═╝\033[0m\033[31m  ░░░██║░░░██║░░██║█████╗░░\033[0m
                            \033[32m░░░██║░░░██║██║░░██╗\033[0m\033[34m  ░░░██║░░░██╔══██║██║░░██╗\033[0m\033[31m  ░░░██║░░░██║░░██║██╔══╝░░\033[0m
                            \033[32m░░░██║░░░██║╚█████╔╝\033[0m\033[34m  ░░░██║░░░██║░░██║╚█████╔╝\033[0m\033[31m  ░░░██║░░░╚█████╔╝███████╗\033[0m
                            \033[32m░░░╚═╝░░░╚═╝░╚════╝░\033[0m\033[34m  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░\033[0m\033[31m  ░░░╚═╝░░░░╚════╝░╚══════╝\033[0m""")
    print("""
                                \033[45m\033[30m  ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█   █▀█ █▀█ █▀▀ █▀ █▀     █▀█  \033[49m\033[0m
                                \033[45m\033[30m  ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░   █▀▀ █▀▄ ██▄ ▄█ ▄█     █▀▀  \033[49m\033[0m

                                \033[43m\033[30m  ▀█▀ █▀█   █▀█ █░█ █ ▀█▀     █▀█ █▀█ █▀▀ █▀ █▀      █▀█  \033[49m\033[0m
                                \033[43m\033[30m  ░█░ █▄█   ▀▀█ █▄█ █ ░█░     █▀▀ █▀▄ ██▄ ▄█ ▄█      ▀▀█  \033[49m\033[0m""")
    print("\n" * 6)
    tts("welcome to tic tac toe - its a two player game so don't forget to bring your friend with you")

    while True:
        tts("to play press p -- to quit press q- so enter your choice" + str(name))
        count = 1
        start = input("Enter your Choice : ")
        print()
        if start == "p" or start=="P":
            li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            li2=[]
            print("\033[1m\u0332" + str(li[0]) + "|\u0332" + str(li[1]) + "|\u0332" + str(li[2]) + "\n\u0332" + str(
                li[3]) + "|\u0332" + str(li[4]) + "|\u0332" + str(li[5]) + "\n" + str(li[6]) + "|" + str(
                li[7]) + "|" + str(
                li[8]) + "\033[0m\n")
            Player_one = name
            tts( name+ "What is your friend's name")
            Player_two = input("Player2 name : ")
            print()
            while count <= 9:
                if count % 2 != 0:
                    print(Player_one + " Your Turn")
                    tts(Player_one + "your turn")
                    tts("Enter Position number")
                    i = int(input("Enter Position no: "))
                    if i not in li2 and i in li:
                        li2.append(i)
                        li[i - 1] = "X"
                    else:
                        count-=1
                        print("Enter a valid move")
                        tts(Player_one + "Plz enter a valid move")
                else:
                    print(Player_two + " Your Turn")
                    tts(Player_two + "your turn")
                    tts("Enter Position number")
                    i = int(input("Enter Position no: "))
                    if i not in li2 and i in li:
                        li2.append(i)
                        li[i - 1] = "O"
                    else:
                        count-=1
                        print("Enter a valid move")
                        tts(Player_two + "Plz enter a valid move")
                count = count + 1
                print("\033[1m\u0332" + str(li[0]) + "|\u0332" + str(li[1]) + "|\u0332" + str(li[2]) + "\n\u0332" + str(
                    li[3]) + "|\u0332" + str(li[4]) + "|\u0332" + str(li[5]) + "\n" + str(li[6]) + "|" + str(
                    li[7]) + "|" + str(li[8]) + "\033[0m\n")
                if li[0] == "X" and li[1] == "X" and li[2] == "X":
                    li[0] = "-"
                    li[1] = "-"
                    li[2] = "-"
                    print(Player_one + " Win")
                    tts(Player_one + " Win")
                    break
                elif li[0] == "O" and li[1] == "O" and li[2] == "O":
                    li[0] = "-"
                    li[1] = "-"
                    li[2] = "-"
                    print(Player_two + " Win")
                    tts(Player_two+" Win")
                    break
                elif li[3] == "X" and li[4] == "X" and li[5] == "X":
                    li[3] = "-"
                    li[4] = "-"
                    li[5] = "-"
                    print(Player_one + " Win")
                    tts(Player_one+"Win")
                    break
                elif li[3] == "O" and li[4] == "O" and li[5] == "O":
                    li[3] = "-"
                    li[4] = "-"
                    li[5] = "-"
                    print(Player_two + " Win")
                    tts(Player_two+"Win")
                    break
                elif li[6] == "X" and li[7] == "X" and li[8] == "X":
                    li[6] = "-"
                    li[7] = "-"
                    li[8] = "-"
                    print(Player_one + " Win")
                    tts(Player_one+"Win")
                    break
                elif li[6] == "O" and li[7] == "O" and li[8] == "O":
                    li[6] = "-"
                    li[7] = "-"
                    li[8] = "-"
                    print(Player_two + " Win")
                    tts(Player_two+"Win")
                    break
                if li[0] == "X" and li[3] == "X" and li[6] == "X":
                    li[0] = "|"
                    li[3] = "|"
                    li[6] = "|"
                    print(Player_one + " Win")
                    tts(Player_one+"Win")
                    break
                elif li[0] == "O" and li[3] == "O" and li[6] == "O":
                    li[0] = "|"
                    li[3] = "|"
                    li[6] = "|"
                    print(Player_two + " Win")
                    tts(Player_two + "Win")
                    break
                elif li[1] == "X" and li[4] == "X" and li[7] == "X":
                    li[1] = "|"
                    li[4] = "|"
                    li[7] = "|"
                    print(Player_one + " Win")
                    tts(Player_one + " Win")
                    break
                elif li[1] == "O" and li[4] == "O" and li[7] == "O":
                    li[1] = "|"
                    li[4] = "|"
                    li[7] = "|"
                    print(Player_two + " Win")
                    tts(Player_two + "Win")
                    break
                elif li[2] == "X" and li[5] == "X" and li[8] == "X":
                    li[2] = "|"
                    li[5] = "|"
                    li[8] = "|"
                    print(Player_one + " Win")
                    tts(Player_one + " Win")
                    break
                elif li[2] == "O" and li[5] == "O" and li[8] == "O":
                    li[2] = "|"
                    li[5] = "|"
                    li[8] = "|"
                    print(Player_two + " Win")
                    tts(Player_two + "Win")
                    break

                elif li[0] == "X" and li[4] == "X" and li[8] == "X":
                    li[0] = "\\"
                    li[4] = "\\"
                    li[8] = "\\"
                    print(Player_one + " Win")
                    tts(Player_one + " Win")
                    break
                elif li[0] == "O" and li[4] == "O" and li[8] == "O":
                    li[0] = "\\"
                    li[4] = "\\"
                    li[8] = "\\"
                    print(Player_two + " Win")
                    tts(Player_two + "Win")
                    break
                elif li[2] == "X" and li[4] == "X" and li[6] == "X":
                    li[2] = "/"
                    li[4] = "/"
                    li[6] = "/"
                    print(Player_one + " Win")
                    tts(Player_one + " Win")
                    break
                elif li[2] == "O" and li[4] == "O" and li[6] == "O":
                    li[2] = "/"
                    li[4] = "/"
                    li[6] = "/"
                    print(Player_two + " Win")
                    tts(Player_two+"Win")
                    break
            print("\033[1m\u0332" + str(li[0]) + "|\u0332" + str(li[1]) + "|\u0332" + str(li[2]) + "\n\u0332" + str(
                li[3]) + "|\u0332" + str(li[4]) + "|\u0332" + str(li[5]) + "\n" + str(li[6]) + "|" + str(
                li[7]) + "|" + str(
                li[8]) + "\033[0m\n")
        elif start == "Q" or start == "q":
            break
        else:
            tts("please give input from the menu only")
            print("Please give input from the main menu only")
    print("Quiting in 3", end="")
    time.sleep(1)
    print("\b2", end="")
    time.sleep(1)
    print("\b1", end="")
    time.sleep(1)
    print("\rGame Over      ")
    tts(" game over - taking you back to main menu")
def rps():
    def emoj(n):
        if n == 1:
            return "🪨"
        elif n == 2:
            return "📃"
        elif n == 3:
            return "✂️"

    print("\n" * 4)
    print("""
                                            \033[32m██████╗░\033[0m      \033[34m██████╗░\033[0m     \033[31m░██████╗\033[0m
                                            \033[32m██╔══██╗\033[0m      \033[34m██╔══██╗\033[0m     \033[31m██╔════╝\033[0m
                                            \033[32m██████╔╝\033[0m      \033[34m██████╔╝\033[0m     \033[31m╚█████╗░\033[0m
                                            \033[32m██╔══██╗\033[0m      \033[34m██╔═══╝░\033[0m     \033[31m░╚═══██╗\033[0m
                                            \033[32m██║░░██║\033[0m      \033[34m██║░░░░░\033[0m     \033[31m██████╔╝\033[0m
                                            \033[32m╚═╝░░╚═╝\033[0m      \033[34m╚═╝░░░░░\033[0m     \033[31m╚═════╝░\033[0m""")
    print("""
                    \033[45m\033[30m  █▀▀ █▀█ █▀█   █▀█ █▀█ █▀   █▀█ █▀█ █▀▀ █▀ █▀             ▄█ ░░▄▀ ▀█ ░░▄▀ ▀█  \033[49m\033[0m
                    \033[45m\033[30m  █▀░ █▄█ █▀▄   █▀▄ █▀▀ ▄█   █▀▀ █▀▄ ██▄ ▄█ ▄█             ░█ ▄▀░░ █▄ ▄▀░░ ▄█  \033[49m\033[0m

                    \033[43m\033[30m  ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█ ░░▄▀ █▀█ █░█ █ ▀█▀                       █▀█ ░░▄▀ █▀█  \033[49m\033[0m
                    \033[43m\033[30m  ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░ ▄▀░░ ▀▀█ █▄█ █ ░█░                       █▀▀ ▄▀░░ ▀▀█  \033[49m\033[0m""")
    print("\n" * 6)
    tts("welcome to Rock Paper scissors - to input rock press 1- for paper press 2 and for scissors press 3 - to play press p and to quit the game press q")
    Flag = True
    while Flag == True:
        tts("do you want to play or quit - please enter your choice")
        start = input("Do you want to play/quit : ")
        if start == "p":
            print("there will three be three rounds of rock paper scissors between us,so get ready",end="")
            tts("there will be three rounds of rock paper scissors between us- so get ready")
            print("\r                                                                       ")
            u = 3
            sp = 0
            sc = 0
            while u > 0:
                print()
                print("ROCK", end="")
                ttf("ROCK")
                print("\rPAPER", end="")
                ttf("PAPER")
                print("\rSCISSORS", end="")
                ttf("SCISSORS")
                print("\rSHOOT    ", end="")
                ttf("SHOOT")
                print("\r         ")
                tts("Choose any one of the rock paper and scissors")
                a = int(input("Enter Your choice : "))
                if a>=1 and a<=3:
                    p = emoj(a)
                    c = emoj(random.randint(1, 3))
                    print(p + "  " + c, end="")
                    time.sleep(2)
                    print()
                    if p == c:
                        print("Its a Draw")
                        tts("its a draw")
                        u += 1
                    elif p == "🪨" and c == "✂️" or p == "✂️" and c == "📃" or p == "📃" and c == "🪨":
                        print("You Win this one 🥺")
                        tts("You win this one")
                        sp += 1
                    else:
                        print("Haha! I Win this one 😏")
                        tts("Haha! I win this one")
                        sc+=1

                else:
                    tts("please enter a valid move")
                    u+=1
                u -= 1
            tts("the score is given below")
            print("\nScore is : " + str(sp) + " - " + str(sc), end="")
            time.sleep(3)
            if sp > sc:
                print("\r\033[1mYou are the winner 🥺        \033[0m")
                tts("You are the winner")
            elif sc > sp:
                print("\r\033[1mI am the winner 😎🏆\033[0m")
                tts("I am the winner")
            else:
                print("\r\033[1mIts a Draw          \033[0m")
        elif start == "Q" or start == "q":
            Flag = False
        else:
            tts("please give input from the menu only")
            print("Please give input from the main menu only")
    print()
    print("Quiting in 3", end="")
    time.sleep(1)
    print("\b2", end="")
    time.sleep(1)
    print("\b1", end="")
    time.sleep(1)
    print("\rGame Over     ")
    tts(" game over - taking you back to main menu")
def minesweeper():
    print("\n" * 4)
    print("""
                    \033[32m███╗░░░███╗██╗███╗░░██╗███████╗░██████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░███████╗██████╗░\033[0m
                    \033[32m████╗░████║██║████╗░██║██╔════╝██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗\033[0m
                    \033[32m██╔████╔██║██║██╔██╗██║█████╗░░╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░██████╔╝█████╗░░██████╔╝\033[0m
                    \033[32m██║╚██╔╝██║██║██║╚████║██╔══╝░░░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░██╔══██╗\033[0m
                    \033[32m██║░╚═╝░██║██║██║░╚███║███████╗██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░░░░███████╗██║░░██║\033[0m
                    \033[32m╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝\033[0m""")
    print("""
                                \033[45m\033[30m  ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█   █▀█ █▀█ █▀▀ █▀ █▀     █▀█  \033[49m\033[0m
                                \033[45m\033[30m  ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░   █▀▀ █▀▄ ██▄ ▄█ ▄█     █▀▀  \033[49m\033[0m

                                \033[43m\033[30m  ▀█▀ █▀█   █▀█ █░█ █ ▀█▀     █▀█ █▀█ █▀▀ █▀ █▀      █▀█  \033[49m\033[0m
                                \033[43m\033[30m  ░█░ █▄█   ▀▀█ █▄█ █ ░█░     █▀▀ █▀▄ ██▄ ▄█ ▄█      ▀▀█  \033[49m\033[0m""")
    print("\n" * 6)
    tts("welcome to minesweeper- to play press p - to quit press q")

    while True:
        tts("Do you want to play or quit")
        us=input("Do you want to play/quit : ").strip()
        if us=="P" or us=="p":
            tts("i have hidden bombs according to the difficulty levels- so Enter your choice")
            user_input = input("Easy Average or Difficult (e/m/d) : ").strip()
            if user_input == "E" or user_input == "e":
                g = [("   1", " 2", " 3", " 4", " 5"),
                     [("1 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("2 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("3 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("4 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("5 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"]]
                g2 = [("   1", " 2", " 3", " 4", " 5"),
                      [("1 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("2 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("3 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("4 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("5 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"]]
                count = 0
                while count < 3:
                    i1 = random.randint(1, 5)
                    i2 = random.randint(1, 5)
                    if g[i1][i2] == "\033[41m💣\033[0m":
                        continue
                    else:
                        g[i1][i2] = "\033[41m💣\033[0m"
                        count += 1
                count = 0
                score = 0
                for i in g2:
                    for j in i:
                        print(j, end="")
                    print()
                while True:
                    print("Enter the row and column separated with space : ")
                    tts("Enter the row and column separated with space : ")
                    s = input().split()
                    print()
                    nrows = int(s[0])
                    mcols = int(s[1])
                    if nrows>=1 and nrows<=5 and mcols>=1 and mcols<=5:
                        if g[nrows][mcols] == "\033[41m💣\033[0m":
                            g2[nrows][mcols] = "\033[41m💣\033[0m"
                            mixer.init()
                            mixer.music.load('D:/blast.mp3')
                            mixer.music.play()
                            for i in g2:
                                for j in i:
                                    print(j, end="")
                                print()
                            print()
                            time.sleep(2)
                            break
                        else:
                            g2[nrows][mcols] = "  "
                            g[nrows][mcols] = "  "
                            mixer.init()
                            mixer.music.load('D:/correct.mp3')
                            mixer.music.play()
                            score += 1
                        for i in g2:
                            for j in i:
                                print(j, end="")
                            print()
                        print()
                    else:
                        print("Enter a valid move\n")
                        tts("enter a valid move")

                for i in g:
                    for j in i:
                        print(j, end="")
                    print()
                mixer.init()
                mixer.music.set_volume(0.15)
                mixer.music.load('D:/mu.mp3')
                mixer.music.play()
                print()
                print("Your Score is : " + str(score) + "/22")
                tts("Your Score is : " + str(score) + "out of 22")
            elif user_input == "m" or user_input == "M":
                g = [("   1", " 2", " 3", " 4", " 5"),
                     [("1 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("2 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("3 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("4 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("5 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"]]
                g2 = [("   1", " 2", " 3", " 4", " 5"),
                      [("1 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("2 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("3 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("4 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("5 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"]]
                count = 0
                while count < 4:
                    i1 = random.randint(1, 5)
                    i2 = random.randint(1, 5)
                    if g[i1][i2] == "\033[41m💣\033[0m":
                        continue
                    else:
                        g[i1][i2] = "\033[41m💣\033[0m"
                        count += 1
                count = 0
                score = 0
                for i in g2:
                    for j in i:
                        print(j, end="")
                    print()
                while True:
                    print("Enter the row and column separated with space : ")
                    tts("Enter the row and column separated with space : ")
                    s = input().split()
                    print()
                    nrows = int(s[0])
                    mcols = int(s[1])
                    if nrows >= 1 and nrows <= 5 and mcols >= 1 and mcols <= 5:
                        if g[nrows][mcols] == "\033[41m💣\033[0m":
                            g2[nrows][mcols] = "\033[41m💣\033[0m"
                            mixer.init()
                            mixer.music.load('D:/.mp3')
                            mixer.music.play()
                            for i in g2:
                                for j in i:
                                    print(j, end="")
                                print()
                            print()
                            time.sleep(2)
                            break
                        else:
                            g2[nrows][mcols] = "  "
                            g[nrows][mcols] = "  "
                            mixer.init()
                            mixer.music.load('D:/correct.mp3')
                            mixer.music.play()
                            score += 1
                        for i in g2:
                            for j in i:
                                print(j, end="")
                            print()
                        print()
                    else:
                        print("Enter a valid move\n")
                        tts("enter a valid move")

                for i in g:
                    for j in i:
                        print(j, end="")
                    print()
                mixer.init()
                mixer.music.set_volume(0.15)
                mixer.music.load('D:/mu.mp3')
                mixer.music.play()
                print()
                print("Your Score is : " + str(score) + "/21")
                tts("Your Score is : " + str(score) + "out of 21")
            elif user_input == "d" or user_input == "D":
                g = [("   1", " 2", " 3", " 4", " 5"),
                     [("1 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("2 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("3 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("4 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"],
                     [("5 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                      "\033[42m  \033[0m"]]
                g2 = [("   1", " 2", " 3", " 4", " 5"),
                      [("1 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("2 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("3 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("4 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"],
                      [("5 "), "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m", "\033[42m  \033[0m",
                       "\033[42m  \033[0m"]]
                count = 0
                while count < 5:
                    i1 = random.randint(1, 5)
                    i2 = random.randint(1, 5)
                    if g[i1][i2] == "\033[41m💣\033[0m":
                        continue
                    else:
                        g[i1][i2] = "\033[41m💣\033[0m"
                        count += 1
                count = 0
                score = 0
                for i in g2:
                    for j in i:
                        print(j, end="")
                    print()
                while True:
                    print("Enter the row and column separated with space : ")
                    tts("Enter the row and column separated with space : ")
                    s = input().split()
                    print()
                    nrows = int(s[0])
                    mcols = int(s[1])
                    if nrows >= 1 and nrows <= 5 and mcols >= 1 and mcols <= 5:
                        if g[nrows][mcols] == "\033[41m💣\033[0m":
                            g2[nrows][mcols] = "\033[41m💣\033[0m"
                            mixer.init()
                            mixer.music.load('D:/blast.mp3')
                            mixer.music.play()
                            for i in g2:
                                for j in i:
                                    print(j, end="")
                                print()
                            print()
                            time.sleep(2)
                            break
                        else:
                            g2[nrows][mcols] = "  "
                            g[nrows][mcols] = "  "
                            mixer.init()
                            mixer.music.load('D:/correct.mp3')
                            mixer.music.play()
                            score += 1
                        for i in g2:
                            for j in i:
                                print(j, end="")
                            print()
                        print()
                    else:
                        print("Enter a valid move\n")
                        tts("enter a valid move")
                for i in g:
                    for j in i:
                        print(j, end="")
                    print()
                mixer.init()
                mixer.music.set_volume(0.15)
                mixer.music.load('D:/mu.mp3')
                mixer.music.play()
                print()
                print("Your Score is : " + str(score) + "/20")
                tts("Your Score is : " + str(score) + "out of 20")
        elif us=="q" or us=="Q":
            break
        else:
            print("Please enter input from the menu")
            tts("please enter input from the menu")
    print("Quiting in 3", end="")
    time.sleep(1)
    print("\b2", end="")
    time.sleep(1)
    print("\b1", end="")
    time.sleep(1)
    print("\rGame Over      ")
    tts(" game over - taking you back to main menu")
def fastestfinger():
    print("\n" * 4)
    print("""
            \033[32m███████╗░█████╗░░██████╗████████╗███████╗░██████╗████████╗\033[0m \033[34m ███████╗██╗███╗░░██╗░██████╗░███████╗██████╗░\033[0m
            \033[32m██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝\033[0m \033[34m ██╔════╝██║████╗░██║██╔════╝░██╔════╝██╔══██╗\033[0m
            \033[32m█████╗░░███████║╚█████╗░░░░██║░░░█████╗░░╚█████╗░░░░██║░░░\033[0m \033[34m █████╗░░██║██╔██╗██║██║░░██╗░█████╗░░██████╔╝\033[0m
            \033[32m██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░\033[0m \033[34m ██╔══╝░░██║██║╚████║██║░░╚██╗█╔══╝░░░██╔══██╗\033[0m
            \033[32m██║░░░░░██║░░██║██████╔╝░░░██║░░░███████╗██████╔╝░░░██║░░░\033[0m \033[34m ██║░░░░░██║██║░╚███║╚██████╔╝███████╗██║░░██║\033[0m
            \033[32m╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░\033[0m \033[34m ╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝\033[0m""")
    print("""
                                    \033[45m\033[30m  ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█   █▀█ █▀█ █▀▀ █▀ █▀     █▀█  \033[49m\033[0m
                                    \033[45m\033[30m  ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░   █▀▀ █▀▄ ██▄ ▄█ ▄█     █▀▀  \033[49m\033[0m

                                    \033[43m\033[30m  ▀█▀ █▀█   █▀█ █░█ █ ▀█▀     █▀█ █▀█ █▀▀ █▀ █▀      █▀█  \033[49m\033[0m
                                    \033[43m\033[30m  ░█░ █▄█   ▀▀█ █▄█ █ ░█░     █▀▀ █▀▄ ██▄ ▄█ ▄█      ▀▀█  \033[49m\033[0m""")
    print("\n"*5)
    tts(" this is the fastest finger - ")
    while True:
        tts("to play press p - to quit press q")
        tts("do you want to play or quit")
        us4=input("Do you want to play/quit : ")
        if us4=="P" or us4=="p":
            print("You have to press the stop button when your name appears on the screen to win.")
            tts("You have to press the stop button when your name appears on the screen to win.")
            li = ["rakshit", "priyam", "purav", "priyank", "rachit","ramesh","suresh"]
            li.append(name)

                # Create an instance of tkinter frame or window
            flag=True
            win = Tk()

            running = True

                # Define a function to print the text in a loop
            def print_text():
                global x
                x = li[random.randint(0, len(li) - 1)]
                if running:
                    print(f"\r {x}", end="")
                    win.after(700, print_text)

                # Define a function to stop the loop
            def on_stop():
                global running
                global x
                running = False
                if x == name:
                    print("\n You won 🎊")
                    tts("You won")
                    win.destroy()
                else:
                    print("\n👍🏻Better luck next time")
                    tts("Better luck next time")
                    win.destroy()

                # to customise the button
            stop = Button(win, text="""█▀ ▀█▀ █▀█ █▀█\n▄█ ░█░ █▄█ █▀▀""")
            stop.config(command=on_stop)
            stop.config(font=('', 20, 'bold'))
            stop.config(bg='#FFFF00')
            stop.config(fg='#000000')
            stop.config(activebackground='#ff0000')
            stop.config(activeforeground='#000000')
            stop.pack(padx=10, pady=10)

            # Run a function to print text in window
            win.after(1000, print_text)

            win.mainloop()
            time.sleep(3)
        elif us4=="q" or us4=="Q":
            break
        else:
            print("Please enter input from the menu")
            tts("please enter input from the menu")
    print("Quiting in 3", end="")
    time.sleep(1)
    print("\b2", end="")
    time.sleep(1)
    print("\b1", end="")
    time.sleep(1)
    print("\rGame Over      ")
    tts(" game over - taking you back to main menu")
def wel():
    print("""

                                    \033[34m░██████╗\033[0m\033[31m░░█████╗\033[0m\033[33m░███╗░░░███╗\033[0m\033[32m███████╗\033[0m\033[31m  ██╗░░██╗\033[0m\033[34m██╗░░░██╗\033[0m\033[32m██████╗░\033[0m
                                    \033[34m██╔════╝\033[0m\033[31m░██╔══██╗\033[0m\033[33m████╗░████║\033[0m\033[32m██╔════╝\033[0m\033[31m  ██║░░██║\033[0m\033[34m██║░░░██║\033[0m\033[32m██╔══██╗\033[0m
                                    \033[34m██║░░██╗\033[0m\033[31m░███████║\033[0m\033[33m██╔████╔██║\033[0m\033[32m█████╗░░\033[0m\033[31m  ███████║\033[0m\033[34m██║░░░██║\033[0m\033[32m██████╦╝\033[0m
                                    \033[34m██║░░╚██╗\033[0m\033[31m██╔══██║\033[0m\033[33m██║╚██╔╝██║\033[0m\033[32m██╔══╝░░\033[0m\033[31m  ██╔══██║\033[0m\033[34m██║░░░██║\033[0m\033[32m██╔══██╗\033[0m
                                    \033[34m╚██████╔╝\033[0m\033[31m██║░░██║\033[0m\033[33m██║░╚═╝░██║\033[0m\033[32m███████╗\033[0m\033[31m  ██║░░██║\033[0m\033[34m╚██████╔╝\033[0m\033[32m██████╦╝\033[0m
                                    \033[34m░╚═════╝░\033[0m\033[31m╚═╝░░╚═╝\033[0m\033[33m╚═╝░░░░░╚═╝\033[0m\033[32m╚══════╝\033[0m\033[31m  ╚═╝░░╚═╝\033[0m\033[34m░╚═════╝░\033[0m\033[32m╚═════╝░\033[0m""")
    print("""                                                                              BY CODE BLASTERS💣""")
    print("""                \033[42m\033[30m  ▀█▀ █ █▀▀   ▀█▀ ▄▀█ █▀▀   ▀█▀ █▀█ █▀▀                                   ▀█▀  \033[49m\033[0m
                \033[42m\033[30m  ░█░ █ █▄▄   ░█░ █▀█ █▄▄   ░█░ █▄█ ██▄                                   ░█░  \033[49m\033[0m

                \033[44m\033[30m  █▀▀ █░█ █▀▀ █▀ █▀ █ █▄░█ █▀▀   █▄░█ █░█ █▀▄▀█ █▄▄ █▀▀ █▀█                  █▀▀   \033[49m\033[0m
                \033[44m\033[30m  █▄█ █▄█ ██▄ ▄█ ▄█ █ █░▀█ █▄█   █░▀█ █▄█ █░▀░█ █▄█ ██▄ █▀▄                  █▄█   \033[49m\033[0m

                \033[41m\033[30m  █▀▄▀█ █ █▄░█ █▀▀   █▀ █░█░█ █▀▀ █▀▀ █▀█ █▀▀ █▀█                          █▀▄▀█  \033[49m\033[0m 
                \033[41m\033[30m  █░▀░█ █ █░▀█ ██▄   ▄█ ▀▄▀▄▀ ██▄ ██▄ █▀▀ ██▄ █▀▄                          █░▀░█  \033[49m\033[0m

                \033[45m\033[30m  █▀█ █▀█ █▀▀ █▄▀   █▀█ ▄▀█ █▀█ █▀▀ █▀█   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀          █▀█   \033[49m\033[0m
                \033[45m\033[30m  █▀▄ █▄█ █▄▄ █░█   █▀▀ █▀█ █▀▀ ██▄ █▀▄   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█          █▀▄   \033[49m\033[0m

                \033[43m\033[30m  █▀▀ ▄▀█ █▀ ▀█▀ █▀▀ █▀ ▀█▀     █▀▀ █ █▄░█ █▀▀ █▀▀ █▀█                     █▀▀   \033[49m\033[0m
                \033[43m\033[30m  █▀░ █▀█ ▄█ ░█░ ██▄ ▄█ ░█░     █▀░ █ █░▀█ █▄█ ██▄ █▀▄                     █▀░   \033[49m\033[0m

                \033[46m\033[30m  █▀▄▀█ █░█ █▀ █ █▀▀   █▀█ █░░ ▄▀█ █▄█ ░░▄▀ █▀█ ▄▀█ █░█ █▀ █▀▀                    █▀█   \033[49m\033[0m
                \033[46m\033[30m  █░▀░█ █▄█ ▄█ █ █▄▄   █▀▀ █▄▄ █▀█ ░█░ ▄▀░░ █▀▀ █▀█ █▄█ ▄█ ██▄                    █▀▀   \033[49m\033[0m""")
while True:
    wel()
    tts("welcome to Game Hub - the world of gaming - Please enter your name")
    name=input("Enter your Name :")
    tts("nice name "+name)
    tts(" what would you like to play - for tic tac toe press -t ,  -for guessing numbers press -g , - for minesweeper press -m , for rock paper scissors press -r, for fastest finger press -f  , to play or pause music press-p ,  to quit the main menu press - q")
    tts("So what's Your choice"+name)
    count=0
    countwin = 0
    while True:
        if countwin==1:
            wel()
            choice=input("Enter your Choice : ")
            if choice=="t" or choice=="T":
                loading()
                tictactoe()
                countwin=1
            elif choice=="g" or choice=="G":
                loading()
                guessingnumber()
                countwin=1
            elif choice=="m" or choice=="M":
                loading()
                minesweeper()
                countwin=1
            elif choice=="r" or choice=="R":
                loading()
                rps()
                countwin=1
            elif choice=="f" or choice=="F":
                loading()
                fastestfinger()
                countwin=1
            elif (choice=="p" or choice=="P") and count%2==0:
                mixer.music.pause()
                tts(" the music is now paused-  plz enter your choice again")
                count+=1
            elif (choice=="p" or choice=="P") and count%2!=0:
                mixer.music.play()
                tts("Playing music -  plz enter your choice")
                count+=1
            elif choice=="q":
                break
            else:
                tts("Enter a Choice from main menu only")
        else:
            choice = input("Enter your Choice : ")
            if choice == "t" or choice == "T":
                countwin = 1
                loading()
                tictactoe()
            elif choice == "g" or choice == "G":
                countwin = 1
                loading()
                guessingnumber()
            elif choice == "m" or choice == "M":
                loading()
                minesweeper()
                countwin=1
            elif choice == "r" or choice == "R":
                countwin = 1
                loading()
                rps()
            elif choice == "f" or choice == "F":
                loading()
                fastestfinger()
                countwin=1
            elif (choice == "p" or choice == "P") and count % 2 == 0:
                mixer.music.pause()
                tts(" the music is now paused-  plz enter your choice again")
                count += 1
            elif (choice == "p" or choice == "P") and count % 2 != 0:
                mixer.music.play()
                tts("Playing music -  plz enter your choice")
                count += 1
            elif choice == "q" or choice=="Q":
                break
            else:
                tts("Enter a Choice from main menu only")

    break
st=datetime.datetime.now()
tts("below is the given time period in which you have played game on our server")
print()
print(f"Today you did gaming for {st-et} seconds")