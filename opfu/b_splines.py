class BSplines(object):

    def __init__(self, t_grids):
        self.t_grids = t_grids
        self.dict_t_grids = {}
        for i in range(0, len(self.t_grids)):
            self.dict_t_grids[i] = self.t_grids[i]
        self.dict_b_t = {}

    def func(self, d, f_grids):
        # B-Spline main function
        if len(f_grids) != (len(self.t_grids) - d - 1):
            raise AttributeError

        def result(t):
            temp = 0
            for kk in range(0, len(f_grids)):
                temp += self.basis_function(kk, d)(t) * f_grids[kk]
            return temp

        return result

    def basis_function(self, k, d):
        # Basis function
        if (k + d >= len(self.t_grids) - 1):
            # The length is incorrect
            raise AttributeError
        if d in self.dict_b_t.keys():
            if k in self.dict_b_t[d]:
                return self.dict_b_t[d][k]
        else:
            self.dict_b_t[d] = {}

        if d > 0:
            def result(t):
                # Follow the formula
                return self.basis_function(k, d - 1)(t) * (t - self.t_grids[k]) / (
                            self.t_grids[k + d] - self.t_grids[k]) + \
                       self.basis_function(k + 1, d - 1)(t) * (self.t_grids[k + d + 1] - t) / (
                                   self.t_grids[k + d + 1] - self.t_grids[k + 1])

            self.dict_b_t[d][k] = result
            return result

        if d == 0:
            # The very basic function
            def result(t):
                if (t >= self.t_grids[k]) and (t < self.t_grids[k + 1]):
                    return 1
                return 0

            self.dict_b_t[d][k] = result
            return result
