"""
Module for Terraform Cloud API Endpoint: Agent Tokens.
"""

from .endpoint import TFCEndpoint
from._constants import Entitlements

class TFCAgentTokens(TFCEndpoint):
    """
    `API Docs \
        <https://www.terraform.io/docs/cloud/api/agent-tokens.html>`_
    """

    def __init__(self, instance_url, org_name, headers, well_known_paths, verify, log_level):
        super().__init__(instance_url, org_name, headers, well_known_paths, verify, log_level)
        self._agent_pools_api_v2_base_url = f"{self._api_v2_base_url}/agent-pools"
        self._auth_tokens_api_v2_base_url = f"{self._api_v2_base_url}/authentication-tokens"

    def required_entitlements(self):
        return [Entitlements.AGENTS]

    def create(self, agent_pool_id, description="api"):
        """
        ``POST /agent-pools/:agent_pool_id/authentication-tokens``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agent-tokens.html#create-an-agent-token>`_
        """
        url = f"{self._agent_pools_api_v2_base_url}/{agent_pool_id}/authentication-tokens"
        payload = {
            "data": {
                "type": "authentication-tokens",
                "attributes": {
                    "description": description
                }
            }
        }
        return self._create(url, payload)

    def list(self, agent_pool_id):
        """
        ``GET /agent-pools/:agent_pool_id/authentication-tokens``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agent-tokens.html#list-agent-tokens>`_
        """
        url = f"{self._agent_pools_api_v2_base_url}/{agent_pool_id}/authentication-tokens"
        return self._list(url)

    def show(self, token_id):
        """
        ``GET /authentication-tokens/:id``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agent-tokens.html#show-an-agent-token>`_
        """
        url = f"{self._auth_tokens_api_v2_base_url}/{token_id}"
        return self._show(url)

    def destroy(self, token_id):
        """
        ``DELETE /api/v2/authentication-tokens/:id``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agent-tokens.html#destroy-an-agent-token>`_

        NOTE: Including this function definition, since it matches what is in
        the docs and is used for the API comparison.
        """
        url = f"{self._auth_tokens_api_v2_base_url}/{token_id}"
        return self._destroy(url)
