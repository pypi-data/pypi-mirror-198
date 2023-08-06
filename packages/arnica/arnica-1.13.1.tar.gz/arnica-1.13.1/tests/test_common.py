import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

""" unit tests for arnica.utils

OST : I heard it through the grapevine, by Leo. Moracchioli
"""

import numpy as np
from arnica.utils.vector_actions import (
    renormalize,
    angle_btw_vects,
    yz_to_theta,
    rtheta2yz,
    rotate_vect_around_x,
    rotate_vect_around_axis,
    dilate_vect_around_x,
    cart_to_cyl,
    clip_by_bounds,
    cyl_to_cart,
    vect_to_quat,
    make_radial_vect,
    mask_cloud,
)

from arnica.utils.directed_projection import (
    projection_kdtree,
    compute_dists,
    project_points,
)
from arnica.utils.cloud2cloud import cloud2cloud
from arnica.utils.nparray2xmf import NpArray2Xmf
from arnica.utils.plot_quad2tri import (
    get_connectivity,
    quad2tri,
    plot_quad2tri,
)

SMALL = 3e-16
DIM1 = 5
DIM2 = 7

BINS = 100


def deviation(fieldx_in, fieldy_in):
    """ plot deviation """

    fieldx = np.ravel(fieldx_in)
    fieldy = np.ravel(fieldy_in)
    corr_norm = np.linalg.norm(fieldx - fieldy, ord=2)
    corr_norm /= np.linalg.norm((fieldx + fieldy) / 2., ord=2)

    plt.cla()
    plt.hist2d(fieldx, fieldy, BINS, norm=LogNorm())
    line45 = np.linspace(np.amin(np.concatenate((fieldx, fieldy), axis=0)),
                         np.amax(np.concatenate((fieldx, fieldy), axis=0)))
    plt.plot(line45, line45, linewidth=2.0, ls='--', c='k')
    plt.xlim(np.amin(fieldx), np.amax(fieldx))
    plt.ylim(np.amin(fieldx), np.amax(fieldx))
    plt.xlabel('File 1', fontsize=16)
    plt.ylabel('File 2', fontsize=16)
    plt.tick_params(axis='x', labelsize=16)
    plt.tick_params(axis='y', labelsize=16)
    textstr = ("L2-norm error:\n" + str(corr_norm))
    plt.gcf().text(0.02,
                   0.02,
                   textstr,
                   fontsize=18,
                   bbox={'facecolor': 'red',
                         'alpha': 0.2})
    plt.rc('font', size=16)
    plt.tight_layout()
    plt.show()


def squared_func(xxx, yyy, zzz):
    """ test function """
    return (3 * xxx ** 2 + 5 * yyy ** 2 + 7 * zzz * 2) / (
            3 ** 2 * 5 ** 2 * 7 ** 2)


def test_nparray2xmf():
    """ test of nparray dump """

    x_coor = np.linspace(0, 1., DIM2 * 10)
    y_coor = np.linspace(0, 1., DIM2 * 10)
    z_coor = np.linspace(0, 1., DIM2 * 10)

    source_xyz = np.stack(np.meshgrid(x_coor, y_coor, z_coor), axis=-1)

    xmf3d = NpArray2Xmf("dummy.h5")
    xmf3d.create_grid(np.take(source_xyz, 0, axis=-1),
                      np.take(source_xyz, 1, axis=-1),
                      np.take(source_xyz, 2, axis=-1))

    xmf3d.add_field(squared_func(np.take(source_xyz, 0, axis=-1),
                                 np.take(source_xyz, 1, axis=-1),
                                 np.take(source_xyz, 2, axis=-1)),
                    "dummy")


