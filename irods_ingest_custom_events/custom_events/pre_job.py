from irods_capability_automated_ingest.core import Core
from irods_capability_automated_ingest.utils import Operation

class event_handler(Core):

    @staticmethod
    def operation(session, meta, **options):
        return Operation.NO_OP

    @staticmethod
    def pre_job(hdlr_mod, logger, meta):
        with open("/tmp/testing_pre_job", "w") as f:
            f.write("If sucessful dump this text in above file.")
