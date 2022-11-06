from django.utils.translation import gettext_lazy as _

YESNO = (
("YES", _('yes')),
("NO", _('no')),
)

COMPANY = "COMPANY"
ASSOCIATION = "ASSOCIATION"
COOWNER = "COOWNER"
BIGMASTER = "BIGMASTER"
ISTYPE = (
    (COMPANY, _("Société")),
    (ASSOCIATION, _("Association")),
    (COOWNER, _("Co-propriété")),
    (BIGMASTER, _("Grand compte")),
)


MATERIALBASE = "MATERIALBASE"
INDUSTRY = "INDUSTRY"
SERVICESCONS = "SERVICESCONS"
GOODCONS = "GOODCONS"
COMPANYFINANCIAL = "COMPANYFINANCIAL"
SERVICESCOLLECT = "SERVICESCOLLECT"
HEALTH = "HEALTH"
TECHNOLOGIES = "TECHNOLOGIES"
PETROLGAS = "PETROLGAS"
TELECOM = "TELECOM"
ICB = (
    (MATERIALBASE, _("Matériaux de base")),
    (INDUSTRY, _("Industries")),
    (SERVICESCONS, _("Services aux consommateurs")),
    (GOODCONS, _("Biens de consommation")),
    (COMPANYFINANCIAL, _("Sociétés Financières")),
    (SERVICESCOLLECT, _("Services aux collectivités")),
    (HEALTH, _("Santé")),
    (TECHNOLOGIES, _("Technologies")),
    (PETROLGAS, _("Pétrole et gaz")),
    (TELECOM, _("Télécommunications")),
)

SRD = "SRD"
COMPA = "COMPA"
COMPB = "COMPB"
COMPC = "COMPC"
EURONEXT_GROWTH = "EURONEXT_GROWTH"
EURONEXT_ACCESS = "EURONEXT_ACCESS"
OTHERS = "OTHERS"
EXCEPT = "EXCEPT"
COMPASPECIAL = "COMPASPECIAL"
DELISTED = "DELISTED"
MARKET = (
    ("SRD", _("SRD")),
    ("COMPA", _("Compartiment A")),
    ("COMPB", _("Compartiment B")),
    ("COMPC", _("Compartiment C")),
    ("EURONEXT_GROWTH", _("Euronext Growth")),
    ("EURONEXT_ACCESS", _("Euronext Access")),
    ("OTHERS", _("Autres titres")),
    ("EXCEPT", _("Hors titres")),
    ("COMPASPECIAL", _("Compartiment spécial")),
    ("DELISTED", _("Valeurs Radiées")),
)

STACKHOLDER_SHAREHOLDER = "SHAREHOLDER"
STACKHOLDER_ASSOCIATE = "ASSOCIATE"
STACKHOLDER_MEMBER = "MEMBER"
STACKHOLDER_ADHERENT = "ADHERENT"
STACKHOLDER_ADVISE = "ADVISE"
STACKHOLDER_KINDS = (
    (STACKHOLDER_SHAREHOLDER, _("Actionnaire(s)")),
    (STACKHOLDER_MEMBER, _("Membre(s)")),
    (STACKHOLDER_ASSOCIATE, _("Associé(es)")),
    (STACKHOLDER_ADHERENT, _("Adhérent(es)")),
    (STACKHOLDER_ADVISE, _("Conseiller(es)")),
)

