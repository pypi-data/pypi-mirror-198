
VASTPY
======

This package is a Python SDK to the VMS (VAST Management System) REST API.

Useage
------

    from vastpy import VASTClient

    # print all views
    client = VASTClient(user='admin', password='123456', address='vast-file-server-vms-kfs2')
    for view in client.views.get():
        print(view)

    # find the default view policy
    policies = client.viewpolicies.get()
    default, = [i for i in policies if i['name'] == 'default']

    # create a new
    view = client.views.post(path='/prod/pgsql', policy_id=default['id'], create_dir=True)
    print(view)
