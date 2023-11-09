from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass


@dataclass
class Team:
    name: str
    info: str
    members: list[str]


Teams = {
    "Management": Team(
        "Management",
        "Management team is in charge of chores and keeping the building in order.",
        ["Nick", "Owen", "Mathew", "Jeremiah", "Ab", "Abigail"],
    ),
    "Community": Team(
        "Community",
        "Community is in charge of events that are done bi weekly",
        ["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
    "Procurement": Team(
        "Procurement",
        "Procurement team is in charge of preparing food for everyone.",
        ["Adrian", "Bryce", "Johnathan", "Blaine", "Wyatt"],
    ),
    "Documentation": Team(
        "Documentation",
        "Documentation team is in charge of documenting everything and posting them online.",
        ["Conner", "Kaleigh", "Blair", "Mina", "Jay", "Joshua", "Kayleah"],
    ),
}


def info(request: HttpRequest, thing: str) -> render:
    context = {"Team": Teams[thing]}
    return render(request, "info.html", context)


def team_(request: HttpRequest) -> HttpResponse:
    context = {"Teams": Teams}
    return render(request, "index.html", context)