STACKHOLDER_DEFAULT = {
    "5192": STACKHOLDER_ADHERENT,
    "5195": STACKHOLDER_ADHERENT,
    "6316": STACKHOLDER_ADHERENT,
    "6317": STACKHOLDER_ADHERENT,
    "6318": STACKHOLDER_ADHERENT,
    "6411": STACKHOLDER_ADHERENT,
    "6595": STACKHOLDER_ADHERENT,
    "6596": STACKHOLDER_ADHERENT,
    "8140": STACKHOLDER_ADHERENT,
    "8210": STACKHOLDER_ADHERENT,
    "8250": STACKHOLDER_ADHERENT,
    "8290": STACKHOLDER_ADHERENT,
    "2310": STACKHOLDER_ASSOCIATE,
    "2320": STACKHOLDER_ASSOCIATE,
    "2385": STACKHOLDER_ASSOCIATE,
    "5202": STACKHOLDER_ASSOCIATE,
    "5203": STACKHOLDER_ASSOCIATE,
    "5306": STACKHOLDER_ASSOCIATE,
    "5307": STACKHOLDER_ASSOCIATE,
    "5308": STACKHOLDER_ASSOCIATE,
    "5309": STACKHOLDER_ASSOCIATE,
    "5370": STACKHOLDER_ASSOCIATE,
    "5385": STACKHOLDER_ASSOCIATE,
    "5410": STACKHOLDER_ASSOCIATE,
    "5415": STACKHOLDER_ASSOCIATE,
    "5422": STACKHOLDER_ASSOCIATE,
    "5426": STACKHOLDER_ASSOCIATE,
    "5430": STACKHOLDER_ASSOCIATE,
    "5431": STACKHOLDER_ASSOCIATE,
    "5432": STACKHOLDER_ASSOCIATE,
    "5442": STACKHOLDER_ASSOCIATE,
    "5443": STACKHOLDER_ASSOCIATE,
    "5451": STACKHOLDER_ASSOCIATE,
    "5453": STACKHOLDER_ASSOCIATE,
    "5454": STACKHOLDER_ASSOCIATE,
    "5455": STACKHOLDER_ASSOCIATE,
    "5458": STACKHOLDER_ASSOCIATE,
    "5459": STACKHOLDER_ASSOCIATE,
    "5460": STACKHOLDER_ASSOCIATE,
    "5470": STACKHOLDER_ASSOCIATE,
    "5485": STACKHOLDER_ASSOCIATE,
    "5498": STACKHOLDER_ASSOCIATE,
    "5499": STACKHOLDER_ASSOCIATE,
    "6511": STACKHOLDER_ASSOCIATE,
    "6521": STACKHOLDER_ASSOCIATE,
    "6532": STACKHOLDER_ASSOCIATE,
    "6533": STACKHOLDER_ASSOCIATE,
    "6534": STACKHOLDER_ASSOCIATE,
    "6535": STACKHOLDER_ASSOCIATE,
    "6536": STACKHOLDER_ASSOCIATE,
    "6538": STACKHOLDER_ASSOCIATE,
    "6539": STACKHOLDER_ASSOCIATE,
    "6540": STACKHOLDER_ASSOCIATE,
    "6541": STACKHOLDER_ASSOCIATE,
    "6542": STACKHOLDER_ASSOCIATE,
    "6543": STACKHOLDER_ASSOCIATE,
    "6544": STACKHOLDER_ASSOCIATE,
    "6551": STACKHOLDER_ASSOCIATE,
    "6554": STACKHOLDER_ASSOCIATE,
    "6558": STACKHOLDER_ASSOCIATE,
    "6560": STACKHOLDER_ASSOCIATE,
    "6561": STACKHOLDER_ASSOCIATE,
    "6562": STACKHOLDER_ASSOCIATE,
    "6563": STACKHOLDER_ASSOCIATE,
    "6564": STACKHOLDER_ASSOCIATE,
    "6565": STACKHOLDER_ASSOCIATE,
    "6566": STACKHOLDER_ASSOCIATE,
    "6567": STACKHOLDER_ASSOCIATE,
    "6568": STACKHOLDER_ASSOCIATE,
    "6569": STACKHOLDER_ASSOCIATE,
    "6571": STACKHOLDER_ASSOCIATE,
    "6572": STACKHOLDER_ASSOCIATE,
    "6573": STACKHOLDER_ASSOCIATE,
    "6574": STACKHOLDER_ASSOCIATE,
    "6575": STACKHOLDER_ASSOCIATE,
    "6576": STACKHOLDER_ASSOCIATE,
    "6577": STACKHOLDER_ASSOCIATE,
    "6578": STACKHOLDER_ASSOCIATE,
    "6585": STACKHOLDER_ASSOCIATE,
    "6588": STACKHOLDER_ASSOCIATE,
    "6589": STACKHOLDER_ASSOCIATE,
    "6597": STACKHOLDER_ASSOCIATE,
    "6598": STACKHOLDER_ASSOCIATE,
    "6599": STACKHOLDER_ASSOCIATE,
    "9224": STACKHOLDER_ASSOCIATE,
    "7230": STACKHOLDER_ADVISE,
    "7312": STACKHOLDER_ADVISE,
    "7344": STACKHOLDER_ADVISE,
    "7346": STACKHOLDER_ADVISE,
    "7347": STACKHOLDER_ADVISE,
    "7348": STACKHOLDER_ADVISE,
    "7345": STACKHOLDER_MEMBER,
    "7353": STACKHOLDER_MEMBER,
    "7354": STACKHOLDER_MEMBER,
    "7355": STACKHOLDER_MEMBER,
    "7356": STACKHOLDER_MEMBER,
    "7365": STACKHOLDER_MEMBER,
    "8410": STACKHOLDER_MEMBER,
    "8420": STACKHOLDER_MEMBER,
    "8450": STACKHOLDER_MEMBER,
    "8470": STACKHOLDER_MEMBER,
    "8490": STACKHOLDER_MEMBER,
    "9110": STACKHOLDER_MEMBER,
    "9150": STACKHOLDER_MEMBER,
    "9210": STACKHOLDER_MEMBER,
    "9220": STACKHOLDER_MEMBER,
    "9221": STACKHOLDER_MEMBER,
    "9222": STACKHOLDER_MEMBER,
    "9223": STACKHOLDER_MEMBER,
    "9230": STACKHOLDER_MEMBER,
    "9260": STACKHOLDER_MEMBER,
}

