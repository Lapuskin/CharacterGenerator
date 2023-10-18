from email.quoprimime import unquote
from random import randint, choice, shuffle
from rest.models import Race, Class, FirstName, LastName, Personality, Background, Weakness, Ideal, Attachment, \
    Peculiarities, Worldview
import rest.serializers as serializer

def gen_name(race):
    first_name = choice(FirstName.objects.filter(race=race))
    first = choice(first_name.name.split(', '))

    last_name = choice(LastName.objects.filter(race=race))
    last = choice(last_name.name.split(', '))
    name = first + ' ' + last
    return {'name': name, 'sex': first_name.sex}

def gen_stats(race):
    base_stats = [15, 14, 13, 12, 10, 8]
    shuffle(base_stats)
    base_stats[0] += race.force_bonus
    base_stats[1]+= race.charisma_bonus
    base_stats[2]+= race.dexterity_bonus
    base_stats[3]+= race.endurance_bonus
    base_stats[4]+= race.intelligence_bonus
    base_stats[5]+= race.wisdom_bonus
    return {'force': base_stats[0], 'charisma': base_stats[1], 'dexterity': base_stats[2], 'endurance': base_stats[3], 'intelligence': base_stats[4], 'wisdom': base_stats[5]}


class Service:
    def uncode(self, request : dict) -> dict:
        uncode_request = {}
        for key in request:
            uncode_request[key] = unquote(request[key])
        return uncode_request

    def get_character(self, request):
        print(request)
        character_race = ''
        character_class = ''
        json_data = {}
        categories = [Race, Class, Personality, Background, Ideal, Weakness, Peculiarities] #Attachment
        for category in categories:
            if 'state' + category.__name__ not in request or request.get('state' + category.__name__) is None:
                max_number = category.objects.all().count()
                rand_number = randint(1, max_number)
                character_category = category.objects.get(number=rand_number)
            else:
                print('state' + category.__name__, request.get(category.__name__))
                character_category = category.objects.get(name=request.get('state' + category.__name__))
            if category is Race:
                json_data.update(gen_name(character_category))
                json_data.update({'stats': gen_stats(character_category)})
            character_serializer = getattr(serializer, category.__name__ + 'Serializer')(character_category, many=False)
            cat_str = category.__name__.lower()
            json_data.update({cat_str: character_serializer.data})

        print(json_data)
        return json_data
