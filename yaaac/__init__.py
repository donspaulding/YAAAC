SERVICE_WSDLS = {
    "AdExtensionOverrideService": "https://adwords.google.com/api/adwords/cm/v201209/AdExtensionOverrideService?wsdl",
    "AdGroupAdService": "https://adwords.google.com/api/adwords/cm/v201209/AdGroupAdService?wsdl",
    "AdGroupCriterionService": "https://adwords.google.com/api/adwords/cm/v201209/AdGroupCriterionService?wsdl",
    "AdGroupService": "https://adwords.google.com/api/adwords/cm/v201209/AdGroupService?wsdl",
    "AdParamService": "https://adwords.google.com/api/adwords/cm/v201209/AdParamService?wsdl",
    "BudgetService": "https://adwords.google.com/api/adwords/cm/v201209/BudgetService?wsdl",
    "BulkOpportunityService": "https://adwords.google.com/api/adwords/cm/v201209/BulkOpportunityService?wsdl",
    "CampaignAdExtensionService": "https://adwords.google.com/api/adwords/cm/v201209/CampaignAdExtensionService?wsdl",
    "CampaignCriterionService": "https://adwords.google.com/api/adwords/cm/v201209/CampaignCriterionService?wsdl",
    "CampaignService": "https://adwords.google.com/api/adwords/cm/v201209/CampaignService?wsdl",
    "CampaignTargetService": "https://adwords.google.com/api/adwords/cm/v201209/CampaignTargetService?wsdl",
    "ConstantDataService": "https://adwords.google.com/api/adwords/cm/v201209/ConstantDataService?wsdl",
    "ConversionTrackerService": "https://adwords.google.com/api/adwords/cm/v201209/ConversionTrackerService?wsdl",
    "CustomerSyncService": "https://adwords.google.com/api/adwords/cm/v201209/CustomerSyncService?wsdl",
    "DataService": "https://adwords.google.com/api/adwords/cm/v201209/DataService?wsdl",
    "ExperimentService": "https://adwords.google.com/api/adwords/cm/v201209/ExperimentService?wsdl",
    "GeoLocationService": "https://adwords.google.com/api/adwords/cm/v201209/GeoLocationService?wsdl",
    "InfoService": "https://adwords.google.com/api/adwords/cm/v201209/InfoService?wsdl",
    "LocationCriterionService": "https://adwords.google.com/api/adwords/cm/v201209/LocationCriterionService?wsdl",
    "ManagedCustomerService": "https://adwords.google.com/api/adwords/cm/v201209/ServicedAccountService?wsdl",
    "MediaService": "https://adwords.google.com/api/adwords/cm/v201209/MediaService?wsdl",
    "MutateJobService": "https://adwords.google.com/api/adwords/cm/v201209/MutateJobService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201209/ReportDefinitionService?wsdl",
    "ReportInstanceService": "https://adwords.google.com/api/adwords/cm/v201209/ReportInstanceService?wsdl",
    "TargetingIdeaService": "https://adwords.google.com/api/adwords/cm/v201209/TargetingIdeaService?wsdl",
    "TrafficEstimatorService": "https://adwords.google.com/api/adwords/cm/v201209/TrafficEstimatorService?wsdl",
    "UserListService": "https://adwords.google.com/api/adwords/cm/v201209/UserListService?wsdl",
}

DEBUG_WSDLS = dict(
        ((k, v.replace('adwords.google.com', 'adwords-sandbox.google.com')) for k, v in SERVICE_WSDLS.items())
)

from yaaac.service import AdwordsService
