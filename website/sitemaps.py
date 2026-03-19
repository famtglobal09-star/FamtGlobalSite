from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'home',
            'about',
            'contact',
            'who_we_help',
            'incorporation',
            'bookkeeping',
            'itin',
            'cpa_letter',
            'tax_filing',
            'finance_solutions',
            'finance_analysis',
            'privacy_policy',
            'terms',
            'disclaimer',
        ]

    def location(self, item):
        return reverse(item)