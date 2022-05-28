class Student:
    Name=str()
    Age=float()
    Tracks=["MD","WD","CE"]
    Score=float()

    # [assignment] Skeleton class. Add your code here
    def __init__(self,Name,Age,Tracks,Score):
        self.Name=Name
        self.Age=Age
        self.Tracks=Tracks
        self.Score=Score
    pass
    def change_name(self):
        print('Peter')
    def change_age(self):
        print(34) 
    def add_track(self):
        print("UI/UX") 
    def get_score(self):
        print("34.0")



Bob = Student(Name="Bob", Age=26, Tracks=["FE","BE"],Score=20.90)
print(Bob.Name)
Bob.change_name()
print(Bob.Age)
Bob.change_age()
print(Bob.Tracks)
Bob.add_track()
print(Bob.Score)
Bob.get_score()

  

