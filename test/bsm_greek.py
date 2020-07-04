import matplotlib.pyplot as plt
import numpy as np

from bin.bsm_greek import delta, gamma, theta, vega, rho

if __name__ == '__main__':
    S0 = 100
    K = 120
    r = 0.01
    sigma = 0.1
    T = 0.5
    dd = 0.001
    is_call = True
    # Delta
    print("###################")
    print("Delta - \n")
    print("Theory: ")
    print(delta(S0, K, r, sigma, T, 0, is_call))
    print("Approach: ")
    print(delta(S0, K, r, sigma, T, dd, is_call))
    print("###################")

    # Gamma
    print("###################")
    print("Gamma - \n")
    print("Theory: ")
    print(gamma(S0, K, r, sigma, T, 0, is_call))
    print("Approach: ")
    print(gamma(S0, K, r, sigma, T, dd, is_call))
    print("###################")

    # Theta
    print("###################")
    print("Theta - \n")
    print("Theory: ")
    print(theta(S0, K, r, sigma, T, 0, is_call))
    print("Approach: ")
    print(theta(S0, K, r, sigma, T, dd, is_call))
    print("###################")

    # Vega
    print("###################")
    print("Vega - \n")
    print("Theory: ")
    print(vega(S0, K, r, sigma, T, 0, is_call))
    print("Approach: ")
    print(vega(S0, K, r, sigma, T, dd, is_call))
    print("###################")

    # rho
    print("###################")
    print("Rho - \n")
    print("Theory: ")
    print(rho(S0, K, r, sigma, T, 0, is_call))
    print("Approach: ")
    print(rho(S0, K, r, sigma, T, dd, is_call))
    print("###################")

    # plot
    S0 = 100
    K = 120
    r = 0.01
    sigma = 0.1
    T = 0.5
    dd = 0.001
    is_call = True

    # Delta
    sx = np.linspace(50, 200, 100)
    sy = [delta(s, K, r, sigma, T, 0, is_call=True) for s in sx]
    plt.plot(sx, sy, label="call")
    sy = [delta(s, K, r, sigma, T, 0, is_call=False) for s in sx]
    plt.plot(sx, sy, label="put")
    plt.title("Delta")
    plt.legend()
    plt.show()

    # gamma
    sx = np.linspace(50, 200, 100)
    sy = [gamma(s, K, r, sigma, T, 0, is_call=True) for s in sx]
    plt.plot(sx, sy, label="call")
    sy = [gamma(s, K, r, sigma, T, 0, is_call=False) for s in sx]
    plt.plot(sx, sy, label="put")
    plt.title("gamma")
    plt.legend()
    plt.show()

    # theta
    sx = np.linspace(0.0000001, 1, 100)
    sy = [gamma(S0, K, r, sigma, t, 0, is_call=True) for t in sx]
    plt.plot(sx, sy, label="call")
    sy = [gamma(S0, K, r, sigma, t, 0, is_call=False) for t in sx]
    plt.plot(sx, sy, label="put")
    plt.title("theta")
    plt.legend()
    plt.show()

    # vega
    sx = np.linspace(0.0000001, 0.15, 100)
    sy = [vega(S0, K, r, sg, T, 0, is_call=True) for sg in sx]
    plt.plot(sx, sy, label="call")
    sy = [vega(S0, K, r, sg, T, 0, is_call=False) for sg in sx]
    plt.plot(sx, sy, label="put")
    plt.title("vega")
    plt.legend()
    plt.show()

    # rho
    sx = np.linspace(0.0000001, 0.5, 100)
    sy = [rho(S0, K, rr, sigma, T, 0, is_call=True) for rr in sx]
    plt.plot(sx, sy, label="call")
    sy = [rho(S0, K, rr, sigma, T, 0, is_call=False) for rr in sx]
    plt.plot(sx, sy, label="put")
    plt.title("rho")
    plt.legend()
    plt.show()
