from keystoneauth1 import loading
from keystoneauth1 import session
loader = loading.get_plugin_loader('password')
from novaclient import client
from keystoneclient.v3 import client as client_keystone
from cinderclient import client as client_cinder
from neutronclient.v2_0 import client as client_neutron
from glanceclient import Client
auth_url = "http://10.10.10.99:5000/v3"
username = "dangvv"
password = "dangvv"
project_name = "dangvv"
user_domain_id = "default"
project_domain_id = "default"
# auth = loader.load_from_options(auth_url="http://192.168.40.11:5000/v3", username='khoadv', password='khoadv', project_name='khoadv', user_domain_id='default', project_domain_id='default')
auth = loader.load_from_options(auth_url=auth_url, username=username, password=password, project_name=project_name, user_domain_id=user_domain_id, project_domain_id=project_domain_id)
sess = session.Session(auth=auth)
glan = Client(2, session=sess)

keystone = client_keystone.Client(session=sess)
nova = client.Client(2, session=sess)
cinder = client_cinder.Client(3, session=sess)
neutron = client_neutron.Client(session=sess)

def get_images(a):
    while True:
        try:
            print(a.__next__()['id'])
        except StopIteration:
            break


get_images(glan.images.list())


# sv = nova.servers.get('76964dea-c6d5-41ca-a06d-52185912c6e5')
# nova.servers.create(svname, image=nova.glance.find_image("cirros"), flavor=nova.flavors.find(id="27c25f6d-dbfe-4e41-ac38-af84eb7256b7"), nics = [{'net-id':"d655fbd3-e847-4be2-9d07-8a3272712ed6"}], block_device_mapping = {'vda':'979c0580-e0cd-4b94-9335-d251c2bc3df5'}, userdata=userdata, key_name=key_name, max_count=max_count)

# neutron.show_network_ip_availability(network='4da56b1d-a25d-47f8-b93b-d87d2d39454b')['network_ip_availability']['used_ips']
# neutron.show_network_ip_availability(network='4da56b1d-a25d-47f8-b93b-d87d2d39454b')['network_ip_availability']['total_ips']
# sv.manager.change_password(server=sv,password='222')
# sv.manager.reboot(server=sv, reboot_type='HARD')
# sv.manager.reboot(server=sv, reboot_type='SOFT')
# sv.manager.update(server=sv, name='khoadv')
# nova.keypairs.create(name="yyy")
# nova.keypairs.list()
# nova.keypairs.create(name="yyy")
# nova.volumes.create_server_volume(server_id="717850a0-d741-420e-adb6-29228a38cc96", volume_id="2fb59473-10f9-4a72-9f74-512325324a80")
# nova.volumes.delete_server_volume(server_id="717850a0-d741-420e-adb6-29228a38cc96", volume_id="2fb59473-10f9-4a72-9f74-512325324a80")
# nova.servers.list(search_opts={'all_tenants': 1})
# cinder.volumes.create(size="1", name="xxx", imageRef="0af7ff75-5352-470e-bc76-17bdc1a50566", volume_type="ceph-ssd")
# nova.servers.get_console_output(server=sv, length=None)
body_sample = {'network': {'name': 'khoadv', 'admin_state_up': True}}
net = neutron.create_network(body=body_sample)
body_create_subnet = {'subnets': [{'cidr': '192.168.199.0/24',
                          'ip_version': 4, 'network_id': net['network']['id']}]}
neutron.create_subnet(body=body_create_subnet)
# nova.servers.interface_detach(server=sv, port_id="07262333-4a62-453d-9bec-82a7ad697dc4")
# nova.servers.interface_attach(server=sv, port_id=None, net_id="f3599663-0cb4-4baa-bc54-649f0d527b94", fixed_ip=None) () port_id la port đã được tạo trước, có port_id rồi thì k cần net_id nữa, có net_id rồi thì k cần port_id nữa. k có fixed_id thì cấp từ dhcp

# nova.servers.create("xxxxxx", image=nova.glance.find_image("cirros"), flavor=nova.flavors.find(id="27c25f6d-dbfe-4e41-ac38-af84eb7256b7"), nics = [{'net-id':"d655fbd3-e847-4be2-9d07-8a3272712ed6"}], block_device_mapping = {'vda':'979c0580-e0cd-4b94-9335-d251c2bc3df5'})
# nova.servers.create("xxxxxx", image=nova.glance.find_image("cirros"), flavor=nova.flavors.find(id="27c25f6d-dbfe-4e41-ac38-af84eb7256b7"), nics = [{'net-id':"d655fbd3-e847-4be2-9d07-8a3272712ed6"}], block_device_mapping_v2 ={"boot_index": "0","uuid": "ac408821-c95a-448f-9292-73986c790911","source_type": "image","volume_size": "2","destination_type": "volume","delete_on_termination": true})
# block_device_mapping_v2 =[{"boot_index": "0", "source_type": "image","volume_size": "2","uuid": "0af7ff75-5352-470e-bc76-17bdc1a50566","destination_type": "volume","delete_on_termination": "0"}]
nova.servers.create("xxxxxx", image=nova.glance.find_image("centos7"), flavor=nova.flavors.find(name="m1.small"), nics = [{'net-id':"d832b168-ae88-45c5-b4c8-4d479b5010cb"}, {'net-id':"d655fbd3-e847-4be2-9d07-8a3272712ed6"}], userdata="#cloud-config\npassword: 123456\nssh_pwauth: True\nchpasswd:\n expire: false")
# keystone.authenticate(auth_url='http://192.168.40.11:5000/v3', username='dang', password='dang', user_domain_name='default', project_domain_name='default')


# import requests
# import json
# import os
# import shutil

# IP_CON = '192.168.40.11'
# admin_id = 'e9cc75db3fe94356a88e5a5b436c3b44'
# admin_pass = 'dang'
# admin_project_id = 'b9c5c4ffbb684197bc0e2217cc887430'
# ssl = 'http'


# def get_token():
#     token = 'a'
#     response = 'b'
#     try:
#         json_payload = {
#           "auth": {
#               "identity": {
#                   "methods": [
#                       "password"
#                   ],
#                   "password": {
#                       "user": {
#                           "id": admin_id,
#                           "password": admin_pass
#                       }
#                   }
#                },
#                "scope": {
#                    "project": {
#                        "id": admin_project_id
#                    }
#                }
#            }
#         }

#         headers = {'content-type': 'application/json', 'accept': 'application'}
#         response = requests.post(url='{0}://{1}:35357/v3/auth/tokens'.format(ssl,IP_CON),
#                                        data=json.dumps(json_payload),
#                                        headers=headers,verify=False)
#         token = response.headers.get('X-Subject-Token')
#     except Exception as e:
#           loger.critical(e)
#     return token

# def show_key(token):
#     try:
#         headers = {'X-Auth-Token':token}
#         response = requests.get(url='{0}://{1}:8774/v2.1/b9c5c4ffbb684197bc0e2217cc887430/os-keypairs/hihi'.format(ssl,IP_CON), headers=headers,verify=False)
#     except:
#         pass
#     return response.json()