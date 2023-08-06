import sys 
import pandas as pd
import math
import lib_dzne_workbook
import lib_dzne_sqlite.exec
import lib_dzne_data
import lib_dzne_manifesto


from lib_dzne_manifesto import get_antibody_data




def main(antibody_ids):
    BASE.heart.fill.antibodies()
    rows = [_main(antibody_id) for antibody_id in antibody_ids]
    df = pd.DataFrame(rows)
    return write_dataFrame(df)

def _main(antibody_id):
    data = get_antibody_data(antibody_id)
    flattened_data = lib_dzne_data.flatten(data)
    return flattened_data


def write_dataFrame(df):
    """Writing data from table into masterfile-template. """
    masterrow = BASE.config.get_config()['masterfile']['keyrow']
    wb = BASE.config.get_workbook()
    ws = wb.active
    for colnum in range(1, ws.max_column + 1):
        currentcell = ws.cell(column=colnum, row=masterrow)
        value = currentcell.value
        if type(value) is not str:
            continue
        value = value.strip()
        if value.startswith('='):
            continue
        if value == "":
            continue
        if value not in df.columns:
            lib_dzne_workbook.set_cell(cell=currentcell, value="")
            continue
        for i, newvalue in enumerate(df[value].tolist()):
            datacell = ws.cell(column=colnum, row=masterrow+i)
            lib_dzne_workbook.set_cell(cell=datacell, value=None if pd.isna(newvalue) else newvalue)
    return wb







