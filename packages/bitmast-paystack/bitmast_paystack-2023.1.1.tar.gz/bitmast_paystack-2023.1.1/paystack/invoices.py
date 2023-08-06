import json
from enum import IntFlag
from typing import Any
import requests

from paystack.util import PayStackGatewayFlag, BusinessDataObject, PayStackRestUrl, Command


__all__ = ('create_invoice', 'list_invoices', 'view_invoice', 'verify_invoice',
           'send_notification', 'invoice_metrics', 'finalize_draft', 'update_invoice',
           'archive_invoice', 'mark_as_paid')


class InvoiceCommandRank(IntFlag):
    CREATE_INVOICE = 179
    LIST_INVOICES = 181
    VIEW_INVOICE = 191
    VERIFY_INVOICE = 193
    SEND_NOTIFICATION = 197
    INVOICE_METRICS = 199
    FINALIZE_DRAFT = 211
    FETCH_INVOICE = 223
    UPDATE_INVOICE = 227
    ARCHIVE_INVOICE = 229
    MARK_AS_PAID = 233


def create_invoice_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    url = bdo.url(PayStackRestUrl.CREATE_INVOICE_URL)
    response = requests.post(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


def list_invoices_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    query = bdo.data
    url = bdo.url(PayStackRestUrl.LIST_INVOICES_URL, params=query)
    response = requests.get(url=url, headers=bdo.header)
    
    return response


def view_invoice_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    query = bdo.data.get('id_or_code')
    url = bdo.url(PayStackRestUrl.VIEW_INVOICE_URL)
    url += f'{query}'
    response = requests.get(url=url, headers=bdo.header)
    
    return response


def verify_invoice_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    # Retrieve invoice code
    query = bdo.data.get('code')
    url = bdo.url(PayStackRestUrl.VERIFY_INVOICE_URL)
    url += f'{query}'
    response = requests.get(url=url, headers=bdo.header)
    
    return response


def send_notification_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    query = bdo.data.get('code')
    url = bdo.url(PayStackRestUrl.SEND_NOTIFICATION_URL)
    url += f'{query}'
    response = requests.post(url=url, headers=bdo.header)
    
    return response


def invoice_metrics_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    url = bdo.url(PayStackRestUrl.INVOICE_METRICS_URL)
    response = requests.get(url=url, headers=bdo.header)
    
    return response


def finalize_draft_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    invoice_id = data.get('invoice_id') or data.get('code')
    url = bdo.url(PayStackRestUrl.FINALIZE_DRAFT_URL)
    url += f'{invoice_id}'
    if 'invoice_id' in data:
        del data['invoice_id']
    elif 'code' in data:
        del data['code']
    response = requests.post(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


def update_invoice_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    invoice_id = data.get('invoice_id') or data.get('id')
    url = bdo.url(PayStackRestUrl.UPDATE_INVOICE_URL)
    url += f'{invoice_id}'
    if 'invoice_id' in data:
        del data['invoice_id']
    elif 'code' in data:
        del data['code']
    response = requests.put(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


def archive_invoice_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    query = bdo.data.get('id_or_code')
    url = bdo.url(PayStackRestUrl.ARCHIVE_INVOICE_URL)
    url += f'{query}'
    response = requests.post(url=url, headers=bdo.header)
    
    return response


def mark_as_paid_cmd(**kwargs) -> Any:
    bdo = BusinessDataObject(use_config=True, **kwargs)
    data = bdo.data
    invoice_id = data.get('invoice_id') or data.get('code')
    url = bdo.url(PayStackRestUrl.MARK_AS_PAID_URL)
    url += f'{invoice_id}'
    if 'invoice_id' in data:
        del data['invoice_id']
    elif 'code' in data:
        del data['code']
    response = requests.post(url=url, data=json.dumps(data), headers=bdo.header)
    
    return response


create_invoice = Command(cmd=create_invoice_cmd, group=PayStackGatewayFlag.INVOICES,
                         rank=InvoiceCommandRank.CREATE_INVOICE, label=None)
list_invoices = Command(cmd=list_invoices_cmd, group=PayStackGatewayFlag.INVOICES,
                        rank=InvoiceCommandRank.LIST_INVOICES, label=None)
view_invoice = Command(cmd=view_invoice_cmd, group=PayStackGatewayFlag.INVOICES,
                       rank=PayStackGatewayFlag.INVOICES, label=None)
verify_invoice = Command(cmd=verify_invoice_cmd, group=PayStackGatewayFlag.INVOICES,
                         rank=InvoiceCommandRank.VERIFY_INVOICE, label=None)
send_notification = Command(cmd=send_notification_cmd, group=PayStackGatewayFlag.INVOICES,
                            rank=InvoiceCommandRank.SEND_NOTIFICATION, label=None)
invoice_metrics = Command(cmd=invoice_metrics_cmd, group=PayStackGatewayFlag.INVOICES,
                          rank=InvoiceCommandRank.INVOICE_METRICS, label=None)
finalize_draft = Command(cmd=finalize_draft_cmd, group=PayStackGatewayFlag.INVOICES,
                         rank=InvoiceCommandRank.FINALIZE_DRAFT, label=None)
update_invoice = Command(cmd=update_invoice_cmd, group=PayStackGatewayFlag.INVOICES,
                         rank=InvoiceCommandRank.UPDATE_INVOICE, label=None)
archive_invoice = Command(cmd=archive_invoice_cmd, group=PayStackGatewayFlag.INVOICES,
                          rank=InvoiceCommandRank.ARCHIVE_INVOICE, label=None)
mark_as_paid = Command(cmd=mark_as_paid_cmd, group=PayStackGatewayFlag.INVOICES,
                       rank=InvoiceCommandRank.MARK_AS_PAID, label=None)
