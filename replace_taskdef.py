import json
import shutil
import re

# backup
f_taskdef = "/home/ec2-user/environment/aws-modern-application-workshop/module-2/aws-cli/task-definition.json"
shutil.copyfile(f_taskdef,f_taskdef+".backup")

# load task-definition.json
with open(f_taskdef, 'r') as f:
    taskdef = f.read()

f_cfout = "/home/ec2-user/environment/cloudformation-core-output.json"
with open(f_cfout, 'r') as fo:
    out_data = json.load(fo)

# print(out_data)
# get replace data
replace_data = []
for data in out_data['Stacks'][0]['Outputs']:
    taskdef = taskdef.replace(data["Description"],data["OutputValue"])

print(taskdef)
# write task-definition.json
with open(f_taskdef, 'w') as f:
    f.write(taskdef)