def tally(tournament_results):
    if tournament_results == '':
        return 'Team                           | MP |  W |  D |  L |  P'
    result = {}
    for line in tournament_results.split('\n'):
        result = get_result(result, line)
    result = calculate_score(result)
    sorted_teams = rank_team(result)
    return print_result(sorted_teams, result)

def get_result(current_result, line):
    team1, team2, result = line.split(';')
    team1_result = current_result.setdefault(team1, {'win': 0, 'loss': 0, 'draw': 0})
    team2_result = current_result.setdefault(team2, {'win': 0, 'loss': 0, 'draw': 0})
    if result == 'win':
        team1_result['win'] += 1
        team2_result['loss'] += 1
    elif result == 'draw':
        team1_result['draw'] += 1
        team2_result['draw'] += 1
    else:
        team1_result['loss'] += 1
        team2_result['win'] += 1
    return current_result

def calculate_score(result):
    for team, team_result in result.items():
        team_result['score'] = team_result['win'] * 3 + team_result['draw']
    return result

# Sort team by score
def rank_team(result):
    teams = sorted(result.keys())
    teams.sort(key=lambda team: result[team]['score'], reverse=True)
    return teams

def print_result(sorted_teams, results):
    template = "{0:31}| {1:2} | {2:2} | {3:2} | {4:2} | {5:2}"
    content = [template.format('Team', 'MP', ' W', ' D', ' L', ' P')]
    for team in sorted_teams:
        result = results[team]
        content.append(template.format(team, result['win'] + result['loss'] + result['draw'], result['win'], result['draw'], result['loss'], result['score']))
    return "\n".join(content)
