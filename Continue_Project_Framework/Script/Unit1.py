def TestImports():
    #import allure
    import faker
    #import openpyxl
    Log.Message("All packages imported successfully!")
    
def test_connection1():
    fake = Faker()
    Log.Message("Faker is working! Name: " + fake.name())
    
def test_connection():
    import sys
    Log.Message("Python executable: " + sys.executable)
    Log.Message("Python version: " + sys.version)
    Log.Message("Site packages paths:")
    for path in sys.path:
        Log.Message(path)
        
from faker import Faker

def test_connecfhdgtion():
    fake = Faker()
    Log.Message("Faker is working! Name: " + fake.name())
        
