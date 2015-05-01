from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from Products.CMFPlone.utils import safe_unicode

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_institution(self):
        return self.context.getProperty('institution', '')
    def set_institution(self, value):
        return self.context.setMemberProperties({'institution': value})
    institution = property(get_institution, set_institution)

    def get_position(self):
        return self.context.getProperty('position', '')
    def set_position(self, value):
        return self.context.setMemberProperties({'position': value})
    position = property(get_position, set_position)
