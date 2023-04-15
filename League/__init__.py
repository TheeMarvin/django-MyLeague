import random

# Define a list of 20 random team names
team_names = ['Raptors', 'Spartans', 'Tigers', 'Vikings', 'Pirates', 'Panthers', 'Sharks', 'Dragons', 'Falcons', 'Jaguars', 'Thunder', 'Warriors', 'Gladiators', 'Lions', 'Cobras', 'Eagles', 'Hawks', 'Scorpions', 'Rhinos', 'Wolves']

# Define a dictionary to store the results of each team
team_results = {}
for team in team_names:
    team_results[team] = {'played': 0, 'won': 0, 'drawn': 0, 'lost': 0, 'goals_for': 0, 'goals_against': 0, 'points': 0}

# Simulate the league
for i in range(190):
    # Select two random teams to play against each other
    team1, team2 = random.sample(team_names, 2)
    # Generate a random scoreline
    goals1, goals2 = random.randint(0, 5), random.randint(0, 5)
    # Update the team results with the outcome of the match
    team_results[team1]['played'] += 1
    team_results[team2]['played'] += 1
    team_results[team1]['goals_for'] += goals1
    team_results[team2]['goals_for'] += goals2
    team_results[team1]['goals_against'] += goals2
    team_results[team2]['goals_against'] += goals1
    if goals1 > goals2:
        team_results[team1]['won'] += 1
        team_results[team1]['points'] += 3
        team_results[team2]['lost'] += 1
    elif goals1 < goals2:
        team_results[team2]['won'] += 1
        team_results[team2]['points'] += 3
        team_results[team1]['lost'] += 1
    else:
        team_results[team1]['drawn'] += 1
        team_results[team1]['points'] += 1
        team_results[team2]['drawn'] += 1
        team_results[team2]['points'] += 1

# Sort the teams by points and goals difference
sorted_teams = sorted(team_results.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=True)

# Display the league table
print('League Table')
print('{:<4} {:<15} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}'.format('Pos', 'Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'Pts'))
for i, (team, results) in enumerate(sorted_teams):
    print('{:<4} {:<15} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}'.format(i+1, team, results['played'], results['won'], results['drawn'], results['lost'], results['goals_for'], results['goals_against'], results['points']))
