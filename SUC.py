def J2eV(val):
    # convert Joule to eV
    return val/e


def eV2J(val):
    # convert eV to Joule
    return val*e


def eVpA2N(val):
    # convert eV/A to Newton
    return eV2J(val)*1e10


def eVpA32Pa(val):
    # convert eV/A^3 to Pa (N/m^2)
    return eV2J(val)*1e30


def kJpMol2eV(val):
    # convert kJ/mol to eV/at.
    return J2eV(val*1000)/NA


def eV2kJpMol(val):
    # convert eV/at. to kJ/mol
    return eV2J(val)/1000*NA

    # Boltzman constant
k = 1.380649e-23

# Elementary charge
e = 1.602176634e-19

# Avogadro's number:
NA = 6.02214076e23

# Boltzman constant in eV
k_eV = J2eV(k)
