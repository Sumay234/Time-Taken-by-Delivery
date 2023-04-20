import os
import sys

class deliveryexception(Exception):
    
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__(error_message)
        self.error_message = deliveryexception.error_message_detail(error_message,error_details=error_details)
        
    
    @staticmethod
    def error_message_detail(error_message:Exception,error_details:sys)->str:
        _,_, exc_tb = error_details.exc_info()
        line_number = exc_tb.tb_frame.f_lineno ## to know the error in line number
        '''
           Note :- here 1) exc_tb      is execute the same function,
                        2) tb_frame    is to find frame in code,
                        3) f_code      is the code error,
                        4) co_filename is for file name
        '''
        
        file_name =exc_tb.tb_frame.f_code.co_filename    ## Extracting the file name in which we will get error
        
        ## to store the error
        error_message=f"Error occured python scrip name [{file_name}]"\
                      f"line number [{exc_tb.tb_linesno}] error message [{error}]."
                      
        return error_message
    
    def __str__(self):
        return deliveryexception.__name__.__str__()
    
    
    
    