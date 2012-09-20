from Acquisition import aq_inner
from zope import schema
from zope.formlib import form
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.app.form.browser import RadioWidget as _RadioWidget

# CMF
from Products.CMFCore.utils import getToolByName

# Plone
from plone.memoize.instance import memoize
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from younglives.content import _

class IVietnamLogoPortlet(IPortletDataProvider):
    """ A portlet for the Vietnam logo. """

class Assignment(base.Assignment):

    implements(IVietnamLogoPortlet)

class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('vietnam-logo.pt')

    def render(self):
        return self._template()

class AddForm(base.AddForm):
    form_fields = form.Fields(IVietnamLogoPortlet)

class EditForm(base.EditForm):
    form_fields = form.Fields(IVietnamLogoPortlet)