def test_cloud2cloud():
    """
    small test of cloud2cloud projection
    """
    size = 1000
    x_coor = np.linspace(0, 1., DIM2 * 10)
    y_coor = np.linspace(0, 1., DIM2 * 10)
    z_coor = np.linspace(0, 1., DIM2 * 10)

    source_xyz = np.stack(np.meshgrid(x_coor, y_coor, z_coor),
                          axis=-1)
    target_xyz = np.stack((np.random.rand(DIM1 * size) * 1.,
                           np.random.rand(DIM1 * size) * 1.,
                           np.random.rand(DIM1 * size) * 1.),
                          axis=-1)

    source_val = {}
    source_val["v"] = squared_func(np.take(source_xyz, 0, axis=-1),
                                   np.take(source_xyz, 1, axis=-1),
                                   np.take(source_xyz, 2, axis=-1), )

    target_ref = squared_func(target_xyz[:, 0],
                              target_xyz[:, 1],
                              target_xyz[:, 2], )

    target_estimate5 = cloud2cloud(source_xyz,
                                   source_val,
                                   target_xyz,
                                   stencil=5)

    target_estimate1 = cloud2cloud(source_xyz,
                                   source_val,
                                   target_xyz,
                                   stencil=1,
                                   limitsource=100000)
    assert np.all(np.abs(target_ref - target_estimate1["v"]) < 1e-4)
    assert np.all(np.abs(target_ref - target_estimate5["v"]) < 1e-5)

def test_clip_by_bounds():
    """ test the clip of a cloud of points by bounds """

    point_cloud = np.array([[0., 0., 1.],
                            [1., np.cos(np.pi/4), np.sin(np.pi/4)],
                            [2., 1., 0.]])
    bounds_dict = {"x": (0.5, 3.0), "y": (0.0, 0.8)}
    exp_out = clip_by_bounds(point_cloud, bounds_dict, keep="out")
    exp_target = np.array([[0., 0., 1.],
                           [2., 1., 0.]])

    exp_out = clip_by_bounds(point_cloud, bounds_dict, keep="in")
    exp_target = np.array([[1., np.cos(np.pi/4), np.sin(np.pi/4)]])

    np.testing.assert_array_equal(exp_out, exp_target)

def test_projection_kdtree():
    r"""
    small test of directed projection

                  xyz(0,1,0)  dir(1,-1,0)
                x
                 \
                 _\|


                ^
                |
  ______________o______x________
  s0     s1     s2     s3     s4
               /          xyz(1,0,0)
xyz(0,0,0)  nml (0,1,0)
    """

    test_points_xyz = np.zeros((DIM2, 3))
    test_points_xyz[:, 1] = 1.0
    test_points_dir = np.zeros((DIM2, 3))
    test_points_dir[:, 0] = 1.0
    test_points_dir[:, 1] = -1.0
    test_points_dir = renormalize(test_points_dir)

    test_surf_xyz = np.zeros((DIM1, 3))
    test_surf_xyz[:, 0] = np.linspace(-2, 2, DIM1)
    test_surf_nml = np.zeros((DIM1, 3))
    test_surf_nml[:, 1] = 1.0

    neighb = 3

    projection = projection_kdtree(
        test_points_xyz,
        test_points_dir,
        test_surf_xyz,
        test_surf_nml,
        neigbors=neighb,
    )

    exp_xyz = np.zeros((DIM2, 3))
    exp_indexes = np.repeat(
        np.array([2, 3, 1])[np.newaxis, :],
        DIM2,
        axis=0)
    exp_cyl_dists = np.repeat(
        np.array([0.0, np.sqrt(2.0) * 0.5, np.sqrt(2.0) * 0.5])[np.newaxis, :],
        DIM2,
        axis=0)

    np.testing.assert_allclose(projection.moved_pts, exp_xyz)
    np.testing.assert_equal(projection.indexes, exp_indexes)
    np.testing.assert_allclose(projection.cyl_dists, exp_cyl_dists, atol=1e-6)
    # assert out_xyz.shape == projection.moved_pts.shape
    # assert np.all(out_xyz == projection.moved_pts)
    # assert out_indexes.shape == projection.indexes.shape
    # assert np.all(out_indexes == projection.indexes)
    # assert out_cyl_dists.shape == exp_out_cyl_dists.shape
    # assert np.all(np.abs(exp_out_cyl_dists - out_cyl_dists) < SMALL)

    project=False
    projection = projection_kdtree(
        test_points_xyz,
        test_points_dir,
        test_surf_xyz,
        test_surf_nml,
        neigbors=neighb,
        project=project)

    exp_xyz = np.tile([0., 1., 0.], (DIM2, 1))
    exp_indexes = np.tile([2, 3, 1], (DIM2, 1))
    exp_cyl_dists = np.tile([0.70710678, 0., 1.4142135], (DIM2, 1))

    np.testing.assert_allclose(projection.moved_pts, exp_xyz)
    np.testing.assert_equal(projection.indexes, exp_indexes)
    np.testing.assert_allclose(projection.cyl_dists, exp_cyl_dists, atol=1e-6)

