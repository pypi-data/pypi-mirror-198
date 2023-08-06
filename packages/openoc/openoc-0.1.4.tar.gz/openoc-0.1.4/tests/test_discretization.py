from openoc.discretization import *


def test_xw_lgl():
    x, w = xw_lgl(1)
    assert np.allclose(x, [0])
    assert np.allclose(w, [2])

    x, w = xw_lgl(2)
    assert np.allclose(x, [-1, 1])
    assert np.allclose(w, [1, 1])

    x, w = xw_lgl(3)
    assert np.allclose(x, [-1, 0, 1])
    assert np.allclose(w, [1 / 3, 4 / 3, 1 / 3])

    x, w = xw_lgl(4)
    assert np.allclose(x, [-1, -1 / np.sqrt(5), 1 / np.sqrt(5), 1])
    assert np.allclose(w, [1 / 6, 5 / 6, 5 / 6, 1 / 6])

    x, w = xw_lgl(5)
    assert np.allclose(x, [-1, -np.sqrt(3 / 7), 0, np.sqrt(3 / 7), 1])
    assert np.allclose(w, [1 / 10, 49 / 90, 32 / 45, 49 / 90, 1 / 10])

    x, w = xw_lgl(10)
    assert np.allclose(x, [-1, -0.9195339081664588138289, -0.7387738651055050750031, -0.4779249498104444956612,
                           -0.1652789576663870246262, 0.1652789576663870246262, 0.4779249498104444956612,
                           0.7387738651055050750031, 0.9195339081664588138289, 1])
    assert np.allclose(w, [0.02222222222222222222222, 0.1333059908510701111262, 0.2248893420631264521195,
                           0.2920426836796837578756, 0.3275397611838974566565, 0.3275397611838974566565,
                           0.292042683679683757876, 0.224889342063126452119, 0.133305990851070111126,
                           0.02222222222222222222222])


def test_T_lgl():
    x, _ = xw_lgl(10)
    y = x ** 2 + 100
    T_y = x ** 2
    assert np.allclose(T_lgl(10) @ y, T_y)

    x, _ = xw_lgl(10)
    y = np.cos(x) - np.pi
    T_y = np.cos(x) - 1
    assert np.allclose(T_lgl(10) @ y, T_y)

    x, _ = xw_lgl(20)
    y = np.exp(x) * 10
    T_y = np.exp(x) * 10 - 10
    assert np.allclose(T_lgl(20) @ y, T_y)


def test_I_lgl():
    x, _ = xw_lgl(10)
    y = x ** 2
    I_y = x ** 3 / 3
    assert np.allclose(I_lgl(10) @ y, I_y)

    x, _ = xw_lgl(10)
    y = x ** 5
    I_y = x ** 6 / 6
    assert np.allclose(I_lgl(10) @ y, I_y)

    x, _ = xw_lgl(20)
    y = np.sin(x)
    I_y = - np.cos(x) + 1
    assert np.allclose(I_lgl(20) @ y, I_y)


def test_lr_c():
    num_point = np.array([10])
    assert np.allclose(lr_c(num_point)[0], [0])
    assert np.allclose(lr_c(num_point)[1], [10])

    num_point = np.arange(2, 5, dtype=np.int32)
    assert np.allclose(lr_c(num_point)[0], [0, 1, 3])
    assert np.allclose(lr_c(num_point)[1], [2, 4, 7])


def test_lr_nc():
    num_point = np.array([10])
    assert np.allclose(lr_nc(num_point)[0], [0])
    assert np.allclose(lr_nc(num_point)[1], [10])

    num_point = np.arange(2, 5, dtype=np.int32)
    assert np.allclose(lr_nc(num_point)[0], [0, 2, 5])
    assert np.allclose(lr_nc(num_point)[1], [2, 5, 9])


def test_xw_c():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([3, 4, 5, 3, 4, 5, 3], dtype=np.int32)
    x, w = xw_c(mesh, num_point)
    y = x ** 2
    assert np.allclose(w @ y, 1 / 3)


def test_xw_nc():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([3, 4, 5, 3, 4, 5, 3], dtype=np.int32)
    x, w = xw_nc(mesh, num_point)
    y = x ** 2
    assert np.allclose(w @ y, 1 / 3)


