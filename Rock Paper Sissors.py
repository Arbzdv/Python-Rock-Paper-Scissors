#FOR SQL SERVER LATER
#docker run -e 'ACCEPT_EULA-Y' -e 'SA-PASSWORD=8746arbzdv' -e 'MSSQL_PID=Express' -p 1433:1433 -d mcr.microsoft.com/mssql/server: 
import getpass, os
import mysql.connector
from mysql.connector import Error
import pandas as pd

def Player():
    global player1
    player1 = input('Player 1, what is your name? : ')
    play1 = player1
    global player2
    player2 = input('Player 2, what is your name? : ')
    play2 = player2 
Player()


def win1():
    global winScore1
    winScore1 = 0
    winScore1 = winScore1 +1
    print(player1,'You have won',winScore1,'games')
    print(player1,'You have lost',lossScore1,'games')
# def loss1():
#     global lossScore1
#     lossScore1 = 0
#     lossScore1 = lossScore1 +1
#     print(player1,'You have won',winScore1,'games')
#     print(player1,'You have lost',lossScore1,'games')
def win2():
    global winScore2
    winScore2 = 0
    winScore2 = winScore2 +1
    print(player2,'You have won',winScore2,'games')
    # print(player2,'You have lost',lossScore2,'games')
# def loss2():
#     global lossScore2
#     lossScore2 = 0
#     lossScore2 = lossScore2 +1
#     print(player2,'You have won',winScore2,'games')
#     print(player2,'You have lost',lossScore2,'games')
#scoreboard function
def scoreboard():
    print('Are you player 1 or player 2?')
    print('Enter 1 for player 1, enter 2 for player 2')
    playerNum = int(input('What is your choice? (1 or 2)'))
    if playerNum == 1:
        

    

def console():
    print("What would you like to do?")
    print("1. New Game")
    print("2. Show scoreboard ")


def GameEngine():
    R = "Rock"
    r = "rock"
    P = "Paper"
    p = "paper"
    S = "Scissors"
    s = "scissors"
    #Head UI anf title 
    print()
    print()
    print()
    print("                       |--------------------------------|")
    print("                       | Welcome To Rock Paper Scissors |")
    print("                       |--------------------------------|")
    print("")
    print("")
    print("     Directions: Play with two people! Player 1 goes first.")
    print("")
    print("                Enter Rock Paper or Scissors to select your move...")
    print("")
    print("")

    #blank space printer


    #player 1 input
    print(player1,"It is your turn!")
    play1 = getpass.getpass("     Rock, Paper, or Scissors?: ", stream = None)
    os.system('cls')
    print()

    if play1 == R:
        print("    your answer has been stored, now it is the other players turn")
        print()
    elif play1 == r:
        print("    your answer has been stored, now it is the other players turn")
        print()
    elif play1 == P:
        print("    your answer has been stored, now it is the other players turn")
        print()
    elif play1 == p:
        print("    your answer has been stored, now it is the other players turn")
        print()
    elif play1 == S:
        print("    your answer has been stored, now it is the other players turn")
        print()
    elif play1 == s:
        print("    your answer has been stored, now it is the other players turn")
        print()
    #to hide first player input from player 2print("")
    print("")
    print()
    
    #prompt player 2 for input
    print("Answer stored, player 2 it is your turn!")
    #player 2 input
    play2 = getpass.getpass("Rock, Paper, or Scissors?: ", stream = None)
    os.system('cls')


    if play2 == R:
        print("   your answer has been stored, now it is the other players turn")
        print()
    elif play2 == r:
        print("   your answer has been stored, now it is the other players turn")
        print()
    elif play2 == P:
        print("   your answer has been stored, now it is the other players turn")
        print()
    elif play2 == p:
        print("   your answer has been stored, now it is the other players turn")
        print()
    elif play2 == S:
        print("   your answer has been stored, now it is the other players turn")
        print()
    elif play2 == s:
        print("   your answer has been stored, now it is the other players turn")
        print()
    #game engine

    #ties
    if play1 == R and play2 == R:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    if play1 == r and play2 == r:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    if play1 == R and play2 == r:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
    if play1 == r and play2 == R:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == P and play2 == P:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == p and play2 == p:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == p and play2 == P:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == P and play2 == p:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == S and play2 == S:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == s and play2 == s:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == S and play2 == s:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    elif play1 == s and play2 == S:
        print("")
        print()
        print("                       |--------------------------------|")
        print("                       |             Tie Game!          |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
    



    #player 1 winning
    elif play1 == P and play2 == R:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == p and play2 == r:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == P and play2 == r:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == p and play2 == R:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == R  and play2 == S :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == r  and play2 == s :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == R  and play2 == S :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == r  and play2 == S :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == S and play2 == P :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == s and play2 == p :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == S and play2 == p :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()
    elif play1 == s and play2 == P :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 1 Wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win1()


    #player 2 wins 
    elif play2 == P and play1 == R:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == p and play1 == r:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == P and play1 == r:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == p and play1 == R:
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == R and play1 == S :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == r and play1 == s :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == R and play1 == s :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        win2()
    elif play2 == r and play1 == S :
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        win2()
    elif play2 == S and play1 == P :
        print()
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == s and play1 == p :
        print()
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == S and play1 == p :
        print()
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    elif play2 == s and play1 == P :
        print()
        print()
        print("                       |--------------------------------|")
        print("                       |          Player 2 wins!        |")
        print("                       |--------------------------------|")
        print("")
        print()
        print()
        print()
        print()
        print()
        win2()
    print()
    do_again = input( "Would you like to play again? (yes/no): ")
    print()
    if do_again == "Yes":
        GameEngine()
    elif do_again == "yes":
        GameEngine()
    else:
        print("RAGE QUIT!")
        exit()
