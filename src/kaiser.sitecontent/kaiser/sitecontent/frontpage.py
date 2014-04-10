from five import grok
from plone import api

from plone.app.layout.navigation.interfaces import INavigationRoot


class FrontageView(grok.View):
    grok.content(INavigationRoot)
    grok.require('zope2.View')
    grok.name('frontpage-view')

    def panelpage(self):
        portal = api.portal.get()
        frontpage = portal['frontpage-content']
        tmpl = frontpage.restrictedTraverse('@@panelpage')()
        return tmpl
