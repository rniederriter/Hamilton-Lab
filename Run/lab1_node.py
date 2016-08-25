import labrad
import time

# Uses the "name" field from the LabRAD server information

lab1_servers = []
lab1_servers.append('Pulser')
lab1_servers.append('Data Vault')
lab1_servers.append('ParameterVault')
lab1_servers.append('ScriptScanner')
lab1_servers.append('Serial Server cg')
lab1_servers.append('DDS9m')
lab1_servers.append('DDS9m2')
lab1_servers.append('digital_sequencer')
lab1_servers.append('analog_sequencer')
lab1_servers.append('conductor')


def check_labrad_is_running():
    try:
        trial_cxn = labrad.connect(name="labrad checker client")
        running = True
    except:
        running = False
    trial_cxn.disconnect()
    return running


def check_node_is_running(node):
    cxn = labrad.connect(name="node checker client")
    if node in cxn.servers:
        running = True
    else:
        running = False
    cxn.disconnect()
    return running


def start_server(node, server):
    """ Start a LabRAD server.
    Parameters
    ----------
    node: labrad node
    server: str, name of the server
    """
    # get the server name without node name
    running_servers = [_tuple[0] for _tuple in node.running_servers()]
    if server in running_servers:
        print server + " is already running"
    else:
        print "starting " + server
        try:
            node.start(server)
        except Exception as error_string:
            print 'ERROR with ' + server
            print 'error message:', error_string


def start_nodes():
    cxn = labrad.connect(name="lab1 Node Client")
    lab1_node_str = "node_lab1"
    while not check_node_is_running(lab1_node_str):
        time.sleep(10)

    lab1_node = cxn.servers[lab1_node_str]
    for server in lab1_servers:
        start_server(lab1_node, server)



if __name__ == '__main__':
    while not check_labrad_is_running():
        time.sleep(10)
    start_nodes()