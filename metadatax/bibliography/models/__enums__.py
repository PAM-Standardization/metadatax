from django_extension.models import ExtendedEnum


class BibliographyType(ExtendedEnum):
    """Type of bibliography"""

    SOFTWARE = ("S", "Software")
    ARTICLE = ("A", "Article")
    CONFERENCE = ("C", "Conference")
    POSTER = ("P", "Poster")


class BibliographyStatus(ExtendedEnum):
    """Bibliography publication status"""

    UPCOMING = ("U", "Upcoming")
    PUBLISHED = ("P", "Published")
