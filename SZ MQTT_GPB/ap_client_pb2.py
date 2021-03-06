# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ap_client.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ap_client.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\037com.ruckuswireless.scg.protobuf'),
  serialized_pb=_b('\n\x0f\x61p_client.proto\"\xf2\x07\n\x0c\x41PClientInfo\x12\x11\n\tclientMac\x18\x01 \x02(\t\x12\x11\n\tipAddress\x18\x02 \x01(\t\x12\x13\n\x0bipv6Address\x18\x03 \x01(\t\x12\x0e\n\x06wlanId\x18\x04 \x01(\x05\x12\x0c\n\x04rssi\x18\x05 \x01(\x05\x12\x1d\n\x15receiveSignalStrength\x18\x06 \x01(\x05\x12\x12\n\nnoiseFloor\x18\x07 \x01(\x05\x12\x0c\n\x04vlan\x18\x08 \x01(\x05\x12\x10\n\x08rxFrames\x18\t \x01(\x04\x12\x0f\n\x07rxBytes\x18\n \x01(\x04\x12\x10\n\x08txFrames\x18\x0b \x01(\x04\x12\x0f\n\x07txBytes\x18\x0c \x01(\x04\x12\x14\n\x0ctxMgmtFrames\x18\r \x01(\x04\x12\x14\n\x0crxMgmtFrames\x18\x0e \x01(\x04\x12\x15\n\rthroughputEst\x18\x0f \x01(\r\x12\x18\n\x10txDropDataFrames\x18\x10 \x01(\x04\x12\x18\n\x10txDropMgmtFrames\x18\x11 \x01(\x04\x12\x16\n\x0erxCRCErrFrames\x18\x12 \x01(\r\x12\x0f\n\x07txRetry\x18\x13 \x01(\r\x12\x0e\n\x06osType\x18\x14 \x01(\t\x12\x1d\n\x05radio\x18\x15 \x01(\x0b\x32\x0e.APClientRadio\x12.\n\x0btcWithQuota\x18\x16 \x03(\x0b\x32\x19.APClientInfo.TCWithQuota\x12\x0e\n\x06\x63peMac\x18\x17 \x01(\t\x12\x12\n\nstickyWeak\x18\x18 \x01(\r\x12\x12\n\ndeviceType\x18\x19 \x01(\x05\x12\x14\n\x0cosVendorType\x18\x1a \x01(\x05\x12\x11\n\tmodelName\x18\x1b \x01(\t\x12\x10\n\x08hostname\x18\x1c \x01(\t\x12\x14\n\x0b\x43onnectMode\x18\xe9\x07 \x01(\t\x12\x11\n\x08Username\x18\xea\x07 \x01(\t\x12\x12\n\tSessionId\x18\xeb\x07 \x01(\t\x12\x1a\n\x11MultipleSessionId\x18\xec\x07 \x01(\t\x12\x11\n\x08\x41uthMode\x18\xed\x07 \x01(\t\x12\x16\n\rDiscTimestamp\x18\xee\x07 \x01(\x04\x12\x13\n\nRxByteRate\x18\xef\x07 \x01(\r\x12\x13\n\nTxByteRate\x18\xf0\x07 \x01(\r\x12\x16\n\rRxAvgByteRate\x18\xf1\x07 \x01(\r\x12\x16\n\rTxAvgByteRate\x18\xf2\x07 \x01(\r\x12\x10\n\x07RxError\x18\xf3\x07 \x01(\r\x12\x10\n\x07TxError\x18\xf4\x07 \x01(\r\x12\x15\n\x0cReassocCount\x18\xf5\x07 \x01(\r\x12\x15\n\x0cTxRetryBytes\x18\xf6\x07 \x01(\r\x12\x13\n\nRxDropPkts\x18\xf7\x07 \x01(\r\x1aK\n\x0bTCWithQuota\x12\x0e\n\x06tcName\x18\x01 \x01(\t\x12\x12\n\ntcMaxQuota\x18\x02 \x01(\t\x12\x18\n\x10tcRemainingQuota\x18\x03 \x01(\t\"\xcc\x01\n\x0c\x41PClientWlan\x12\x0c\n\x04ssid\x18\x01 \x02(\t\x12\r\n\x05\x62ssid\x18\x02 \x01(\t\x12\x0c\n\x04vlan\x18\x03 \x01(\x05\x12\x11\n\twsgWlanId\x18\x04 \x01(\x05\x12\x0e\n\x06wlanId\x18\x05 \x01(\x05\x12\x14\n\x0cwlangroup_id\x18\x06 \x01(\t\x12\x15\n\rwlantenant_id\x18\x07 \x01(\t\x12\x16\n\x0ewlangroup_name\x18\x08 \x01(\t\x12\x17\n\x0fwlantenant_name\x18\t \x01(\t\x12\x10\n\x08wlanName\x18\n \x01(\t\"\x85\x01\n\rAPClientRadio\x12\x0f\n\x07radioId\x18\x01 \x02(\x05\x12\x0c\n\x04mode\x18\x02 \x01(\t\x12\x11\n\tradioMode\x18\x03 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\x12\x14\n\x0c\x63hannelWidth\x18\x05 \x01(\r\x12\x1b\n\x04wlan\x18\x06 \x01(\x0b\x32\r.APClientWlan\"\x93\x03\n\rAPClientStats\x12\x0f\n\x07version\x18\x01 \x02(\r\x12\n\n\x02\x61p\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x11\n\tseqNumber\x18\x04 \x01(\x04\x12\x0f\n\x07zone_id\x18\x05 \x01(\t\x12\x1e\n\x07\x63lients\x18\x06 \x03(\x0b\x32\r.APClientInfo\x12\x12\n\napgroup_id\x18\x07 \x01(\t\x12\x12\n\ncluster_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\x12\x13\n\x0b\x61ptenant_id\x18\n \x01(\t\x12\x0e\n\x06map_id\x18\x0b \x01(\t\x12\x15\n\raptenant_name\x18\x0c \x01(\t\x12\x11\n\tzone_name\x18\r \x01(\t\x12\x14\n\x0c\x61pgroup_name\x18\x0e \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x0f \x01(\t\x12\x12\n\nsampleTime\x18\x10 \x01(\x04\x12\x1b\n\x13\x61ggregationInterval\x18\x11 \x01(\r\x12\x12\n\ndeviceName\x18\x12 \x01(\t\x12\x14\n\x0cserialNumber\x18\x13 \x01(\tB!\n\x1f\x63om.ruckuswireless.scg.protobuf')
)




