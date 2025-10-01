"""
mayavi_football.py
Approximate soccer ball using Mayavi: white sphere + 12 dark panel patches (icosahedron vertices).
"""

import numpy as np
from mayavi import mlab

def unit_icosa_vertices():
    """Return the 12 vertices of a unit icosahedron centered at origin."""
    phi = (1 + np.sqrt(5.0)) / 2.0  # golden ratio
    verts = np.array([
        (-1,  phi,  0),
        ( 1,  phi,  0),
        (-1, -phi,  0),
        ( 1, -phi,  0),

        ( 0, -1,  phi),
        ( 0,  1,  phi),
        ( 0, -1, -phi),
        ( 0,  1, -phi),

        ( phi,  0, -1),
        ( phi,  0,  1),
        (-phi,  0, -1),
        (-phi,  0,  1),
    ], dtype=float)
    # normalize to unit radius
    verts /= np.linalg.norm(verts, axis=1).reshape((-1,1))
    return verts

def draw_football(radius=1.0, patch_scale=0.28, patch_resolution=20):
    # Create sphere grid
    n_theta, n_phi = 80, 80
    theta = np.linspace(0, 2*np.pi, n_theta)
    phi = np.linspace(0, np.pi, n_phi)
    th, ph = np.meshgrid(theta, phi)
    x = radius * np.sin(ph) * np.cos(th)
    y = radius * np.sin(ph) * np.sin(th)
    z = radius * np.cos(ph)

    mlab.figure(bgcolor=(0.2, 0.2, 0.2), size=(900, 700))

    # White sphere (the ball base)
    # We set color directly; using scalars is unnecessary here.
    mlab.mesh(x, y, z, color=(0.96, 0.96, 0.96), representation='surface', opacity=1.0)

    # Compute 12 icosahedron vertices and place dark patches there
    verts = unit_icosa_vertices() * radius

    # For each vertex, draw a flattened "patch" by plotting a small sphere-like blob
    # and then slightly scaling it along the radial direction to make it appear as a flattened patch.
    for v in verts:
        # center of patch
        cx, cy, cz = v

        # Create a small sphere grid for the patch, then project it slightly onto the ball surface
        u = np.linspace(0, 2*np.pi, patch_resolution)
        v_ang = np.linspace(0, np.pi, patch_resolution)
        uu, vv = np.meshgrid(u, v_ang)

        # small sphere coordinates around origin
        r_patch = patch_scale * radius
        px = r_patch * np.sin(vv) * np.cos(uu)
        py = r_patch * np.sin(vv) * np.sin(uu)
        pz = r_patch * np.cos(vv)

        # rotate patch so its +z aligns with vertex direction
        # compute rotation: we want to rotate patch's local +z (0,0,1) to direction d = v/norm(v)
        d = np.array([cx, cy, cz])
        d_norm = d / np.linalg.norm(d)

        # find orthonormal basis (u_axis, v_axis, w_axis) with w_axis = d_norm
        w = d_norm
        # choose arbitrary vector not parallel to w to start Gram-Schmidt
        arbitrary = np.array([0.0, 0.0, 1.0]) if abs(w[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
        u_axis = np.cross(arbitrary, w)
        if np.linalg.norm(u_axis) < 1e-6:
            arbitrary = np.array([0.0, 1.0, 0.0])
            u_axis = np.cross(arbitrary, w)
        u_axis /= np.linalg.norm(u_axis)
        v_axis = np.cross(w, u_axis)

        # map local patch coords to world coords
        P = (np.outer(np.ones(px.size), cx)
             + (px.ravel()[:, None] * u_axis[None, :])
             + (py.ravel()[:, None] * v_axis[None, :])
             + (pz.ravel()[:, None] * w[None, :]))
        Px = P[:, 0].reshape(px.shape)
        Py = P[:, 1].reshape(py.shape)
        Pz = P[:, 2].reshape(pz.shape)

        # Slightly shrink patch radially so it sits on the ball surface (avoid z-fighting)
        radial_dirs = np.vstack([Px.ravel(), Py.ravel(), Pz.ravel()]).T
        radial_norms = np.linalg.norm(radial_dirs, axis=1)
        radial_dirs = (radial_dirs.T / radial_norms).T
        radial_pos = (radius - 0.005) * radial_dirs  # place just above surface
        Px = radial_pos[:,0].reshape(Px.shape)
        Py = radial_pos[:,1].reshape(Py.shape)
        Pz = radial_pos[:,2].reshape(Pz.shape)

        # Draw the patch as a dark surface
        mlab.mesh(Px, Py, Pz, color=(0.06, 0.06, 0.06), opacity=1.0)

    # lighting / view polish
    mlab.view(azimuth=60, elevation=60, distance=6*radius)
    mlab.roll(0)
    mlab.orientation_axes()
    mlab.show()

if __name__ == "__main__":
    draw_football()
