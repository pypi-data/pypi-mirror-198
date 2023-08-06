import asyncio
from typing import Optional

from pymodbus.register_read_message import ReadHoldingRegistersResponse

from unipi_control.config import HardwareDefinition
from unipi_control.config import LogPrefix
from unipi_control.config import logger
from unipi_control.features import EastronMeter


class EastronSDM120M:
    def __init__(self, neuron, definition: HardwareDefinition) -> None:
        """Initialize Eastron SDM120M electricity meter.

        Attributes
        ----------
        neuron: class
            The Neuron class for registering features.
        """
        self.neuron = neuron
        self.definition: HardwareDefinition = definition
        self._sw_version: Optional[str] = None

    def _parse_feature_meter(self, modbus_feature: dict) -> None:
        meter: EastronMeter = EastronMeter(
            neuron=self.neuron,
            definition=self.definition,
            sw_version=self._sw_version,
            **modbus_feature,
        )

        self.neuron.features.register(meter)

    def _parse_feature(self, modbus_feature: dict) -> None:
        feature_type: str = modbus_feature["feature_type"].lower()

        if func := getattr(self, f"_parse_feature_{feature_type}", None):
            func(modbus_feature)

    async def _get_sw_version(self) -> Optional[str]:
        await asyncio.sleep(4e-3)

        sw_version: Optional[str] = None

        data: dict = {
            "address": 64514,
            "count": 2,
            "slave": self.definition.unit,
        }

        try:
            response: ReadHoldingRegistersResponse = await self.neuron.modbus_client.serial.read_holding_registers(
                **data
            )

            if not response.isError():
                meter_code: str = f"{format(response.registers[0], '0x')}{format(response.registers[1], '0x')}"
                sw_version = f"{meter_code[:3]}.{meter_code[3:]}"
        except asyncio.exceptions.TimeoutError:
            logger.error("%s Timeout on: %s", LogPrefix.MODBUS, data)

        return sw_version

    def parse_features(self) -> None:
        """Parse features from hardware definition."""
        for modbus_feature in self.definition.modbus_features:
            self._parse_feature(modbus_feature)

    async def init(self) -> None:
        """Initialize Eastron SDM120M device class.

        Read software version from Modbus RTU and parse features.
        """
        self._sw_version = await self._get_sw_version()
        self.parse_features()
