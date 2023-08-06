
from common.log import insert_exception
from prettytable import PrettyTable
import requests
import json,os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv("./config.env")
 
from_mail = os.getenv("FromMail")
from_mail_pwd = os.getenv("FromMailPwd")
to_mail = os.getenv("ToMail")
port = os.getenv("Port")
smtp_server = os.getenv("SMTPServer")
subject = os.getenv("Subject")
mail_text = os.getenv("Mailtext")
fms_mail_text = os.getenv("fmsMailtext")
fms_subject = os.getenv("fmsSubject")
mail_url = os.getenv("Mail_URL")
mail_header = {
    "Authorization": os.getenv("Mail_Key"),
    "Content-Type": "application/json",
}


def get_table(data) -> PrettyTable:
    """
        This will create tabular data
    Args:
        request (_type_):
        data - List of content
    Returns:
        return table formatted html data
    """
    columns = ["AWB", "Invoice No", "Order Date", "Reason"]
    table = PrettyTable()
    table.field_names = columns
    for tdata in data:
        dat = [
            tdata["OrderNo"],
            tdata["InvoiceNo"],
            tdata["OrderDate"],
            tdata["Reason"],
        ]
        table.add_row(dat)
    return table


def get_table_fmsdata(data) -> PrettyTable:
    columns = ["AWB", "Order No", "Shipment No"]
    table = PrettyTable()
    table.field_names = columns
    for tdata in data:
        dat = [
            tdata["awb"],
            tdata["order_no"],
            tdata["shipment_no"],
        ]
        table.add_row(dat)
    return table


def send_mail(type,awbdata):
    """
        This will send formatted data
    Args:
        request (_type_):
        awbdata - List of content
    Returns:
        return success if mail send successfully other wise fail
    """
    try:
        mailtext=""
        subject = ""
        if type == "Reg":
            mailtable=get_table(awbdata)
            mailtext=mail_text
            subject=subject
        elif type == "fms":
            mailtable=get_table_fmsdata(awbdata)
            mailtext=fms_mail_text
            subject=fms_subject
            
        html = (
            """\
                <html>
                <head></head>
                <body>
                    <p>"""
            + mailtext
            + """</p><br>"""
            + mailtable.get_html_string(
                attributes={
                    "border": 2,
                    "style": "border-width: 2px; border-collapse: collapse;",
                }
            )
            + """
                </body>
                </html>
                """
        )
        datatosend = mail_data(
            to=to_mail,
            subject=subject,
            body=str(html))

        response = requests.post(
            mail_url,
            json=datatosend.dict(),
            headers=mail_header,
        )
        if response.status_code == 200:
            res = response.json()
            if res["isSuccess"]:
                return "Success"
            else:
                return "Failed"
    except Exception as e:
        insert_exception(
                "Something went wrong while sending mail - {}".format(str(e)))
        return "Failed"


class mail_data(BaseModel):
    to: str
    subject: str
    body: str
