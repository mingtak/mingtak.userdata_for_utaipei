from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from Products.CMFPlone.utils import safe_unicode

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_blogName(self):
        return self.context.getProperty('blogName', '')
    def set_blogName(self, value):
        return self.context.setMemberProperties({'blogName': value})
    blogName = property(get_blogName, set_blogName)

    def get_blogDescription(self):
        return self.context.getProperty('blogDescription', '')
    def set_blogDescription(self, value):
        return self.context.setMemberProperties({'blogDescription': value})
    blogDescription = property(get_blogDescription, set_blogDescription)

    def get_blogOnOff(self):
        return self.context.getProperty('blogOnOff', '')
    def set_blogOnOff(self, value):
        return self.context.setMemberProperties({'blogOnOff': value})
    blogOnOff = property(get_blogOnOff, set_blogOnOff)
