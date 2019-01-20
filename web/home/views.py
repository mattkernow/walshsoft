from django.http import HttpResponse
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("WALSHSOFT", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("ROCKS!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]

    renderer = FigletText("ASCIIMATICS", font='big')

    screen.play([Scene(effects, 500)])


def home(request):

    return HttpResponse({'hello': '00000'}, content_type='application/json')

Screen.wrapper(demo)