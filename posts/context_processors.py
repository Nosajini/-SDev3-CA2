from .models import Board

def menu_links(request):
    links = Board.objects.all()
    return dict(links=links)
