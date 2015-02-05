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
    blogName = schema.TextLine(
        title=_(u'label_blogName', default=u'Blog name'),
        default=_(u"My funlog space"),
        required=True,
    )

    blogDescription = schema.Text(
        title=_(u'label_description', default=u'Blog description'),
        required=False,
    )

    blogOnOff = schema.Bool(
        title=_(u'label_description', default=u'Blog siwtch.'),
        description=_(u'Funlog switch turn on/off'),
        default=True,
        required=False,
    )
