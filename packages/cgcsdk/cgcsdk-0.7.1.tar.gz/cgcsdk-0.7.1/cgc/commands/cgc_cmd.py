import click
from cgc.commands.cgc_cmd_responses import cgc_status_response
from cgc.commands.compute.compute_cmd import compute_delete
from cgc.utils.requests_helper import call_api, EndpointTypes
from cgc.utils.click_group import CustomCommand
from cgc.utils.prepare_headers import get_api_url_and_prepare_headers
from cgc.utils.response_utils import retrieve_and_validate_response_send_metric
from cgc.telemetry.basic import telemetry_permission_set


@click.command("rm", cls=CustomCommand)
@click.argument("name", type=click.STRING)
def cgc_rm(name: str):
    """
    Delete an app in user namespace
    """
    compute_delete(name)


@click.command("status", cls=CustomCommand)
def cgc_status():
    """Lists available and used resources"""
    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/compute/status"
    metric = "compute.status"
    __res = call_api(
        request=EndpointTypes.get,
        url=url,
        headers=headers,
    )
    click.echo(
        cgc_status_response(retrieve_and_validate_response_send_metric(__res, metric))
    )


@click.command("telemetry", cls=CustomCommand)
def sending_telemetry_permission():
    """Changing permission for sending telemetry"""

    click.echo(
        f"Sending telemetry is now {'enabled' if telemetry_permission_set() else 'disabled'}"
    )
