import os
import sys
import django

# 👇 Add your project root to Python path (adjust path if needed)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 👇 Set your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voice.settings')

# 👇 Setup Django
django.setup()

# 👇 Now you can import your models
from vapp.models import Category, Action, Keyword, Question, Response

# 1. Category
cat = Category.objects.create(name="locksystem")

# 2. Actions
unlock_action = Action.objects.create(name="Unlock", category=cat)
lock_action = Action.objects.create(name="Lock", category=cat)

# 3. Keywords + Questions + Responses
data = [
    ("unlock", unlock_action, "Door is now unlocked.", "What do you want to unlock? A door, a lock, or something else?"),
    ("open lock", unlock_action, "Opening the lock...", "What do you want to unlock? A door, a lock, or something else?"),
    ("disable lock", unlock_action, "Lock has been disabled.", "What do you want to unlock? A door, a lock, or something else?"),
    ("unlatch", unlock_action, "Unlatching the door...", "What do you want to unlock? A door, a lock, or something else?"),
    ("lock", lock_action, "Door is now locked.", "What do you want to lock? A door, a cabinet, a lock or something else?"),
    ("secure lock", lock_action, "Securing the lock...", "What do you want to lock? A door, a cabinet, a lock or something else?"),
    ("close lock", lock_action, "Locking the door...", "What do you want to lock? A door, a cabinet, a lock or something else?"),
]

for phrase, action, resp_text, ques_text in data:
    keyword = Keyword.objects.create(phrase=phrase, action=action)
    Question.objects.create(keyword=keyword, text=ques_text)
    Response.objects.create(keyword=keyword, text=resp_text)

print("✅ Data populated successfully.")
