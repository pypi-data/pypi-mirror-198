from sila2_interop_communication_tester.grpc_stubs import SiLAFramework_pb2
from sila2_interop_communication_tester.grpc_stubs.MetadataConsumerTest_pb2 import (
    Subscribe_ReceivedStringMetadataAsCharacters_Parameters,
)
from sila2_interop_communication_tester.grpc_stubs.MetadataProvider_pb2 import Metadata_StringMetadata
from sila2_interop_communication_tester.test_client.helpers.error_handling import raises_invalid_metadata_error
from sila2_interop_communication_tester.test_client.helpers.utils import pack_metadata


def test_subscribe_received_string_metadata_as_charactersfails_without_metadata(metadataconsumertest_stub):
    stream = metadataconsumertest_stub.Subscribe_ReceivedStringMetadataAsCharacters(
        Subscribe_ReceivedStringMetadataAsCharacters_Parameters()
    )
    with raises_invalid_metadata_error():
        next(stream)


def test_subscribe_received_string_metadata_as_charactersfails_with_empty_string_metadata(metadataconsumertest_stub):
    stream = metadataconsumertest_stub.Subscribe_ReceivedStringMetadataAsCharacters(
        request=Subscribe_ReceivedStringMetadataAsCharacters_Parameters(),
        metadata=pack_metadata(Metadata_StringMetadata()),
    )
    with raises_invalid_metadata_error():
        next(stream)


def test_subscribe_received_string_metadata_as_charactersworks_with_abc(metadataconsumertest_stub):
    stream = metadataconsumertest_stub.Subscribe_ReceivedStringMetadataAsCharacters(
        request=Subscribe_ReceivedStringMetadataAsCharacters_Parameters(),
        metadata=pack_metadata(Metadata_StringMetadata(StringMetadata=SiLAFramework_pb2.String(value="abc"))),
    )
    assert [msg.ReceivedStringMetadataAsCharacters.value for msg in stream] == list("abc")


def test_subscribe_received_string_metadata_as_charactersworks_with_abcde(metadataconsumertest_stub):
    stream = metadataconsumertest_stub.Subscribe_ReceivedStringMetadataAsCharacters(
        request=Subscribe_ReceivedStringMetadataAsCharacters_Parameters(),
        metadata=pack_metadata(Metadata_StringMetadata(StringMetadata=SiLAFramework_pb2.String(value="abcde"))),
    )
    assert [msg.ReceivedStringMetadataAsCharacters.value for msg in stream] == list("abcde")
