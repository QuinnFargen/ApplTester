
def SampleInserts():
    # Example Insert
       TotalVisa = {"first_name": "Quinn",    # 0
              "last_name": "Testing",  # 1
              "email_address": "test@test.com",  # 2
              "verify_email_address": "test@test.com",  # 3
              "address_line_1": "123 Test Lane",  # 4
              "address_city": "Sioux Falls",  # 5
              "address_state": "SOUTH DAKOTA",  # 6
              "address_zip": "57107",  # 7
              "home_phone": "5555555555",  # 8
              "mobile_phone": "5555555555",  # 9
              "has_checking_account": "No",  # 10
              "dob_mm": "04",  # 11
              "dob_dd": "02",  # 12
              "dob_yyyy": "1996",  # 13
              "ssn": "666666666",  # 14
              "verify_ssn": "666666666",  # 15
              "occupation": "Retired",  # 16
              "monthly_income_amount": "123",  # 17
              "monthly_obligation_amount": "321",  # 18
              "has_debit_credit_card": "No",  # 19
              "cash_advance": "No",  # 20
              "additional_card": "No"  # 21
              }
       FstPrem = {"first_name": "Nonsense",    # 0
              "last_name": "Testing",  # 1
              "address_line_1": "123 Test Lane",  # 4
              "address_city": "Sioux Falls",  # 5
              "address_state": "SOUTH DAKOTA",  # 6
              "address_zip": "57107",  # 7
              "email_address": "test@test.com",  # 2
              "verify_email_address": "test@test.com",  # 3
              "home_phone": "2234567890",  # 8
              "mobile_phone": "2233216547",  # 9
              "has_checking_account": "No",  # 10
              "dob_mm": "04",  # 11
              "dob_dd": "02",  # 12
              "dob_yyyy": "1996",  # 13
              "ssn": "666666666",  # 14
              "verify_ssn": "666666666",  # 15
              "occupation": "Retired",  # 16
              "monthly_income_amount": "123",  # 17
              "monthly_obligation_amount": "321",  # 18
              "annual_income_amount": "23000",  # 17
              "has_debit_credit_card": "No",  # 19
              "cash_advance": "No",  # 20
              "additional_card": "No"  # 21
              }
       inserts = {"TotalVisa" : TotalVisa,
              "FstPrem" : FstPrem
              }
    return inserts
