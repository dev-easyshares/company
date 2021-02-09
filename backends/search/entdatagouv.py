from company.backends.search import SearchBackend
from io import BytesIO
import base64, pycurl, json, re

class SearchBackend(SearchBackend):
    siren_url = 'https://entreprise.data.gouv.fr/api/sirene/v1/siren/%s'
    fulltext_url = 'https://entreprise.data.gouv.fr/api/sirene/v1/full_text/%s'
    since_format = '%Y%m%d'
    raw_address = "%(street_number)s %(way)s %(route)s %(locality)s %(postal_code)s"

    def call_webservice(self, url):
        buffer = BytesIO() 
        c = pycurl.Curl() 
        c.setopt(c.URL, url) 
        c.setopt(c.WRITEDATA, buffer) 
        c.perform() 
        response_code = c.getinfo(c.RESPONSE_CODE) 
        c.close()
        return json.loads(buffer.getvalue()), response_code

    def get_companies(self, url, qreq):
        message, companies, total, pages = (False, [], 0, 0)
        buffer, response_code = self.call_webservice(url % qreq)
        company = self.companies(buffer.get('siege_social', [buffer]), response_code)
        if not self.message:
            if url == self.siren_url:
                company = [company]
            for company in self.companies(buffer.get('etablissement', [buffer]), response_code):
                companies.append({
                    'siret': company.get('siret', None),
                    'denomination':company.get('l1_normalisee', None),
                    'legalform': company.get('nature_juridique_entreprise', None),
                    'ape': company.get('activite_principale', None),
                    'ape_noun': None,
                    'since': self.since(company.get('date_creation', None)),
                    'category': company.get('categorie_entreprise', None),
                    'slice_effective':  company.get('tranche_effectif_salarie_entreprise', None),
                    'siege': company.get('etablissementSiege', None),
                    'address': {
                        'street_number': company.get("numero_voie", None),
                        'way': company.get("type_voie", None),
                        'route': company.get("libelle_voie", None),
                        'locality': company.get("libelle_commune", None),
                        'postal_code': company.get("code_postal", None),
                        'country': 'france',
                        'country_code': 'fr',
                        'cedex': company.get("cedex", None),
                        'cedex_code': None,
                        'special': None,
                        'complement': None,
                        'index': None,
                        
                    }
                })
                companies['raw_address'] = self.raw_address % companies['address']
            total = buffer.get('total_results', 0)
            pages = buffer.get('total_pages', 0)
        return message, companies, total, pages

    def get_company_by_siren(self, siren):
        return self.get_companies(self.siren_url, siren)

    def get_active_companies(self, number, offset):
        return self.get_companies('etatAdministratifUniteLegale:A', number, offset)

    def get_company_by_fulltext(self, fulltext):
        fulltext = re.sub(r"\s+", '-', fulltext)
        return self.get_companies(self.fulltext_url, fulltext)