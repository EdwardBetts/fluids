# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    List,
    Optional,
    Union,
)


def Armand(x: float, rhol: float, rhog: float) -> float: ...


def Baroczy(x: float, rhol: float, rhog: float, mul: float, mug: float) -> float: ...


def Beattie_Whalley(x: float, mul: float, mug: float, rhol: float, rhog: float) -> float: ...


def Chisholm_Armand(x: float, rhol: float, rhog: float) -> float: ...


def Chisholm_voidage(x: float, rhol: float, rhog: float) -> float: ...


def Cicchitti(x: float, mul: float, mug: float) -> float: ...


def Dix(x: float, rhol: float, rhog: float, sigma: float, m: float, D: float, g: float = ...) -> float: ...


def Domanski_Didion(x: float, rhol: float, rhog: float, mul: float, mug: float) -> float: ...


def Duckler(x: float, mul: float, mug: float, rhol: float, rhog: float) -> float: ...


def Fauske(x: float, rhol: float, rhog: float) -> float: ...


def Fourar_Bories(x: float, mul: float, mug: float, rhol: float, rhog: float) -> float: ...


def Graham(
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    m: float,
    D: float,
    g: float = ...
) -> float: ...


def Gregory_Scott(x: float, rhol: float, rhog: float) -> float: ...


def Guzhov(x: float, rhol: float, rhog: float, m: float, D: float) -> float: ...


def Harms(
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    m: float,
    D: float
) -> float: ...


def Huq_Loth(x: float, rhol: float, rhog: float) -> float: ...


def Kawahara(x: float, rhol: float, rhog: float, D: float) -> float: ...


def Kopte_Newell_Chato(
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    m: float,
    D: float,
    g: float = ...
) -> float: ...


def Lin_Kwok(x: float, mul: float, mug: float) -> float: ...


def Lockhart_Martinelli_Xtt(
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    pow_x: float = ...,
    pow_rho: float = ...,
    pow_mu: float = ...,
    n: Optional[float] = ...
) -> float: ...


def McAdams(x: float, mul: float, mug: float) -> float: ...


def Nicklin_Wilkes_Davidson(x: float, rhol: float, rhog: float, m: float, D: float, g: float = ...) -> float: ...


def Nishino_Yamazaki(x: float, rhol: float, rhog: float) -> float: ...


def Rouhani_1(x: float, rhol: float, rhog: float, sigma: float, m: float, D: float, g: float = ...) -> float: ...


def Rouhani_2(x: float, rhol: float, rhog: float, sigma: float, m: float, D: float, g: float = ...) -> float: ...


def Smith(x: float, rhol: float, rhog: float) -> float: ...


def Steiner(x: float, rhol: float, rhog: float, sigma: float, m: float, D: float, g: float = ...) -> float: ...


def Sun_Duffey_Peng(
    x: float,
    rhol: float,
    rhog: float,
    sigma: float,
    m: float,
    D: float,
    P: float,
    Pc: float,
    g: float = ...
) -> float: ...


def Tandon_Varma_Gupta(
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    m: float,
    D: float
) -> float: ...


def Thom(x: float, rhol: float, rhog: float, mul: float, mug: float) -> float: ...


def Turner_Wallis(x: float, rhol: float, rhog: float, mul: float, mug: float) -> float: ...


def Woldesemayat_Ghajar(
    x: float,
    rhol: float,
    rhog: float,
    sigma: float,
    m: float,
    D: float,
    P: float,
    angle: float = ...,
    g: float = ...
) -> float: ...


def Xu_Fang_voidage(x: float, rhol: float, rhog: float, m: float, D: float, g: float = ...) -> float: ...


def Yashar(
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    m: float,
    D: float,
    g: float = ...
) -> float: ...


def Zivi(x: float, rhol: float, rhog: float) -> float: ...


def density_two_phase(alpha: float, rhol: float, rhog: float) -> float: ...


def gas_liquid_viscosity(
    x: float,
    mul: float,
    mug: float,
    rhol: Optional[float] = ...,
    rhog: Optional[float] = ...,
    Method: Optional[str] = ...
) -> float: ...


def gas_liquid_viscosity_methods(
    rhol: Optional[float] = ...,
    rhog: Optional[float] = ...,
    check_ranges: bool = ...
) -> List[str]: ...


def homogeneous(x: float, rhol: float, rhog: float) -> float: ...


def liquid_gas_voidage(
    x: float,
    rhol: float,
    rhog: float,
    D: Optional[float] = ...,
    m: Optional[float] = ...,
    mul: Optional[float] = ...,
    mug: Optional[float] = ...,
    sigma: Optional[float] = ...,
    P: Optional[float] = ...,
    Pc: Optional[float] = ...,
    angle: int = ...,
    g: float = ...,
    Method: Optional[str] = ...
) -> float: ...


def liquid_gas_voidage_methods(
    x: float,
    rhol: float,
    rhog: float,
    D: Optional[float] = ...,
    m: Optional[float] = ...,
    mul: Optional[float] = ...,
    mug: Optional[float] = ...,
    sigma: Optional[float] = ...,
    P: Optional[float] = ...,
    Pc: Optional[float] = ...,
    angle: float = ...,
    g: float = ...,
    check_ranges: bool = ...
) -> List[str]: ...


def two_phase_voidage_experimental(rho_lg: float, rhol: float, rhog: float) -> float: ...

__all__: List[str]