def test_c2nc():
    num_point = np.array([3, 4], dtype=np.int32)
    f_c2nc = c2nc(num_point)
    # 1D
    v_c = np.arange(6, dtype=np.float64)
    assert np.allclose(f_c2nc(v_c), [0, 1, 2, 2, 3, 4, 5])

    # 2D
    v_c = np.arange(12, dtype=np.float64).reshape(6, 2)
    assert np.allclose(f_c2nc(v_c), [[0, 1], [2, 3], [4, 5], [4, 5], [6, 7], [8, 9], [10, 11]])


def test_nc2c():
    num_point = np.array([3, 4], dtype=np.int32)
    f_nc2c = nc2c(num_point)
    # 1D
    v_nc = np.arange(7, dtype=np.float64)
    assert np.allclose(f_nc2c(v_nc), [0, 1, 5, 4, 5, 6])

    # 2D
    v_nc = np.arange(14, dtype=np.float64).reshape(7, 2)
    assert np.allclose(f_nc2c(v_nc), [[0, 1], [2, 3], [10, 12], [8, 9], [10, 11], [12, 13]])


def test_T_c():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([6, 7, 5, 6, 7, 5, 6], dtype=np.int32)
    f_c2nc = c2nc(num_point)
    x, _ = xw_c(mesh, num_point)
    x_nc = f_c2nc(x)
    y = x
    l_nc, r_nc = lr_nc(num_point)
    T_y = np.zeros_like(x_nc)
    for i in range(len(num_point)):
        T_y[l_nc[i]:r_nc[i]] = x_nc[l_nc[i]:r_nc[i]] - (mesh[i] + mesh[i + 1]) / 2
    assert np.allclose(T_c(mesh, num_point) @ y, T_y)


def test_T_nc():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([6, 7, 5, 6, 7, 5, 6], dtype=np.int32)
    x, _ = xw_nc(mesh, num_point)
    y = x
    l_nc, r_nc = lr_nc(num_point)
    T_y = np.zeros_like(x)
    for i in range(len(num_point)):
        T_y[l_nc[i]:r_nc[i]] = x[l_nc[i]:r_nc[i]] - (mesh[i] + mesh[i + 1]) / 2
    assert np.allclose(T_nc(mesh, num_point) @ y, T_y)


def test_I_c():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([6, 7, 5, 6, 7, 5, 6], dtype=np.int32)
    f_c2nc = c2nc(num_point)
    x, _ = xw_c(mesh, num_point)
    x_nc = f_c2nc(x)
    y = x ** 2
    l_nc, r_nc = lr_nc(num_point)
    I_y = x_nc ** 3 / 3
    for i in range(len(num_point)):
        t_m = (mesh[i] + mesh[i + 1]) / 2
        I_y[l_nc[i]:r_nc[i]] -= t_m ** 3 / 3
    assert np.allclose(I_c(mesh, num_point) @ y, I_y)


def test_I_nc():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([6, 7, 5, 6, 7, 5, 6], dtype=np.int32)
    x, _ = xw_nc(mesh, num_point)
    y = x ** 2
    l_nc, r_nc = lr_nc(num_point)
    I_y = x ** 3 / 3
    for i in range(len(num_point)):
        t_m = (mesh[i] + mesh[i + 1]) / 2
        I_y[l_nc[i]:r_nc[i]] -= t_m ** 3 / 3
    assert np.allclose(I_nc(mesh, num_point) @ y, I_y)


def test_lr_v():
    num_point = np.array([2, 3, 4, 5], dtype=np.int32)
    continuity_xu = np.array([True, False, True, False], dtype=bool)
    l_v, r_v = lr_v(num_point, continuity_xu)
    # L_c = 11, L_nc = 14
    assert np.allclose(l_v, [0, 11, 25, 36])
    assert np.allclose(r_v, [11, 25, 36, 50])


def test_lr_m():
    num_point = np.array([2, 3, 4, 5], dtype=np.int32)
    continuity_xu = np.array([True, False, True, False], dtype=bool)
    l_m, r_m = lr_m(num_point, continuity_xu)
    # L_c = 11, L_nc = 14
    assert np.allclose(l_m, [0, 14, 28, 42])
    assert np.allclose(r_m, [14, 28, 42, 56])


