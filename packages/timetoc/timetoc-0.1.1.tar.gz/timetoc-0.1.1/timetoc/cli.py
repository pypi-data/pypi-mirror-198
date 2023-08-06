# from os import environ
import os
from os import environ
from pathlib import Path

import typer
from rich.console import Console
from rich.prompt import Prompt

from timetoc.login import get_acess_token
from timetoc.timeparser import parse_date_range
from timetoc.timetracking import add_work_day

app = typer.Typer()
console = Console()

TIME_TRACK_BASE_URL = os.environ["TIME_TRACK_BASE_URL"]


@app.command()
def main():
    token_file = Path("./token_file")
    if token_file.is_file():
        access_token = open(token_file).readlines(0)[0]
    else:
        console.print("token file not found!", style="red")
        access_token = access_token_by_login()

    day_str = Prompt.ask("Day", default="yesterday")
    days = parse_date_range(day_str)
    for day in days:
        console.print("Day: ", day, style="bold red")
        start = Prompt.ask("Start Time", default="09:00")
        finish = Prompt.ask("Finish Time", default="17:00")
        break_start = Prompt.ask("Break Start", default="12:00")
        break_finish = Prompt.ask("Break Finish", default="13:00")
        is_home_office = typer.confirm("Is Home Office?", default=True)

        try:
            add_work_day(
                day=day,
                start=start,
                finish=finish,
                break_start=break_start,
                break_finish=break_finish,
                is_home_office=is_home_office,
                token=access_token,
            )
        except:
            console.print("Token expired please login again")
            access_token = access_token_by_login()
            add_work_day(
                day=day,
                start=start,
                finish=finish,
                break_start=break_start,
                break_finish=break_finish,
                is_home_office=is_home_office,
                token=access_token,
            )


def access_token_by_login():
    time_track_login = typer.confirm("Headless login?")
    if time_track_login:
        if not environ.get("TIME_TRACK_EMAIL") or environ.get("TIME_TRACK_PASSWORD"):
            email = Prompt.ask("Email")
            password = Prompt.ask("Password", password=True)
        else:
            email = environ["TIME_TRACK_EMAIL"]
            password = environ["TIME_TRACK_PASSWORD"]
        access_token = get_acess_token(email=email, password=password, headless=False)
    else:
        access_token = get_acess_token()

    return access_token


if __name__ == "__main__":
    app()
