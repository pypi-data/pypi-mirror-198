from functools import partial
from typing import Tuple, Callable, Union, Sequence, Optional

import einops
import torch

from torch_cubic_b_spline_grid.interpolate_grids import (
    interpolate_grid_1d as _interpolate_grid_1d,
    interpolate_grid_2d as _interpolate_grid_2d,
    interpolate_grid_3d as _interpolate_grid_3d,
    interpolate_grid_4d as _interpolate_grid_4d,
)
from torch_cubic_b_spline_grid.utils import coerce_to_multichannel_grid

CoordinateLike = Union[float, Sequence[float], torch.Tensor]


class CubicBSplineGrid(torch.nn.Module):
    """Base class for continuous parametrisations of multidimensional spaces."""
    resolution: Tuple[int, ...]
    ndim: int
    _data: torch.nn.Parameter
    _interpolation_function: Callable

    def __init__(
        self,
        resolution: Optional[Tuple[int, ...]] = None,
        n_channels: int = 1
    ):
        super().__init__()
        if resolution is None:
            resolution = [2] * self.ndim
        grid_shape = tuple([n_channels, *resolution])
        self.data = torch.zeros(size=grid_shape)

    def forward(self, u: torch.Tensor) -> torch.Tensor:
        u = self._coerce_to_batched_coordinates(u)  # (b, d)
        interpolated = self._interpolation_function(self._data, u)
        return self._unpack_interpolated_output(interpolated)

    @classmethod
    def from_grid_data(cls, data: torch.Tensor):
        """

        Parameters
        ----------
        data: torch.Tensor
            (c, *grid_dimensions) or (*grid_dimensions) array of multichannel values at
            each grid point.
        """
        grid = cls()
        grid.data = data
        return grid

    @property
    def data(self) -> torch.Tensor:
        return self._data.detach()

    @data.setter
    def data(self, grid_data: torch.Tensor) -> None:
        grid_data = coerce_to_multichannel_grid(grid_data, grid_ndim=self.ndim)
        self._data = torch.nn.Parameter(grid_data)

    @property
    def n_channels(self) -> int:
        return self._data.shape[0]

    @property
    def resolution(self) -> Tuple[int, ...]:
        return tuple(self._data.shape[1:])

    def _coerce_to_batched_coordinates(self, u: torch.Tensor) -> Tuple[torch.Tensor, ]:
        u = torch.atleast_1d(torch.as_tensor(u, dtype=torch.float32))
        self._input_is_coordinate_like = u.shape[-1] == self.ndim
        if self._input_is_coordinate_like is False and self.ndim == 1:
            u = einops.rearrange(u, '... -> ... 1')  # add singleton coord dimension
        else:
            u = torch.atleast_2d(u)  # add batch dimension if missing
        u, self._packed_shapes = einops.pack([u], pattern='* coords')
        if u.shape[-1] != self.ndim:
            ndim = u.shape[-1]
            raise ValueError(
                f'Cannot interpolate on a {self.ndim}D grid with {ndim}D coordinates'
            )
        return u

    def _unpack_interpolated_output(self, interpolated: torch.Tensor) -> torch.Tensor:
        [interpolated] = einops.unpack(
            interpolated, packed_shapes=self._packed_shapes, pattern='* coords'
        )
        if self._input_is_coordinate_like is False and self.ndim == 1:
            interpolated = einops.rearrange(interpolated, '... 1 -> ...')
        return interpolated


class CubicBSplineGrid1d(CubicBSplineGrid):
    """Continuous parametrisation of a 1D space with a specific resolution."""
    ndim: int = 1
    _interpolation_function: Callable = partial(_interpolate_grid_1d)

    def __init__(
        self,
        resolution: Optional[Union[int, Tuple[int]]] = None,
        n_channels: int = 1):
        if isinstance(resolution, int):
            resolution = tuple([resolution])
        super().__init__(resolution, n_channels)


class CubicBSplineGrid2d(CubicBSplineGrid):
    """Continuous parametrisation of a 2D space with a specific resolution."""
    ndim: int = 2
    _interpolation_function: Callable = partial(_interpolate_grid_2d)


class CubicBSplineGrid3d(CubicBSplineGrid):
    """Continuous parametrisation of a 3D space with a specific resolution."""
    ndim: int = 3
    _interpolation_function: Callable = partial(_interpolate_grid_3d)


class CubicBSplineGrid4d(CubicBSplineGrid):
    """Continuous parametrisation of a 4D space with a specific resolution."""
    ndim: int = 4
    _interpolation_function: Callable = partial(_interpolate_grid_4d)
