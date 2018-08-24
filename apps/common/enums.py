from enum import Enum


class ADDRESS_TYPE(Enum):
    """
    地址类型
    """
    DEFAULT = 0
    STORE_ADDRESS = 1
    USER_HOME_ADDRESS = 2
    USER_COMPANY_ADDRESS = 3