def test_compute_dists():
    """ test of computation of cylindrical distances """

    test_points_xyz = np.zeros((DIM2, 3))
    test_points_dir = np.zeros((DIM2, 3))
    test_points_dir[:, 0] = 1.0
    test_points_dir[:, 1] = -1.0
    test_points_dir = renormalize(test_points_dir)

    neighb = 3
    test_surf_xyz = np.zeros((DIM2, neighb, 3))
    test_surf_xyz[:, 1, 0] = 1.
    test_surf_xyz[:, 2, 0] = -1.
    test_surf_nml = np.zeros((DIM2, neighb, 3))
    test_surf_nml[:, :, 1] = 1.
    
    tol = 1000.

    _, out_cyl_dists = compute_dists(
        test_points_xyz,
        test_points_dir,
        test_surf_xyz,
        test_surf_nml,
        tol,
    )
    exp_out_cyl_dists = np.array([[0., 0.70710678, 0.70710678],
                                  [0., 0.70710678, 0.70710678],
                                  [0., 0.70710678, 0.70710678],
                                  [0., 0.70710678, 0.70710678],
                                  [0., 0.70710678, 0.70710678],
                                  [0., 0.70710678, 0.70710678],
                                  [0., 0.70710678, 0.70710678]])

    assert out_cyl_dists.shape == exp_out_cyl_dists.shape
    np.testing.assert_allclose(out_cyl_dists, exp_out_cyl_dists)


def test_project_points():
    """ test the projection of points on a plan defined by a point and a normal """

    test_points_xyz = np.zeros((DIM2, 3))
    test_points_xyz[:, 1] = 1.
    test_points_dir = np.zeros((DIM2, 3))
    test_points_dir[:, 1] = -1.
    test_surf_xyz = np.zeros((DIM2, DIM1, 3))
    test_surf_xyz[:,:,0] = np.linspace(-2., 2., DIM1)

    proj = project_points(test_points_xyz, test_points_dir, test_surf_xyz)
    
    exp_out_proj_pts = np.tile(np.array([0., 0., 0.]), (DIM2, DIM1, 1))
    exp_out_axi_dists = np.tile(np.array([1., 1., 1., 1., 1.]), (DIM2, 1))
    exp_out_rad_dists = np.tile(np.array([2., 1., 0., 1., 2.]), (DIM2, 1))
    np.testing.assert_array_equal(exp_out_proj_pts, proj.proj_pts)
    np.testing.assert_array_equal(exp_out_axi_dists, proj.axi_dists)
    np.testing.assert_array_equal(exp_out_rad_dists, proj.rad_dists)

def test_renormalize():
    """ test renormalize in 1D an 2D arrays of 3D components"""
    in_x = np.ones((DIM1, 3))
    out_x = in_x / np.sqrt(3)
    assert np.all(renormalize(in_x) == out_x)
    in_x = np.ones((DIM1, DIM2, 3))
    out_x = in_x / np.sqrt(3)
    assert np.all(renormalize(in_x) == out_x)


