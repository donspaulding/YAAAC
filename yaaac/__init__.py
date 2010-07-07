VERSION = "0.2.1"
SERVICE_WSDLS = {
    "CampaignService": "https://adwords.google.com/api/adwords/cm/v201003/CampaignService?wsdl",
    "CampaignTargetService": "https://adwords.google.com/api/adwords/cm/v201003/CampaignTargetService?wsdl",
    "CampaignCriterionService": "https://adwords.google.com/api/adwords/cm/v201003/CampaignCriterionService?wsdl",
    "CampaignAdExtensionService": "https://adwords.google.com/api/adwords/cm/v201003/CampaignAdExtensionService?wsdl",
    "AdGroupAdService": "https://adwords.google.com/api/adwords/cm/v201003/AdGroupAdService?wsdl",
    "AdGroupService": "https://adwords.google.com/api/adwords/cm/v201003/AdGroupService?wsdl",
    "AdGroupCriterionService": "https://adwords.google.com/api/adwords/cm/v201003/AdGroupCriterionService?wsdl",
    "AdExtensionOverrideService": "https://adwords.google.com/api/adwords/cm/v201003/AdExtensionOverrideService?wsdl",
    "AdParamService": "https://adwords.google.com/api/adwords/cm/v201003/AdParamService?wsdl",
    "ReportInstanceService": "https://adwords.google.com/api/adwords/cm/v201003/ReportInstanceService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201003/ReportDefinitionService?wsdl",
    "BidLandscapeService": "https://adwords.google.com/api/adwords/cm/v201003/BidLandscapeService?wsdl",
    "GeoLocationService": "https://adwords.google.com/api/adwords/cm/v201003/GeoLocationService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201003/ReportDefinitionService?wsdl",
    "MediaService": "https://adwords.google.com/api/adwords/cm/v201003/MediaService?wsdl",
    "BidLandscapeService": "https://adwords.google.com/api/adwords/cm/v201003/BidLandscapeService?wsdl"
}

DEBUG_WSDLS = dict(
        ((k, v.replace('adwords.google.com', 'adwords-sandbox.google.com')) for k,v in SERVICE_WSDLS.items())
)

from yaaac.service import AdwordsService
