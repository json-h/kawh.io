from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .forms import league_form
from .functions import get_espn_league, current_season
from .models import *

def index(request):
    return render(request, 'main/index.html')

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


def search(request):
    if 'term' in request.GET:
        players = Players.objects.filter(full_name__istartswith=request.GET.get('term'))
        suggest = list()
        for player in players:
            suggest.append(player.full_name)
        return JsonResponse(suggest, safe=False)
    
    if 'player_name' in request.GET:
        players = Players.objects.filter(full_name=request.GET.get('player_name'))
        return HttpResponseRedirect(reverse('player', kwargs={'p_id':players[0].player_id}))

def import_league(request):
    
    league_data = league_form(request.POST or None)
    if league_data.is_valid(): 
        
        if not request.session.session_key:
            request.session.save()

        user_league_id = league_data.cleaned_data['league_id']
        user_priv = league_data.cleaned_data['private']
        user_espn_s2 = league_data.cleaned_data['espn_s2']
        user_swid = league_data.cleaned_data['swid']

        league = get_espn_league(user_league_id, current_season, user_priv, user_espn_s2, user_swid)
        
        if not league.teams:
            return render(request, 'main/error.html', {'error': league})
        else:
            for team in league.teams:
                appended_id = str(user_league_id)+str(team.team_id)
                
                ESPNTeams.objects.update_or_create(
                    team_id=appended_id, 
                    defaults=
                        {
                            'league_id':user_league_id, # just in case something goes wrong later on
                            'name':team.team_name,
                            'abrv':team.team_abbrev,
                            'division_name':team.division_name,
                            'logo_url':team.logo_url
                        }
                )
                for player in team.roster:
                    try:
                        nba = Players.objects.get(full_name=player.name)
                    except Players.DoesNotExist as e:
                        continue
                    
                    ESPNPlayers.objects.get_or_create(
                        team=ESPNTeams(team_id=appended_id),
                        player=Players(player_id=nba.player_id)
                    )
            
            setup_teams = ESPNTeams.objects.filter(team_id__startswith=user_league_id)
            setup_players = ESPNPlayers.objects.filter(team__team_id__startswith=user_league_id).order_by('-player__seasonaverages__mins')

            return render(request, 'main/setup.html', {'teams': setup_teams, 'team_players':setup_players})

    return render(request, 'main/import_league.html', {'form': league_data})

def player(request, p_id):
    try:
        player_data = Players.objects.get(player_id=p_id)
        game_data = Games.objects.filter(player__player_id=player_data.player_id).order_by('-game_date')
        season_data = SeasonAverages.objects.filter(player__player_id=player_data.player_id).first()
    except Players.DoesNotExist as e:
        return render(request, 'main/error.html', {'error': e})
    except Games.DoesNotExist as e:
        game_data = None
        season_data = None

    headshot_url = "https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/" + str(player_data.player_id) + ".png"
    
    return render(request, 'main/player.html', {'player':player_data,'season':season_data,'games':game_data,'picture':headshot_url})