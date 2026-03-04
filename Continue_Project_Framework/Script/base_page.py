class BasePage:
    
    # You no longer need def find(self, obj_path) with eval!
    
    def click(self, obj):
        # 'obj' is already the TestComplete Alias object
        obj.Click()
        
    def type_text(self, obj, text):
        #obj.SetText("")
        obj.SetText(text)