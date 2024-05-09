"""
Requirements collection
The requirements for Cricinfo are defined below:

R1: The system should be able to track the stats of all (players), (teams), and (matches).
R2: The system should be able to track all scores or wickets that occurred for each ball.
The system should also provide a live commentary for every ball.
R3: The system should be able to keep track of all matches—Test, T20, and ODI matches.
R4: The system should be able to keep track of ongoing and previous tournaments.
The system should also be able to show a points table for all teams participating in a tournament.
R5: The system should be able to show the result of all previous televised matches.
R6: All teams should select some players who will participate in the tournament known as the tournament squad.
R7: For every match, the teams should be able to select 11 players to play on the field from the tournament squad, known as the playing eleven.
R8: The admin of the system should be able to add tournaments, matches, teams, players, and news to the system.
"""

class Player:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

class Match:
    def __init__(self, teams, match_type):
        self.teams = teams
        self.match_type = match_type

class Tournament:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams

class System:
    def __init__(self):
        self.players = []
        self.teams = []
        self.matches = []
        self.tournaments = []

    def add_player(self, player):
        self.players.append(player)

    def add_team(self, team):
        self.teams.append(team)

    def add_match(self, match):
        self.matches.append(match)

    def add_tournament(self, tournament):
        self.tournaments.append(tournament)
        
    def get_player_stats(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player.stats
        return None

    def get_team_stats(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team.players
        return None

    def get_match_stats(self, match_type):
        match_stats = []
        for match in self.matches:
            if match.match_type == match_type:
                match_stats.append(match)
        return match_stats

class Ball:
    def __init__(self, score=None, wicket=False):
        self.score = score
        self.wicket = wicket

class Commentary:
    def __init__(self, ball, commentary):
        self.ball = ball
        self.commentary = commentary

class Match:
    def __init__(self, teams, match_type):
        self.teams = teams
        self.match_type = match_type
        self.balls = []
        self.commentaries = []

    def add_ball(self, ball):
        self.balls.append(ball)

    def add_commentary(self, commentary):
        self.commentaries.append(commentary)

    def get_balls(self):
        return self.balls

    def get_commentaries(self):
        return self.commentaries
    
class TournamentTracker:
    def __init__(self):
        self.ongoing_tournaments = []
        self.previous_tournaments = []

    def add_ongoing_tournament(self, tournament):
        self.ongoing_tournaments.append(tournament)

    def add_previous_tournament(self, tournament):
        self.previous_tournaments.append(tournament)

    def get_ongoing_tournaments(self):
        return self.ongoing_tournaments

    def get_previous_tournaments(self):
        return self.previous_tournaments