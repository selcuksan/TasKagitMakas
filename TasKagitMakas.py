from random import *
from Move import *
class Move():
    move=["","",""]
    move[0] = "tas"
    move[1] = "kagit"
    move[2] = "makas"
class Person():
    def __init__(self,name,surname=""):
        self.name=name
        self.surname=surname
        self.point=0
    @staticmethod
    def gainPoint(obje):
        obje.point+=1
    @staticmethod
    def showResults(totalGame):
        print("*************************************")
        print(f"{p1.name}: {p1.point}")
        print(f"{p2.name}: {p2.point}")
        print(f"berabere: {totalGame-(p2.point+p1.point)}")
    @staticmethod
    def playGame(i):
        p1.move=choice(Move.move)
        p2.move=choice(Move.move)
        if p1.move==p2.move:
            print(f"{i+1}.oyun = {p1.name}->{p1.move} || {p2.name}->{p2.move}\nBERABERE")
        elif p1.move=="tas" and p2.move=="kagit":
            print(f"{i+1}.oyun = {p1.name}->{p1.move} || {p2.name}->{p2.move}\n{p2.name} kazandı")
            Person.gainPoint(p2)
        elif p1.move=="tas" and p2.move=="makas":
            print(f"{i+1}.oyun = {p1.name}->{p1.move} || {p2.name}->{p2.move}\n{p1.name} kazandı")
            Person.gainPoint(p1)
        elif p1.move=="makas" and p2.move=="tas":
            print(f"{i+1}.oyun = {p1.name}->{p1.move} || {p2.name}->{p2.move}\n{p2.name} kazandı")
            Person.gainPoint(p2)
        elif p1.move=="makas" and p2.move=="kagit":
            print(f"{i+1}.oyun = {p1.name}->{p1.move} || {p2.name}->{p2.move}\n{p1.name} kazandı")
            Person.gainPoint(p1)
        elif p1.move=="kagit" and p2.move=="makas":
            print(f"{i+1}.oyun = {p1.name}->{p1.move} || {p2.name}->{p2.move}\n{p2.name} kazandı")
            Person.gainPoint(p2)
        elif p1.move=="kagit" and p2.move=="tas":
            print(f"{i+1}.oyun = {p1.name}->{p1.move} || {p2.name}->{p2.move}\n{p1.name} kazandı")
            Person.gainPoint(p1)





p1_name=input("kullanıcı 1: ")
p2_name=input("kullanıcı 2: ")
p1=Person(p1_name)
p2=Person(p2_name)
totalGame=int(input("Kaç defa oynamak istersiniz"))
i=0
while i<totalGame:
    Person.playGame(i)
    i+=1
print("*************************************")
print(f"{totalGame} kez oynandı")
Person.showResults(totalGame)