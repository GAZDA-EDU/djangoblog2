from django.db import models

class DodatkoweInfo(models.Model):
    DoesNotExist = None
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Action'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Drama'),
    }
    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    # Metoda wyświetlająca nazwę i rok filmu.
    def __str__(self):
    #   return self.tytul + ' (' + str(self.rok) + ')'
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})". format(self.tytul, self.rok)

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)
