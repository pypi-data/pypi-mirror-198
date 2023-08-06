from dto.custom_exception_model_dto import (
    CustomSuccessResponseModelDto,
    FieldDataDto,
    CustomResponseModelDto,
    ExceptionResponseWithStatus
)  
from flask import Response
from http import HTTPStatus
import uuid
import json


def set_response(message, status_code):
    """
        This will create successful response
    Args:
        request (_type_):
        message - Response message
        status_code - status code
    Returns:
        return formatted successful response
    """
    return_message = json.loads(CustomSuccessResponseModelDto(
        message=message, status_code=status_code
    ).json())
    return return_message


def send_failed_response(message="BAD REQUEST",
                         field_msg="",
                         status_code=HTTPStatus.BAD_REQUEST,
                         type="BAD_REQUEST",
                         field="",
                         value=""):
    """
        This will create failed response
    Args:
        request (_type_):
        message= Reponse message
        field_msg= Field message
        status_code= Status code
        type= Response type
        field= List of data
        value= Response value
    Returns:
        return formatted successful response
    """
    uuid = str(get_guid())
    request_trace_id = str(get_guid())
    fieldsdata: list[FieldDataDto] = []
    if field != "":
        data = FieldDataDto()
        data.field = field
        data.message = field_msg
        data.value = value
        fieldsdata.append(data)

    response = json.loads(
        CustomResponseModelDto(message=message,
                               status_code=status_code,
                               id=uuid,
                               traceid=request_trace_id,
                               type="/errors/" + type,
                               fields=fieldsdata
                               ).json()
    )
    return response


def get_guid():
    return uuid.uuid4()



def build_exception_response(
    type: str,
    exception_msg: str,
    shipment_no: str = None,
    status=HTTPStatus.BAD_REQUEST,
    fields: list[FieldDataDto] = [],
):
    """Helper class to generate the expection repsponse

    Args:
        type (str): Type of error
        exception_msg (str): Exception message to display
        status (int, optional): HTTP Status for each shipment_no.
        Defaults to HTTPStatus.BAD_REQUEST.
        fields (list[ExceptionField], optional): _description_. Defaults to [].

    Returns:
        ExceptionResponse: _description_
    """
    exception_response = ExceptionResponseWithStatus(
        shipment_id=shipment_no,
        traceid=str(get_guid()),
        type=type,
        message=exception_msg,
        status_code=status,
        fields=fields,
    )

    return json.loads(exception_response.json())