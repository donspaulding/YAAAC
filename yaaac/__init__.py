SERVICE_WSDLS = {
    "AdExtensionOverrideService": "https://adwords.google.com/api/adwords/cm/v201306/AdExtensionOverrideService?wsdl",
    "AdGroupAdService": "https://adwords.google.com/api/adwords/cm/v201306/AdGroupAdService?wsdl",
    "AdGroupCriterionService": "https://adwords.google.com/api/adwords/cm/v201306/AdGroupCriterionService?wsdl",
    "AdGroupService": "https://adwords.google.com/api/adwords/cm/v201306/AdGroupService?wsdl",
    "AdParamService": "https://adwords.google.com/api/adwords/cm/v201306/AdParamService?wsdl",
    "BudgetService": "https://adwords.google.com/api/adwords/cm/v201306/BudgetService?wsdl",
    "BulkOpportunityService": "https://adwords.google.com/api/adwords/cm/v201306/BulkOpportunityService?wsdl",
    "CampaignAdExtensionService": "https://adwords.google.com/api/adwords/cm/v201306/CampaignAdExtensionService?wsdl",
    "CampaignCriterionService": "https://adwords.google.com/api/adwords/cm/v201306/CampaignCriterionService?wsdl",
    "CampaignService": "https://adwords.google.com/api/adwords/cm/v201306/CampaignService?wsdl",
    "CampaignTargetService": "https://adwords.google.com/api/adwords/cm/v201306/CampaignTargetService?wsdl",
    "ConstantDataService": "https://adwords.google.com/api/adwords/cm/v201306/ConstantDataService?wsdl",
    "ConversionTrackerService": "https://adwords.google.com/api/adwords/cm/v201306/ConversionTrackerService?wsdl",
    "CustomerSyncService": "https://adwords.google.com/api/adwords/cm/v201306/CustomerSyncService?wsdl",
    "DataService": "https://adwords.google.com/api/adwords/cm/v201306/DataService?wsdl",
    "ExperimentService": "https://adwords.google.com/api/adwords/cm/v201306/ExperimentService?wsdl",
    "GeoLocationService": "https://adwords.google.com/api/adwords/cm/v201306/GeoLocationService?wsdl",
    "InfoService": "https://adwords.google.com/api/adwords/cm/v201306/InfoService?wsdl",
    "LocationCriterionService": "https://adwords.google.com/api/adwords/cm/v201306/LocationCriterionService?wsdl",
    "ManagedCustomerService": "https://adwords.google.com/api/adwords/cm/v201306/ServicedAccountService?wsdl",
    "MediaService": "https://adwords.google.com/api/adwords/cm/v201306/MediaService?wsdl",
    "MutateJobService": "https://adwords.google.com/api/adwords/cm/v201306/MutateJobService?wsdl",
    "ReportDefinitionService": "https://adwords.google.com/api/adwords/cm/v201306/ReportDefinitionService?wsdl",
    "ReportInstanceService": "https://adwords.google.com/api/adwords/cm/v201306/ReportInstanceService?wsdl",
    "TargetingIdeaService": "https://adwords.google.com/api/adwords/cm/v201306/TargetingIdeaService?wsdl",
    "TrafficEstimatorService": "https://adwords.google.com/api/adwords/cm/v201306/TrafficEstimatorService?wsdl",
    "UserListService": "https://adwords.google.com/api/adwords/cm/v201306/UserListService?wsdl",
}

DEBUG_WSDLS = dict(
        ((k, v.replace('adwords.google.com', 'adwords-sandbox.google.com')) for k, v in SERVICE_WSDLS.items())
)

from yaaac.service import AdwordsService
