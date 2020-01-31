from nornir import InitNornir
from nornir.plugins.functions.text import print_result, print_title
from nornir.plugins.tasks.networking import netmiko_send_config, netmiko_send_command
#THIS IS JUST A COMMENT FOR PURPOSES OF TESTING@:
def baseconfig(ipvzero):
    ipvzero.run(task=netmiko_send_config, config_file= "config_text")
    ipvzero.run(task=netmiko_send_command, command_string = "show run | sec user")

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

devices = nr.filter(asn=123)
results = devices.run(task = baseconfig)

print_title("DEPLOYING AUTOMATED BASELINE CONFIGURATIONS")
print_result(results)

