from pydantic import BaseModel


class FieldDataDto(BaseModel):
    message: str | None
    field: str | None
    value: str | None


class CustomResponseModelDto(BaseModel):
    status_code: int | None
    id: str | None
    traceid: str | None
    type: str | None
    message: str | None
    fields: list[FieldDataDto] | None


class CustomSuccessResponseModelDto(BaseModel):
    status_code: int | None
    message: str | None


class ExceptionResponse(BaseModel):
    shipment_id: str = None
    traceid: str
    type: str
    message: str
    fields: list[FieldDataDto] = []


class ExceptionResponseWithStatus(ExceptionResponse):
    status_code: int
