import matplotlib.pyplot as plt
import pyfits
from mpl_toolkits.axes_grid.axes_grid import AxesGrid
from pywcsgrid2.axes_wcs import AxesWcs, GridHelperWcs
from mpl_toolkits.axes_grid.inset_locator import zoomed_inset_axes, mark_inset
from mpl_toolkits.axes_grid.axislines import Axes

if 1:

    f = pyfits.open("pspc_skyview.fits")
    d = f[0].data
    h = f[0].header

    fig = plt.figure(1)

    grid_helper = GridHelperWcs(wcs=h)
    grid_helper.update_wcsgrid_params(label_density=(5,5))

    grid = AxesGrid(fig, (1, 1, 1), nrows_ncols = (1, 1),
                    cbar_mode="single", cbar_pad="2%",
                    cbar_location="right",
                    axes_class=(AxesWcs, dict(grid_helper=grid_helper)))

    main_axes = grid[0]
    cb_axes = grid.cbar_axes[0] # colorbar axes
    
    im = main_axes.imshow(d, origin="lower", cmap=plt.cm.gray_r,
                        vmin=4.e-05, vmax=0.00018,
                        interpolation="nearest")

    cb_axes.colorbar(im)
    cb_axes.axis["right"].major_ticklabels.set_visible(True)

    axins = zoomed_inset_axes(main_axes, zoom=3, loc=1,
                              axes_class=Axes)

    for a in axins.axis.values():
        a.toggle(all=False, ticks=True)

    im2 = axins.imshow(d, origin="lower", interpolation="nearest",
                       vmin=9.e-05, vmax=18.e-05,
                       cmap=plt.cm.gray_r)

    axins.set_xlim(120, 160)
    axins.set_ylim(120, 160)

    mark_inset(main_axes, axins, loc1=2, loc2=4, fc="none", ec="0.5")

    plt.draw()
    plt.show()
