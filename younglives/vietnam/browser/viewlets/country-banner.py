from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class CountryBannerViewlet(ViewletBase):
    render = ViewPageTemplateFile('country-banner.pt')

    def update(self):
        pass
