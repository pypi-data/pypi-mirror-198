from ._types import UserTypes, SignInResultTypes
import datetime


class User:
    def __init__(
            self,
            combo_token: str,
            sys_version: str,
            device_id: str,
            device_name: str,
            device_model: str,
            *,
            nickname: str = "",
            user_type: UserTypes = UserTypes.ANDROID_USER
    ):
        """
        :param combo_token: The **x-rpc-combo_token** in headers
        :param sys_version: The **x-rpc-sys_version** in headers
        :param device_id: The **x-rpc-device_id** in headers
        :param device_name: The **x-rpc-device_name** in headers
        :param device_model: The **x-rpc-device_model** in headers
        :key nickname: Nickname used for identification, should be a str
        :key user_type: Type of user, should be a type of UserTypes
        """
        self.nickname: str = nickname
        self.type: UserTypes = user_type
        self._headers = {
            "x-rpc-combo_token": combo_token,
            "x-rpc-client_type": str(self.type.value),
            "x-rpc-sys_version": sys_version,
            "x-rpc-channel": "mihoyo",
            "x-rpc-device_id": device_id,
            "x-rpc-device_name": device_name,
            "x-rpc-device_model": device_model,
            "x-rpc-app_id": "1953439974",
            "x-rpc-vendor_id": "1"
        }

    @property
    def headers(self):
        return self._headers


class WalletData:
    def __init__(self,
                 user: User,
                 coin: int,
                 free_time: int,
                 send_free_time: int,
                 play_card: bool,
                 coin_limit: int,
                 free_time_limit: int
                 ):
        self._user = user
        self._coin = coin
        self._free_time = free_time
        self._send_free_time = send_free_time
        self._is_play_card = play_card
        self._coin_limit = coin_limit
        self._free_time_limit = free_time_limit

    @classmethod
    def from_wallet(cls, user: User, wallet_data: dict):
        """
        Build walletData from json
        :param user:
        :param wallet_data:
        :return:
        """
        coin = int(wallet_data["coin"]["coin_num"])
        send_free_time = int(wallet_data["free_time"]["send_freetime"])
        free_time = int(wallet_data["free_time"]["free_time"])
        play_card = wallet_data["play_card"]["expire"] != 0
        coin_limit = int(wallet_data["coin"]["coin_limit"])
        free_time_limit = int(wallet_data["free_time"]["free_time_limit"])
        return cls(user, coin, free_time, send_free_time, play_card, coin_limit, free_time_limit)

    @property
    def coin(self):
        """
        Get the user's coins
        :return: The user's coins
        """
        return self._coin

    @property
    def free_time(self):
        """
        Get the user's free time
        :return: The user's free time
        """
        return self._free_time

    @property
    def send_free_time(self):
        """
        Get new free time from user
        :return: New free time from user
        """
        return self._send_free_time

    @property
    def is_play_card(self):
        """
        Get whether the user is a play card
        :return: The user is a play card
        """
        return self._is_play_card

    @property
    def coin_limit(self):
        """
        Get coin limit
        :return: Coin limit
        """
        return self._coin_limit

    @property
    def free_time_limit(self):
        """
        Get free time limit
        :return: Free time limit
        """
        return self._free_time_limit

    @property
    def user(self):
        """
        Get the owner of the wallet
        :return: The owner of the wallet
        """
        return self._user

    def free_date_time(self) -> datetime.time:
        return datetime.time(self.free_time // 60, self.free_time % 60)

    def coin_date_time(self) -> datetime.time:
        ct = self.coin // 10
        return datetime.time(ct // 60, ct % 60)


class SignInResult:
    def __init__(self, wallet_data: WalletData):
        self._wallet_data = wallet_data

    @property
    def wallet_data(self):
        """
        Get the wallet data
        :return: wallet data
        """
        return self._wallet_data

    @property
    def result(self) -> SignInResultTypes:
        """
        Get the result of action
        :return: 0 for success, 1 for signed in, 2 for exceeding the limit, -1 for failure
        """
        if self._wallet_data.free_time >= self._wallet_data.free_time_limit:
            result = SignInResultTypes.OVER_LIMIT
        elif self._wallet_data.send_free_time == 0:
            result = SignInResultTypes.DONE
        elif self._wallet_data.send_free_time != 0:
            result = SignInResultTypes.SUCCESS
        else:
            result = SignInResultTypes.ERROR
        return result

    @property
    def user(self):
        """
        Get the user of the action
        :return: The user of the action
        """
        return self._wallet_data.user
