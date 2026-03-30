class Team():
    def __init__(self, name):
        self.name = name
        self.players = []
    
    def add_player(self,name,score):
        return self.players.append({
            "name":name,
            "score":score
        })
   
    def __len__(self):
        return len(self.players)
    
    def __str__(self):
        najveci = max(player["score"] for player in self.players)
        return f"Team {self.name}: {len(self.players)} players, top score: {najveci}  "
    
    def __repr__(self):
        return f"Team('{self.name}', {len(self.players)} players)"
    
    def __contains__(self, name):
        return any(player['name']==name for player in self.players)
    
    def __getitem__(self, index):
        return self.players[index]
    
    def __add__(self, other):
        new_team = Team("All Stars")
        new_team.players = self.players + other.players
        return new_team
    
    def __eq__(self, other):
      return (len(self.players) == len(other.players) and
        sum(p["score"] for p in self.players) == sum(p["score"] for p in other.players))    

t1 = Team("Lakers")
t1.add_player("Daris", 95)
t1.add_player("Ana", 88)
t1.add_player("Marko", 72)

t2 = Team("Bulls")
t2.add_player("Ivan", 90)
t2.add_player("Sara", 85)

t3 = Team("Clone")
t3.add_player("X", 95)
t3.add_player("Y", 88)
t3.add_player("Z", 72)

print(len(t1))              # 3
print(t1)                   # Team Lakers: 3 players, top score: 95
print(repr(t1))             # Team('Lakers', 3 players)
print("Daris" in t1)        # True
print("Boris" in t1)        # False
print(t1[0])                # {"name": "Daris", "score": 95}
merged = t1 + t2
print(merged)               # Team All Stars: 5 players, top score: 95
print(t1 == t3)             # True  (same count, same total score)
print(t1 == t2)             # False
        