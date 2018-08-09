'''
This file contains all the sports functions:-
1. Cricket Scores
2. Football Scores
3. Players - Cricket
4. Players - Football
5. Teams - Cricket
6. Teams - Football
'''

def cricket(data):
    api_key = '5UguUkoPgXeISdZ6FqrXZs1o6I33'
    url = {
        'matches_list':'http://cricapi.com/api/matches/',
        'score':'http://cricapi.com/api/cricketScore/',
        'player_stats':'http://cricapi.com/api/playerStats?pid=',
        'ball_by_ball':'http://cricapi.com/api/ballByBall',
        'summary':'http://cricapi.com/api/fantasySummary/'
    }

    
    

