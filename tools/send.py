from feapder.utils.tools import *
from tools.message import *
from tools.message.qywxmsg import smtp_gyqq


def send_msg(msg, level="DEBUG", message_prefix="", keyword=""):
    if setting.WARNING_LEVEL == "ERROR":
        if level.upper() != "ERROR":
            return

    if setting.DINGDING_WARNING_URL:
        dingding_warning(keyword + msg, message_prefix=message_prefix)

    if setting.EMAIL_RECEIVER:
        title = message_prefix or msg
        if len(title) > 50:
            title = title[:50] + "..."
        email_warning(msg, message_prefix=message_prefix, title=title)

    # if setting.QYWX_KEY or setting.EMAIL_PASSWORD:
    #     wecom_bot("可达鸭查寝版",keyword + msg)
    #     smtp_gyqq("gzist爱查寝", keyword + msg)

    if setting.EMAIL_PASSWORD:
        smtp_gyqq("gzist爱查寝",keyword + msg)

    if setting.FEISHU_WARNING_URL:
        feishu_warning(keyword + msg, message_prefix=message_prefix)

    if setting.QMSG_WARNING_URL:
        qmsg_warning(keyword + msg, message_prefix=message_prefix)


if __name__ == '__main__':
    send_msg("123")
