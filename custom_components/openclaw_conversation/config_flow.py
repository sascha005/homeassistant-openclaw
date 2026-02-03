from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries

from .const import (
    CONF_AGENT_ID,
    CONF_HOST,
    CONF_TOKEN,
    DEFAULT_AGENT_ID,
    DEFAULT_HOST,
    DOMAIN,
)


class OpenClawConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title="OpenClaw", data=user_input)

        schema = vol.Schema(
            {
                vol.Required(CONF_HOST, default=DEFAULT_HOST): str,
                vol.Required(CONF_TOKEN): str,
                vol.Optional(CONF_AGENT_ID, default=DEFAULT_AGENT_ID): str,
            }
        )

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
