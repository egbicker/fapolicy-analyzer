# Copyright Concurrent Technologies Corporation 2022
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Any, Mapping, NamedTuple, Optional, cast

from fapolicy_analyzer.ui.actions import (
    ERROR_RULES_CONFIG,
    RECEIVED_RULES_CONFIG,
    REQUEST_RULES_CONFIG,
)
from redux import Action, Reducer, handle_actions


class RuleConfigState(NamedTuple):
    error: Optional[str]
    loading: bool
    rules_config: Mapping[str, str]


def _create_state(state: RuleConfigState, **kwargs: Optional[Any]) -> RuleConfigState:
    return RuleConfigState(**{**state._asdict(), **kwargs})


def handle_request_rules_config(state: RuleConfigState, _: Action) -> RuleConfigState:
    return _create_state(state, loading=True, error=None)


def handle_received_rules_config(
    state: RuleConfigState, action: Action
) -> RuleConfigState:
    payload = cast(Mapping[str, str], action.payload)
    return _create_state(state, rules_config=payload, error=None, loading=False)


def handle_error_rules_config(
    state: RuleConfigState, action: Action
) -> RuleConfigState:
    payload = cast(str, action.payload)
    return _create_state(state, error=payload, loading=False)


rules_config_reducer: Reducer = handle_actions(
    {
        REQUEST_RULES_CONFIG: handle_request_rules_config,
        RECEIVED_RULES_CONFIG: handle_received_rules_config,
        ERROR_RULES_CONFIG: handle_error_rules_config,
    },
    RuleConfigState(error=None, rules_config={}, loading=False),
)
