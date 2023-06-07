# SpeakeasyAPI SDK

## Overview

Speakeasy API: The Speakeasy API allows teams to manage common operations with their APIs

The Speakeasy Platform Documentation
<https://docs.speakeasyapi.dev>
### Available Operations

* [validate_api_key](#validate_api_key) - Validate the current api key.

## validate_api_key

Validate the current api key.

### Example Usage

```python
import speakeasy_api


s = speakeasy_api.SpeakeasyAPI(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


res = s.speakeasy_api.validate_api_key()

if res.status_code == 200:
    # handle response
```