STOCK_SHAREHOLDER = "SHAREHOLDER"
STOCK_VOICE = "VOICE"
STOCK_SHARES = "SHARES"
STOCK_TITLE = "TITLE"
STOCK_KINDS = (
    (STOCK_SHAREHOLDER, _("Titre(s)")),
    (STOCK_VOICE, _("Voix")),
    (STOCK_SHARES, _("Part(s) sociale(s)")),
    (STOCK_TITLE, _("Titre(s)")),
)

STOCK_DEFAULT = {
    "5196": STOCK_SHARES,
    "5202": STOCK_SHARES,
    "5203": STOCK_SHARES,
    "5306": STOCK_SHARES,
    "5307": STOCK_SHARES,
    "5308": STOCK_SHARES,
    "5309": STOCK_SHARES,
    "5370": STOCK_SHARES,
    "5385": STOCK_SHARES,
    "5410": STOCK_SHARES,
    "5415": STOCK_SHARES,
    "5422": STOCK_SHARES,
    "5426": STOCK_SHARES,
    "5430": STOCK_SHARES,
    "5431": STOCK_SHARES,
    "5432": STOCK_SHARES,
    "5442": STOCK_SHARES,
    "5443": STOCK_SHARES,
    "5451": STOCK_SHARES,
    "5453": STOCK_SHARES,
    "5454": STOCK_SHARES,
    "5455": STOCK_SHARES,
    "5458": STOCK_SHARES,
    "5459": STOCK_SHARES,
    "5460": STOCK_SHARES,
    "5470": STOCK_SHARES,
    "5485": STOCK_SHARES,
    "5498": STOCK_SHARES,
    "5499": STOCK_SHARES,
    "6316": STOCK_SHARES,
    "6317": STOCK_SHARES,
    "6318": STOCK_SHARES,
    "6511": STOCK_SHARES,
    "6521": STOCK_SHARES,
    "6532": STOCK_SHARES,
    "6533": STOCK_SHARES,
    "6534": STOCK_SHARES,
    "6535": STOCK_SHARES,
    "6536": STOCK_SHARES,
    "6538": STOCK_SHARES,
    "6539": STOCK_SHARES,
    "6540": STOCK_SHARES,
    "6541": STOCK_SHARES,
    "6542": STOCK_SHARES,
    "6543": STOCK_SHARES,
    "6544": STOCK_SHARES,
    "6551": STOCK_SHARES,
    "6554": STOCK_SHARES,
    "6558": STOCK_SHARES,
    "6560": STOCK_SHARES,
    "6561": STOCK_SHARES,
    "6562": STOCK_SHARES,
    "6563": STOCK_SHARES,
    "6564": STOCK_SHARES,
    "6565": STOCK_SHARES,
    "6566": STOCK_SHARES,
    "6567": STOCK_SHARES,
    "6568": STOCK_SHARES,
    "6569": STOCK_SHARES,
    "6571": STOCK_SHARES,
    "6572": STOCK_SHARES,
    "6573": STOCK_SHARES,
    "6574": STOCK_SHARES,
    "6575": STOCK_SHARES,
    "6576": STOCK_SHARES,
    "6577": STOCK_SHARES,
    "6578": STOCK_SHARES,
    "6585": STOCK_SHARES,
    "6588": STOCK_SHARES,
    "6589": STOCK_SHARES,
    "6597": STOCK_SHARES,
    "6598": STOCK_SHARES,
    "6599": STOCK_SHARES,
    "5720": STOCK_VOICE,
    "5195": STOCK_VOICE,
    "6210": STOCK_VOICE,
    "6220": STOCK_VOICE,
    "6537": STOCK_VOICE,
    "7312": STOCK_VOICE,
    "7321": STOCK_VOICE,
    "7322": STOCK_VOICE,
    "7323": STOCK_VOICE,
    "9150": STOCK_VOICE,
    "9210": STOCK_VOICE,
    "9220": STOCK_VOICE,
    "9221": STOCK_VOICE,
    "9222": STOCK_VOICE,
    "9224": STOCK_VOICE,
    "9230": STOCK_VOICE,
    "9260": STOCK_VOICE,
}


