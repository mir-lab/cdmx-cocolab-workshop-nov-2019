com = mod('comEXT').Com

class GeneralCom(com):
    def __init__(self, myOp):
        self.MyOp   = myOp

        com.__init__(self, self.MyOp)
        print("GeneralCom init from {}".format(self.MyOp))
    
    def Hello(self, message):
        role = op.Project.Role.eval()

        if role == 'controller':
            print("Hello CDMX, I'm the Controller")
        elif role == 'draw':
            print("Hello CDMX, I'm a Draw node")
        else:
            pass
    
    def UpdateTargetBase(self, message):
        '''
        Exmample Message

            message = {
                'messagekind'	: 'UpdateTargetBase',
                'target'        : None,
                'targetOp'		: 'base_movie_player_msg_mode',
                'sender'		: op.Project.Role.eval(),
                'output'		: None,
                'pars'		    : dictOfPars,
                'value'			: None
                }
        '''

        role = op.Project.Role.eval() 

        if role == 'draw':
            targetOp    = op.Draw.op(message.get('targetOp'))
            parsDict    = message.get('pars')
            print(targetOp)
            op.Project.UpdateCustomPars(targetOp, parsDict)
        
        else:
            pass
