from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


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
