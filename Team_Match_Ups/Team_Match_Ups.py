import os
from itertools import combinations

path = os.path.dirname(os.path.abspath(__file__))
with open(path+'/teams.txt', 'r') as f:
    teams = [line.strip() for line in f]

matchup_t_list = list(combinations(teams, 2))

with open(path+'/matchups.txt', mode='wt', encoding='utf-8') as new_file:
    for game in matchup_t_list:
        new_file.write("{} vs {}\n".format(game[0], game[1]))


# match_ups = []
# for f_team in teams:
#     first_team = f_team
#     for s_team in teams:
#         second_team = s_team
#         game = "{} vs {}".format(first_team, second_team)
#         match_ups.append(game)

# with open(path+'/matchups.txt', mode='wt', encoding='utf-8') as new_file:
#     for game in match_ups:
#         new_file.write("{}\n".format(game))
