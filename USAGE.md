<!-- Start SDK Example Usage -->
```python
import speakeasy_api
from speakeasy_api.models import operations

s = speakeasy_api.SpeakeasyAPI(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetApisRequest(
    metadata={
        "provident": [
            'quibusdam',
            'unde',
            'nulla',
        ],
        "corrupti": [
            'vel',
            'error',
            'deserunt',
            'suscipit',
        ],
        "iure": [
            'debitis',
            'ipsa',
        ],
    },
    op=operations.GetApisOp(
        and_=False,
    ),
)

res = s.apis.get_apis(req)

if res.apis is not None:
    # handle response
```
<!-- End SDK Example Usage -->