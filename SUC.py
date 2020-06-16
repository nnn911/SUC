def J2eV(val):
    # convert Joule to eV
    return val/e


def eV2J(val):
    # convert eV to Joule
    return val*e


def eVpA2N(val):
    # convert eV/A to Newton
    return val*e*1e10


def eVpA32Pa(val):
    # convert eV/A^3 to Pa (N/m^2)
    return val*e*1e30


# Boltzman constant
k = 1.380649e-23

# Elementary charge
e = 1.602176634e-19

# Avogadro's number:
NA = 6.02214076e23

# Boltzman constant in eV
k_eV = J2eV(k)