_APCLIENTINFO_TCWITHQUOTA = _descriptor.Descriptor(
  name='TCWithQuota',
  full_name='APClientInfo.TCWithQuota',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tcName', full_name='APClientInfo.TCWithQuota.tcName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcMaxQuota', full_name='APClientInfo.TCWithQuota.tcMaxQuota', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcRemainingQuota', full_name='APClientInfo.TCWithQuota.tcRemainingQuota', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=955,
  serialized_end=1030,
)

_APCLIENTINFO = _descriptor.Descriptor(
  name='APClientInfo',
  full_name='APClientInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientMac', full_name='APClientInfo.clientMac', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipAddress', full_name='APClientInfo.ipAddress', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6Address', full_name='APClientInfo.ipv6Address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlanId', full_name='APClientInfo.wlanId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='APClientInfo.rssi', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiveSignalStrength', full_name='APClientInfo.receiveSignalStrength', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='noiseFloor', full_name='APClientInfo.noiseFloor', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vlan', full_name='APClientInfo.vlan', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rxFrames', full_name='APClientInfo.rxFrames', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rxBytes', full_name='APClientInfo.rxBytes', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txFrames', full_name='APClientInfo.txFrames', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txBytes', full_name='APClientInfo.txBytes', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txMgmtFrames', full_name='APClientInfo.txMgmtFrames', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rxMgmtFrames', full_name='APClientInfo.rxMgmtFrames', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throughputEst', full_name='APClientInfo.throughputEst', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txDropDataFrames', full_name='APClientInfo.txDropDataFrames', index=15,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txDropMgmtFrames', full_name='APClientInfo.txDropMgmtFrames', index=16,
      number=17, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rxCRCErrFrames', full_name='APClientInfo.rxCRCErrFrames', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txRetry', full_name='APClientInfo.txRetry', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osType', full_name='APClientInfo.osType', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radio', full_name='APClientInfo.radio', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcWithQuota', full_name='APClientInfo.tcWithQuota', index=21,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpeMac', full_name='APClientInfo.cpeMac', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stickyWeak', full_name='APClientInfo.stickyWeak', index=23,
      number=24, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceType', full_name='APClientInfo.deviceType', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osVendorType', full_name='APClientInfo.osVendorType', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelName', full_name='APClientInfo.modelName', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='APClientInfo.hostname', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ConnectMode', full_name='APClientInfo.ConnectMode', index=28,
      number=1001, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Username', full_name='APClientInfo.Username', index=29,
      number=1002, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SessionId', full_name='APClientInfo.SessionId', index=30,
      number=1003, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MultipleSessionId', full_name='APClientInfo.MultipleSessionId', index=31,
      number=1004, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AuthMode', full_name='APClientInfo.AuthMode', index=32,
      number=1005, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DiscTimestamp', full_name='APClientInfo.DiscTimestamp', index=33,
      number=1006, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RxByteRate', full_name='APClientInfo.RxByteRate', index=34,
      number=1007, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TxByteRate', full_name='APClientInfo.TxByteRate', index=35,
      number=1008, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RxAvgByteRate', full_name='APClientInfo.RxAvgByteRate', index=36,
      number=1009, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TxAvgByteRate', full_name='APClientInfo.TxAvgByteRate', index=37,
      number=1010, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RxError', full_name='APClientInfo.RxError', index=38,
      number=1011, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TxError', full_name='APClientInfo.TxError', index=39,
      number=1012, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ReassocCount', full_name='APClientInfo.ReassocCount', index=40,
      number=1013, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TxRetryBytes', full_name='APClientInfo.TxRetryBytes', index=41,
      number=1014, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RxDropPkts', full_name='APClientInfo.RxDropPkts', index=42,
      number=1015, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_APCLIENTINFO_TCWITHQUOTA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=1030,
)


