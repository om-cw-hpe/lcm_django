from kubernetes import client, config
from .lib import lib
import os

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(config_file=r"k8s_info/scripts/k3s.yaml")

v1 = client.CoreV1Api()
v2 = client.AppsV1Api()

def list_namespaced_deployment(con, ns):
    ret = con.list_namespaced_deployment(ns)
    #print("These are the deployments in namespace "+ ns+'\n')
    for i in ret.items:
        #print(i.metadata.name) 
        read_pods_in_ns(con, ns, i.metadata.name)

def read_pods_in_ns(con, ns, name):
    ret = con.read_namespaced_deployment(name, ns, pretty='pretty')
    for i in ret.spec.template.spec.containers:
        print(i.image + "\n")

def get_nodes(con = v1):
    ret = con.list_node()
    data = []
    for i in ret.items:
        data.append({'Node_Name': i.metadata.name, 'Node_IP': i.status.addresses[0].address})
    return data
#'Node_Role': str(i.metadata.labels['node-role.kubernetes.io/master'], 'Node_IP': i.metadata.labels['k3s.io/internal-ip'])

def main():
    '''con = v1
    ns = "default"
    def list_ns(con):
        data =[]
        ret = lib.list_all_pod(con)
        for i in ret.items:
            data.append({'namespace': str(i.metadata.namespace), 'pod_name': str(i.metadata.name), 'pod_ip': str(i.status.pod_ip)})
        return data
    return list_ns(v1)'''
     
    get_nodes(v1)
    '''lib.list_all_pod(v1)

    for ns in (lib.list_all_namespaces(v1)):
        list_namespaced_deployment(v2, ns)
    res = lib.get_node(v1)
    for i in res.items:
        print(i.metadata.name + "\t" )
        print(i.status.capacity)'''
if __name__ == '__main__':
    main()