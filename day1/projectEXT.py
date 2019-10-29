class Project:

    def __init__(self, myOp):
        self.MyOp = myOp
        self.Role = myOp.par.Role

        print("Project init from {}".format(myOp))

    def RoleColor(self, role):
        color = {
            'controller'    : (0.117, 0.0, 0.13),
            'draw'          : (0.0, 0.114, 0.020),
            'default'       : (0.1, 0.105, 0.112)
        }
        default = color.get('default')
        return color.get(role, default)

    def ChangeBg(self, role):
        color = self.RoleColor(role)
        ui.colors['worksheet.bg'] = color
    
    def ConfigureProject(self, role):
        self.ChangeBg(role)
        op('container_output').Setup(role)
    