import pandas as pd
import numpy as np

def gaussian(mu, sig):
    def f(x):
        return np.exp(-0.5 * (x - mu) ** 2 / sig) / np.sqrt(2 * np.pi * sig)
    return f

def calc_mean(m, gauss):
    return m * gauss / np.sum(m * gauss)

if __name__ == '__main__':
    # data
    data = np.array([8, 3, 6, 9, 7, 6, 2, 6, 4, 4, 5, 7])
    dataN = len(data)

    # initial parameter {{m_A, mu_A, sig_A}, ...}
    m = np.array([1 / 3, 1 / 3, 1 / 3])
    mu = np.array([7.0, 3.0, 5.0])
    sig = np.array([1.0, 1.0, 1.0])

    for i in range(0, 2):
        N = gaussian(mu, sig)

        matrix = []
        for d in data:
            matrix.append(np.append(d, calc_mean(m, N(d))))

        df = pd.DataFrame(matrix, columns=list("xABC"))
        print ("mean values")
        print (df.round(3), "\n")

        m = np.array([])
        mu = np.array([])
        sig = np.array([])

        for c in "ABC":
            tot = sum(df[c])
            m = np.append(m, tot / dataN)

            nmu = sum(df[c].values * data) / tot
            mu = np.append(mu, nmu)

            nsig = sum(df[c].values * (data - nmu) ** 2) / tot
            sig = np.append(sig, nsig)


        print ("new param")
        print ("m    :", m.round(3))
        print ("mu   :", mu.round(3))
        print ("sig^2:", sig.round(3))
        print ("\n")