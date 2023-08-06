'''Effect classes for HapticMaster

Classes
-------
Effect
Spring
Damper
BiasForce
Shaker

Functions
---------
create()
get_stiffness()
set_stiffness(value)
get_dampfactor()
set_dampfactor(value)
get_deadband()
set_deadband(value)
get_direction()
set_direction(value)
get_maxforce()
set_maxforce(value)
get_dampglobal()
set_dampglobal(value)

create()
set_dampcoef()

create()
get_force()
set_force()

create()
get_frequency1()
set_frequency1(value)
get_frequency2()
set_frequency2(value)
get_direction()
set_direction(value)
get_posmax()
set_posmax(value)
get_velmax()
set_velmax(value)
get_accmax()
set_accmax(value)
get_stiffness()
set_stiffness(value)
get_dampfactor()
set_dampfactor(value)
get_deadband()
set_deadband(value)
get_maxforce()
set_maxforce(value)

'''

from dataclasses import dataclass
import logging
import numpy as np
import numpy.typing as npt
from haptic_master.base import Base


@dataclass(frozen=True, slots=True)
class Effect(Base):
    '''Generic class for effects'''


@dataclass(frozen=True, slots=True)
class Spring(Effect):
    '''A class for spring effect

    Methods
    -------
    create()
        Create a spring effect on the robot
    get_stiffness()
        Get the stiffness of the spring from the robot
    set_stiffness(value)
        Set the stiffness of the spring on the robot
    get_dampfactor()
        Get the damping factor coefficient of the spring from the robot
    set_dampfactor(value)
        Set the damping factor coefficient of the spring on the robot
    get_deadband()
        Get the deadband length of the spring from the robot
    set_deadband(value)
        Set the deadband length of the spring on the robot
    get_direction()
        Get the direction of the spring from the robot
    set_direction(value)
        Set the direction of the spring on the robot
    get_maxforce()
        Get the maximum force of the spring from the robot
    set_maxforce(value)
        Set the maximum force of the spring on the robot
    get_dampglobal()
        Get the global damping status of the spring from the robot
    set_dampglobal(value)
        Set the global damping status of the spring on the robot

    '''

    def create(self) -> bool:
        '''Create a spring on the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'create spring {self.name}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return f'Effect spring with name {self.name} created' in response

    def get_stiffness(self) -> float:
        '''Get the spring coefficient from the robot

        Returns
        -------
        float: Stiffness of the spring [N/m]

        '''

        msg = f'get {self.name} stiffness'

        return float(self.robot.send_message(msg))

    def set_stiffness(self, value: float) -> bool:
        '''Set the stiffness of the spring on the robot

        Parameters
        ----------
        value (float): The stiffness of the spring to be set [N/m]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'set {self.name} stiffness {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Spring\'s stiffness set' in response

    def get_dampfactor(self) -> float:
        '''Get the damping factor of the spring from the robot

        Returns
        -------
        float: Damping factor of the spring [non-dimensional]

        '''

        msg = f'get {self.name} dampfactor'

        return float(self.robot.send_message(msg))

    def set_dampfactor(self, value: float) -> bool:
        '''Set the damping factor of the spring on the robot

        Parameters
        ----------
        value (float): Damping factor of the spring [non-dimensional]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'set {self.name} dampfactor {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Spring\'s damp factor set' in response

    def get_deadband(self) -> float:
        '''Get the deadband length of the spring from the robot

        Returns
        -------
        float: Deadband length of the spring [m]

        '''

        msg = f'get {self.name} deadband'

        return float(self.robot.send_message(msg))

    def set_deadband(self, value: float) -> bool:
        '''Set the deadband length of the spring

        Parameters
        ----------
        value (float): Deadband length of the spring [m]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'set {self.name} deadband {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Spring\'s deadband set' in response

    def get_direction(self) -> npt.NDArray:
        '''Get the direction of the spring from the robot

        Returns
        -------
        npt.NDArray: Direction unit vector read from the robot [non-dimensional]

        '''

        msg = f'get {self.name} direction'

        return self.robot.string_to_array(self.robot.send_message(msg))

    def set_direction(self, value: npt.NDArray) -> bool:
        '''Set the direction of the spring on the robot

        Parameters
        ----------
        value (npt.NDArray): Unit vector for the spring direction [non-dimensional]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        if isinstance(value, np.ndarray):
            msg = f'set {self.name} direction [{",".join(str(v) for v in value)}]'
        else:
            msg = f'set {self.name} direction {str(value).replace(" ", "")}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Spring\'s direction set' in response

    def get_maxforce(self) -> float:
        '''Get the maximum force of the spring from the robot

        Returns
        -------
        float: Maximum force value read from the robot [N]

        '''

        msg = f'get {self.name} maxforce'

        return float(self.robot.send_message(msg))

    def set_maxforce(self, value: float) -> bool:
        '''Set the maximum spring force on the robot

        Parameters
        ----------
        value (float): Maximum force value [N]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'set {self.name} maxforce {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Spring\'s maximum force set' in response

    def get_dampglobal(self) -> bool:
        '''Get the global damping status of the spring from the robot

        Returns
        -------
        bool: Condition for the global damping status of the spring [non-dimensional]

        '''

        msg = f'get {self.name} dampglobal'

        return self.robot.string_to_bool(self.robot.send_message(msg))

    def set_dampglobal(self, value: bool) -> bool:
        '''Set global damping condition of the spring

        Parameters
        ----------
        value (bool): Global damping condition for the spring

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'set {self.name} dampglobal {str(value).lower()}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Spring\'s damping global set' in response


@dataclass(frozen=True, slots=True)
class Damper(Effect):
    '''A class for spring effect

    Methods
    -------
    create()
        Create a spring effect on the robot
    get_dampcoef()
        Get the damping coefficients in of the damper from the robot
    set_dampcoef()
        Set the damping coefficients of the damper on the robot

    '''

    def create(self) -> bool:
        '''Create a damper on the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'create damper {self.name}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return f'Effect damper with name {self.name} created' in response

    def get_dampcoef(self) -> npt.NDArray:
        '''Get the damping coefficients of the damper from the robot

        Returns
        -------
        npt.NDArray: Spatial damping coefficients of the damper [Ns/m]

        '''

        msg = f'get {self.name} dampcoef'

        return self.robot.string_to_array(self.robot.send_message(msg))

    def set_dampcoef(self, value: npt.NDArray) -> bool:
        '''Set spatial damping coefficients of the damper on the robot

        Parameters
        ----------
        value (npt.NDArray): Spatial damping coefficients [Ns/m]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        if isinstance(value, np.ndarray):
            msg = f'set {self.name} direction [{",".join(str(v) for v in value)}]'
        else:
            msg = f'set {self.name} direction {str(value).replace(" ", "")}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Damper\'s damp coefficient set' in response


@dataclass(frozen=True, slots=True)
class BiasForce(Effect):
    '''A class for bias force effect

    Methods
    -------
    create()
        Create a bias force effect on the robot
    get_force()
        Get the force value of the bias force from the robot
    set_force()
        Set the force value of the bias force on the robot

    '''

    def create(self) -> bool:
        '''Create a bias force on the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'create biasforce {self.name}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return f'Effect biasforce with name {self.name} created' in response

    def get_force(self) -> npt.NDArray:
        '''Get the force vector of the bias force from the robot

        Returns
        -------
        npt.NDArray: Force vector [N]

        '''

        msg = f'get {self.name} force'

        return self.robot.string_to_array(self.robot.send_message(msg))

    def set_force(self, value: npt.NDArray) -> bool:
        '''Set bias force value on the robot

        Parameters
        ----------
        value (npt.NDArray): Bias force value [N]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        if isinstance(value, np.ndarray):
            msg = f'set {self.name} force [{",".join(str(v) for v in value)}]'
        else:
            msg = f'set {self.name} force {str(value).replace(" ", "")}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Bias force\'s force set' in response

@dataclass(frozen=True, slots=True)
class Shaker(Effect):
    '''A class for shaker effect

    Methods
    -------
    create()
        Create a shaker effect on the robot
    get_frequency1()
        Get the initial frequency of the shaker from the robot
    set_frequency1(value)
        Set the initial frequency of the shaker on the robot
    get_frequency2()
        Get the final frequency of the shaker from the robot
    set_frequency2(value)
        Set the final frequency of the shaker on the robot
    get_direction()
        Get the direction of the oscillation from the robot
    set_direction(value)
        Set the direction of the oscillation on the robot
    get_posmax()
        Get the maximum oscillation amplitude from the robot
    set_posmax(value)
        Set the maximum oscillation amplitude on the robot
    get_velmax()
        Get the maximum oscillation velocity from the robot
    set_velmax(value)
        Set the maximum oscillation velocity on the robot
    get_accmax()
        Get the maximum oscillation acceleration from the robot
    set_accmax(value)
        Set the maximum oscillation acceleration on the robot
    get_stiffness()
        Get the stiffness of the stabilising spring from the robot
    set_stiffness(value)
        Set the stiffness of the stabilising spring on the robot
    get_dampfactor()
        Get the damping factor of the stabilising spring from the robot
    set_dampfactor(value)
        Set the damping factor of the stabilising spring on the robot
    get_deadband()
        Get the deadband length of the stabilising spring from the robot
    set_deadband(value)
        Set the deadband length of the stabilising spring on the robot
    get_maxforce()
        Get the maximum force of the stabilising spring from the robot
    set_maxforce(value)
        Set the maximum force of the stabilising spring on the robot

    '''

    def create(self) -> bool:
        '''Create a shaker on the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = f'create shaker {self.name}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return f'Effect shaker with name {self.name} created' in response


    def get_frequency1(self) -> float:
        '''Get the begining frequency of the shaker from the robot

        Returns
        -------
        float: Initial frequency [Hz]

        '''

        msg =  f'get {self.name} frequency1'

        return float(self.robot.send_message(msg))

    def set_frequency1(self, value: float) -> bool:
        '''Set begining frequency of the shaker on the robot

        Parameters
        ----------
        value (float): Frequency [Hz]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} frequency1 {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s frequency1 set' in response

    def get_frequency2(self) -> float:
        '''Get the ending frequency of the shaker from the robot

        Returns
        -------
        float: Final frequency [Hz]

        '''

        msg =  f'get {self.name} frequency2'

        return float(self.robot.send_message(msg))

    def set_frequency2(self, value: float) -> bool:
        '''Set ending frequency of the shaker on the robot

        Parameters
        ----------
        value (float): Frequency [Hz]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} frequency2 {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s frequency2 set' in response

    def get_direction(self) -> npt.NDArray:
        '''Get the oscillation direction of the shaker from the robot

        Returns
        -------
        npt.NDArray: Direction unit vector [non-dimensional]

        '''

        msg =  f'get {self.name} direction'

        return self.robot.string_to_array(self.robot.send_message(msg))

    def set_direction(self, value: npt.NDArray) -> bool:
        '''Set oscillation direction of the shaker on the robot

        Parameters
        ----------
        value (npt.NDArray): Unit vector [non-dimensional]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        if isinstance(value, np.ndarray):
            msg = f'set {self.name} direction [{",".join(str(v) for v in value)}]'
        else:
            msg = f'set {self.name} direction {str(value).replace(" ", "")}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s direction set' in response

    def get_posmax(self) -> float:
        '''Get the maximum oscillation amplitude of the shaker from the robot

        Returns
        -------
        float: Oscillation amplitude [m]

        '''

        msg =  f'get {self.name} posmax'

        return float(self.robot.send_message(msg))

    def set_posmax(self, value: float) -> bool:
        '''Set maximum oscillation amplitude of the shaker on the robot

        Parameters
        ----------
        value (float): Maximum oscillation amplitude [m]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} posmax {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s maximum position set' in response

    def get_velmax(self) -> float:
        '''Get the maximum oscillation velocity of the shaker from the robot

        Returns
        -------
        float: Oscillation velocity [m/s]

        '''

        msg =  f'get {self.name} velmax'

        return float(self.robot.send_message(msg))

    def set_velmax(self, value: float) -> bool:
        '''Set maximum oscillation velocity of the shaker on the robot

        Parameters
        ----------
        value (float): Maximum oscillation velocity [m/s]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} velmax {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s maximum velocity set' in response

    def get_accmax(self) -> float:
        '''Get the maximum oscillation acceleration of the shaker from the robot

        Returns
        -------
        float: Oscillation acceleration [m/s^2]

        '''

        msg =  f'get {self.name} accmax'

        return float(self.robot.send_message(msg))

    def set_accmax(self, value: float) -> bool:
        '''Set maximum oscillation acceleration of the shaker on the robot

        Parameters
        ----------
        value (float): Maximum oscillation acceleration [m/s^2]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} accmax {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s maximum acceleration set' in response

    def get_stiffness(self) -> float:
        '''Get the stabilising spring stiffness of the shaker from the robot

        Returns
        -------
        float: Spring stiffness [N/s]

        '''

        msg =  f'get {self.name} stiffness'

        return float(self.robot.send_message(msg))

    def set_stiffness(self, value: float) -> bool:
        '''Set the stabilising spring stiffness of the shaker on the robot

        Parameters
        ----------
        value (float): Spring stiffness [N/m]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} stiffness {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s stiffness set' in response

    def get_dampfactor(self) -> float:
        '''Get the stabilising damping factor of the shaker from the robot

        Returns
        -------
        float: Damping factor [non-dimensional]

        '''

        msg =  f'get {self.name} dampfactor'

        return float(self.robot.send_message(msg))

    def set_dampfactor(self, value: float) -> bool:
        '''Set the damping factor of the stabilising spring of the shaker on the robot

        Parameters
        ----------
        value (float): Damping factor [non-dimensional]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} dampfactor {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s damp factor set' in response

    def get_deadband(self) -> float:
        '''Get the stabilising spring deadband length of the shaker from the robot

        Returns
        -------
        float: Deadband length [m]

        '''

        msg =  f'get {self.name} deadband'

        return float(self.robot.send_message(msg))

    def set_deadband(self, value: float) -> bool:
        '''Set the deadband length of the stabilising spring of the shaker on the robot

        Parameters
        ----------
        value (float): Deadband length [m]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} deadband {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s deadband set' in response

    def get_maxforce(self) -> float:
        '''Get the stabilising spring maximum force of the shaker from the robot

        Returns
        -------
        float: Maximum force [N]

        '''

        msg =  f'get {self.name} maxforce'

        return float(self.robot.send_message(msg))

    def set_maxforce(self, value: float) -> bool:
        '''Set the maximum force of the stabilising spring of the shaker on the robot

        Parameters
        ----------
        value (float): Maximum force [N]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg =  f'set {self.name} maxforce {value}'

        response = self.robot.send_message(msg)

        logging.info(response)

        return 'Shaker\'s maximum force set' in response
