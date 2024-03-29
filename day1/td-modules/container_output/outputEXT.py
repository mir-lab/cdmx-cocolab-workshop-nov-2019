class Output:

    def __init__(self, myOp):
        self.MyOp = myOp
        print("Output init from {}".format(myOp))
    
    def OutputCleanup(self):
        oldOps = self.MyOp.findChildren(type=COMP, depth=1)
        for eachOp in oldOps:
            eachOp.destroy()

    def SetOutputSize(self):
        # find all of our container COMPS
        outputComps = self.MyOp.findChildren(type=containerCOMP, depth=1)

        # list comphrehensions for width and height
        width = [container.width for container in outputComps]
        height = [container.height for container in outputComps]

        # set widths and heights
        op.Output.par.w = sum(width)
        op.Output.par.h = max(height)

    def Setup(self, role):
        print('Configure Output as {}'.format(role))
        # destroy ops
        self.OutputCleanup()
        nodeX = 0

        if role == 'controller':
            newOp = self.MyOp.loadTox('td-modules/container_controller/container_controller.tox')
            newOp.nodeX = nodeX
        
        elif role == 'draw':
            newOp = self.MyOp.loadTox('td-modules/container_draw/container_draw.tox')
            newOp.nodeX = nodeX
        
        elif role == 'mixedController':
            ops = [ 'td-modules/container_controller/container_controller.tox',
                    'td-modules/container_draw/container_draw.tox']
            for eachOp in ops:
                newOp = self.MyOp.loadTox(eachOp)
                newOp.nodeX = nodeX
                nodeX += 200
            
        self.SetOutputSize()