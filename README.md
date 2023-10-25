# ppgcc-deep-learning-pinn

:floppy_disk: [google drive](https://drive.google.com/drive/folders/1q4rUKQ8sSXJGirQYPOodSbaE9h4kbZ_q?usp=drive_link)

# notebooks

- `notebooks/dho_with_param_learning.ipynb`<br/> In this notebook we will try to write code for a PINN that solves the **Damped Harmonic Oscillator** (DHO) problem. We will not use the parameter learning approach. Instead, we will use a MLP to learn the solution of the DHO problem. Then, we turn the MLP in a PINN by adding the DHO ODE as a loss function.<br/> The goal here is not to get the best results, but to get a working code that we can use as a starting point for the parameter learning approach.

- `notebooks/dho_without_param_learning_debug_0.ipynb`<br/> In this notebook we will try to make some experiments with the **Damped Harmonic Oscillator** (DHO) synthetic data. Here the goal is to vary some hyperparameters and see how the model behaves in terms interpolation -- rather than extrapolation.

- `notebooks/dho_without_param_learning_debug_1.ipynb`<br/> In this notebook we will try to make some experiments with the **Damped Harmonic Oscillator** (DHO) synthetic data. Here the goal is to explore the ability of the model to learn regions out of both locations and training domain.

- `notebooks/dho_without_param_learning_debug_2.ipynb`<br/> In this notebook we will try to make some experiments with the **Damped Harmonic Oscillator** (DHO) synthetic data. Here the goal is to explore the ability of the model to learn the ODE's solution given that we only know data from lower and upper bounds of domain.

- `notebooks/dho_with_param_learning_debug_0.ipynb` <br/> In this notebook we will try to make some experiments with the **Driven Harmonic Oscillator** (DHO) synthetic data. We try to learn the intensity $F_0$ of sinonoidal driven force in $$m\ddot{x} + c\dot{x} + kx = F_0\cos(\omega t + \phi_d)$$

- `notebooks/nlc_without_param_learning.ipynb` <br/>In this notebook we will try to estimate the parameters of the **Newton's Law of Cooling (NLC)** using a Physics-Informed Neural Network (PINN). We will compare the results with that obtained using a simple Ordinary Least Squares (OLS) regression.


# references

`todo`