_APCLIENTWLAN = _descriptor.Descriptor(
  name='APClientWlan',
  full_name='APClientWlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='APClientWlan.ssid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bssid', full_name='APClientWlan.bssid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vlan', full_name='APClientWlan.vlan', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wsgWlanId', full_name='APClientWlan.wsgWlanId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlanId', full_name='APClientWlan.wlanId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlangroup_id', full_name='APClientWlan.wlangroup_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlantenant_id', full_name='APClientWlan.wlantenant_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlangroup_name', full_name='APClientWlan.wlangroup_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlantenant_name', full_name='APClientWlan.wlantenant_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlanName', full_name='APClientWlan.wlanName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1033,
  serialized_end=1237,
)


_APCLIENTRADIO = _descriptor.Descriptor(
  name='APClientRadio',
  full_name='APClientRadio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='radioId', full_name='APClientRadio.radioId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='APClientRadio.mode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radioMode', full_name='APClientRadio.radioMode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='APClientRadio.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channelWidth', full_name='APClientRadio.channelWidth', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlan', full_name='APClientRadio.wlan', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1240,
  serialized_end=1373,
)


_APCLIENTSTATS = _descriptor.Descriptor(
  name='APClientStats',
  full_name='APClientStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='APClientStats.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ap', full_name='APClientStats.ap', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='APClientStats.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqNumber', full_name='APClientStats.seqNumber', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='APClientStats.zone_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clients', full_name='APClientStats.clients', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apgroup_id', full_name='APClientStats.apgroup_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='APClientStats.cluster_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='APClientStats.domain_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aptenant_id', full_name='APClientStats.aptenant_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='APClientStats.map_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aptenant_name', full_name='APClientStats.aptenant_name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_name', full_name='APClientStats.zone_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apgroup_name', full_name='APClientStats.apgroup_name', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='APClientStats.domain_name', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampleTime', full_name='APClientStats.sampleTime', index=15,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregationInterval', full_name='APClientStats.aggregationInterval', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceName', full_name='APClientStats.deviceName', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialNumber', full_name='APClientStats.serialNumber', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1376,
  serialized_end=1779,
)

_APCLIENTINFO_TCWITHQUOTA.containing_type = _APCLIENTINFO
_APCLIENTINFO.fields_by_name['radio'].message_type = _APCLIENTRADIO
_APCLIENTINFO.fields_by_name['tcWithQuota'].message_type = _APCLIENTINFO_TCWITHQUOTA
_APCLIENTRADIO.fields_by_name['wlan'].message_type = _APCLIENTWLAN
_APCLIENTSTATS.fields_by_name['clients'].message_type = _APCLIENTINFO
DESCRIPTOR.message_types_by_name['APClientInfo'] = _APCLIENTINFO
DESCRIPTOR.message_types_by_name['APClientWlan'] = _APCLIENTWLAN
DESCRIPTOR.message_types_by_name['APClientRadio'] = _APCLIENTRADIO
DESCRIPTOR.message_types_by_name['APClientStats'] = _APCLIENTSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

APClientInfo = _reflection.GeneratedProtocolMessageType('APClientInfo', (_message.Message,), {

  'TCWithQuota' : _reflection.GeneratedProtocolMessageType('TCWithQuota', (_message.Message,), {
    'DESCRIPTOR' : _APCLIENTINFO_TCWITHQUOTA,
    '__module__' : 'ap_client_pb2'
    # @@protoc_insertion_point(class_scope:APClientInfo.TCWithQuota)
    })
  ,
  'DESCRIPTOR' : _APCLIENTINFO,
  '__module__' : 'ap_client_pb2'
  # @@protoc_insertion_point(class_scope:APClientInfo)
  })
_sym_db.RegisterMessage(APClientInfo)
_sym_db.RegisterMessage(APClientInfo.TCWithQuota)

APClientWlan = _reflection.GeneratedProtocolMessageType('APClientWlan', (_message.Message,), {
  'DESCRIPTOR' : _APCLIENTWLAN,
  '__module__' : 'ap_client_pb2'
  # @@protoc_insertion_point(class_scope:APClientWlan)
  })
_sym_db.RegisterMessage(APClientWlan)

APClientRadio = _reflection.GeneratedProtocolMessageType('APClientRadio', (_message.Message,), {
  'DESCRIPTOR' : _APCLIENTRADIO,
  '__module__' : 'ap_client_pb2'
  # @@protoc_insertion_point(class_scope:APClientRadio)
  })
_sym_db.RegisterMessage(APClientRadio)

APClientStats = _reflection.GeneratedProtocolMessageType('APClientStats', (_message.Message,), {
  'DESCRIPTOR' : _APCLIENTSTATS,
  '__module__' : 'ap_client_pb2'
  # @@protoc_insertion_point(class_scope:APClientStats)
  })
_sym_db.RegisterMessage(APClientStats)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
