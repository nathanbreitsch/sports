import sys
import os
sys.path.append('sports')
from sports import app

if not os.path.isfile("sports.db"):
    os.system("database_setup.py")
    os.system("import_data.py")

if __name__ == "__main__":
    app.run()
