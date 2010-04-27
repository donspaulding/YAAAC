VERSION = "0.2alpha"
SERVICE_WSDLS = {
    "CampaignService": "https://adwords.google.com/api/adwords/cm/v200909/CampaignService?wsdl",
    "AdGroupAdService": "https://adwords.google.com/api/adwords/cm/v200909/AdGroupAdService?wsdl",
    "AdGroupService": "https://adwords.google.com/api/adwords/cm/v200909/AdGroupService?wsdl",
    "OptionsService": "https://adwords.google.com/api/adwords/o/",
    "InfoService": "https://adwords.google.com/api/adwords/info/",
}

DEBUG_WSDLS = dict(
        ((k, v.replace('adwords.google.com', 'adwords-sandbox.google.com')) for k,v in SERVICE_WSDLS.items())
)

from yaaac.client import Client
