## 1D Kalman Filter

def update(mean1, var1, mean2, var2):
	new_mean = (var2*mean1 + var1*mean2)/(var1 + var2)
	new_var = 1./(1./var1 + 1./var2)
	return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
	new_mean = mean1 + mean2
	new_var = var1 + var2
	return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0
sig = 1

# measure, then move (update, then predict)

for i in zip(measurements, motion):
	mu, sig = update(mu, sig, i[0], measurement_sig)
	print "update:", [mu,sig]
	mu, sig = predict(mu, sig, i[1], motion_sig)
	print "predict:", [mu, sig]

print [mu, sig]