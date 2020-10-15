import click
from pdfToSpeechReader import getInformation

@click.command()
@click.argument("pdf_path")
def main(pdf_path):
    """Please provide the relative path to the .pdf file, use slashes"""
    print(getInformation(pdf_path))


if __name__ == "__main__":
    main()