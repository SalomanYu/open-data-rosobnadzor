import xmltodict
import json

from models import Certificate, ActualEducationOrganization

def try_get_value_by_key(data:dict, key: str, dop_param: str = None) -> str | None:
    try:
        if dop_param: result = data[key][dop_param]
        else: result = data[key]
    except:
        result = None
    finally:
        return result

def prepare_certificates(items: list[dict]) -> list[Certificate]:
    list_of_certificates: list[Certificate] = []
    for item in items:
        list_of_certificates.append(Certificate(
            IsFederal=try_get_value_by_key(item, "IsFederal"),
            Id =  try_get_value_by_key(item, "Id"),
            ActualEducationOrganizationId =  try_get_value_by_key(item, "ActualEducationOrganization", dop_param="Id"),
            StatusName =  try_get_value_by_key(item, "StatusName"),
            StatusCode =  try_get_value_by_key(item, "StatusCode"),
            TypeName =  try_get_value_by_key(item, "TypeName"),
            TypeCode =  try_get_value_by_key(item, "TypeCode"),
            RegionName =  try_get_value_by_key(item, "RegionName"),
            RegionCode =  try_get_value_by_key(item, "RegionCode"),
            FederalDistrictName =  try_get_value_by_key(item, "FederalDistrictName"),
            FederalDistrictShortName =  try_get_value_by_key(item, "FederalDistrictShortName"),
            FederalDistrictCode =  try_get_value_by_key(item, "FederalDistrictCode"),
            RegNumber =  try_get_value_by_key(item, "RegNumber"),
            SerialNumber =  try_get_value_by_key(item, "SerialNumber"),
            FormNumber =  try_get_value_by_key(item, "FormNumber"),
            IssueDate =  try_get_value_by_key(item, "IssueDate"),
            EndDate =  try_get_value_by_key(item, "EndDate"),
            ControlOrgan =  try_get_value_by_key(item, "ControlOrgan"),
            PostAddress =  try_get_value_by_key(item, "PostAddress"),
            EduOrgFullName =  try_get_value_by_key(item, "EduOrgFullName"),
            EduOrgShortName =  try_get_value_by_key(item, "EduOrgShortName"),
            EduOrgINN =  try_get_value_by_key(item, "EduOrgINN"),
            EduOrgOGRN =  try_get_value_by_key(item, "EduOrgOGRN"),
            IndividualEntrepreneurLastName =  try_get_value_by_key(item, "IndividualEntrepreneurLastName"),
            IndividualEntrepreneurFirstName =  try_get_value_by_key(item, "IndividualEntrepreneurFirstName"),
            IndividualEntrepreneurMiddleName =  try_get_value_by_key(item, "IndividualEntrepreneurMiddleName"),
            IndividualEntrepreneurAddress =  try_get_value_by_key(item, "IndividualEntrepreneurAddress"),
            IndividualEntrepreneurEGRIP =  try_get_value_by_key(item, "IndividualEntrepreneurEGRIP"),
            IndividualEntrepreneurINN =  try_get_value_by_key(item, "IndividualEntrepreneurINN")
        ))
    return list_of_certificates
    
def prepare_educations(items: list[dict]) -> list[ActualEducationOrganization]:
    list_of_educations: list[ActualEducationOrganization] = []
    for i in items:
        try:item = i["ActualEducationOrganization"]
        except: continue
        list_of_educations.append(ActualEducationOrganization(
            Id = try_get_value_by_key(item, 'Id'),
            FullName = try_get_value_by_key(item, 'FullName'),
            ShortName = try_get_value_by_key(item, 'ShortName'),
            HeadEduOrgId = try_get_value_by_key(item, 'HeadEduOrgId'),
            IsBranch = try_get_value_by_key(item, 'IsBranch'),
            PostAddress = try_get_value_by_key(item, 'PostAddress'),
            Phone = try_get_value_by_key(item, 'Phone'),
            Fax = try_get_value_by_key(item, 'Fax'),
            Email = try_get_value_by_key(item, 'Email'),
            WebSite = try_get_value_by_key(item, 'WebSite'),
            OGRN =try_get_value_by_key(item, 'OGRN'),
            INN = try_get_value_by_key(item, 'INN'),
            KPP = try_get_value_by_key(item, 'KPP'),
            HeadName = try_get_value_by_key(item, 'HeadName'),
            HeadPost = try_get_value_by_key(item, 'HeadPost'),
            FormName = try_get_value_by_key(item, 'FormName'),
            FormCode = try_get_value_by_key(item, 'FormCode'),
            KindName = try_get_value_by_key(item, 'KindName'),
            KindCode = try_get_value_by_key(item, 'KindCode'),
            TypeName = try_get_value_by_key(item, 'TypeName'),
            TypeCode = try_get_value_by_key(item, 'TypeCode'),
            RegionName = try_get_value_by_key(item, 'RegionName'),
            RegionCode = try_get_value_by_key(item, 'RegionCode'),
            FederalDistrictCode = try_get_value_by_key(item, 'FederalDistrictCode'),
            FederalDistrictName = try_get_value_by_key(item, 'FederalDistrictName'),
            FederalDistrictShortName = try_get_value_by_key(item, 'FederalDistrictShortName'),
        ))
    return list_of_educations



def convert_xml_to_json(xmlPath: str):
    with open(xmlPath, 'r', encoding="utf-8") as myfile:
        obj = xmltodict.parse(myfile.read())

    jsonPath = xmlPath.replace(".xml", ".json")
    with open(jsonPath, "w", encoding="utf-8") as myfile:
        json.dump(obj, myfile, ensure_ascii=False, indent=2)