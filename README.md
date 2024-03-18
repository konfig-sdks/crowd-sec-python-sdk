<div align="center">

[![Visit Crowdsec](./header.png)](https://www.crowdsec.net&#x2F;)

# Crowdsec<a id="crowdsec"></a>

CrowdSec local API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`crowdsec.bouncers.get_decisions_stream`](#crowdsecbouncersget_decisions_stream)
  * [`crowdsec.bouncers.get_decisions_stream_0`](#crowdsecbouncersget_decisions_stream_0)
  * [`crowdsec.bouncers.get_information`](#crowdsecbouncersget_information)
  * [`crowdsec.bouncers.get_information_0`](#crowdsecbouncersget_information_0)
  * [`crowdsec.watchers.authenticate_session`](#crowdsecwatchersauthenticate_session)
  * [`crowdsec.watchers.create_alerts`](#crowdsecwatcherscreate_alerts)
  * [`crowdsec.watchers.delete_alert_by_id`](#crowdsecwatchersdelete_alert_by_id)
  * [`crowdsec.watchers.get_alert_by_id`](#crowdsecwatchersget_alert_by_id)
  * [`crowdsec.watchers.get_alert_by_id_0`](#crowdsecwatchersget_alert_by_id_0)
  * [`crowdsec.watchers.list_alerts`](#crowdsecwatcherslist_alerts)
  * [`crowdsec.watchers.register_watcher`](#crowdsecwatchersregister_watcher)
  * [`crowdsec.watchers.remove_alerts`](#crowdsecwatchersremove_alerts)
  * [`crowdsec.watchers.remove_decision_by_id`](#crowdsecwatchersremove_decision_by_id)
  * [`crowdsec.watchers.remove_decisions`](#crowdsecwatchersremove_decisions)
  * [`crowdsec.watchers.search_alerts`](#crowdsecwatcherssearch_alerts)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=CrowdSec&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from crowd_sec_python_sdk import CrowdSec, ApiException

crowdsec = CrowdSec(
    api_key_authorizer="YOUR_API_KEY",
)

try:
    # getDecisionsStream
    get_decisions_stream_response = crowdsec.bouncers.get_decisions_stream(
        startup=True,
        scopes="string_example",
        origins="string_example",
        scenarios_containing="string_example",
        scenarios_not_containing="string_example",
    )
    print(get_decisions_stream_response)
except ApiException as e:
    print("Exception when calling BouncersApi.get_decisions_stream: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["message"])
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from crowd_sec_python_sdk import CrowdSec, ApiException

crowdsec = CrowdSec(
    api_key_authorizer="YOUR_API_KEY",
)


async def main():
    try:
        # getDecisionsStream
        get_decisions_stream_response = await crowdsec.bouncers.aget_decisions_stream(
            startup=True,
            scopes="string_example",
            origins="string_example",
            scenarios_containing="string_example",
            scenarios_not_containing="string_example",
        )
        print(get_decisions_stream_response)
    except ApiException as e:
        print("Exception when calling BouncersApi.get_decisions_stream: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["message"])
            pprint(e.body["errors"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from crowd_sec_python_sdk import CrowdSec, ApiException

crowdsec = CrowdSec(
    api_key_authorizer="YOUR_API_KEY",
)

try:
    # getDecisionsStream
    get_decisions_stream_response = crowdsec.bouncers.raw.get_decisions_stream(
        startup=True,
        scopes="string_example",
        origins="string_example",
        scenarios_containing="string_example",
        scenarios_not_containing="string_example",
    )
    pprint(get_decisions_stream_response.body)
    pprint(get_decisions_stream_response.body["new"])
    pprint(get_decisions_stream_response.body["deleted"])
    pprint(get_decisions_stream_response.headers)
    pprint(get_decisions_stream_response.status)
    pprint(get_decisions_stream_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BouncersApi.get_decisions_stream: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["message"])
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `crowdsec.bouncers.get_decisions_stream`<a id="crowdsecbouncersget_decisions_stream"></a>

Returns a list of new/expired decisions. Intended for bouncers that need to "stream" decisions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_decisions_stream_response = crowdsec.bouncers.get_decisions_stream(
    startup=True,
    scopes="string_example",
    origins="string_example",
    scenarios_containing="string_example",
    scenarios_not_containing="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### startup: `bool`<a id="startup-bool"></a>

If true, means that the bouncers is starting and a full list must be provided

##### scopes: `str`<a id="scopes-str"></a>

Comma separated scopes of decisions to fetch

##### origins: `str`<a id="origins-str"></a>

Comma separated name of origins. If provided, then only the decisions originating from provided origins would be returned.

##### scenarios_containing: `str`<a id="scenarios_containing-str"></a>

Comma separated words. If provided, only the decisions created by scenarios containing any of the provided word would be returned.

##### scenarios_not_containing: `str`<a id="scenarios_not_containing-str"></a>

Comma separated words. If provided, only the decisions created by scenarios, not containing any of the provided word would be returned.

#### 🔄 Return<a id="🔄-return"></a>

[`DecisionsStreamResponse`](./crowd_sec_python_sdk/pydantic/decisions_stream_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisions/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.bouncers.get_decisions_stream_0`<a id="crowdsecbouncersget_decisions_stream_0"></a>

Returns a list of new/expired decisions. Intended for bouncers that need to "stream" decisions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
crowdsec.bouncers.get_decisions_stream_0(
    startup=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### startup: `bool`<a id="startup-bool"></a>

If true, means that the bouncer is starting and a full list must be provided

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisions/stream` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.bouncers.get_information`<a id="crowdsecbouncersget_information"></a>

Returns information about existing decisions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = crowdsec.bouncers.get_information(
    scope="string_example",
    value="string_example",
    type="string_example",
    ip="string_example",
    range="string_example",
    contains=True,
    origins="string_example",
    scenarios_containing="string_example",
    scenarios_not_containing="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

scope to which the decision applies (ie. IP/Range/Username/Session/...)

##### value: `str`<a id="value-str"></a>

the value to match for in the specified scope

##### type: `str`<a id="type-str"></a>

type of decision

##### ip: `str`<a id="ip-str"></a>

IP to search for (shorthand for scope=ip&value=)

##### range: `str`<a id="range-str"></a>

range to search for (shorthand for scope=range&value=)

##### contains: `bool`<a id="contains-bool"></a>

indicate if you're looking for a decision that contains the value, or that is contained within the value

##### origins: `str`<a id="origins-str"></a>

Comma separated name of origins. If provided, then only the decisions originating from provided origins would be returned.

##### scenarios_containing: `str`<a id="scenarios_containing-str"></a>

Comma separated words. If provided, only the decisions created by scenarios containing any of the provided word would be returned.

##### scenarios_not_containing: `str`<a id="scenarios_not_containing-str"></a>

Comma separated words. If provided, only the decisions created by scenarios, not containing any of the provided word would be returned.

#### 🔄 Return<a id="🔄-return"></a>

[`GetDecisionsResponse`](./crowd_sec_python_sdk/pydantic/get_decisions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.bouncers.get_information_0`<a id="crowdsecbouncersget_information_0"></a>

Returns information about existing decisions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
crowdsec.bouncers.get_information_0(
    scope="string_example",
    value="string_example",
    type="string_example",
    ip="string_example",
    range="string_example",
    contains=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

scope to which the decision applies (ie. IP/Range/Username/Session/...)

##### value: `str`<a id="value-str"></a>

the value to match for in the specified scope

##### type: `str`<a id="type-str"></a>

type of decision

##### ip: `str`<a id="ip-str"></a>

IP to search for (shorthand for scope=ip&value=)

##### range: `str`<a id="range-str"></a>

range to search for (shorthand for scope=range&value=)

##### contains: `bool`<a id="contains-bool"></a>

indicate if you're looking for a decision that contains the value, or that is contained within the value

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisions` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.authenticate_session`<a id="crowdsecwatchersauthenticate_session"></a>

Authenticate current to get session ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
authenticate_session_response = crowdsec.watchers.authenticate_session(
    machine_id="string_example",
    password="string_example",
    scenarios=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### machine_id: `str`<a id="machine_id-str"></a>

##### password: `str`<a id="password-str"></a>

##### scenarios: [`WatcherAuthRequestScenarios`](./crowd_sec_python_sdk/type/watcher_auth_request_scenarios.py)<a id="scenarios-watcherauthrequestscenarioscrowd_sec_python_sdktypewatcher_auth_request_scenariospy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WatcherAuthRequest`](./crowd_sec_python_sdk/type/watcher_auth_request.py)
Information about the watcher to be reset

#### 🔄 Return<a id="🔄-return"></a>

[`WatcherAuthResponse`](./crowd_sec_python_sdk/pydantic/watcher_auth_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/watchers/login` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.create_alerts`<a id="crowdsecwatcherscreate_alerts"></a>

Push alerts to API

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_alerts_response = crowdsec.watchers.create_alerts(
    body=[
        {
            "scenario": "scenario_example",
            "scenario_hash": "scenario_hash_example",
            "scenario_version": "scenario_version_example",
            "message": "message_example",
            "events_count": 1,
            "start_at": "start_at_example",
            "stop_at": "stop_at_example",
            "capacity": 1,
            "leakspeed": "leakspeed_example",
            "simulated": True,
            "events": [
                {
                    "timestamp": "timestamp_example",
                    "meta": [{}],
                }
            ],
            "source": {
                "scope": "scope_example",
                "value": "value_example",
            },
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddAlertsRequest`](./crowd_sec_python_sdk/type/add_alerts_request.py)
Push alerts to the API

#### 🔄 Return<a id="🔄-return"></a>

[`AddAlertsResponse`](./crowd_sec_python_sdk/pydantic/add_alerts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alerts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.delete_alert_by_id`<a id="crowdsecwatchersdelete_alert_by_id"></a>

Delete alert for given alert ID (only from cscli)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_alert_by_id_response = crowdsec.watchers.delete_alert_by_id(
    alert_id="alert_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### alert_id: `str`<a id="alert_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteAlertsResponse`](./crowd_sec_python_sdk/pydantic/delete_alerts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alerts/{alert_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.get_alert_by_id`<a id="crowdsecwatchersget_alert_by_id"></a>

Get alert by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_alert_by_id_response = crowdsec.watchers.get_alert_by_id(
    alert_id="alert_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### alert_id: `str`<a id="alert_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Alert`](./crowd_sec_python_sdk/pydantic/alert.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alerts/{alert_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.get_alert_by_id_0`<a id="crowdsecwatchersget_alert_by_id_0"></a>

Get alert by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
crowdsec.watchers.get_alert_by_id_0(
    alert_id="alert_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### alert_id: `str`<a id="alert_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alerts/{alert_id}` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.list_alerts`<a id="crowdsecwatcherslist_alerts"></a>

Allows to search for alerts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_alerts_response = crowdsec.watchers.list_alerts(
    scope="string_example",
    value="string_example",
    scenario="string_example",
    ip="string_example",
    range="string_example",
    since="1970-01-01T00:00:00.00Z",
    until="1970-01-01T00:00:00.00Z",
    simulated=True,
    has_active_decision=True,
    decision_type="string_example",
    limit=3.14,
    origin="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

show alerts for this scope

##### value: `str`<a id="value-str"></a>

show alerts for this value (used with scope)

##### scenario: `str`<a id="scenario-str"></a>

show alerts for this scenario

##### ip: `str`<a id="ip-str"></a>

IP to search for (shorthand for scope=ip&value=)

##### range: `str`<a id="range-str"></a>

range to search for (shorthand for scope=range&value=)

##### since: `datetime`<a id="since-datetime"></a>

search alerts newer than delay (format must be compatible with time.ParseDuration)

##### until: `datetime`<a id="until-datetime"></a>

search alerts older than delay (format must be compatible with time.ParseDuration)

##### simulated: `bool`<a id="simulated-bool"></a>

if set to true, decisions in simulation mode will be returned as well

##### has_active_decision: `bool`<a id="has_active_decision-bool"></a>

only return alerts with decisions not expired yet

##### decision_type: `str`<a id="decision_type-str"></a>

restrict results to alerts with decisions matching given type

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

number of alerts to return

##### origin: `str`<a id="origin-str"></a>

restrict results to this origin (ie. lists,CAPI,cscli)

#### 🔄 Return<a id="🔄-return"></a>

[`GetAlertsResponse`](./crowd_sec_python_sdk/pydantic/get_alerts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alerts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.register_watcher`<a id="crowdsecwatchersregister_watcher"></a>

This method is used when installing crowdsec (cscli->APIL)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
crowdsec.watchers.register_watcher(
    machine_id="string_example",
    password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### machine_id: `str`<a id="machine_id-str"></a>

##### password: `str`<a id="password-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WatcherRegistrationRequest`](./crowd_sec_python_sdk/type/watcher_registration_request.py)
Information about the watcher to be registered

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/watchers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.remove_alerts`<a id="crowdsecwatchersremove_alerts"></a>

Allows to delete alerts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_alerts_response = crowdsec.watchers.remove_alerts(
    scope="string_example",
    value="string_example",
    scenario="string_example",
    ip="string_example",
    range="string_example",
    since="1970-01-01T00:00:00.00Z",
    until="1970-01-01T00:00:00.00Z",
    has_active_decision=True,
    alert_source="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

delete alerts for this scope

##### value: `str`<a id="value-str"></a>

delete alerts for this value (used with scope)

##### scenario: `str`<a id="scenario-str"></a>

delete alerts for this scenario

##### ip: `str`<a id="ip-str"></a>

delete Alerts with IP (shorthand for scope=ip&value=)

##### range: `str`<a id="range-str"></a>

delete alerts concerned by range (shorthand for scope=range&value=)

##### since: `datetime`<a id="since-datetime"></a>

delete alerts added after YYYY-mm-DD-HH:MM:SS

##### until: `datetime`<a id="until-datetime"></a>

delete alerts added before YYYY-mm-DD-HH:MM:SS

##### has_active_decision: `bool`<a id="has_active_decision-bool"></a>

delete only alerts with decisions not expired yet

##### alert_source: `str`<a id="alert_source-str"></a>

delete only alerts with matching source (ie. cscli/crowdsec)

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteAlertsResponse`](./crowd_sec_python_sdk/pydantic/delete_alerts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alerts` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.remove_decision_by_id`<a id="crowdsecwatchersremove_decision_by_id"></a>

Delete decision for given decision ID (only from cscli)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_decision_by_id_response = crowdsec.watchers.remove_decision_by_id(
    decision_id="decision_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### decision_id: `str`<a id="decision_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteDecisionResponse`](./crowd_sec_python_sdk/pydantic/delete_decision_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisions/{decision_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.remove_decisions`<a id="crowdsecwatchersremove_decisions"></a>

Delete decisions(s) for given filters (only from cscli)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_decisions_response = crowdsec.watchers.remove_decisions(
    scope="string_example",
    value="string_example",
    type="string_example",
    ip="string_example",
    range="string_example",
    scenario="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

scope to which the decision applies (ie. IP/Range/Username/Session/...)

##### value: `str`<a id="value-str"></a>

the value to match for in the specified scope

##### type: `str`<a id="type-str"></a>

type of decision

##### ip: `str`<a id="ip-str"></a>

IP to search for (shorthand for scope=ip&value=)

##### range: `str`<a id="range-str"></a>

range to search for (shorthand for scope=range&value=)

##### scenario: `str`<a id="scenario-str"></a>

scenario to search

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteDecisionResponse`](./crowd_sec_python_sdk/pydantic/delete_decision_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowdsec.watchers.search_alerts`<a id="crowdsecwatcherssearch_alerts"></a>

Allows to search for alerts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
crowdsec.watchers.search_alerts(
    scope="string_example",
    value="string_example",
    scenario="string_example",
    ip="string_example",
    range="string_example",
    since="1970-01-01T00:00:00.00Z",
    until="1970-01-01T00:00:00.00Z",
    simulated=True,
    has_active_decision=True,
    decision_type="string_example",
    limit=3.14,
    origin="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

show alerts for this scope

##### value: `str`<a id="value-str"></a>

show alerts for this value (used with scope)

##### scenario: `str`<a id="scenario-str"></a>

show alerts for this scenario

##### ip: `str`<a id="ip-str"></a>

IP to search for (shorthand for scope=ip&value=)

##### range: `str`<a id="range-str"></a>

range to search for (shorthand for scope=range&value=)

##### since: `datetime`<a id="since-datetime"></a>

search alerts newer than delay (format must be compatible with time.ParseDuration)

##### until: `datetime`<a id="until-datetime"></a>

search alerts older than delay (format must be compatible with time.ParseDuration)

##### simulated: `bool`<a id="simulated-bool"></a>

if set to true, decisions in simulation mode will be returned as well

##### has_active_decision: `bool`<a id="has_active_decision-bool"></a>

only return alerts with decisions not expired yet

##### decision_type: `str`<a id="decision_type-str"></a>

restrict results to alerts with decisions matching given type

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

number of alerts to return

##### origin: `str`<a id="origin-str"></a>

restrict results to this origin (ie. lists,CAPI,cscli)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alerts` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
