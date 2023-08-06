from pydantic import BaseModel  # pylint: disable=E0611


class Config(BaseModel):  # pylint: disable=R0903
    max_users: int
    use_email_notification: bool
    use_sms_notification: bool
