class Controller:

    def __init__(self, myOp):
        self.MyOp = myOp
        print("Controller init from {}".format(myOp))
    
    def SendUpdateTargetBase(self, target, pageName, ignoreList, sceneOp):
        parsAsDict = op.Project.PageToDict(target, pageName, ignoreList)
        msg = {
            'messagekind'	: 'UpdateTargetBase',
            'target'		: 'draw',
            'targetOp'		: sceneOp,
            'sender'		: op.Project.Role.eval(),
            'output'		: None,
            'pars'		    : parsAsDict,
            'value'			: None
            }
        
        op.Com.SendMulticast(msg)
        pass
    
    def SendChangeVisability(self, visState, transTime):
        
        targetOp    = 'base_logic_and_clock'
        newVal      = 1 / transTime
        fade        = 1 if visState else -1
        newVal      *= fade    

        parsAsDict = {
            'Fade'          : newVal
        }

        msg = {
            'messagekind'   : 'ChangeVisability',
            'target'        : 'all',
            'targetOp'      : targetOp,
            'sender'        : op.Project.Role.eval(),
            'pars'          : parsAsDict
        }
        op.Com.SendMulticast(msg)
        pass
    
    def SendChangeScene(self, sceneOp):
        parsDict = {
            'Selecttarget' : 'base_{}'.format(sceneOp)
        }

        msg = {
            'messagekind'       : 'ChangeScene',
            'targetOp'          : 'Scenes',
            'target'            : 'all',
            'sender'            : op.Project.Role.eval(),
            'pars'              : parsDict
        }
        op.Com.SendMulticast(msg)
        pass
