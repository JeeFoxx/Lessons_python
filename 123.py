import file_operations, random
from faker import Faker
fake = Faker("ru_RU")

alphabet = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

def create_and_save_files():
    # Инициализация переменных
    skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар",
              "Стремительный удар", "Кислотный взгляд", "Тайный побег",
              "Ледяной выстрел", "Огненный заряд"]
    
    runic_skills = []
    
    for skill in skills:
        runic_skill = ""
        for letter in skill:
            runic_skill += alphabet.get(letter)
        runic_skills.append(runic_skill)
    
    skills_samples = random.choices(runic_skills, k=10)
    
    contexts = []
    for i in range(10):
        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()
        strength = random.randint(3, 18)
        agility = random.randint(3, 18)
        endurance = random.randint(3, 18)
        intelligence = random.randint(3, 18)
        luck = random.randint(3, 18)
        skill_1 = skills_samples[i][0]
        skill_2 = skills_samples[i][1]
        skill_3 = skills_samples[i][2]
        
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "job": job,
            "town": town,
            "strength": strength,
            "agility": agility,
            "endurance": endurance,
            "intelligence": intelligence,
            "luck": luck,
            "skill_1": skill_1,
            "skill_2": skill_2,
            "skill_3": skill_3
        }
        contexts.append(context)
    
    for context in contexts:
        file_operations.render_template("charsheet.svg", f"{context['first_name']}_{context['last_name']}.svg", context)

create_and_save_files()