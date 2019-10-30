import socket

class Project:

    def __init__(self, myOp):
        self.MyOp = myOp
        self.Role = myOp.par.Role
        self.MachineName = socket.gethostname()
        self.MachineIp = socket.gethostbyname(self.MachineName)

        # confirm in text port that we've inited the project class
        print("Project init from {}".format(myOp))

    def RoleColor(self, role):
        # color dict
        color = {
            'controller'    : (0.117, 0.0, 0.13),
            'draw'          : (0.0, 0.114, 0.020),
            'default'       : (0.1, 0.105, 0.112)
        }

        # our default color is in the color dict, and is the default bg color of TD
        default = color.get('default')
        return color.get(role, default)

    def ChangeBg(self, role=''):
        # changes the bg of TD based on the role
        color = self.RoleColor(role)
        ui.colors['worksheet.bg'] = color
    
    def ConfigureProject(self, role):
        # this is our configuration order of operations
        self.ChangeBg(role)
        op('container_output').Setup(role)


    def PageToDict(self, target_op, target_page, ignore_list):
        # create empty par_dict with input name as the preset_name value
        par_dict = {}

        # loop through each parameter in the target_op and capture its name and
        # value only if its custom page matches the input string for target_page, 
        # and the pars are not on the ignore_list
        for each_par in target_op.pars():
            if each_par.isCustom and each_par.page == target_page and each_par.name not in ignore_list:
                par_dict[each_par.name] = each_par.val
        return par_dict

    def UpdateCustomPars(self, target_op, parsDict):
        print(parsDict)
        for each_key, each_val in parsDict.items():
            setattr(target_op.par, each_key, each_val)
        #target_op.pars(each_key)[0].val = each_val
        pass