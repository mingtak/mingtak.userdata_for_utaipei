from zope.interface import Interface, implements
from zope import schema
#from plone.app.textfield import RichText
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone import api
from Products.CMFPlone.utils import safe_unicode

from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.component import queryUtility
from plone.registry.interfaces import IRegistry

from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from mingtak.userdata import MessageFactory as _


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


from plone.app.users.userdataschema import IUserDataSchema

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    country = schema.TextLine(
        title=_(u'label_country', default=u'Country'),
        description=_(u'help_country',
                      default=u"Fill in which country you live in."),
        required=False,
    )

    detail = schema.Text(
        title=_(u'label_detail', default=u'Detail'),
        description=_(u'help_detail',
                      default=u"Detail description for member."),
        required=False,
    )
