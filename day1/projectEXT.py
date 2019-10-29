class Project:

    def __init__(self, myOp):
        self.MyOp = myOp
        self.Role = myOp.par.Role

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
    