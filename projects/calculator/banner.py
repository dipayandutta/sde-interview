"""
This is the class for the banner text
"""


class Banner:
    def __init__(self):
        self.text = r"""

                                     
  ####    ##   #       ####  
 #    #  #  #  #      #    # 
 #      #    # #      #      
 #      ###### #      #      
 #    # #    # #      #    # 
  ####  #    # ######  ####

        """

    def show_banner(self) -> None:
        print(f"{self.text}")
