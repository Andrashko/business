from scrapy.dupefilters import RFPDupeFilter

class CustomDupefilter(RFPDupeFilter):

    def request_seen(self, request):
        # fp = request_fingerprint(request)
        # if fp in self.fingerprints:
        #     return True
        # self.fingerprints.add(fp)
        return False
