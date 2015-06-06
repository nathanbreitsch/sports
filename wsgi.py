import sys
import os
sys.path.append('sports')
from sports import app

if not os.path.isfile("./sports/sports.db"):
    os.system("./sports/database-setup.py")
    os.system("./sports/import_data.py")

if __name__ == "__main__":
    app.run()
