from django.conf import settings
from django.utils.module_loading import import_string
from mighty.functions import test

def search_by_siren(backend, siren):
    return backend.get_company_by_siren(siren)

def search_by_fulltext(backend, fulltext):
    return backend.get_company_by_fulltext(fulltext)

def get_backend(backend, search):
    if search.isdigit() and len(search) == 9:
        return search_by_siren(import_string(backend)(), search)
    return search_by_fulltext(import_string(backend)(), search)

def merge_company(backends):
    base = {}
    for pos, datas in enumerate(backends):
        for key,data in datas.items():
            if data:
                if key in base and data != base[key] and datas['lastupdate'] > base['lastupdate'][0]:
                    base[key] = (data, datas['lastupdate'])
                else:
                    base[key] = (data, datas['lastupdate'])
    return {key: value[0] for key, value in base.items()}

def merge_backends(results):
    return [merge_company([datas for backend, datas in backends.items()]) for company, backends in results.items()]

def backends_loop(search):
    results = {}
    ftotal, fpages = (0, 0)
    for backend in settings.COMPANYFILLER_BACKEND:
        return get_backend(backend, search)
        companies, total, pages = get_backend('%s.SearchBackend' % backend, search)
        ftotal = total if total > ftotal else ftotal
        pages = pages if pages > fpages else fpages
        for company in companies:
            if company['denomination'] in results:
                results[company['denomination']][backend] = company
            else:
                results[company['denomination']] = { backend: company }
    return merge_backends(results), ftotal, fpages