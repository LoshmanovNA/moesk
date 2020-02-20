
class ClaimModel:

    def __init__(self,
                 reassignment_claim_number='И1600123456102',
                 user_date_birth='01.01.1981',
                 user_passport_number='1234567890',
                 user_passport_date='01.01.1998',
                 user_passport_code='123456',
                 user_passport_issued='Отделение №1',
                 user_fl_snils='14542724657',
                 user_other_document='Другой документ',
                 user_ip_egrip='111111111111111',
                 user_ul_kpp='000000000',
                 user_ul_egrul_num='0000000000000',
                 user_reestr_date='06.10.2018',
                 user_inn='000000000000',
                 user_rs='11111111111111111111',
                 user_bik='044525745',
                 user_bank='ООО Банк',
                 user_address_house='10',
                 user_address_index='123456',
                 proxy_number='123456',
                 proxy_date='01.01.1981',
                 proxy_fio='Доверенов Доверитель Доверяевич',
                 trustee_notice_email='user@user.user',
                 trustee_notice_phone='990000000'):

        # Номер заявки для переуступки
        self.reassignment_claim_number = reassignment_claim_number
        # Документы заявителя
        self.user_date_birth = user_date_birth
        self.user_passport_number = user_passport_number
        self.user_passport_date = user_passport_date
        self.user_passport_code = user_passport_code
        self.user_passport_issued = user_passport_issued
        self.user_fl_snils = user_fl_snils
        self.user_other_document = user_other_document
        # Реквизиты заявителя
        self.user_ip_egrip = user_ip_egrip
        self.user_ul_kpp = user_ul_kpp
        self.user_ul_egrul_num = user_ul_egrul_num
        self.user_reestr_date = user_reestr_date
        self.user_inn = user_inn
        self.user_rs = user_rs  # Расчетный счет
        self.user_bik = user_bik
        self.user_bank = user_bank
        # Адрес регистрации / направления корреспонденции
        self.user_address_house = user_address_house
        self.user_address_index = user_address_index
        # Данные представителя по доверенности
        self.proxy_number = proxy_number
        self.proxy_date = proxy_date
        self.proxy_fio = proxy_fio
        self.trustee_notice_email = trustee_notice_email
        self.trustee_notice_phone = trustee_notice_phone
