import unittest
import json


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.dict = {
            "make": self.make,
            "model": self.model,
            "year": self.year
        }


class MyEncoder(json.JSONEncoder):
    def default(self, veh):
        if isinstance(veh, Vehicle):
            return veh.dict
        return super().default(self, veh)


class MyDecoder(json.JSONDecoder):
    def decode_vehicle(self, veh):
        return Vehicle(**veh)


class TestMyFunctions(unittest.TestCase):
    def test_my_encoder(self):
        vehicle = Vehicle("Toyota", "Camry", 2020)
        encoder = MyEncoder()
        encoded_vehicle = encoder.default(vehicle)
        expected_output = {"make": "Toyota", "model": "Camry", "year": 2020}
        self.assertEqual(encoded_vehicle, expected_output)

    def test_my_decoder(self):
        vehicle_data = {"make": "Ford", "model": "Mustang", "year": 2019}
        decoder = MyDecoder()
        decoded_vehicle = decoder.decode_vehicle(vehicle_data)
        expected_vehicle = Vehicle("Ford", "Mustang", 2019)
        self.assertEqual(vars(decoded_vehicle), vars(expected_vehicle))

