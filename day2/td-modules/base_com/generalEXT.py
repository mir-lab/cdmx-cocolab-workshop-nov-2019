com = mod('comEXT').Com

class GeneralCom(com):
    def __init__(self, myOp):
        self.MyOp   = myOp

        com.__init__(self, self.MyOp)
        print("GeneralCom init from {}".format(self.MyOp))
    
    def Hello(self, message):
        role = op.Project.GetCurrentRole()

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

        role = op.Project.GetCurrentRole()

        if role == 'draw' or role == 'controller' or role == 'mixedController':
            targetOp    = op.Scenes.op(message.get('targetOp'))
            parsDict    = message.get('pars')
            op.Project.UpdateCustomInternalPars(targetOp, parsDict)
        
        else:
            pass

    def ChangeVisability(self, message):
        role = op.Project.GetCurrentRole()
        if role == 'controller' or role == 'mixedController':
            targetOp = op.Controller.op(message.get('targetOp'))
            parsDict = message.get('pars')
            op.Project.UpdateCustomPars(targetOp, parsDict)
        
        else:
            pass
        pass

    def ChangeScene(self, message):
        role = op.Project.GetCurrentRole()
        targetOp = eval( 'op.{}'.format( message.get('targetOp')) )
        print(targetOp)
        parsDict = message.get('pars')

        op.Project.UpdateCustomPars( op(targetOp), parsDict)

        pass