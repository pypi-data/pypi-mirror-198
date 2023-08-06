# -*- coding: utf-8 -*-
import json
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *


def demo():
    import urllib.request
    import json

    with urllib.request.urlopen('https://fakerapi.it/api/v1/persons?_quantity=30') as f:
        data = json.load(f)['data']

    put_datatable(
        data,
        actions=[
            ("Edit Email", lambda row_id: datatable_update('persons', input("Email"), row_id, "email")),
            ("Reset Row", lambda row_id: datatable_update('persons', data[row_id], row_id)),
            ("Delete", lambda row_id: datatable_remove('persons', row_id)),
        ],
        onselect=lambda row_id: toast('Selected row: %s' % row_id),
        instance_id='persons'
    )

    put_button('Append to head', lambda: datatable_insert('persons', data[:5], 0))
    put_button('Append to tail', lambda: datatable_insert('persons', data[:5]))
    put_button("Reset", lambda: datatable_update('persons', data))


import json


def main():
    set_env(output_max_width='90%')

    if False:
        import urllib.request
        # https://www.ag-grid.com/example-assets/small-olympic-winners.json
        with urllib.request.urlopen('https://fakerapi.it/api/v1/persons?_quantity=30') as f:
            data = json.load(f)['data']
    else:
        f = "/Users/wangweimin/repos/pywebio-battery/d.json"
        data = json.load(open(f))
    instance_id = '0'

    put_button("Update whole table", onclick=lambda: datatable_update(instance_id, data[:10]))

    def add():
        datatable_insert(instance_id, data[0], 0)
        datatable_insert(instance_id, data[-5:])

    put_buttons(['add'], [add])

    def update(idx):
        if isinstance(idx, list):
            idx = idx[0]
        d = data[idx]
        d['job_id'] = 'updated'
        datatable_update(instance_id, d, idx)

    def show(d):
        toast(str(type(d)))
        toast(d)

    def delete(idx):
        datatable_remove(instance_id, idx)

    actions = [
        ('Show idx', show),
        None,
        ('Update', update),
        ('Delete', delete),

    ]
    column_args = {
        's3': {
            'hide': True
        }
    }
    grid_args = {
        'defaultColDef': {
            'maxWidth': 300
        },
        'onGridReady': JSFunction('')
    }


    # with popup("table"):
    #     put_datatable(
    #         data,
    #         actions=actions,
    #         onselect=show,
    #         multiple_select=False,
    #         # id_field='job_id',
    #         # instance_id=instance_id,
    #         column_args=column_args,
    #         grid_args=grid_args,
    #         # enterprise_key='test',
    #     )

    put_datatable(
        data[:20],
        height='auto',
        actions=actions,
        onselect=show,
        multiple_select=False,
        # id_field='job_id',
        # instance_id=instance_id,
        column_args=column_args,
        grid_args=grid_args,
        # enterprise_key='test',
    )

    put_collapse("Table", put_datatable(
        data[:20],
        height='auto',
        actions=actions,
        onselect=show,
        multiple_select=False,
        # id_field='job_id',
        # instance_id=instance_id,
        column_args=column_args,
        grid_args=grid_args,
        # enterprise_key='test',
    ))



    put_tabs([
        {'title': 'Text', 'content': 'Hello world'},
        {'title': 'Text', 'content': put_datatable(
            data,
            actions=actions,
            onselect=show,
            multiple_select=False,
            # id_field='job_id',
            instance_id=instance_id,
            column_args=column_args,
            grid_args=grid_args,
            enterprise_key='test',
        )

         },
    ])

    # put_editable_datatable(
    #     data,
    #     actions=actions,
    #     onselect=show,
    #     inplace_update=True,
    #     edit_callback=lambda *d: toast(str(d)),
    #     # id_field='job_id',
    #     editable_fields=['job_id'],
    #     instance_id=instance_id,
    #     column_args=column_args,
    #     grid_args=grid_args,
    #     enterprise_key='test',
    # )
    put_code('sdfaf')


if __name__ == '__main__':
    start_server([main, demo], port=8088, debug=True, cdn=False)
