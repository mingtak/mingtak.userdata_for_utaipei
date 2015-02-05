from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from Products.CMFPlone.utils import safe_unicode

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_country(self):
        return self.context.getProperty('country', '')
    def set_country(self, value):
        return self.context.setMemberProperties({'country': value})
    country = property(get_country, set_country)

    def get_detail(self):
        return self.context.getProperty('detail', '')
    def set_detail(self, value):
        return self.context.setMemberProperties({'detail': value})
    detail = property(get_detail, set_detail)
