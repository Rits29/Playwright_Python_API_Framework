from typing import Optional
from payloads.models.base_payload_model import BasePayloadModel
from pydantic import Field

class GetVersionRequest(BasePayloadModel):

    tracking_id: Optional[str] = None
    tracking_id: Optional[str] = Field(default=None, description="Optional tracking identifier for SOAP header")

    @classmethod
    def generate(cls, tracking_id: Optional[str] = None):
        return cls(tracking_id=tracking_id)

    def serialize(self):
        header = ""
        if self.tracking_id:
            header = f"""
            <soapenv:Header>
                <trackingId>{self.tracking_id}</trackingId>
            </soapenv:Header>
            """
        else:
            header = "<soapenv:Header/>"

        return f"""<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ns="http://axisversion.sample">

{header}

<soapenv:Body>
    <ns:getVersion/>
</soapenv:Body>

</soapenv:Envelope>
"""