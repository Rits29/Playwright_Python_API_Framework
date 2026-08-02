import random
import string


class RandomDataGenerator:

    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_integer(min_value=1, max_value=1000):
        return random.randint(min_value, max_value)

    @staticmethod
    def generate_random_alphanumeric(length=6):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    @staticmethod
    def generate_random_event():
        events = ["Conference", "Workshop", "Seminar", "Meetup"]
        return random.choice(events)
    
    @staticmethod
    def generate_random_venue():
        venues = ["Convention Center", "Hotel Ballroom", "University Hall", "Community Center", "City Club"]
        return random.choice(venues)
    
    @staticmethod
    def generate_random_city():
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
        return random.choice(cities)
    
    @staticmethod
    def generate_random_date():
        year = random.randint(2027, 2029)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # To avoid complications with different month lengths
        return f"{year}-{month:02d}-{day:02d}"
    
    @staticmethod
    def generate_random_url():
        return f"https://example.com/{RandomDataGenerator.generate_random_string(5)}.jpg"

