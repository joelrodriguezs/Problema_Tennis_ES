

class Game:
    def __init__(self,player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        
    def get_score(self):
        points_player_1 = self.player_1.get_points()
        points_player_2 = self.player_2.get_points()
        carac_1 = ""
        carac_2 = ""
        if points_player_1 == points_player_2:
            if (points_player_1 > 0) and (points_player_2) > 0:
                if points_player_1 == 1: return "Fifteen-All"
                if points_player_1 == 2: return "Thirty-All"
                return "Deuce"
            else:
                return "Love-All"

        if points_player_1 > 3 and (points_player_1 > points_player_2):
            if(points_player_1-points_player_2)==1:return "Advantage player1"
            else: return "Win for player1"

        if points_player_2 > 3 and (points_player_1 < points_player_2):
            if (points_player_2 - points_player_1) == 1:
                return "Advantage player2"
            else:return "Win for player2"

        if (points_player_1 == 0): carac_1 = "Love-"
        if (points_player_1 == 1): carac_1 = "Fifteen-"
        if (points_player_1 == 2): carac_1 = "Thirty-"
        if (points_player_1 == 3): carac_1 = "Forty-"

        if (points_player_2 == 0): carac_2 = "Love"
        if (points_player_2 == 1): carac_2 = "Fifteen"
        if (points_player_2 == 2): carac_2 = "Thirty"
        if (points_player_2 == 3): carac_2 = "Forty"

        return carac_1+carac_2






    def won_point(self, player):
        if self.player_1.is_equal(player):
            self.player_1.inc_point()
        else:
            self.player_2.inc_point()
          
        