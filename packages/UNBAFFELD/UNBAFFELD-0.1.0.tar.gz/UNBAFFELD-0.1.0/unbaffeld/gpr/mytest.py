from gpfit import GPTSFit
import numpy as np
import matplotlib.pyplot as plt
import os, sys

import gpflow as GPflow
import tensorflow as tf
import tensorflow_probability as tfp
from tensorflow_probability import distributions as tfd
from gpflow.utilities import print_summary

curdir = os.path.dirname(os.path.abspath(__file__))
pardir = os.path.abspath(os.path.join(curdir, './workflow/'))
sys.path.append(pardir)
from syndata import efitAiData

myprof = efitAiData("./workflow/hmode.yml")
myprof.add_syndata()
myprof.add_outliers()
norm = 1./np.max(myprof.profile)
myprof.profile *= norm
x = myprof.r
N = len(x)
yerr = (1.11-x)*norm #np.random.uniform(0.01,2.0,N)
y = np.zeros(N)
for i in range(N):
        y[i] = myprof.profile[i] + np.random.normal(0.0,yerr[i])
xx = np.linspace(0.0,1.1,200)
X = x[:,None]
Y = y[:,None]
XX = xx[:,None]

includeErrors = True

GPflow.config.set_default_float(np.float64)
GPflow.config.set_default_jitter(1e-10)
k1 = GPflow.kernels.Matern52(lengthscales=1.0)
k2 = GPflow.kernels.Matern52(lengthscales=0.1)
kernel = GPflow.kernels.ChangePoints([k1,k2,k1],locations=[0.95,1.0],steepness=50.0)
if (includeErrors):
        likelihood = GPflow.likelihoods.Gaussian(scale=GPflow.functions.Polynomial(degree=2))
        model = GPflow.models.GPR((X, Y), kernel, likelihood=likelihood)
else:
        model = GPflow.models.GPR((X, Y), kernel)

# setup priors for kernel, likelihood, etc.
f64 = GPflow.utilities.to_default_float
model.kernel.locations = [f64(0.95),f64(1.0)]
model.kernel.steepness = f64(50.0)
model.kernel.kernels[0].variance.prior = tfd.Gamma(f64(1.0), f64(2.0))
model.kernel.kernels[1].variance.prior = tfd.Gamma(f64(1.0), f64(2.0))
model.kernel.kernels[0].lengthscales.prior = tfd.Uniform(low=f64(0.001),high=f64(5.))
model.kernel.kernels[1].lengthscales.prior = tfd.Uniform(low=f64(0.001),high=f64(5.))
if (not includeErrors):
        model.likelihood.variance.prior = tfd.Gamma(f64(1.), f64(2.))# tfd.Uniform(low=f64(1.0),high=f64(30.0)) #tfd.Uniform(low=f64(1e-4),high=f64(2.)) # 

# optimize hyperparameters
opt = GPflow.optimizers.Scipy()
opt_logs = opt.minimize(model.training_loss,
                        model.trainable_variables,
                        options=dict(maxiter=2000))
print_summary(model)
mean, var = model.predict_f(XX)
mean /= norm
var /= norm*norm
m = np.array(mean[:,0])
v = np.array(var[:,0])
samples = model.predict_f_samples(XX, 50)
samples = np.array(samples[:,:,0]).T

y /= norm

fig = plt.figure()
ax = plt.subplot(111)
ax.errorbar(x,y,yerr,marker='o',mfc='black',mec='black',linestyle='')
plt.plot(x,y,'ko')
#ax.plot(xx, samples, 'g-', alpha=0.1)
ax.plot(xx, m, '-', color='red')
ax.fill_between(xx, m - 2.*np.sqrt(v), m + 2.*np.sqrt(v), color='red', alpha=0.2)
plt.show()