import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'Generator.settings'
django.setup()

from rest.models import Race, Class, FirstName, LastName, Personality, Ideal, Peculiarities, Weakness, Worldview

def main():
    # models = [Race, Class, FirstName, LastName, Personality, Ideal, Peculiarities, Weakness, Worldview]
    models = [Personality, Ideal]
    for model in models:
        index = 1
        for obj in model.objects.all():
            obj.number = index
            obj.save()
            index += 1
    print('done')

if __name__ == "__main__":
    main()