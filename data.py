import os
import requests
import random


from datetime import datetime

def get_date_from_datetime(datetime_str):
    try:
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")
        return str(datetime_obj.date())
    except ValueError:
        return str(datetime_str)

def generate_account_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])
random_account_number = generate_account_number()

def download_image(url):
    baseurl = "http://admin.bibaabo.com/"
    if url is None:
        print("Image URL is None")
        return None
    
    imgurl = baseurl + url
    response = requests.get(imgurl)
    
    if response.status_code == 200:
        file_name = os.path.basename(url)
        file_path = os.path.join("statics", file_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_path
    else:
        print(f"Failed to download image from {url}")
        return None

def typeconversion(data):

    personal_data = data["personalDetailModels"]
    relations_data = data['relationsModels']
    occ_data = data['educationOccupationModels']
    citizen_data = data['documentsModel']['Citizenship']
    pass_data =  data['documentsModel']['Passport']
    add_data = data['addresseModels']
    nominee_data = data['nomineeModel']
    pep_data= data['pepDetailModels']
    pan_data = data['documentsModel']['Pan']
    birth_data = data['documentsModel']['Birth Certificate']
    cred_data = data['documentsModel']['Credentials Document']

    signature_nominee = download_image(cred_data.get("profileImage"))

    annualIncome = int(occ_data.get("annualIncome"))

    if annualIncome <= 100000:
        annualIncome = "Up to 1 Lakh"
    elif annualIncome <= 200000:
        annualIncome = "1 Lakh to 2 Lakhs"
    elif annualIncome <= 500000:
        annualIncome = "2 Lakhs to 5 Lakhs"
    elif annualIncome > 500000:
        annualIncome = "5 Lakhs & Above"
    else:
        annualIncome = "Not Available"

    IsRelatedToPoliticianCheck = 1 if pep_data['pepName'] and pep_data['pepOtherRelation'] else 0
    isPoliticianCheck = 1 if pep_data['selectedStatus'] else 0
    personal_data_dict = {
        "firstName": personal_data.get("firstName"),
        "middleName": personal_data.get("secondName"),
        "lastName": personal_data.get("lastName"),
        "dobBS": get_date_from_datetime(personal_data.get("dateOfBirthInBs")),
        "Gender": personal_data.get("gender"),
        "nationality": personal_data.get("nationality"),
        "maritalStatus": relations_data['maritalStatus'],
        "grandFatherName": relations_data['grandFatherName'],
        "fatherName": relations_data['fatherName'],
        "motherName": relations_data['motherName'],
        "husbandOrWifeName": relations_data['spouseName'],
        "sonName": relations_data['sonNames'],
        "daughterName": relations_data['daughterNames'],
        "daughterInLawName": relations_data['daughterInLawName'],
        "fatherInLawName": relations_data['fatherInLawName'],
        "motherInLawName": relations_data['motherInLawName'],
        "panNo": pan_data['panNumber'],
        "isMinor":'',
        "citizenshipNumber": citizen_data['citizenshipNumber'],
        "citizenshipIssueDistrict": citizen_data['issuePlace'],
        "citizenshipIssueDateBS": get_date_from_datetime(citizen_data['bsIssueDate']),
        "passportNumber":pass_data['passportNumber'],
        "passportIssueDistrict":pass_data['issuePlace'],
        "passportIssueDateBS":get_date_from_datetime(pass_data['bsIssueDate']),
        "passportExpireDateBS" : get_date_from_datetime(pass_data['bsIssueDate']),
        "bankName": "xyz",
        "accountNum": random_account_number,
        "accountType": "S.B. Account",
        "bankAddress": "ktm",
        "Next": "Next",
        "cCountry": "Nepal",
        "cProvince": add_data[1]['province'],
        "cDistrict": add_data[1]['district'],
        "cLocalUnit": add_data[1]['localLevel'],
        "select2-cLocalUnitName-container": add_data[1]['localbody'],
        "cWardNum": add_data[1]['ward'],
        "cTole": add_data[1]['tole'],
        "cMobNum": personal_data['mobile'],
        "cEmail": personal_data['email'],
        "cTelephoneNum": personal_data['phone'],
        "isPermanentAddressSameAsCurrentAddress": False,
        "pCountry": "Nepal",
        "pProvince": add_data[0]['province'],
        "pDistrict": add_data[0]['district'],
        "pLocalUnits": add_data[0]['localLevel'],
        "select2-pLocalUnitName-container": add_data[0]['localbody'],
        "pWardNum": add_data[0]['ward'],
        "pTole": add_data[0]['tole'],
        "pMobileNum": personal_data['mobile'],
        "pEmail": personal_data['email'],
        "pTelephoneNum": personal_data['phone'],
        "Next1": "Next",
       
        "occType": occ_data['otherOccupation'],
        "financialDetailsOptions": annualIncome,
        "annualIncomeLimitTrading": annualIncome,
        "businessType":occ_data['businessSector'],
        "orgName": occ_data['companyName'],
        "orgAddress": occ_data['officeAddress'],
        "orgdesignation": occ_data['position'],
        "employeeId": '',
        "HasAutomaticTransactionCheck": "",
        "accountStatement": "",
        "incomeSource":occ_data['otherIncomeSource'],
        "HasAnotherTradingAcctCheck": "",
        "brokerName": "  ",
        "clientId": '  ',
        "IsInvolvedinInvestmentCheck": "1",
        "companyName": occ_data['instituteName'],
        "companyDesignation": occ_data['position'],
        "isPoliticianCheck": isPoliticianCheck,
        "IsRelatedToPoliticianCheck":IsRelatedToPoliticianCheck,
        "PoliticianName":pep_data['pepName'],
        "PoliticianRelation": pep_data['pepOtherRelation'],
        "HasBenificiaryCheck": " ",
        "BenificiaryName": "  ",
        "BenificiaryRelation": " ",
        "HasCriminalCaseCheck": " ",
        "CrimeClause": " ",
        "isBlacklistedCheck": " ",

        "Next2": "Next",

        "NomineeFullName": f"{nominee_data.get('nomineeFirstName')} {nominee_data.get('nomineeMiddleName', '')} {nominee_data.get('nomineeLastName', '')}",
        "NomineeRelation": nominee_data['nomineeRelation'],
        "NomineeCtzNo": nominee_data['nomineeDocumentNumber'],
        "NomineeCtzIssueDistrict": "Dhading",
        "NomineeCtzIssueDateBS": get_date_from_datetime(nominee_data['nomineeDocumentIssueBS']),
        "NomineeCtzIssueDateAD":get_date_from_datetime(nominee_data['nomineeDocumentIssueAD']),
        "NomineeCountry": "Nepal",
        "NomineeProvince": "Bagmati",
        "NomineeDistrict": "Dhading",
        "nomineeLocalUnit": " VDC ",
        "select2-nomineelocalunitName-container":"Benighat",
        "nomineeWardNum": "2",
        "nomineeTole": "Benighat",
        "NomineeMobileNo": nominee_data['nomineeContact'],
        "NomineeEmail": nominee_data['nomineeMail'],
        "NomineeTelNo": " ",

        "Next3": "Next",
        "file0": {"value":signature_nominee, "field": "BankChequePhoto"},
        "file1":{"value":signature_nominee,"field":"MinorPhoto"},
        "file2":{"value":download_image(birth_data.get("certificateImage")),"field":"BirthCertificate"},
        "file3":{"value":signature_nominee,"field":"MinorSelfieWithDocument"},
        "file4":{"value":signature_nominee,"field":"GuardianPhoto"},
        "file5":{"value":signature_nominee,"field":"GuardianCitizenship"},
        "file6":{"value":signature_nominee,"field":"GuardianCtzBack"},
        "file7":{"value":signature_nominee,"field":"GuardianThumbLeft"},
        "file8":{"value":signature_nominee,"field":"GuardianThumbRight"},
        "file9":{"value":signature_nominee,"field":"GuardianSignature"},
        "file10":{"value":signature_nominee,"field":"GuardianSelfie"},
        "file11":{"value":signature_nominee,"field":"GuardianMap"},

        "file12":{"value":signature_nominee ,"field":"NomineePhoto"},
        "file13":{"value":download_image(nominee_data.get("rightThumb")) ,"field":"NomineeThumbRight"},
        "file14":{"value":download_image(nominee_data.get("leftThumb")) ,"field":"NomineeThumbLeft"},
        "file15":{"value":download_image(nominee_data.get("frontImage")) ,"field":"NomineeCtzFront"},
        "file16":{"value":download_image(nominee_data.get("backImage")) ,"field":"NomineeCtzBack"},
        "file17":{"value":download_image(nominee_data.get("signature")) ,"field":"NomineeSignature"},

        "file18":{"value":download_image(pan_data.get("nepaliFront")),"field":"BankChequePhoto"},
        "file19":{"value":download_image(pan_data.get("nepaliFront")),"field":"PanCard"},
        "file20":{"value":download_image(pan_data.get("nepaliFront")),"field":"GuardianPanCard"},

        "file21":{"value":download_image(cred_data.get("profileImage")),"field":"ApplicantPhoto"},
        "file22":{"value":download_image(cred_data.get("locationMapImage")),"field":"AccountHolderMap"},
        "file23":{"value":download_image(cred_data.get("signatureImage")),"field":"ApplicantSignature"},
        "file24":{"value":download_image(cred_data.get("rightThumbImage")),"field":"ApplicantThumbRight"},
        "file25":{"value":download_image(cred_data.get("leftThumbImage")),"field":"ApplicantThumbLeft"},

        "file26":{"value":download_image(citizen_data.get("frontImage")),"field":"CitizenshipFront"},
        "file27":{"value":download_image(citizen_data.get("backImage")),"field":"CitizenshipBack"},
        "file28":{"value":download_image(citizen_data.get("selfieImage")),"field":"SelfieWithDocument"},

        "file29":{"value":download_image(citizen_data.get("selfieImage")),"field":"ForeignEmployeeCard"},
        "companyBranch":"Head office",
        "chkIsSelfVerification":"1",
        "isAgreedTC":"1",
        "Next4": "Next",
        "Next5": "Next",
        "finish":"",
        "VideoKyc":"VideoKyc",
        "Ok":"Ok",
        "finish1":"",
        "submissionCode":"",
        "finalok":"Ok"
    }
    return personal_data_dict
