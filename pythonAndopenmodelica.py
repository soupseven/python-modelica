from OMPython import ModelicaSystem
import matplotlib.pyplot as plt

model_path="E:/111jieping/fangzhenjiyouhua/"
mod=ModelicaSystem(model_path + "simulationAndOpt.mo","simulationAndOpt.system")

mod.setParameters(["x=2","y=2"])

mod.buildModel()

mod.setSimulationOptions(["stopTime=2.0","tolerance=1e-08"])
mod.simulate(resultfile="result.mat")
result=mod.getSolutions(["time","energy"])
print(result)
plt.plot(result[0],result[1])
plt.show()
