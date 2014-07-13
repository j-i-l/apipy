class InfoStructure():
    def __init__(self,
                 pubDomain,
                 pubApiPath,
                 privDomain,
                 privApiPath,
                 ):
        self.pubDomain = pubDomain
        self.pubApiPath = pubApiPath
        self.privDomain = privDomain
        self.privApiPath = privApiPath
        #this might be put into a config file at some point
        self.pubAddress = self.pubDomain + self.pubApiPath
        self.privAddress = self.privDomain + self.privApiPath
        self.currenices = ()
