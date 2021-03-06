from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .forms import league_form
from .functions import create_league, current_season, get_espn_league
from .models import *

# Main Page
def index(request):
    return render(request, 'main/index.html')

# Import the test league
def test(request):
    request.session['leagueId'] = 99158049
    request.session['teamId'] = 991580491
    return render(request, 'main/index.html')

# Refresh the league data
def refresh(request):
    # Check if the user currently has a league id stored in cookies
    if request.session['leagueId']:
        user_league = ESPNLeagues.objects.get(league_id=request.session['leagueId'])
        espn_league = get_espn_league(user_league.league_id, current_season, user_league.priv, user_league.espn_s2, user_league.swid)
        if not espn_league.teams:
            return render(request, 'main/error.html', {'error': espn_league})
        else:
            create_league(user_league, espn_league)
        return HttpResponseRedirect(reverse('index'))
    # If not, this function shouldn't be run
    else:
        return render(request, 'main/error.html', {'error': 'Something went wrong.'})

# Show the league page
def league(request):
    league_teams = ESPNTeams.objects.select_related('espnteamaverages').select_related('espnteamstandarddeviations').prefetch_related('espnplayers_set__player__seasonaverages').filter(team_id__startswith=request.session['leagueId'])
    return render(request, 'main/league.html', {'teams': league_teams})

# User chooses their team from the imported league
def success(request):
    if 'teamId' in request.GET:
            try:
                team = ESPNTeams.objects.get(team_id=request.GET.get('teamId'))
            except ESPNTeams.DoesNotExist as e:
                return render(request, 'main/error.html', {'error':'Something went wrong when choosing your team.'})
            request.session['leagueId'] = team.league_id
            request.session['teamId'] = team.team_id
            return render(request, 'main/success.html')
    else:
        return render(request, 'main/error.html', {'error':'Something went wrong.'})

# Searchbar functionality
def search(request):
    # Autocomplete response
    if 'term' in request.GET:
        players = Players.objects.filter(full_name__icontains=request.GET.get('term'))
        suggest = list()
        for player in players:
            suggest.append(player.full_name)
        return JsonResponse(suggest, safe=False)
    
    # Search response on player selection
    if 'player_name' in request.GET:
        players = Players.objects.filter(full_name=request.GET.get('player_name'))
        return HttpResponseRedirect(reverse('player', kwargs={'p_id':players[0].player_id}))

# Import the user's league
def import_league(request):
    
    league_data = league_form(request.POST or None)
    if league_data.is_valid(): 
        
        # Save cookie
        if not request.session.session_key:
            request.session.save()

        # Inputted data
        user_league_id = league_data.cleaned_data['league_id']
        user_priv = league_data.cleaned_data['private']
        user_espn_s2 = league_data.cleaned_data['espn_s2']
        user_swid = league_data.cleaned_data['swid']

        espn_league = get_espn_league(user_league_id, current_season, user_priv, user_espn_s2, user_swid)
        
        # If the retrieved league doesn't have data, then return error
        if not hasattr(espn_league, 'teams'):
            return render(request, 'main/error.html', {'error': "Couldn't retrive this league. Check if it is private or if you have the correct values."})
        else:
            user_league, created = ESPNLeagues.objects.update_or_create(
                league_id=user_league_id,
                defaults={
                    'priv': user_priv,
                    'espn_s2': user_espn_s2,
                    'swid': user_swid
                }
            )
            
            # Retrieve and store league details
            create_league(user_league, espn_league)
            
            setup_teams = ESPNTeams.objects.filter(team_id__startswith=user_league_id)
            setup_players = ESPNPlayers.objects.filter(team__team_id__startswith=user_league_id).order_by('-player__seasonaverages__mins')

            return render(request, 'main/setup.html', {'teams': setup_teams, 'team_players':setup_players})

    return render(request, 'main/import_league.html', {'form': league_data})

# Player profile view
def player(request, p_id):
    try:
        player_data = Players.objects.get(player_id=p_id)
        game_data = Games.objects.filter(player__player_id=player_data.player_id).order_by('-game_date')
        season_data = SeasonAverages.objects.filter(player__player_id=player_data.player_id).first()
        league_stddev = LeagueAverageStandardDeviation.objects.get()
    except Players.DoesNotExist as e:
        return render(request, 'main/error.html', {'error': e})
    # Player has no game data, so just return nothing
    except Games.DoesNotExist as e:
        game_data = None
        season_data = None

    headshot_url = "https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/" + str(player_data.player_id) + ".png"
    
    return render(request, 'main/player.html', {
            'player':player_data,
            'season':season_data,
            'games':game_data, 
            'league_avg_stddev': league_stddev, 
            'picture':headshot_url
        }
    )

# All players list (this should be done better)
def players_list(request, stat):
    
    try:
        if stat == "avg":
            player_data = Players.objects.select_related('seasonaverages').all()
        elif stat == "std":
            player_data = Players.objects.select_related('standarddeviations').all()
    except Players.DoesNotExist as e:
        return render(request, 'main/error.html', {'error': e})
    
    if stat not in ["avg", "std"]:
        return render(request, 'main/error.html')

    return render(request, 'main/players_list.html', {'players':player_data, 'statistic_type':stat})

# Week statistics view
def compare(request, week_num):
    try:
        week_statistics = ESPNWeekStatistics.objects.filter(league__league_id=request.session['leagueId'], week=week_num)
    except ESPNWeekStatistics.DoesNotExist as e:
        return render(request, 'main/error.html', {'error': e})
    
    current_weeks = ESPNWeekStatistics.objects.order_by().values('week').distinct()
    return render(request, 'main/roto.html', {
            'week_statistics': week_statistics, 
            'week_num': week_num, 
            'current_weeks': current_weeks
        }
    )