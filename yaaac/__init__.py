VERSION = "0.2.3"
SERVICE_WSDLS = {
    "CampaignService": "https://adwords.google.com/api/adwords/cm/v201008/CampaignService?wsdl",
    "CampaignTargetService": "https://adwords.google.com/api/adwords/cm/v201008/CampaignTargetService?wsdl",
    "CampaignCriterionService": "https://adwords.google.com/api/adwords/cm/v201008/CampaignCriterionService?wsdl",
    "CampaignAdExtensionService": "https://adwords.google.com/api/adwords/cm/v201008/CampaignAdExtensionService?wsdl",
    "AdGroupAdService": "https://adwords.google.com/api/adwords/cm/v201008/AdGroupAdService?wsdl",
    "AdGroupService": "https://adwords.google.com/api/adwords/cm/v201008/AdGroupService?wsdl",
    "AdGroupCriterionService": "https://adwords.google.com/api/adwords/cm/v201008/AdGroupCriterionService?wsdl",
    "AdExtensionOverrideService": "https://adwords.google.com/api/adwords/cm/v201008/AdExtensionOverrideService?wsdl",
    "AdParamService": "https://adwords.google.com/api/adwords/cm/v201008/AdParamService?wsdl",
    "ReportInstanceService": "https://adwords.google.com/api/adwords/cm/v201008/ReportInstanceService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201008/ReportDefinitionService?wsdl",
    "BidLandscapeService": "https://adwords.google.com/api/adwords/cm/v201008/BidLandscapeService?wsdl",
    "GeoLocationService": "https://adwords.google.com/api/adwords/cm/v201008/GeoLocationService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201008/ReportDefinitionService?wsdl",
    "MediaService": "https://adwords.google.com/api/adwords/cm/v201008/MediaService?wsdl",
    "BidLandscapeService": "https://adwords.google.com/api/adwords/cm/v201008/BidLandscapeService?wsdl"
}

DEBUG_WSDLS = dict(
        ((k, v.replace('adwords.google.com', 'adwords-sandbox.google.com')) for k,v in SERVICE_WSDLS.items())
)

from yaaac.service import AdwordsService
