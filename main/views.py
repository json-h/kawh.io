from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import league_form
from .functions import get_espn_league, current_season
from .models import *

def index(request):
    return render(request, 'main/index.html')

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
        
        user_session_id = request.session.session_key
        user_league_id = league_data.cleaned_data['league_id']
        user_priv = league_data.cleaned_data['private']
        user_espn_s2 = league_data.cleaned_data['espn_s2']
        user_swid = league_data.cleaned_data['swid']

        league = get_espn_league(user_league_id, current_season, user_priv, user_espn_s2, user_swid)

        if Exception:
            return render(request, 'main/error.html', {'error': league})
        else:
            session_league = Leagues.objects.create(session_id=user_session_id, league_id=user_league_id, priv=user_priv, espn_s2=user_espn_s2, swid=user_swid)
            return HttpResponseRedirect('main/error.html', {'error': 'SUCCESS!!!!!!!!'})

    return render(request, 'main/import_league.html', {'form': league_data})

def player(request, p_id):
    
    try:
        player_data = Players.objects.get(player_id=p_id)
    except Players.DoesNotExist as e:
        return render(request, 'main/error.html', {'error': e})
    
    game_data = Games.objects.filter(player__player_id=player_data.player_id).order_by('-game_date')
    season_data = SeasonAverages.objects.filter(player__player_id=player_data.player_id)

    headshot_url = "https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/" + str(player_data.player_id) + ".png"
    
    return render(request, 'main/player.html', {'player':player_data,'season':season_data[0],'games':game_data,'picture':headshot_url})