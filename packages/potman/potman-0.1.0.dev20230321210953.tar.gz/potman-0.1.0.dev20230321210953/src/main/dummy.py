# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#   Copyright (c) 2023 Patrick Hohenecker (PH). All Rights Reserved.          #
#                                                                             #
#   IT IS STRICTLY PROHIBITED TO USE, COPY, MODIFY, OR DISTRIBUTE THIS        #
#   SOFTWARE IN SOURCE OR BINARY FORMS FOR ANY PURPOSE.                       #
#                                                                             #
#   IN NO EVENT SHALL PH BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,         #
#   SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS,    #
#   ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF    #
#   PH HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                    #
#                                                                             #
#   PH SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED      #
#   TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A           #
#   PARTICULAR PURPOSE. PH HAS NO OBLIGATION TO PROVIDE MAINTENANCE,          #
#   SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.                         #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import potman


def __main() -> None:

    data = potman.fetch("dummy:clause_type_classification_v1")
    print(data.info())


if __name__ == "__main__":

    __main()
