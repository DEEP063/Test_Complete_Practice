import login_page
import config

def test_valid_login():
  
    login = login_page.LoginPage()
    Log.Message(config.Config.BASE_URL)
    login.open(config.Config.BASE_URL)
    login.login("admin@test.com", "Admin@123")

    if "dashboard" in Browsers.Item('chrome').URL:
        Log.Message("PASS - Login Successful")
    else:
        Log.Error("FAIL - Login Failed")