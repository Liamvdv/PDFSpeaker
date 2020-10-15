import click
from pdfToSpeechReader import readOut, getInformation

@click.command()
@click.argument("encrypt", "")
def main():
    print("Okey")

@click.command()
@click.argument("info")
def info(info):

@click.command()
@click.argument("readout")
def read():
    print("Not OKey")

if __name__ == "__main__":
    main()