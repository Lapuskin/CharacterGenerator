from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    force_bonus = models.IntegerField()
    dexterity_bonus = models.IntegerField()
    endurance_bonus = models.IntegerField()
    wisdom_bonus = models.IntegerField()
    intelligence_bonus = models.IntegerField()
    charisma_bonus = models.IntegerField()
    link = models.CharField(max_length=100)
    min_height = models.IntegerField()
    max_height = models.IntegerField()
    old = models.IntegerField(default=0)
    youth = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    number = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.name}"


class LastName(models.Model):
    name = models.CharField(max_length=300)
    genus = models.CharField(max_length=30, default='')
    number = models.IntegerField(default=0)
    race = models.ManyToManyField(Race)

    def __str__(self):
        return f"{self.name} from {self.race}"

class FirstName(models.Model):
    name = models.CharField(max_length=300)
    race = models.ManyToManyField(Race)
    sex = models.BooleanField(default=0)
    genus = models.CharField(max_length=30, default='')
    number = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name} from {self.race}"


class Class(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} class"

class PersonalityMeaning(models.Model):
    letter = models.CharField(max_length=1)
    meaning = models.CharField(max_length=300)


    def __str__(self):
        return f"{self.letter}"

class Personality(models.Model):
    first_letter = models.ForeignKey(PersonalityMeaning, on_delete=models.DO_NOTHING,related_name='first_letter_personality', default=None)
    second_letter = models.ForeignKey(PersonalityMeaning, on_delete=models.DO_NOTHING,related_name='second_letter_personality', default=None)
    third_letter = models.ForeignKey(PersonalityMeaning, on_delete=models.DO_NOTHING,related_name='third_letter_personality', default=None)
    fourth_letter = models.ForeignKey(PersonalityMeaning, on_delete=models.DO_NOTHING,related_name='fourth_letter_personality', default=None)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_letter}{self.second_letter}{self.third_letter}{self.fourth_letter}"

class Background(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

class Peculiarities(models.Model):
    description = models.CharField(max_length=230)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.description}."

class Worldview(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}."


class Ideal(models.Model):
    description = models.CharField(max_length=100)
    worldview = models.ForeignKey(Worldview, on_delete=models.DO_NOTHING, default=None)
    number = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.description}."


class Weakness(models.Model):
    description = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.description}."

class Attachment(models.Model):
    description = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.description}."