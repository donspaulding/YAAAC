VERSION = "0.2alpha"
SERVICE_WSDLS = {
    "CampaignService": "https://adwords.google.com/api/adwords/cm/v201002/CampaignService?wsdl",
    "CampaignTargetService": "https://adwords.google.com/api/adwords/cm/v201002/CampaignTargetService?wsdl",
    "CampaignCriterionService": "https://adwords.google.com/api/adwords/cm/v201002/CampaignCriterionService?wsdl",
    "CampaignAdExtensionService": "https://adwords.google.com/api/adwords/cm/v201002/CampaignAdExtensionService?wsdl",
    "AdGroupAdService": "https://adwords.google.com/api/adwords/cm/v201002/AdGroupAdService?wsdl",
    "AdGroupService": "https://adwords.google.com/api/adwords/cm/v201002/AdGroupService?wsdl",
    "AdGroupCriterionService": "https://adwords.google.com/api/adwords/cm/v201002/AdGroupCriterionService?wsdl",
    "AdExtensionOverrideService": "https://adwords.google.com/api/adwords/cm/v201002/AdExtensionOverrideService?wsdl",
    "AdParamService": "https://adwords.google.com/api/adwords/cm/v201002/AdParamService?wsdl",
    "ReportInstanceService": "https://adwords.google.com/api/adwords/cm/v201002/ReportInstanceService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201002/ReportDefinitionService?wsdl",
    "BidLandscapeService": "https://adwords.google.com/api/adwords/cm/v201002/BidLandscapeService?wsdl",
    "GeoLocationService": "https://adwords.google.com/api/adwords/cm/v201002/GeoLocationService?wsdl",
}

DEBUG_WSDLS = dict(
        ((k, v.replace('adwords.google.com', 'adwords-sandbox.google.com')) for k,v in SERVICE_WSDLS.items())
)

from yaaac.client import AdwordsService
