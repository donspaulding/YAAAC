SERVICE_WSDLS = {
    "AdExtensionOverrideService": "https://adwords.google.com/api/adwords/cm/v201109/AdExtensionOverrideService?wsdl",
    "AdGroupAdService": "https://adwords.google.com/api/adwords/cm/v201109/AdGroupAdService?wsdl",
    "AdGroupCriterionService": "https://adwords.google.com/api/adwords/cm/v201109/AdGroupCriterionService?wsdl",
    "AdGroupService": "https://adwords.google.com/api/adwords/cm/v201109/AdGroupService?wsdl",
    "AdParamService": "https://adwords.google.com/api/adwords/cm/v201109/AdParamService?wsdl",
    "BulkOpportunityService": "https://adwords.google.com/api/adwords/cm/v201109/BulkOpportunityService?wsdl",
    "CampaignAdExtensionService": "https://adwords.google.com/api/adwords/cm/v201109/CampaignAdExtensionService?wsdl",
    "CampaignCriterionService": "https://adwords.google.com/api/adwords/cm/v201109/CampaignCriterionService?wsdl",
    "CampaignService": "https://adwords.google.com/api/adwords/cm/v201109/CampaignService?wsdl",
    "CampaignTargetService": "https://adwords.google.com/api/adwords/cm/v201109/CampaignTargetService?wsdl",
    "ConstantDataService": "https://adwords.google.com/api/adwords/cm/v201109/ConstantDataService?wsdl",
    "ConversionTrackerService": "https://adwords.google.com/api/adwords/cm/v201109/ConversionTrackerService?wsdl",
    "CreateAccountService": "https://adwords.google.com/api/adwords/mcm/v201109/CreateAccountService?wsdl",
    "CustomerSyncService": "https://adwords.google.com/api/adwords/cm/v201109/CustomerSyncService?wsdl",
    "DataService": "https://adwords.google.com/api/adwords/cm/v201109/DataService?wsdl",
    "ExperimentService": "https://adwords.google.com/api/adwords/cm/v201109/ExperimentService?wsdl",
    "GeoLocationService": "https://adwords.google.com/api/adwords/cm/v201109/GeoLocationService?wsdl",
    "InfoService": "https://adwords.google.com/api/adwords/cm/v201109/InfoService?wsdl",
    "LocationCriterionService": "https://adwords.google.com/api/adwords/cm/v201109/LocationCriterionService?wsdl",
    "MediaService": "https://adwords.google.com/api/adwords/cm/v201109/MediaService?wsdl",
    "MutateJobService": "https://adwords.google.com/api/adwords/cm/v201109/MutateJobService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201109/ReportDefinitionService?wsdl",
    "ReportInstanceService": "https://adwords.google.com/api/adwords/cm/v201109/ReportInstanceService?wsdl",
    "ServicedAccountService": "https://adwords.google.com/api/adwords/cm/v201109/ServicedAccountService?wsdl",
    "TargetingIdeaService": "https://adwords.google.com/api/adwords/cm/v201109/TargetingIdeaService?wsdl",
    "TrafficEstimatorService": "https://adwords.google.com/api/adwords/cm/v201109/TrafficEstimatorService?wsdl",
    "UserListService": "https://adwords.google.com/api/adwords/cm/v201109/UserListService?wsdl",
}

DEBUG_WSDLS = dict(
        ((k, v.replace('adwords.google.com', 'adwords-sandbox.google.com')) for k, v in SERVICE_WSDLS.items())
)

from yaaac.service import AdwordsService