def test_v2m():
    num_point = np.array([2, 3, 4, 5], dtype=np.int32)
    continuity_xu = np.array([True, False, True, False], dtype=bool)
    f_v2m = v2m(num_point, continuity_xu)
    L_v = 50
    v = np.arange(L_v, dtype=np.float64)
    m = f_v2m(v)
    l_v, r_v = lr_v(num_point, continuity_xu)
    l_m, r_m = lr_m(num_point, continuity_xu)
    f_c2nc = c2nc(num_point)
    assert np.allclose(m[l_m[0]:r_m[0]], f_c2nc(v[l_v[0]:r_v[0]]))
    assert np.allclose(m[l_m[1]:r_m[1]], v[l_v[1]:r_v[1]])
    assert np.allclose(m[l_m[2]:r_m[2]], f_c2nc(v[l_v[2]:r_v[2]]))
    assert np.allclose(m[l_m[3]:r_m[3]], v[l_v[3]:r_v[3]])


def test_m2v():
    num_point = np.array([2, 3, 4, 5], dtype=np.int32)
    continuity_xu = np.array([True, False, True, False], dtype=bool)
    f_m2v = m2v(num_point, continuity_xu)
    L_m = 56
    m = np.arange(L_m, dtype=np.float64)
    v = f_m2v(m)
    l_v, r_v = lr_v(num_point, continuity_xu)
    l_m, r_m = lr_m(num_point, continuity_xu)
    f_nc2c = nc2c(num_point)
    assert np.allclose(v[l_v[0]:r_v[0]], f_nc2c(m[l_m[0]:r_m[0]]))
    assert np.allclose(v[l_v[1]:r_v[1]], m[l_m[1]:r_m[1]])
    assert np.allclose(v[l_v[2]:r_v[2]], f_nc2c(m[l_m[2]:r_m[2]]))
    assert np.allclose(v[l_v[3]:r_v[3]], m[l_m[3]:r_m[3]])


def test_V_lgl_aug():
    x, _ = xw_lgl(10)
    x_aug, _ = xw_lgl(11)
    y = x ** 2 + 100
    V_y = x_aug ** 2 + 100
    assert np.allclose(V_lgl_aug(10) @ y, V_y)

    x, _ = xw_lgl(10)
    x_aug, _ = xw_lgl(11)
    y = np.cos(x) - np.pi
    V_y = np.cos(x_aug) - np.pi
    assert np.allclose(V_lgl_aug(10) @ y, V_y)

    x, _ = xw_lgl(20)
    x_aug, _ = xw_lgl(21)
    y = np.exp(x) * 10
    V_y = np.exp(x_aug) * 10
    assert np.allclose(V_lgl_aug(20) @ y, V_y)


def test_I_lgl_aug():
    x, _ = xw_lgl(10)
    x_aug, _ = xw_lgl(11)
    y = x ** 2
    I_y = x_aug ** 3 / 3
    assert np.allclose(I_lgl_aug(10) @ y, I_y)

    x, _ = xw_lgl(10)
    x_aug, _ = xw_lgl(11)
    y = x ** 5
    I_y = x_aug ** 6 / 6
    assert np.allclose(I_lgl_aug(10) @ y, I_y)

    x, _ = xw_lgl(20)
    x_aug, _ = xw_lgl(21)
    y = np.sin(x)
    I_y = - np.cos(x_aug) + 1
    assert np.allclose(I_lgl_aug(20) @ y, I_y)


def test_V_c_aug():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([6, 7, 5, 6, 7, 5, 6], dtype=np.int32)
    x, _ = xw_c(mesh, num_point)
    x_nc_aug, _ = xw_nc(mesh, num_point + 1)
    y = np.sin(x)
    T_y = np.sin(x_nc_aug)
    assert np.allclose(V_c_aug(mesh, num_point) @ y, T_y)


def test_V_nc_aug():
    mesh = np.array([0, 0.1, 0.3, 0.4, 0.7, 0.8, 0.85, 1], dtype=np.float64)
    num_point = np.array([6, 7, 5, 6, 7, 5, 6], dtype=np.int32)
    x_nc, _ = xw_nc(mesh, num_point)
    x_nc_aug, _ = xw_nc(mesh, num_point + 1)
    y = np.sin(x_nc)
    T_y = np.sin(x_nc_aug)
    assert np.allclose(V_nc_aug(mesh, num_point) @ y, T_y)
