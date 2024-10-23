import typer
from aria_parser import *
from typing_extensions import Annotated
from types import List, Dict, Tuple

app = typer.Typer()

infile_type = Annotated[str, typer.Option()]

@app.command()
def recommend(infile: str, outfile: str, prompt: str = None) -> str:
    """
    Generate a recommendation for a given Aria script.
    """
    with open(infile, "r") as f:
        script = f.read()
    recommendation = generate_recommendation(script, prompt)
    with open(outfile, "w") as f:
        f.write(recommendation)
    typer.echo(f"Recommendation written to {outfile}.")

@app.command()
def context(infile: str, outfile: str, prompt: str = None) -> str:
    """
    Understand the contents of an Aria script and generate a summary.
    """
    with open(infile, "r") as f:
        script = f.read()
    summary = generate_summary(script, prompt)
    with open(outfile, "w") as f:
        f.write(summary)
    typer.echo(f"Summary written to {outfile}.")

def main():
    app()


if __name__ == "__main__":
    main()
