## Introduction

Provides information about the gateway server.

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_ngio_gateway.c3addon)

## Dependence

- [rex_ngio_authentication](rex_ngio_authentication.md)

## Usage

[Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHmAgqX3E_USBI1geg)

### Prepare

Put [rex_ngio_authentication](rex_ngio_authentication.md) into project, and set property `App id` and `AES key`.

### Get date-time

```mermaid
graph TB

Action["Action:Get date time"] --> ActionIsSuccess

subgraph Callback
ActionIsSuccess{Action<br>is success} --> |Yes| CondOnSuccess["Condition:On get date time"]
ActionIsSuccess --> |No| CondOnError["Condition:On get date time error"]
CondOnSuccess --- ExpResult["Expression:Datetime"]
CondOnError --- ExpError["Expression:ErrorMessage"]
end
```

1. `Action:Get date time`
2. Callback
    - Success : `Condition:On get date time`
        - `Expression:Datetime`
    - Error : `Condition:On login error`
        - `Expression:ErrorMessage`

----

### Get version

```mermaid
graph TB

Action["Action:Get version"] --> ActionIsSuccess

subgraph Callback
ActionIsSuccess{Action<br>is success} --> |Yes| CondOnSuccess["Condition:On get version"]
ActionIsSuccess --> |No| CondOnError["Condition:On get version error"]
CondOnSuccess --- ExpResult["Expression:Version"]
CondOnError --- ExpError["Expression:ErrorMessage"]
end
```

1. `Action:Get version`
2. Callback
    - Success : `Condition:On get version`
        - `Expression:Version`
    - Error : `Condition:On get version error`
        - `Expression:ErrorMessage`

----

### Ping

```mermaid
graph TB

Action["Action:Ping"] --> ActionIsSuccess

subgraph Callback
ActionIsSuccess{Action<br>is success} --> |Yes| CondOnSuccess["Condition:On pong"]
ActionIsSuccess --> |No| CondOnError["Condition:On pong error"]
CondOnError --- ExpError["Expression:ErrorMessage"]
end
```

1. `Action:Ping`
2. Callback
    - Success : `Condition:On pong`
    - Error : `Condition:On pong error`
        - `Expression:ErrorMessage`