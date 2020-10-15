import click
from pdfToSpeechReader import readOut

"""

@click.command()
@click.argument("pdf_file_path")
@click.option("--start-page", "-sp", "start_page", 
              help="start reading on page", default=0, type=click.INT)
@click.option("--exclude-pages", "ep", "excluded_pages",
              help="skip pages with 1,2,...,N", default=False, type=click.STRING)
@click.option("--speaker-rate", "sr", "speaker_rate",
              help="Rate of speech.", default=False, type=click.INT)
@click.option("--speaker-volume", "svol", "speaker_volume",
              help="Volume of speech.", default=False, type=click.FLOAT)
@click.option("--speaker-voice", "svoi", "speaker_voice",
              help="Voice of speaker.", default="f", type=click.STRING)
def main(pdf_file_path,
         start_page,
         excluded_pages,
         speaker_rate,
         speaker_volume,
         speaker_voice
         ):
    excluded_pages= [c.strip() for c in excluded_pages.split(',')]
    readOut(pdf_file_name = pdf_file_path,
            start_from_page = start_page,
            excluded_pages = excluded_pages or [[]],
            speaker_rate = speaker_rate or 100,
            speaker_volume = speaker_volume or 1.0,
            speaker_voice = speaker_voice
            )
"""
@click.command()
@click.argument("pdf_file_path")
def main(pdf_file_path):
    readOut(pdf_file_path)

if __name__ == "__main__":
    main()