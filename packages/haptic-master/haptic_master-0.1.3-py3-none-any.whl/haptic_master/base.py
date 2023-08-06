'''Base class for the effects and the objects

Classes
-------
Base

Functions
---------
get_pos()
set_pos(value)
get_vel()
set_vel(value)
get_att()
set_att(value)

Variables
---------
name
robot

'''

from dataclasses import dataclass
import logging
import numpy as np
import numpy.typing as npt
from .haptic_master import HapticMaster


@dataclass(frozen=True, slots=True)
class Base:
    '''Base class shared by effects and objects of the HapticMaster API

    Attributes
    ----------
    name (str): Name of the effect/object
    robot (HapticMaster): The robot where the effect/object is going to be implemented

    Methods
    -------
    get_pos()
        Get the position of the effect/object from the robot
    set_pos(value)
        Set the position of the effect/object on the robot
    get_vel()
        Get the velocity of the effect/object from the robot
    set_vel(value)
        Set the velocity of the effect/object on the robot
    get_att()
        Get the orientation of the effect/object from the robot
    set_att(value)
        Set the orientation of the effect/object on the robot

    '''

    name: str
    robot: HapticMaster

    def get_pos(self) -> npt.NDArray:
        '''Get the position of the effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'get {self.name} pos'

        return self.robot.string_to_array(self.robot.send_message(msg))

    def set_pos(self, value: npt.NDArray) -> bool:
        '''Set the position of the effect/object on the robot

        Parameters
        ----------
        value (npt.NDArray): The position of the effect/object to be set

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        if type(value) == np.ndarray:
            msg = f'set {self.name} direction [{",".join(str(v) for v in value)}]'
        else:
            msg = f'set {self.name} direction {str(value).replace(" ", "")}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Effect\'s position set' in response

    def get_vel(self) -> npt.NDArray:
        '''Get the velocity of the effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = f'get {self.name} vel'

        return self.robot.string_to_array(self.robot.send_message(msg))

    def set_vel(self, value: npt.NDArray) -> bool:
        '''Set the velocity of the effect/object on the robot

        Parameters
        ----------
        value (npt.NDArray): The velocity of the effect/object to be set

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        if type(value) == np.ndarray:
            msg = f'set {self.name} direction [{",".join(str(v) for v in value)}]'
        else:
            msg = f'set {self.name} direction {str(value).replace(" ", "")}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Effect\'s velocity set' in response

    def get_att(self) -> npt.NDArray:
        '''Get the attitude (orientation) of the effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = f'get {self.name} att'

        return self.robot.string_to_array(self.robot.send_message(msg))

    def set_att(self, value: npt.NDArray) -> bool:
        '''Set the attitude (orientation) of the effect/object on the robot

        Parameters
        ----------
        value (npt.NDArray): The orientation of the effect/object to be set as
                      a unit quaternion

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        if type(value) == np.ndarray:
            msg = f'set {self.name} direction [{",".join(str(v) for v in value)}]'
        else:
            msg = f'set {self.name} direction {str(value).replace(" ", "")}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Effect\'s attitude set' in response

    def set_enable(self) -> bool:
        '''Enable the effect/object

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = f'set {self.name} enable'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'enabled' in response

    def set_disable(self) -> bool:
        '''Disable the effect/object

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = f'set {self.name} disable'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'disabled' in response

    def get_enabled(self) -> bool:
        '''Get the enable/disable status of an effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = f'get {self.name} enabled'

        return self.robot.string_to_bool(self.robot.send_message(msg))

    def remove(self) -> bool:
        '''Remove an effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'remove {self.name}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Removed' in response
