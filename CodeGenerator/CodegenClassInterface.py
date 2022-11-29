from abc import ABC, abstractmethod

class CodegenClassInterface(ABC):
    @abstractmethod
    def run():
        ''' This method will be executed when the script is run
        '''
        pass
    