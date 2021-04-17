
def SampleInserts():
    # Example Insert
    Pg1 = {"first_name": "Quinn",    # 0
           "last_name": "Testing",  # 1
           "email_address": "test@test.com",  # 2
           "verify_email_address": "test@test.com",  # 3
           "address_line_1": "123 Test Lane",  # 4
           "address_city": "Sioux Falls",  # 5
           "address_state": "SOUTH DAKOTA",  # 6
           "address_zip": "57107",  # 7
           "home_phone": "5555555555",  # 8
           "mobile_phone": "5555555555",  # 9
           "has_checking_account": "No"  # 10
           }
    Pg2 = {"dob_mm": "04",  # 0
           "dob_dd": "02",  # 1
           "dob_yyyy": "1996",  # 2
           "ssn": "666666666",  # 3
           "verify_ssn": "666666666",  # 4
           "occupation": "Retired",  # 5
           "monthly_income_amount": "123",  # 6
           "monthly_obligation_amount": "321",  # 7
           "has_debit_credit_card": "No",  # 8
           "cash_advance": "No",  # 9
           "additional_card": "No"  # 10
           }
    Pg3 = {}
    inserts = [Pg1, Pg2, Pg3]
    return inserts


# SHOULD SWITCH TO DICTIONARIES!!!


# def SampleInserts():
#     # Example Insert
#     Pg1 = ['Quinn'    # 0
#            , 'Testing'  # 1
#            , 'test@test.com'  # 2
#            , 'test@test.com'  # 3
#            , '123 Test Lane'  # 4
#            , 'Sioux Falls'  # 5
#            , 'SOUTH DAKOTA'  # 6
#            , '57107'  # 7
#            , '5555555555'  # 8
#            , '5555555555'  # 9
#            , 'No'  # 10
#            ]
#     Pg2 = ['04'  # 0
#            , '02'  # 1
#            , '1996'  # 2
#            , '666666666'  # 3
#            , '666666666'  # 4
#            , 'Retired'  # 5
#            , '123'  # 6
#            , '321'  # 7
#            , 'No'  # 8
#            , 'No'  # 9
#            , 'No'  # 10
#            ]
#     Pg3 = []
#     inserts = [Pg1, Pg2, Pg3]
#     return inserts
