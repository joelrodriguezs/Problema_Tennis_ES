class Player:
    def __init__(self,name):
        self.player_name = name
        self.player_points = 0
        
    def get_name(self):
        return self.player_name
    
    def get_points(self):
        return self.player_points
    
    def inc_point(self):
        self.player_points = self.player_points + 1
        
    def is_equal(self,player):
        if self.player_name == player.player_name:return True
        else:return False