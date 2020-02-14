
class MainPageLocators:
    # Кнопки подачи заявок
    MAIN_PAGE_BUTTON_CLAIM_TP_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                      '@href, "new?operation_type_id=1")]'
    MAIN_PAGE_BUTTON_CLAIM_CONSOLIDATION_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                                 '@href, "new?operation_type_id=6")]'
    MAIN_PAGE_BUTTON_CLAIM_DU_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                      '@href, "new?operation_type_id=5")]'
    MAIN_PAGE_BUTTON_CLAIM_RECOVERY_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                            '@href, "new?operation_type_id=3")]'
    MAIN_PAGE_BUTTON_CLAIM_REDISTRIBUTION_XPATH = '//div[@class="claim-types"]/a[contains(' \
                                                  '@href, "new?operation_type_id=2")]'