def test_angle_btw_vects():
    """ test angle btw vects in 1D an 2D arrays of 3D components"""
    # todo : failing test to fix
    in_x1 = np.zeros((DIM1, 3))
    in_x1[:, 2] = 1.0
    in_x2 = np.zeros((DIM1, 3))
    in_x2[:, 1] = 1.0
    out = angle_btw_vects(in_x1, in_x2, convert_to_degree=True)

    assert np.all(out == np.ones((DIM1)) * 90.)

    in_x1 = np.zeros((DIM1, DIM2, 3))
    in_x1[:, :, 2] = 1.0
    in_x2 = np.zeros((DIM1, DIM2, 3))
    in_x2[:, :, 1] = 1.0
    out = angle_btw_vects(in_x1, in_x2, convert_to_degree=True)
    assert np.all(out == np.ones((DIM1, DIM2)) * 90.)


def test_yz_to_theta():
    """ test convertion to theta
           0pi=0deg
              Y
              ^
              |
              |
-0.5pi=-90deg     o------>Z   0.5pi=90deg
    """
    in_x = np.zeros((DIM1, 3))
    in_x[:, 2] = 1.0
    out = yz_to_theta(in_x)
    assert np.all(out == np.ones((DIM1)) * np.pi * 0.5)

    in_x = np.zeros((DIM1, 3))
    in_x[:, 1] = 1.0
    out = yz_to_theta(in_x)
    assert np.all(out == np.ones((DIM1)) * 0.)

    in_x = np.zeros((DIM1, DIM2, 3))
    in_x[:, :, 2] = -1.0
    out = yz_to_theta(in_x)
    assert np.all(out == np.ones((DIM1, DIM2)) * -0.5 * np.pi)

def test_rtheta2yz():
    """ test conversion of r, theta to y, z-axis """

    in_r = np.ones(DIM1) * 2.
    in_theta = np.ones(DIM1) * np.pi / 4.
    out = rtheta2yz(in_r, in_theta)
    np.testing.assert_allclose(out[0], np.ones(DIM1) * 1.414213562373095)
    np.testing.assert_allclose(out[1], np.ones(DIM1) * 1.414213562373095)

    in_r = np.ones((DIM1, DIM2)) * 2.
    in_theta = np.ones((DIM1, DIM2)) * np.pi * 3 / 4
    out = rtheta2yz(in_r, in_theta)
    np.testing.assert_allclose(out[0], np.ones((DIM1, DIM2)) * -1.414213562373095)
    np.testing.assert_allclose(out[1], np.ones((DIM1, DIM2)) * 1.414213562373095)

def test_rotate_vect_around_x():
    """ test the rotation of vectors """
    in_x = np.zeros((DIM1, 3))
    in_x[:, 2] = 1.0
    out = rotate_vect_around_x(in_x, 90.0)
    exp_out = np.zeros((DIM1, 3))
    exp_out[:, 1] = -1.0
    assert np.all(np.abs(out - exp_out) < SMALL)

    in_x = np.zeros((DIM1, DIM2, 3))
    in_x[:, :, 2] = 1.0
    out = rotate_vect_around_x(in_x, 90.0)
    exp_out = np.zeros((DIM1, DIM2, 3))
    exp_out[:, :, 1] = -1.0
    assert out.shape == exp_out.shape
    assert np.all(np.abs(out - exp_out) < SMALL)

def test_rotate_vect_around_axis():
    """ test of rotation of vectors around several axis """

    in_x = np.zeros((DIM1, 3))
    in_x[:, 2] = 1.0
    out = rotate_vect_around_axis(in_x, ([1, 0, 0], 90.0))
    exp_out = np.zeros((DIM1, 3))
    exp_out[:, 1] = -1.0
    assert np.all(np.abs(out - exp_out) < SMALL)

    out = rotate_vect_around_axis(in_x,
                                  ([0, 1, 0], 45.),
                                  ([4., 0., 2.1], 64.))
    exp_out = np.tile([0.55922829, -0.79579036, 0.232339], (DIM1, 1))
    np.testing.assert_allclose(out, exp_out)

