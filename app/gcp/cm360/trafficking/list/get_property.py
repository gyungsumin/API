import re


def campaign(service, cm_profile: str, cm_account: str, cm_advertiser: str, regexp: str = None,
             s_date: str = None, e_date: str = None):
    campaign_list = service.campaigns().list(profileId=cm_profile).execute()['campaigns']

    campaign_list = [e for e in campaign_list if e['startDate'] >= s_date]
    campaign_list = [e for e in campaign_list if e['endDate'] >= e_date]

    if regexp is not None:
        regexp = re.compile(regexp)
        campaign_list = [e for e in campaign_list if regexp.search(e['name']) is True]

    return campaign_list


def placement(service, cm_profile: str, cm_account: str, cm_advertiser: str, regexp: str = None,
              s_date: str = None, e_date: str = None, campaign_id_list: list = None):
    placement_list = service.placements().list(profileId=cm_profile).execute()['placements']

    placement_list = [e for e in placement_list if e['startDate'] >= s_date]
    placement_list = [e for e in placement_list if e['endDate'] >= e_date]

    if regexp is not None:
        regexp = re.compile(regexp)
        placement_list = [e for e in placement_list if regexp.search(e['name']) is True]

    if campaign_id_list is not None:
        placement_list = [e for e in placement_list if e['campaignId'] in campaign_id_list]

    return placement_list


def ad(service, cm_profile: str, cm_account: str, cm_advertiser: str, regexp: str = None,
       s_date: str = None, e_date: str = None, campaign_id_list: list = None, placement_id_list: list = None):
    ad_list = service.ads().list(profileId=cm_profile).execute()['ads']

    ad_list = [e for e in ad_list if e['startDate'] >= s_date]
    ad_list = [e for e in ad_list if e['endDate'] >= e_date]

    if regexp is not None:
        regexp = re.compile(regexp)
        ad_list = [e for e in ad_list if regexp.search(e['name']) is True]

    if campaign_id_list is not None:
        ad_list = [e for e in ad_list if e['campaignId'] in campaign_id_list]

    if placement_id_list is not None:
        ad_list = [e for e in ad_list if e['placementId'] in placement_id_list]

    return ad_list