COMMON = "COMMON"
PREFERRED = "PREFERRED"
BSPCE = "BSPCE"
BSA = "BSA"
BSAR = "BSAR"
BSAAR = "BSAAR"
AGA = "AGA"

COMMON_TR = _("Ordinaire")
PREFERRED_TR = _("Préférences")
BSPCE_TR = _("Bon(s) de souscription de part(s) de créateur d'entreprise")
BSA_TR = _("Bon(s) de souscription d'action(s)")
BSAR_TR = _("Bon(s) de souscription d'action(s) remboursable(s)")
BSAAR_TR = _("Bon(s) de souscription et/ou d'acquisition d'action(s) remboursable(s)")
AGA_TR = _("Attribution gratuite d’action(s)")

STOCK_TYPE_DEFAULT = (
    (COMMON, COMMON_TR),
    (PREFERRED, PREFERRED_TR),
    (BSPCE, BSPCE_TR),
    (BSA, BSA_TR),
    (BSAR, BSAR_TR),
    (BSAAR, BSAAR_TR),
    (AGA, AGA_TR),
)
STOCK_TYPE_MEMBER = ((COMMON, COMMON_TR),)
STOCK_TYPE_DILUTED = (BSPCE, BSA, BSAR, BSAAR, AGA)

OCTOLO = "OCTOLO"
BRING = "BRING"
MBRSHIP = "MBRSHIP"
PLEDGE = "PLEDGE"
EMITPART = "EMITPART"
EMITBS = "EMITBS"
REDEEM = "REDEEM"
ASSIGN = "ASSIGN"
EXCHANGE = "EXCHANGE"
DONATE = "DONATE"
LOAN = "LOAN"
FUSION = "FUSION"
SPLIT = "SPLIT"
CONVENTION = "CONVENTION"
TRUST = "TRUST"
SEIZURE = "SEIZURE"

OCTOLO_TR = _("inscription octolo")
BRING_TR = _("apports de parts sociales/actions")
MBRSHIP_TR  = _("adhésion")
PLEDGE_TR = _("nantissement de parts sociales")
EMITPART_TR = _("émission d’action /parts")
EMITBS_TR = _("émission de titres (BSA, BSPCE …)")
REDEEM_TR = _("rachat d’actions par la société")
ASSIGN_TR = _("cessions")
EXCHANGE_TR = _("échange")
DONATE_TR = _("donations")
LOAN_TR = _("prêt d’actions")
FUSION_TR = _("fusion")
SPLIT_TR = _("scission")
CONVENTION_TR = _("conventions sur les parts sociales")
TRUST_TR = _("fiducie")
SEIZURE_TR = _("saisie de parts sociales")
ATTRIBUTION_TR = _("attribution")
EXERCICE_TR = _("exercice")
MOVE_TYPE_DEFAULT = (
    (OCTOLO, OCTOLO_TR),
    (BRING, BRING_TR),
    (MBRSHIP, MBRSHIP_TR),
    (PLEDGE, PLEDGE_TR),
    (EMITPART, EMITPART_TR),
    (EMITBS, EMITBS_TR),
    (REDEEM, REDEEM_TR),
    (ASSIGN, ASSIGN_TR),
    (EXCHANGE, EXCHANGE_TR),
    (DONATE, DONATE_TR),
    (LOAN, LOAN_TR),
    (FUSION, FUSION_TR),
    (SPLIT, SPLIT_TR),
    (CONVENTION, CONVENTION_TR),
    (TRUST, TRUST_TR),
    (SEIZURE, SEIZURE_TR),
)