class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1
 
    def equal_scores(self):
        scoresequal_dict = {0 : "Love-All", 1 : "Fifteen-All", 2 : "Thirty-All"}
        return scoresequal_dict.get(self.player1_score, "Deuce")

    def advantage_or_win(self):
        minus_result = self.player1_score - self. player2_score
        if abs(minus_result) == 1:
            return f"Advantage {'player1' if minus_result > 0 else 'player2'}"
        elif abs(minus_result) >= 2:
            return f"Win for {'player1' if minus_result > 0 else 'player2'}"
        return ""

    def normal_scores(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.player1_score]}-{score_names[self.player2_score]}"

    def get_score(self):
        score = ""
        winning_points = 4

        if self.player1_score == self.player2_score:
            score = self.equal_scores()
    
        elif self.player1_score >= winning_points or self.player2_score >= winning_points:
            score = self.advantage_or_win()
        else:
            score = self.normal_scores()

        return score
