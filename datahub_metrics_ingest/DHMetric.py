from typing import Optional

class DHMetric():

    def __init__(self):
        self._timestamp = None
        self._granularity = None
        self._dh_id = None
        self._dh_source_name = None
        self._user_segment = None
        self._access_type = None
        self._count = None

    @property
    def timestamp(self) -> str:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: str):
        self._timestamp = value

    @property
    def granularity(self) -> str:
        return self._granularity

    @granularity.setter
    def granularity(self, value: str):
        self._granularity = value

    @property
    def dh_id(self) -> str:
        return self._dh_id

    @dh_id.setter
    def dh_id(self, value: str):
        self._dh_id = value

    @property
    def dh_source_name(self) -> str:
        return self._dh_source_name

    @dh_source_name.setter
    def dh_source_name(self, value: str):
        self._dh_source_name = value

    @property
    def user_segment(self) -> Optional[str]:
        return self._user_segment

    @user_segment.setter
    def user_segment(self, value: str):
        self._user_segment = value

    @property
    def access_type(self) -> Optional[str]:
        return self._access_type

    @access_type.setter
    def access_type(self, value: str):
        self._access_type = value

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int):
        self._count = value