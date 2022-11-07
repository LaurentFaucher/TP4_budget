import os
os.system("git bisect start 9846db e4cfc6f77")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")