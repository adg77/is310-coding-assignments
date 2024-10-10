from rich.console import Console
from rich.table import Table
console = Console()

movies = [
    {
        "Released": "Oct 14, 1994",
        "Title": "The Shawshank Redemption",
        "Box Office": "$58,500,000"
    },
    {
        "Released": "Jul 14, 2010",
        "Title": "Inception",
        "Box Office": "$836,800,000"
    },
    {
        "Released": "Jun 11, 1993",
        "Title": "Jurassic Park",
        "Box Office": "$1,033,900,000"
    },
    {
        "Released": "Dec 19, 2001",
        "Title": "The Lord of the Rings: The Fellowship of the Ring",
        "Box Office": "$897,700,000"
    },
    {
        "Released": "Oct 26, 2014",
        "Title": "Interstellar",
        "Box Office": "$677,500,000"
    }
]

def display_movies(movies):
    table = Table(title="My Favorite Movies")
    table.add_column("Released", justify="center", style="red", no_wrap=True)
    table.add_column("Title", style="grey0")
    table.add_column("Box Office", justify="right", style="green")

    for movie in movies:
        table.add_row(movie["Released"], movie["Title"], movie["Box Office"])

    console.print(table)

def get_movie_data():
    new_movie = {}
    new_movie["Released"] = console.input("[red]Enter release date (e.g., Dec 15, 2017): [/red]")
    new_movie["Title"] = console.input("[blue]Enter movie title: [/blue]")
    new_movie["Box Office"] = console.input("[green]Enter box office earnings (e.g., $1,000,000,000): [/green]")
    return new_movie

def confirm_movie_data(new_movie):
    console.print("\n[green]You entered the following data:[/green]")
    console.print("[red]Released:[/red] {}".format(new_movie['Released']))
    console.print("[blue]Title:[/blue] {}".format(new_movie['Title']))
    console.print("[green]Box Office:[/green] {}".format(new_movie['Box Office']))
    confirmation = console.input("[dark_orange]Is this data correct? (y/n): [/dark_orange]")
    return confirmation.lower() == 'y'

console.print("[grey0]Example Movie Data:[/grey0]")
display_movies(movies)

new_movie = get_movie_data()
if confirm_movie_data(new_movie):
    movies.append(new_movie)
    file_path = "movies_data.txt"
    with open(file_path, "w") as file:
        for movie in movies:
            file.write("Released: {}, Title: {}, Box Office: {}\n".format(movie['Released'], movie['Title'], movie['Box Office']))
    console.print("[grey0]Updated Movie Data:[/grey0]")
    display_movies(movies)
    console.print("[green]Data has been saved to {}[/green]".format(file_path))
else:
    console.print("[red]Rerun and re-enter the correct data.[/red]")