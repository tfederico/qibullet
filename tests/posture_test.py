#!/usr/bin/env python
# coding: utf-8
import unittest
from qibullet import SimulationManager
from qibullet import NaoVirtual, PepperVirtual


class PostureTest(unittest.TestCase):
    """
    Unittests for Pepper's postures
    """

    def test_invalid_posture(self):
        """
        Test the robustness of the @goToPosture method by sending an invalid
        posture
        """
        self.assertFalse(
            PostureTest.robot.goToPosture("invalid", 0.5))

    def test_stand_posture(self):
        """
        Test the Stand posture
        """
        self.assertTrue(
            PostureTest.robot.goToPosture("Stand", 0.5))
        self.assertTrue(
            PostureTest.robot.goToPosture("stand", 0.5))

    def test_stand_init_posture(self):
        """
        Test the StandInit posture
        """
        self.assertTrue(
            PostureTest.robot.goToPosture("StandInit", 0.5))
        self.assertTrue(
            PostureTest.robot.goToPosture("standInit", 0.5))

    def test_stand_zero_posture(self):
        """
        Test the StandZero posture
        """
        self.assertTrue(
            PostureTest.robot.goToPosture("StandZero", 0.5))
        self.assertTrue(
            PostureTest.robot.goToPosture("standZero", 0.5))

    def test_crouch_posture(self):
        """
        Test the Crouch posture
        """
        self.assertTrue(
            PostureTest.robot.goToPosture("Crouch", 0.5))
        self.assertTrue(
            PostureTest.robot.goToPosture("crouch", 0.5))


class PepperPostureTest(PostureTest):
    """
    Unittests for Pepper's postures
    """

    @classmethod
    def setUpClass(cls):
        """
        Launches a simulation and spawns the Pepper virtual robot
        """
        PostureTest.simulation = SimulationManager()
        PostureTest.client = PostureTest.simulation.launchSimulation(
            gui=False)

        PostureTest.robot = PostureTest.simulation.spawnPepper(
            PostureTest.client,
            spawn_ground_plane=True)

    @classmethod
    def tearDownClass(cls):
        """
        Stops the simulation
        """
        PostureTest.simulation.stopSimulation(
            PostureTest.client)


class NaoPostureTest(PostureTest):
    """
    Unittests for Nao's postures
    """

    @classmethod
    def setUpClass(cls):
        """
        Launches a simulation and spawns the NAO virtual robot
        """
        PostureTest.simulation = SimulationManager()
        PostureTest.client = PostureTest.simulation.launchSimulation(
            gui=False)

        PostureTest.robot = PostureTest.simulation.spawnNao(
            PostureTest.client,
            spawn_ground_plane=True)

    @classmethod
    def tearDownClass(cls):
        """
        Stops the simulation
        """
        PostureTest.simulation.stopSimulation(
            PostureTest.client)


class RomeoPostureTest(PostureTest):
    """
    Unittests for Romeo's postures
    """

    @classmethod
    def setUpClass(cls):
        """
        Launches a simulation and spawns the NAO virtual robot
        """
        PostureTest.simulation = SimulationManager()
        PostureTest.client = PostureTest.simulation.launchSimulation(
            gui=False)

        PostureTest.robot = PostureTest.simulation.spawnRomeo(
            PostureTest.client,
            spawn_ground_plane=True)

    @classmethod
    def tearDownClass(cls):
        """
        Stops the simulation
        """
        PostureTest.simulation.stopSimulation(
            PostureTest.client)


if __name__ == "__main__":
    unittest.main()
