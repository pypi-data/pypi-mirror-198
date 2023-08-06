from scrapse.leggitalia import utils


def show_filters(j: bool = True, s: bool = True, l: bool = True):
    """
        Shows possible values to be assigned to respective filters to extract judgments
    """
    if j:
        print(f'Judicial bodies {utils.JUDICIAL_BODIES}\n')
    if s:
        print(f'Sections {utils.SECTIONS}\n')
    if l:
        print(f'Locations {utils.LOCATIONS}\n')
