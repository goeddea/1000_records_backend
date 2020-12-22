import beam
from records.models import Record, Artist


# Create your views here.

class RecordViewSet(beam.ViewSet):
    model = Record
    fields = [
        "artist",
        "title",
    ]

class ArtistViewSet(beam.ViewSet):
    model = Artist
    fields = [
        "name",
    ]