def test_dilate_vect_around_x():
    """ test the dilatation of vectors around x """

    azimuth = np.array([-45., 0., 45.])
    np_ar_vect = np.array([[0., np.cos(np.pi/4), -np.sin(np.pi/4)],
                           [0., 1., 0.],
                           [0., np.cos(np.pi/4), np.sin(np.pi/4)]])
    exp_out = dilate_vect_around_x(azimuth, np_ar_vect)
    exp_target = np.array([[0., -1., 0.],
                           [0., 1., 0.],
                           [0., -1., 0.]])

    np.testing.assert_allclose(exp_out, exp_target, atol=1e-8)

def test_cart_to_cyl():
    """ test the conversion from xyz-system to cyl-system """

    vects_xyz = np.array([[0., 0., 1.],
                          [1., np.cos(np.pi/4), np.sin(np.pi/4)],
                          [2., 1., 0.]])
    exp_out = cart_to_cyl(vects_xyz)
    exp_target = np.array([[0., 1., np.pi/2],
                           [1., 1., np.pi/4],
                           [2., 1., 0.]])

    np.testing.assert_allclose(exp_out, exp_target)

def test_cyl_to_cart():
    """ test the conversion from cyl-system to xyz-system """

    vects_cyl = np.array([[0., 1., np.pi/2],
                          [1., 1., np.pi/4],
                          [2., 1., 0.]])
    exp_out = cyl_to_cart(vects_cyl)
    exp_target = np.array([[0., 0., 1.],
                           [1., np.cos(np.pi/4), np.sin(np.pi/4)],
                           [2., 1., 0.]])

    np.testing.assert_allclose(exp_out, exp_target, atol=1e-8)

def test_clip_by_bounds():
    """ test of the clip of field by bounds dict """

    points_coord = np.arange(DIM2 * 3.).reshape((DIM2, 3))
    bounds = {"x": (3., 13.)}
    out = clip_by_bounds(points_coord, bounds, keep="in", return_mask=False)
    out_target = [[3.,   4.,  5.],
                  [6.,   7.,  8.],
                  [9.,  10., 11.],
                  [12., 13., 14.]]
    np.testing.assert_array_equal(out, out_target)

    bounds = {"x": (3., 13.),
              "z": (6., 1.e6)}
    out = clip_by_bounds(points_coord, bounds, keep="out", return_mask=True)
    out_target = np.array([1, 1, 0, 0, 0, 1, 1], dtype=bool)
    np.testing.assert_array_equal(out, out_target)

def test_vect_to_quat():
    """ test the building of a quaternion from two vects """

    vect_t = np.array([0., 1., 1.])
    vect_s = np.array([0., 0., 2.])
    exp_out = vect_to_quat(vect_t, vect_s).as_rotvec()
    exp_target = np.array([-np.pi / 4, 0., 0.])

    np.testing.assert_allclose(exp_out, exp_target, atol=1e-8)

    vect_t = np.array([[0., 1., 1.],
                       [1., 2., 0.]])
    vect_s = np.array([[0., 0., 2.],
                       [0., 2., 1.]])
    exp_out = vect_to_quat(vect_t, vect_s).as_rotvec()
    exp_target = np.array([[-0.78539816, 0., 0.],
                           [-0.42900074, 0.21450037, -0.42900074]])

    np.testing.assert_allclose(exp_out, exp_target, atol=1e-8)

