import base_page
import tc  # Bring your wrapper import back!

# Explicitly pull TestComplete globals into this module's scope
TestedApps = tc.TestedApps
Aliases = tc.Aliases

class LoginPage(base_page.BasePage):
    
    @property
    def USERNAME(self):
        return Aliases.browser.pageSwagLabs.textboxUserName
        
    @property
    def PASSWORD(self):
        return Aliases.browser.pageSwagLabs.textboxPassword
        
    @property
    def LOGIN_BTN(self):
        return Aliases.browser.pageSwagLabs.submitbuttonLogin

    def open(self, base_url):
        TestedApps.msedge.Params.SimpleParams.CommandLineParameters = base_url
        TestedApps.msedge.Run()

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)