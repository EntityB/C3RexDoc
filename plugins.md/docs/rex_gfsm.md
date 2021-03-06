## Introduction

Describe [finite state machine](http://en.wikipedia.org/wiki/Finite-state_machine).

Icon: [Icons8](https://icons8.com/)

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_gfsm.c3addon)

## Dependence

None

## Usage

[Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHly95jwX8WJF-ww0q)

### Flow chart

```mermaid
graph TB

subgraph Go to next state
subgraph Transfer logic
Request["Action:Request"]  --> CondOnTransferLogic["Condition:On transfer logic(CurState)"]
CondOnTransferLogic --> SetNextState["Subevent:<br>Action:Set next state"]
end

GoToState["Action:Go to state"]

end

SetNextState --> CondOnStateChanged["Condition:On state changed<br>----<br>PreState --> CurState"]
GoToState["Action:Go to state"] --> CondOnStateChanged

subgraph State changing action
CondOnStateChanged --> HasCondOnTransfer{"Has<br>Condition:On transfer<br>in event sheet"}
HasCondOnTransfer --> |Yes| CondOnTransfer["Condition:On transfer<br>----<br>PreState --> CurState"]
HasCondOnTransfer --> |No| HasCondOnExit{"Has<br>Condition:On exit<br>in event sheet"}

subgraph On exit
HasCondOnExit --> |Yes| CondOnExit["Condition:On exit<br>----<br>PreState"]
HasCondOnExit --> |No| CondOndefaultExit["Condition:On default exit"]
end

CondOnExit --> HasCondOnEnter{"Has<br>Condition:On enter<br>in event sheet"}
CondOndefaultExit --> HasCondOnEnter

subgraph On enter
HasCondOnEnter --> |Yes| CondOnEnter["Condition:On enter<br>----<br>CurState"]
HasCondOnEnter --> |No| CondOndefaultEnter["Condition:On default enter"]
end

end
```

### Go to next state

- `Action:Request`, get and go to next state by event. Style of *behavior tree*.
    1. `Action:Request`, go to next state which determined by
    2. `Condition:On transfer logic(Curstate)` 
        1. set next state by `Action:Set next state`
            - State will not change if `Action:Set next state` does not invoke.
- `Action:Go to state`, go to next state directly.

### State changing actions

Add actions under these conditions, which will be triggered when state is changed from `Expression:PreState` to `Expression:CurState`

1. `Condition:On state changed` 
2. If `Condition:On transfer` is in event sheet,
    - `Condition:On state changed` 
    - Else
        1. If `Condition:On exit` is in event sheet,
            - `Condition:On exit`
            - Else `Condition:On default exit`
        2. If `Condition:On enter` is in event sheet,
            - `Condition:On enter`
            - Else `Condition:On default enter`

!!! warning
    Don't change state (`Action:Request` or `Action:Go to state`) under these conditions directly.  
    Inserts a `System action: wait (0)` above `Action:Request` or `Action:Go to state`, which could suspend remaining actions until next tick.

### Initial state

Set initial state in property `Initial state`.

### Debug

Dump current state by `Expression:CurState` under `Condition:On state changed`, to track the state changing.