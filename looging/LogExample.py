import logging

print("***************START***************")

#logging.basicConfig(filename="CISCO-SB015", level=logging.NOTSET)
#logging.basicConfig(filename="CISCO-SB015", level=logging.DEBUG)
#logging.basicConfig(filename="CISCO-SB015", level=logging.INFO)
#logging.basicConfig(filename="CISCO-SB015", level=logging.WARNING)
#logging.basicConfig(filename="CISCO-SB015", level=logging.ERROR)
logging.basicConfig(filename="CISCO-SB015", level=logging.CRITICAL)

logging.debug("I am Debug Log Messages - 1")
logging.debug("I am Debug Log Messages - 2")
logging.debug("I am Debug Log Messages - 3")
logging.debug("I am Debug Log Messages - 4")

logging.info("I am Info Log Messages - 1")
logging.info("I am Info Log Messages - 2")
logging.info("I am Info Log Messages - 3")
logging.info("I am Info Log Messages - 4")

logging.warning("I am warning Log Messages - 1")
logging.warning("I am warning Log Messages - 2")
logging.warning("I am warning Log Messages - 3")
logging.warning("I am warning Log Messages - 4")

logging.error("I am Error Log Messages - 1")
logging.error("I am Error Log Messages - 2")
logging.error("I am Error Log Messages - 3")
logging.error("I am Error Log Messages - 4")

logging.critical("I am Critical Log Messages - 1")
logging.critical("I am Critical Log Messages - 2")
logging.critical("I am Critical Log Messages - 3")
logging.critical("I am Critical Log Messages - 4")


print("****************END***************")