def test_make_radial_vect():
    """ test function making vectors radial """

    coord = np.zeros((DIM1, 3))
    coord[:, 1] = 1.
    coord[:, 2] = -1.
    vects = np.zeros((DIM1, 3))
    vects[:, 0] = 1.
    vects[:, 1] = 1.
    vects = renormalize(vects)

    out = make_radial_vect(coord, vects)
    np.testing.assert_allclose(out, vects, atol=1e-6)

    coord[:, 1] = 6.
    out = make_radial_vect(coord, vects)
    out_target = [[0.70710678, 0.69748583, -0.11624764],
                  [0.70710678, 0.69748583, -0.11624764],
                  [0.70710678, 0.69748583, -0.11624764],
                  [0.70710678, 0.69748583, -0.11624764],
                  [0.70710678, 0.69748583, -0.11624764]]
    np.testing.assert_allclose(out, out_target, atol=1e-6)

def test_mask_cloud():
    """ test vector masking """
    in_x = np.stack((np.linspace(-2, 2, DIM1),
                     np.linspace(-2, 2, DIM1),
                     np.linspace(-2, 2, DIM1)),
                    axis=0)
    for i, axe in enumerate(["x", "y", "z"]):
        out = mask_cloud(in_x,
                         axis=axe,
                         support=(-1.0, 1.0))
        exp_out = (in_x[:, i] >= -1.0) * (in_x[:, i] < 1.0)
        assert np.all(out == exp_out)

    in_x = np.repeat(in_x[:, np.newaxis, :],
                     DIM2,
                     axis=1)
    for i, axe in enumerate(["x", "y", "z"]):
        out = mask_cloud(in_x,
                         axis=axe,
                         support=(-1.0, 1.0))
        exp_out = (in_x[:, :, i] >= -1.0) * (in_x[:, :, i] < 1.0)
        assert out.shape == exp_out.shape
        assert np.all(out == exp_out)

    in_x = np.stack((np.zeros(DIM1),
                     np.ones(DIM1),
                     np.linspace(-2, 2, DIM1)),
                    axis=0)
    out = mask_cloud(in_x,
                     axis="r",
                     support=(0, 2.0))
    exp_out = np.hypot(np.take(in_x, 1, axis=-1),
                       np.take(in_x, 2, axis=-1)) < 2.0
    assert np.all(out == exp_out)

    out = mask_cloud(in_x,
                     axis="theta",
                     support=(-20.0, 20))
    theta = np.rad2deg(yz_to_theta(in_x))
    exp_out = (theta >= -20.0) * (theta < 20.0)
    assert np.all(out == exp_out)

    exception_reached = False
    try:
        mask_cloud(in_x,
                   axis="dummy",
                   support=(-20.0, 20))
    except IOError:
        exception_reached = True

    assert exception_reached

def test_get_connectivity():
    """ test get_connectivity """

    i = 1
    j = 2
    shape = (4, 4)

    connectivity_target = [[6, 7, 21], [7, 11, 21], [11, 10, 21], [10, 6, 21]]
    np.testing.assert_array_equal(get_connectivity(i, j, shape), connectivity_target)

def test_quad2tri():
    """ test of quad2tri """

    x, y = np.meshgrid(np.linspace(0., 1., 3),
                       np.linspace(0., 1., 5))
    grid = np.stack((y, x), axis=-1)

    field = np.ones((5,3))
    field[:, 0] = 2.

    triangulation, field = quad2tri(grid, field)

    field_tgt = [2., 1., 1., 2., 1., 1., 2., 1., 1.,
                 2., 1., 1., 2., 1., 1., 1.5, 1., 1.5,
                 1., 1.5, 1., 1.5, 1.]
    np.testing.assert_array_equal(field, field_tgt)

def test_plot_quad2tri():
    """ test of plotting of quad2tri """

    x, y = np.meshgrid(np.linspace(0., 1., 3),
                       np.linspace(0., 1., 5))
    grid = np.stack((y, x), axis=-1)
    field = np.ones((5,3))
    field[:, 0] = 2.
    title = "Test_plot_quad2tri"

    plt_out = plot_quad2tri(grid, title, field)
    assert isinstance(plt_out, type(plt))
    plt_out = plot_quad2tri(grid, title, field, shading=False)
    assert isinstance(plt_out, type(plt))
