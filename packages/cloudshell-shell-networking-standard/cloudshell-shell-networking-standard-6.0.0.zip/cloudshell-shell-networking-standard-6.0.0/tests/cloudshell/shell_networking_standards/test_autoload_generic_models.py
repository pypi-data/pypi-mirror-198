from cloudshell.shell.standards.autoload_generic_models import (
    GenericChassis,
    GenericModule,
    GenericPort,
    GenericPortChannel,
    GenericPowerPort,
    GenericSubModule,
)

from cloudshell.shell.standards.networking.autoload_model import NetworkingResourceModel


def test_resource_model(api):
    resource_name = "resource name"
    shell_name = "shell name"
    family_name = "CS_Switch"

    resource = NetworkingResourceModel(resource_name, shell_name, family_name, api)

    assert resource.family_name == family_name
    assert resource.shell_name == shell_name
    assert resource.name == resource_name
    assert repr(resource.relative_address) == ""
    assert resource.resource_model == "GenericResource"
    assert resource.cloudshell_model_name == f"{shell_name}.{resource.resource_model}"

    assert resource.entities.Chassis == GenericChassis
    assert resource.entities.Module == GenericModule
    assert resource.entities.SubModule == GenericSubModule
    assert resource.entities.Port == GenericPort
    assert resource.entities.PortChannel == GenericPortChannel
    assert resource.entities.PowerPort == GenericPowerPort

    assert isinstance(resource.unique_identifier, str)
    assert resource.unique_identifier
