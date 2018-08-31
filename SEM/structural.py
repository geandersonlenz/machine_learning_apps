import pandas as pd

# variaveis latentes = vl
# variaveis observaveis = vo

# load data from mongodb ou sql
df = pd.read_csv('retail_may.csv')

# create variables for models



"""
measurement model
"""
# criar lista de vo de cada vl
# fazer análise fatorial de cada lista de vl
# fazer matriz de covariancia de cada lista de vl
# fazer matriz de correlaçao de cada lista de vl 
class MeasurementModel:

    def __init__(self):
        self.obs1 = []
        self.obs2 = []
        self.obs3 = []
        #self.obs = obs

    def createObs1(self, number):
        self.obs1.append(number)

    def createObs2(self, number):
        self.obs2.append(number)

    def createObs3(self, number):
        self.obs3.append(number)


    def createNameLatent1(self):
        a = 'latente1'
        if len(self.obs1) == 0:
            b = 1
        else:
            b = len(self.obs1) + 1
        c = str(b)
        return a + c

    def createNameLatent2(self):
        a = 'latente2'
        if len(self.obs2) == 0:
            b = 1
        else:
            b = len(self.obs2) + 1
        c = str(b)
        return a + c

    def createNameLatent3(self):
        a = 'latente3'
        if len(self.obs3) == 0:
            b = 1
        else:
            b = len(self.obs3) + 1
        c = str(b)
        return a + c

    def getObs1(self):
        return self.obs1

    def getObs2(self):
        return self.obs2

    def getObs3(self):
        return self.obs2

    def createConstruto1(self, alfa, beta):
        #alfa = createNameLatent()
        #beta = getObs()
        gama = {alfa: beta}
        return gama

    def createConstruto2(self, delta, zeta):
        #alfa = createNameLatent()
        #beta = getObs()
        eta = {delta: zeta}
        return eta

    def createConstruto3(self, teta, iota):
        #alfa = createNameLatent()
        #beta = getObs()
        capa = {teta: iota}
        return capa

    def chunks(self, l):
        # For item i in a range that is a length of l,
        for i in range(0, len(l)):
            # Create an index range for l of n items:
            yield l[i]

# 1. criar observaveis

mm = MeasurementModel()
# latent variable 01
mm.createObs1([10, 12, 13, 14])
mm.createObs1([100, 200, 300, 400])
mm.createObs1([1000, 2000, 3000, 4000])
alfa = mm.createNameLatent1()
beta = mm.getObs1()
print(mm.createConstruto1(alfa, beta))

# latent variable 02
mm.createObs2([101, 121, 131, 141])
mm.createObs2([1000, 2000, 3000, 4000])
mm.createObs2([5000, 10000, 15000, 20000])
delta = mm.createNameLatent2()
zeta = mm.getObs2()
print(mm.createConstruto2(delta, zeta))

# latent variable 03
mm.createObs3([101, 121, 131, 141])
mm.createObs3([444, 555, 666, 777, 888])
mm.createObs3([5000, 10000, 15000, 20000])
teta = mm.createNameLatent3()
iota = mm.getObs3()
print(mm.createConstruto3(teta, iota))


"""
strucutural model
"""
