from five import grok
from plone import api

from plone.app.layout.navigation.interfaces import INavigationRoot


class FrontpageView(grok.View):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('frontpage-view')

    def panelpage(self):
        portal = api.portal.get()
        frontpage = portal['frontpage-content']
        tmpl = frontpage.restrictedTraverse('@@panelpage')()
        return tmpl
