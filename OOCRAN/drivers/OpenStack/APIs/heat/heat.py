from heatclient.client import Client
from time import sleep
from drivers.OpenStack.APIs.keystone.keystone import get_project_id
from drivers.OpenStack.APIs.keystone.keystone import get_token


def credentials(nvfi, vim):
    heat = Client('1', endpoint="http://"+vim.ip+":8004/v1/"+get_project_id(nvfi.operator, vim), token=get_token(nvfi, vim))
    return heat


def create_stack(nvfi, template, vim):
    heat = credentials(nvfi, vim)
    stack = heat.stacks.create(stack_name=nvfi.name, template=template, parameters={})
    uid = stack['stack']['id']

    stack = heat.stacks.get(stack_id=uid).to_dict()
    while stack['stack_status'] == 'CREATE_IN_PROGRESS':
        print "Creating stack."
        stack = heat.stacks.get(stack_id=uid).to_dict()
        sleep(10)

    if stack['stack_status'] == 'CREATE_COMPLETE':
        print "Stack succesfully created."
    else:
        return "Stack fall to unknow status: {}".format(stack)


def delete_stack(nvfi, vim):
    heat = credentials(nvfi,vim)
    stack = heat.stacks.get(nvfi.name)
    heat.stacks.delete(stack.parameters['OS::stack_id'])