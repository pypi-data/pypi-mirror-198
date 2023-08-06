from typing import Optional

import typer

app = typer.Typer()


@app.command()
def hello(name: str, iq: int, display_iq: bool = True, age: Optional[int] = None):
    print(f"Hello {name}")
    if display_iq:
        print(f"Your IQ is {iq}")
    if age:
        typer.echo(f"You have this age: {age}")
    else:
        typer.echo("Age not known!")



@app.command()
def goodbye():
    print("Goodbye")


if __name__ == "__main__":
    app()