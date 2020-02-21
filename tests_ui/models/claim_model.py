
class ClaimModel:

    def __init__(self,
                 # Данные для первого шага
                 reassignment_claim_number='И1600123456102',
                 # Данные для второго шага
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
                 region='Московская обл',
                 area='Волоколамский',
                 city='Волоколамск',
                 street='Аграрная',
                 post_index='123456',
                 proxy_number='123456',
                 proxy_date='01.01.1981',
                 proxy_fio='Доверенов Доверитель Доверяевич',
                 trustee_notice_email='user@user.user',
                 trustee_notice_phone='990000000',
                 # Данные для 3 шага
                 consolidation_filial_id=True,
                 epu_type=True,
                 cadastral_number='77:03:0006026:1009',
                 temp_connection_period=True,
                 max_power='15',
                 pre_power='30',
                 voltage_level=True,
                 reliability_level=True,
                 connection_points='1',
                 object_readiness=True):

        # Первый шаг
        self.reassignment_claim_number = reassignment_claim_number
        # Второй шаг
        self.user_date_birth = user_date_birth
        self.user_passport_number = user_passport_number
        self.user_passport_date = user_passport_date
        self.user_passport_code = user_passport_code
        self.user_passport_issued = user_passport_issued
        self.user_fl_snils = user_fl_snils
        self.user_other_document = user_other_document
        self.user_ip_egrip = user_ip_egrip
        self.user_ul_kpp = user_ul_kpp
        self.user_ul_egrul_num = user_ul_egrul_num
        self.user_reestr_date = user_reestr_date
        self.user_inn = user_inn
        self.region = region
        self.area = area
        self.city = city
        self.street = street
        self.post_index = post_index
        self.proxy_number = proxy_number
        self.proxy_date = proxy_date
        self.proxy_fio = proxy_fio
        self.trustee_notice_email = trustee_notice_email
        self.trustee_notice_phone = trustee_notice_phone
        # Третий шаг
        self.consolidation_filial_id = consolidation_filial_id
        self.epu_type = epu_type
        self.cadastral_number = cadastral_number
        self.temp_connection_period = temp_connection_period
        self.max_power = max_power
        self.pre_power = pre_power
        self.voltage_level = voltage_level
        self.reliability_level = reliability_level
        self.connection_points = connection_points
        self.object_readiness = object_readiness


